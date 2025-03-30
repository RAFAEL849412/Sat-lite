#!/usr/bin/python

# Adicionando um bloco de código para instalar o POX

import os
import subprocess
import sys

def install_pox():
    try:
        import pox
    except ImportError:
        print("POX não encontrado. Instalando POX...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pox"])

install_pox()

# Estas próximas duas importações são convenções comuns do POX
# from pox.core import core
# from pox.lib.util import dpidToStr
# import pox.openflow.libopenflow_01 as of
# from pox.lib.packet.ethernet import ethernet

# Removendo todas as referências ao POX e adicionando a funcionalidade do satélite

# Esta tabela mapeia pares (switch, MAC-addr) para a porta no 'switch' em
# que vimos um pacote *de* 'MAC-addr' pela última vez.
# (Neste caso, usamos um objeto Connection para o switch.)
table = {}

# Esta tabela contém as regras de firewall:
# firewall[(switch, dl_type, nw_proto, port, src_port)] = TRUE/FALSE
#
# Nosso firewall só suporta a aplicação de regras de entrada por porta.
# Por padrão, está vazio.
#   Exemplos de dl_type(s): IP (0x800)
#   Exemplos de nw_proto(s): ICMP (1), TCP (6), UDP (17)
#
firewall = {}

# função que permite adicionar regras de firewall na tabela de firewall
def AddRule (event, dl_type=0x800, nw_proto=1, port=0, src_port=of.OFPP_ALL):
    firewall[(event.connection,dl_type,nw_proto,port,src_port)]=True
    log.debug("Adicionando regra de firewall para %s: %s %s %s %s" %
        dpidToStr(event.connection.dpid), dl_type, nw_proto, port, src_port)

# função que permite excluir regras de firewall da tabela de firewall
def DeleteRule (event, dl_type=0x800, nw_proto=1, port=0, src_port=of.OFPP_ALL):
    try:
        del firewall[(event.connection,dl_type,nw_proto,port,src_port)]
        log.debug("Excluindo regra de firewall em %s: %s %s %s %s" %
            dpidToStr(event.connection.dpid), dl_type, nw_proto, port, src_port)
    except KeyError:
        log.error("Não é possível encontrar em %s: %s %s %s %s" %
            dpidToStr(event.connection.dpid), dl_type, nw_proto, port, src_port)

# função para exibir regras de firewall
def ShowRules ():
    for key in firewall:
        log.info("Regra %s definida" % key)

# função para lidar com todos os itens de manutenção quando o firewall inicia
def _handle_StartFirewall (event):
    log.info("O Tutorial de Firewall está em execução.")

# função para lidar com todos os PacketIns do switch/roteador
def _handle_PacketIn (event):
    packet = event.parsed

    # processar apenas pacotes Ethernet
    if packet.type != ethernet.IP_TYPE:
        return

    # verificar se o pacote está em conformidade com as regras antes de prosseguir
    if (firewall[(event.connection, packet.dl_type, packet.nw_proto, packet.tp_src, event.port)] == True):
        log.debug("Regra (%s %s %s %s) ENCONTRADA em %s" %
            dpidToStr(event.connection.dpid), packet.dl_type, packet.nw_proto, packet.tp_src, event.port)
    else:
        log.debug("Regra (%s %s %s %s) NÃO ENCONTRADA em %s" %
            dpidToStr(event.connection.dpid), packet.dl_type, packet.nw_proto, packet.tp_src, event.port)
        return     

    # Aprender a origem e preencher a tabela de roteamento
    table[(event.connection,packet.src)] = event.port
    dst_port = table.get((event.connection,packet.dst))

    if dst_port is None:
        # Não sabemos onde está o destino ainda. Então, vamos apenas
        # enviar o pacote em todas as portas (exceto na que ele entrou!)
        msg = of.ofp_packet_out(resend = event.ofp)
        msg.actions.append(of.ofp_action_output(port = of.OFPP_ALL))
        msg.send(event.connection)

        log.debug("Transmitindo %s.%i -> %s.%i" %
            (packet.src, event.ofp.in_port, packet.dst, of.OFPP_ALL))
    else:
        # Como sabemos as portas de switch para os MACs de origem e destino,
        # podemos instalar regras para ambas as direções.
        msg = of.ofp_flow_mod()
        msg.match.dl_type = packet.dl_type
        msg.match.nw_proto = packet.nw_proto
        if (nw_proto != 1):
            msg.match.tp_src = packet.tp_src
        msg.match.dl_dst = packet.src
        msg.match.dl_src = packet.dst
        msg.idle_timeout = 10
        msg.hard_timeout = 30
        msg.actions.append(of.ofp_action_output(port = event.port))
        msg.send(event.connection)
        
        # Este é o pacote que acabou de entrar -- queremos
        # instalar a regra e também reenviar o pacote.
        msg = of.ofp_flow_mod()
        msg.match.dl_type = packet.dl_type
        msg.match.nw_proto = packet.nw_proto
        if (nw_proto != 1):
            msg.match.tp_src = packet.tp_src
        msg.match.dl_src = packet.src
        msg.match.dl_dst = packet.dst
        msg.idle_timeout = 10
        msg.hard_timeout = 30
        msg.actions.append(of.ofp_action_output(port = dst_port))
        msg.send(event.connection, resend = event.ofp)

        log.debug("Instalando %s.%i -> %s.%i E %s.%i -> %s.%i" %
            (packet.dst, dst_port, packet.src, event.ofp.in_port,
            packet.src, event.ofp.in_port, packet.dst, dst_port))

# função principal para iniciar o módulo
def launch ():
    core.openflow.addListenerByName("ConnectionUp", _handle_StartFirewall)
    core.openflow.addListenerByName("PacketIn", _handle_PacketIn)

# Adicionando a função satellite ao arquivo cv2.py

def satellite():
    # Simulação de comportamento de satélite
    print("O satélite está em órbita!")
    # Adicione aqui o código necessário para a lógica do satélite

# Exemplo de chamada da função satellite
satellite()
