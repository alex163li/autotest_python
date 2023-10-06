import smtplib
from os.path import basename
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

fromaddr = "lialin163@yandex.ru"
toaddr = "lialin163@yandex.ru"
mypass = "LTkQAMzizYE4zHcYgpzh"
reportname = "log.txt"

msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "HELLO WORLD"
text = "Hello"

msg.attach(MIMEText(text))

with open(reportname, "rb") as f:
    part = MIMEApplication(f.read(), Name=basename(reportname))
    part['Content-Disposition'] = f'attachment; filename="{basename(reportname)}"'
    msg.attach(part)

# body = "Это пробное сообщение"
# msg.attach(MIMEText(body, 'plain'))

server = smtplib.SMTP_SSL('smtp.mail.ru', 465)
server.login(fromaddr, mypass)
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
