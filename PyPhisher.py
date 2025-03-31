import smtplib
import argparse
import re
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def banner():
    print("#################################")
    print("#          PyPhisher            #")
    print("#       by: sneakerhax          #")
    print("#################################")

def main(args):
    pish(args)

def pish(args):
    # Abre o arquivo HTML
    message_html = open_html_file(args.html)
    # Substitui os links no HTML
    html_output = replace_links(args.url_replace, message_html)
    # Cria a mensagem MIME
    message = mime_message(args.subject, args.sendto, args.sender, html_output)
    # Envia o e-mail
    send_email(args.server, args.port, args.username, args.password, args.sender, args.sendto, message)

def open_html_file(file):
    with open(file, 'r') as open_html:
        email_html = open_html.read()
    return email_html

def replace_links(url, message):
    # Substitui links no HTML usando expressões regulares
    html_regex = re.compile(r"""(?i)\b((?:[a-z][\w-]+:(?:/{1,3}|[a-z0-9%])|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>\[\]]+|\(([^\s()<>\[\]]+|(\([^\s()<>\[\]]+\)))*\))+(?:\(([^\s()<>\[\]]+|(\([^\s()<>\[\]]+\)))*\)|[^\s`!(){};:'".,<>?\[\]]))""")
    html_output = html_regex.sub(url, message)
    return html_output

def mime_message(subject, sendto, sender, html):
    msg = MIMEMultipart('alternative')
    msg['To'] = sendto
    msg['From'] = sender
    msg['Subject'] = subject
    message = MIMEText(html, 'html')
    msg.attach(message)
    return msg.as_string()

def send_email(server, port, username, password, sender, sendto, message):
    try:
        s = smtplib.SMTP(server, port)
        s.starttls()                                                                                                                                                    s.ehlo()                                                                                                                                                        s.login(username, password)                                                                                                                                     s.sendmail(sender, sendto, message)                                                                                                                             s.quit()                                                                                                                                                        print("Email enviado com sucesso!")
    except Exception as e:
        print(f"Erro ao enviar email: {e}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--server', required=True, type=str, help='Endereço do servidor SMTP')
    parser.add_argument('--port', required=True, type=int, help='Porta do servidor SMTP')
    parser.add_argument('--username', required=True, type=str, help='Nome de usuário do servidor')
    parser.add_argument('--password', required=True, type=str, help='Senha do servidor')
    parser.add_argument('--html', required=True, type=str, help='Caminho para o arquivo HTML')
    parser.add_argument('--url_replace', required=True, type=str, help='URL para substituir')
    parser.add_argument('--subject', required=True, type=str, help='Assunto do e-mail')
    parser.add_argument('--sender', required=True, type=str, help='Endereço de e-mail do remetente')
    parser.add_argument('--sendto', required=True, type=str, help='Endereço de e-mail do destinatário')

    args = parser.parse_args()

    banner()
    main(args)
