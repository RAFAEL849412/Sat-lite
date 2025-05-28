#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random

class AntivirusBot:
    def __init__(self):
        self.p = 606341371901192354470259703076328716992246317693812238045286463

        self.g = [160057538006753370699321703048317480466874572114764155861735009,
                  255466303302648575056527135374882065819706963269525464635673824]

        self.connecte = [
            [460868776123995205521652669050817772789692922946697572502806062,
             263320455545743566732526866838203345604600592515673506653173727],

            [270400597838364567126384881699673470955074338456296574231734133,
             526337866156590745463188427547342121612334530789375115287956485]
        ]

        # Dados simulados
        self.bye = ["tchau", "adeus"]
        self.thank_you = ["obrigado", "valeu"]
        self.thank_response = ["De nada!", "Sem problemas!", "Fico feliz em ajudar!"]
        self.greetings = ["olá", "oi"]
        self.sent_tokens = [
            "vírus detectado",
            "como remover malware",
            "o que é um vírus de computador",
            "como se proteger"
        ]

    def response(self, user_input):
        user_input = user_input.lower()
        if "vírus" in user_input:
            return "⚠️ Vírus detectado! Mova o arquivo para a quarentena ou exclua-o imediatamente."
        elif "malware" in user_input:
            return "🛡️ Para remover malware, execute uma varredura completa no sistema e atualize seu antivírus."
        elif "vírus de computador" in user_input:
            return "🧬 Um vírus de computador é um tipo de software malicioso que se replica e pode causar danos ao sistema."
        elif "protegido" in user_input or "proteger" in user_input:
            return "🔒 Mantenha seu antivírus atualizado e evite downloads suspeitos para se proteger."
        else:
            return "❓ Ameaça desconhecida. Por favor, execute uma verificação completa no sistema."

    def bot_initialize(self, user_msg):
        flag = True
        while flag:
            user_response = user_msg.lower()
            if user_response not in self.bye:
                if user_response == '/iniciar':
                    return "👋 Bem-vindo! Eu sou seu Assistente Antivírus. Posso ajudar a detectar e remover ameaças do seu sistema.\nDigite 'tchau' para sair."
                elif user_response in self.thank_you:
                    return random.choice(self.thank_response)
                elif user_response in self.greetings:
                    return random.choice(self.greetings).capitalize() + "! Como posso ajudar na proteção do seu sistema hoje?"
                else:
                    bot_resp = self.response(user_response)
                    if user_response in self.sent_tokens:
                        self.sent_tokens.remove(user_response)
                    return bot_resp
            else:
                flag = False
                return random.choice(["👋 Tchau! Fique seguro online!", "🔐 Até logo! Seu sistema está protegido.", "🛑 Encerrando. Continue seguro!"])

# init
if __name__ == "__main__":
    bot = AntivirusBot()
    bot.bot_initialize("/iniciar")
    bot.bot_initialize("olá")
    bot.bot_initialize("vírus detectado")
    bot.bot_initialize("obrigado")
    bot.bot_initialize("tchau")
