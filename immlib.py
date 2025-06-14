#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: search_opcode.py
# Description: Plugin do Immunity Debugger para procurar instruções em código montado.

from immlib import *

def main(args):
    imm = Debugger()

    if not args:
        imm.log("[!] Nenhuma instrução fornecida. Exemplo de uso: JMP ESP")
        return "[!] Por favor, forneça uma instrução para procurar."

    search_code = " ".join(args)
    
    try:
        search_bytes = imm.assemble(search_code)
    except Exception as e:
        imm.log("[!] Erro ao montar a instrução: %s" % str(e))
        return "[!] Instrução inválida ou erro na montagem."

    search_results = imm.search(search_bytes)

    if not search_results:
        imm.log("[*] Nenhuma ocorrência encontrada para: %s" % search_code)
        return "[*] Nenhuma ocorrência encontrada."

    for hit in search_results:
        code_page = imm.getMemoryPagebyAddress(hit)
        access = code_page.getAccess(human=True)

        if "execute" in access.lower():
            imm.log("[*] Encontrado: %s em 0x%08X (Acesso: %s)" % (search_code, hit, access), address=hit)

    return "[*] Busca finalizada. Verifique a janela de Log no Immunity Debugger."
