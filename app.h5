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
    message_html = open_html_file(args.html)
    html_output = replace_links(args.url_replace, message_html)
    message = mime_message(args.subject, args.sendto, args.sender, html_output)
    send_email(args.server, args.port, args.username, args.password, args.sender, args.sendto, message)

def open_html_file(file):
    with open(file, 'r', encoding='utf-8') as f:
        return f.read()

def replace_links(url, message):
    regex = re.compile(r'https?://[^\s"]+')
    return regex.sub(url, message)

def mime_message(subject, sendto, sender, html):
    msg = MIMEMultipart('alternative')
    msg['To'] = sendto
    msg['From'] = sender
    msg['Subject'] = subject
    msg.attach(MIMEText(html, 'html'))
    return msg.as_string()

def send_email(server, port, username, password, sender, sendto, message):
    try:
        with smtplib.SMTP(server, port) as s:
            s.starttls()
            s.login(username, password)
            s.sendmail(sender, sendto, message)
        print("Email enviado com sucesso!")
    except Exception as e:
        print(f"Erro ao enviar email: {e}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--server', required=True, help='Servidor SMTP')
    parser.add_argument('--port', type=int, required=True, help='Porta SMTP')
    parser.add_argument('--username', required=True, help='Usuário SMTP')
    parser.add_argument('--password', required=True, help='Senha SMTP')
    parser.add_argument('--html', required=True, help='Arquivo HTML')
    parser.add_argument('--url_replace', required=True, help='URL que substitui os links')
    parser.add_argument('--subject', required=True, help='Assunto do e-mail')
    parser.add_argument('--sender', required=True, help='Email do remetente')
    parser.add_argument('--sendto', required=True, help='Email do destinatário')

    banner()
    main(parser.parse_args())
