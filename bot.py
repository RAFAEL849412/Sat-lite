'''
RISC-V assembler.
'''
# Mara Huldra 2021, based on riscv-assembler by Kaya Celebi
# SPDX-License-Identifier: MIT  
from collections import namedtuple

__all__ = ['Assembler']

class UnknownInstruction(Exception):
    def __init__(self, instr):
        self.message = 'Unknown instruction ' + instr
        super().__init__(self.message)

class ImmediateOutOfRange(Exception):
    def __init__(self, message = 'Immediate value is out of range'):
        self.message = message
        super().__init__(self.message)

R_instr = namedtuple('R_instr', ['opcode', 'f3', 'f7'])
I_instr = namedtuple('I_instr', ['opcode', 'f3'])
I_instr_sys = namedtuple('I_instr_sys', ['opcode', 'f3', 'imm'])
I_instr_shift = namedtuple('I_instr_shift', ['opcode', 'f3', 'imm6'])
S_instr = namedtuple('S_instr', ['opcode', 'f3'])
B_instr = namedtuple('B_instr', ['opcode', 'f3'])
U_instr = namedtuple('U_instr', ['opcode'])
J_instr = namedtuple('J_instr', ['opcode'])

# Pseudo-instructions defined by the RISC-V spec
PSEUDO_INSTR = [
    'la', 'lla', # l{b|h|w|d} s{b|h|w|d} variants handled as instruction
    'nop', 'li', 'mv', 'not', 'neg', 'negw', 'sext.w',
    'seqz', 'snez', 'sltz', 'sgtz',
    'beqz', 'bnez', 'blez', 'bgez', 'bltz', 'bgtz',
    'bgt', 'ble', 'bgtu', 'bleu',
    'j', 'jr', 'ret', # jal, jalr variants handled as instructions
]

# ABI register to machine register mapping
R_MAP = {
    'ra': 'x1',   'sp': 'x2',  'gp': 'x3',
    'tp': 'x4',   't0': 'x5',  't1': 'x6',  't2': 'x7',
    # fp is another name for s0, the first callee-saved register
    'fp': 'x8',   's0': 'x8',  's1': 'x9',  'a0': 'x10',
    'a1': 'x11',  'a2': 'x12', 'a3': 'x13', 'a4': 'x14',
    'a5': 'x15',  'a6': 'x16', 'a7': 'x17', 's2': 'x18',
    's3': 'x19',  's4': 'x20', 's5': 'x21', 's6': 'x22',
    's7': 'x23',  's8': 'x24', 's9': 'x25', 's10': 'x26',
    's11': 'x27', 't3': 'x28', 't4': 'x29', 't5': 'x30',
    't6': 'x31',
}

# Instruction forms
INSTR_DATA = {
    'add': R_instr(opcode='0110011', f3='000', f7='0000000'),
    'addi': I_instr(opcode='0010011', f3='000'),
    'addiw': I_instr(opcode='0011011', f3='000'),
    'addw': R_instr(opcode='0111011', f3='000', f7='0000000'),
    'and': R_instr(opcode='0110011', f3='111', f7='0000000'),
    'andi': I_instr(opcode='0010011', f3='111'),
    'auipc': U_instr(opcode='0010111'),
    'beq': B_instr(opcode='1100011', f3='000'),
    'bge': B_instr(opcode='1100011', f3='101'),
    'bgeu': B_instr(opcode='1100011', f3='111'),
    'blt': B_instr(opcode='1100011', f3='100'),
    'bltu': B_instr(opcode='1100011', f3='110'),
    'bne': B_instr(opcode='1100011', f3='001'),
    'csrrc': I_instr(opcode='1110011', f3='011'),
    'csrrci': I_instr(opcode='1110011', f3='111'),
    'csrrs': I_instr(opcode='1110011', f3='010'),
    'csrrsi': I_instr(opcode='1110011', f3='110'),
    'csrrw': I_instr(opcode='1110011', f3='001'),
    'csrrwi': I_instr(opcode='1110011', f3='101'),
    'div': R_instr(opcode='0110011', f3='100', f7='0000001'),
    'divu': R_instr(opcode='0110011', f3='101', f7='0000001'),
    'divuw': R_instr(opcode='0111011', f3='101', f7='0000001'),
    'divw': R_instr(opcode='0111011', f3='100', f7='0000001'),
    'ebreak': I_instr_sys(opcode='1110011', f3='000', imm='000000000001'),
    'ecall': I_instr_sys(opcode='1110011', f3='000', imm='000000000000'),
    'fence': I_instr(opcode='0001111', f3='000'),
    'fence.i': I_instr(opcode='0001111', f3='001'),
    'jal': J_instr(opcode='1101111'),
    'jalr': I_instr(opcode='1100111', f3='000'),
    'lb': I_instr(opcode='0000011', f3='000'),
    'lbu': I_instr(opcode='0000011', f3='100'),
    'ld': I_instr(opcode='0000011', f3='011'),
    'lh': I_instr(opcode='0000011', f3='001'),
    'lhu': I_instr(opcode='0000011', f3='101'),
    'lui': U_instr(opcode='0110111'),
    'lw': I_instr(opcode='0000011', f3='010'),
    'lwu': I_instr(opcode='0000011', f3='110'),
    'mul': R_instr(opcode='0110011', f3='000', f7='0000001'),
    'mulh': R_instr(opcode='0110011', f3='001', f7='0000001'),
    'mulsu': R_instr(opcode='0110011', f3='010', f7='0000001'),
    'mulu': R_instr(opcode='0110011', f3='011', f7='0000001'),
    'mulw': R_instr(opcode='0111011', f3='000', f7='0000001'),
    'or': R_instr(opcode='0110011', f3='110', f7='0000000'),
    'ori': I_instr(opcode='0010011', f3='110'),
    'rem': R_instr(opcode='0110011', f3='110', f7='0000001'),
    'remu': R_instr(opcode='0110011', f3='111', f7='0000001'),
    'remuw': R_instr(opcode='0111011', f3='111', f7='0000001'),
    'remw': R_instr(opcode='0111011', f3='110', f7='0000001'),
    'sb': S_instr(opcode='0100011', f3='000'),
    'sd': S_instr(opcode='0100011', f3='011'),
    'sh': S_instr(opcode='0100011', f3='001'),
    'sll': R_instr(opcode='0110011', f3='001', f7='0000000'),
    'slli': I_instr_shift(opcode='0010011', f3='001', imm6='000000'),
    'slliw': I_instr_shift(opcode='0011011', f3='001', imm6='000000'),
    'sllw': R_instr(opcode='0111011', f3='001', f7='0000000'),
    'slri': I_instr_shift(opcode='0010011', f3='101', imm6='000000'),
    'slrw': R_instr(opcode='0111011', f3='101', f7='0000000'),
    'slt': R_instr(opcode='0110011', f3='010', f7='0000000'),
    'slti': I_instr(opcode='0010011', f3='010'),
    'sltiu': I_instr(opcode='0010011', f3='011'),
    'sltu': R_instr(opcode='0110011', f3='011', f7='0000000'),
    'sra': R_instr(opcode='0110011', f3='101', f7='0100000'),
    'srai': I_instr_shift(opcode='0010011', f3='101', imm6='010000'),
    'sraiw': I_instr_shift(opcode='0011011', f3='101', imm6='010000'),
    'sraw': R_instr(opcode='0111011', f3='101', f7='0100000'),
    'srl': R_instr(opcode='0110011', f3='101', f7='0000000'),
    'srliw': I_instr_shift(opcode='0011011', f3='101', imm6='000000'),
    'sub': R_instr(opcode='0110011', f3='000', f7='0100000'),
    'subw': R_instr(opcode='0111011', f3='000', f7='0100000'),
    'sw': S_instr(opcode='0100011', f3='010'),
    'xor': R_instr(opcode='0110011', f3='100', f7='0000000'),
    'xori': I_instr(opcode='0010011', f3='100'),
}

def parse_imm(s, imin=-0xffffffff, imax=0xffffffff):
    if isinstance(s, int):
        pass
    elif isinstance(s, str):
        s = int(s, 0)
    else:
        raise ValueError('Invalid immediate value type')

    if s < imin or s > imax:
        raise ImmediateOutOfRange(s)

    return s

def reg_to_bin(x):
    if not x.startswith('x'):
        x = R_MAP[x]
    assert(x[0] == 'x')
    x = int(x[1:])
    assert(x >= 0 and x < 32)
    return f'{x:05b}'

class Assembler:
    def __init__(self):    
        pass

    def calc_jump(self, x, line_num):
        if isinstance(x, int):
            return x
        x = x.split()
        return parse_imm(x[0])

    #create instruction
    def R_type(self, *, instr, rs1, rs2, rd):
        assert(isinstance(instr, R_instr))

        return ''.join([
            instr.f7,
            reg_to_bin(rs2),
            reg_to_bin(rs1),
            instr.f3,
            reg_to_bin(rd),
            instr.opcode
        ])

    def I_type(self, *, instr, rs1, imm, rd):
        assert(isinstance(instr, I_instr))

        imm = parse_imm(imm, -(1 << 11), (1 << 11) - 1)

        return ''.join([
            f'{imm & 0xfff:012b}',
            reg_to_bin(rs1),
            instr.f3,
            reg_to_bin(rd),
            instr.opcode
        ])

    def I_type_shift(self, *, instr, rs1, imm, rd):
        assert(isinstance(instr, I_instr_shift))

        imm = parse_imm(imm, 0, 63)

        return ''.join([
            instr.imm6,
            f'{imm:06b}',
            reg_to_bin(rs1),
            instr.f3,
            reg_to_bin(rd),
            instr.opcode
        ])

    def I_type_sys(self, *, instr):
        assert(isinstance(instr, I_instr_sys))

        return ''.join([
            instr.imm,
            '00000',
            instr.f3,
            '00000',
            instr.opcode
        ])

    def S_type(self, *, instr, rs1, rs2, imm):
        assert(isinstance(instr, S_instr))

        imm = parse_imm(imm, -(1 <<  11), (1 << 11) - 1)

        return ''.join([
            f'{(imm >> 5) & 0x7f:07b}',
            reg_to_bin(rs2),
            reg_to_bin(rs1),
            instr.f3,
            f'{imm & 0x1f:05b}',
            instr.opcode
        ])

    def B_type(self, *, instr, rs1, rs2, imm):
        assert(isinstance(instr, B_instr))

        imm = parse_imm(imm, -(1 << 12), (1 << 12) - 1)
        assert((imm & 1) == 0)

        return ''.join([
            f'{(imm >> 12) & 0x1:01b}',
            f'{(imm >> 5) & 0x3f:06b}',
            reg_to_bin(rs2),
            reg_to_bin(rs1),
            instr.f3,
            f'{(imm >> 1) & 0xf:04b}',
            f'{(imm >> 11) & 0x1:01b}',
            instr.opcode
        ])


    def U_type(self, *, instr, imm, rd):
        assert(isinstance(instr, U_instr))

        imm = parse_imm(imm, 0, 0xffffffff)
        assert((imm & 0xfff) == 0)

        return ''.join([
            f'{imm >> 12:020b}',
            reg_to_bin(rd),
            instr.opcode
        ])

    def J_type(self, *, instr, imm, rd):
        assert(isinstance(instr, J_instr))

        imm = parse_imm(imm, -(1 << 20), (1 << 20) - 1)
        assert((imm & 1) == 0)

        return  ''.join([
            f'{(imm >> 20) & 0x1:01b}',
            f'{(imm >> 1) & 0x3ff:010b}',
            f'{(imm >> 11) & 0x1:01b}',
            f'{(imm >> 12) & 0xff:08b}',
            reg_to_bin(rd),
            instr.opcode
        ])


    def assemble(self, line, i=0):
        pos = line.find('#')
        if pos != -1:
            line = line[0:pos]

        tokens = line.strip().split(None, 1)

        inst = tokens[0].strip()
        if len(tokens) > 1:
            operands = [x.strip() for x in tokens[1].split(',')]
        else:
            operands = []

        return self.assemble_list([inst] + operands, i)

    def assemble_list(self, instr, i=0):
        res = []

        if instr[0] in {'sb', 'sh', 'sw', 'sd',
                        'lb', 'lbu', 'lw', 'lwu', 'lh', 'lhu', 'ld'}:
            # '0(sp)' to ['0', 'sp']
            instr = instr[:]
            w_spl = instr[2].split('(')
            instr[2] = w_spl[0]
            instr.append(w_spl[1].replace(')',''))

        irec = INSTR_DATA.get(instr[0])

        if isinstance(irec, R_instr):
            res.append(self.R_type(instr=irec, rs1=instr[2], rs2=instr[3], rd=instr[1]))
        elif isinstance(irec, I_instr):
            if instr[0] == 'jalr':
                if len(instr) == 4:
                    res.append(self.I_type(instr=irec, rs1=instr[2], imm=self.calc_jump(instr[3],i), rd=instr[1]))
                else:
                    res.append(self.I_type(instr=irec, rs1=instr[1], imm=0, rd='x1'))
            elif instr[0] in {'lb', 'lbu', 'lh', 'lhu', 'lw', 'lwu', 'ld'}:
                res.append(self.I_type(instr=irec, rs1=instr[3], imm=instr[2], rd=instr[1]))
            else:
                res.append(self.I_type(instr=irec, rs1=instr[2], imm=instr[3], rd=instr[1]))
        elif isinstance(irec, I_instr_sys):
            res.append(self.I_type_sys(instr=irec))
        elif isinstance(irec, I_instr_shift):
            res.append(self.I_type_shift(instr=irec, rs1=instr[2], imm=instr[3], rd=instr[1]))
        elif isinstance(irec, S_instr):
            res.append(self.S_type(instr=irec, rs1=instr[3], rs2=instr[1], imm=instr[2]))
        elif isinstance(irec, B_instr):
            res.append(self.B_type(instr=irec, rs1=instr[1], rs2=instr[2], imm=self.calc_jump(instr[3], i)))
        elif isinstance(irec, U_instr):
            res.append(self.U_type(instr=irec, imm=instr[2], rd=instr[1]))
        elif isinstance(irec, J_instr):
            if len(instr) == 3:
                res.append(self.J_type(instr=irec, imm=self.calc_jump(instr[2],i), rd=instr[1]))
            else:
                res.append(self.J_type(instr=irec, imm=self.calc_jump(instr[1],i), rd='x1'))
        elif instr[0] in PSEUDO_INSTR:
            im = INSTR_DATA
            if instr[0] == 'li': # "Myriad sequences"
                immval = parse_imm(instr[2])
                if immval >= (1<<11) and immval < 0x80000000:
                    if (immval & 0xfff) < 0x800: # round down, add
                        res.append(self.U_type(instr=im['lui'], imm=immval & 0xfffff000, rd=instr[1]))
                        res.append(self.I_type(instr=im['addi'], rs1=instr[1], imm=immval & 0x7ff, rd=instr[1]))
                    else: # round up, subtract
                        res.append(self.U_type(instr=im['lui'], imm=(immval & 0xfffff000) + 0x1000, rd=instr[1]))
                        res.append(self.I_type(instr=im['addi'], rs1=instr[1], imm=(immval & 0x7ff) - 0x800, rd=instr[1]))
                elif immval == 0xffffffff: # TODO: 64 bit only
                    res.append(self.I_type(instr=im['addiw'], rs1='x0', imm=-1, rd=instr[1]))
                else: # TODO: handle other ranges
                    res.append(self.I_type(instr=im['addi'], rs1='x0', imm=instr[2], rd=instr[1]))
            elif instr[0] == 'nop': # nop → addi x0, x0, 0
                res.append(self.I_type(instr=im['addi'], rs1='x0', imm=0, rd='x0'))
            elif instr[0] == 'mv': # mv rd, rs → addi rd, rs, 0
                res.append(self.I_type(instr=im['addi'], rs1=instr[2], imm=0, rd=instr[1]))
            elif instr[0] == 'not': # not rd, rs → xori rd, rs, -1
                res.append(self.I_type(instr=im['xori'], rs1=instr[2], imm=-1, rd=instr[1]))
            elif instr[0] == 'neg': # neg rd, rs → sub rd, x0, rs
                res.append(self.R_type(instr=im['sub'], rs1='x0', rs2=instr[2], rd=instr[1]))
            elif instr[0] == 'la': # la rd, symbol (non-PIC) → auipc rd, delta[31 : 12] + delta[11]; addi rd, rd, delta[11:0]
                res.append(self.U_type(instr=im['auipc'], imm=self.calc_jump(instr[2],i), rd=instr[1]))
            elif instr[0] == 'j': # j offset → jal x0, offset
                res.append(self.J_type(instr=im['jal'], imm=self.calc_jump(instr[1],i), rd='x0'))
            elif instr[0] == 'jr': # jr rs → jalr x0, 0(rs)
                res.append(self.I_type(instr=im['jalr'], rs1=instr[1], imm=0, rd='x0'))
            elif instr[0] == 'ret': # ret → jalr x0, 0(x1)
                res.append(self.I_type(instr=im['jalr'], rs1='x1', imm=0, rd='x0'))
            elif instr[0] == 'bgt': # bgt rs, rt, offset → blt rt, rs, offset
                res.append(self.B_type(instr=im['blt'], rs1=instr[2], rs2=instr[1], imm=self.calc_jump(instr[3],i)))
            elif instr[0] == 'ble': # ble rs, rt, offset → bge rt, rs, offset
                res.append(self.B_type(instr=im['bge'], rs1=instr[2], rs2=instr[1], imm=self.calc_jump(instr[3], i)))
            elif instr[0] == 'sext.w': # sext.w rd, rs → addiw rd, rs, 0
                res.append(self.I_type(instr=im['addiw'], rd=instr[1], rs1=instr[2], imm=0))
            elif instr[0] == 'seqz': # seqz rd, rs → sltiu rd, rs, 1
                res.append(self.I_type(instr=im['sltiu'], rd=instr[1], rs1=instr[2], imm=1))
            elif instr[0] == 'snez': # snez rd, rs → sltu rd, x0, rs
                res.append(self.R_type(instr=im['sltu'], rd=instr[1], rs1='x0', rs2=instr[2]))
            elif instr[0] == 'sltz': # sltz rd, rs → slt rd, rs, x0
                res.append(self.R_type(instr=im['slt'], rd=instr[1], rs1=instr[2], rs2='x0'))
            elif instr[0] == 'sgtz': # sgtz rd, rs → slt rd, x0, rs
                res.append(self.R_type(instr=im['slt'], rd=instr[1], rs1='x0', rs2=instr[2]))
            else:
                raise NotImplementedError(instr[0])
        else:
            raise UnknownInstruction(instr[0])

        return res