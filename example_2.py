# coding=utf-8

from smtplib import SMTP_SSL
from email.mime.text import MIMEText
from email.header import Header

"""
    First case, simply sending mail. Using SMTP_SSL function.
"""

# Information of the mail
mailInfo = {
    "from": "****@163.com",
    "to": "****@qq.com",
    "hostname": "smtp.163.com",
    "username": "****@163.com",
    "password": "******",
    "mailencoding": "utf-8"
}

if __name__ == '__main__':
    mailHeader = raw_input("Header: ")
    mailText = raw_input("Body: ")

    mailInfo['mailtext'] = mailText
    mailInfo['mailsubject'] = mailHeader

    smtp = SMTP_SSL(mailInfo["hostname"])
    smtp.set_debuglevel(1)
    smtp.ehlo(mailInfo["hostname"])
    smtp.login(mailInfo["username"], mailInfo["password"])

    msg = MIMEText(mailInfo["mailtext"], "text", mailInfo["mailencoding"])
    msg["Subject"] = Header(mailInfo["mailsubject"], mailInfo["mailencoding"])
    msg["from"] = mailInfo["from"]
    msg["to"] = mailInfo["to"]
    smtp.sendmail(mailInfo["from"], mailInfo["to"], msg.as_string())

    smtp.quit()


"""
    Second case, simply sending mail. Use SMTP function.
"""
# from email import encoders
# from email.header import Header
# from email.mime.text import MIMEText
# from email.utils import parseaddr, formataddr
#
# import smtplib
#
#
# def _format_addr(s):
#     name, addr = parseaddr(s)
#     return formataddr((Header(name, 'utf-8').encode(), addr))
#
# from_addr = raw_input('From: ')
# password = raw_input('Password: ')
# to_addr = raw_input('To: ')
# smtp_server = raw_input('SMTP server: ')
#
#
# # Information is come from user's input.
# msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
# msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
# msg['To'] = _format_addr('管理员 <%s>' % to_addr)
# msg['Subject'] = Header('来自SMTP的问候……', 'utf-8').encode()
#
# server = smtplib.SMTP(smtp_server, 25)
# server.set_debuglevel(1)
# server.login(from_addr, password)
# server.sendmail(from_addr, [to_addr], msg.as_string())
# server.quit()

"""
    Third case, sending mail with files. Using MIMEMultipart class.
"""
# from email import encoders
# from email.header import Header
# from email.mime.text import MIMEText
# from email.utils import parseaddr, formataddr
# from email.mime.multipart import MIMEMultipart, MIMEBase
#
# import smtplib
#
#
# def _format_addr(s):
#     name, addr = parseaddr(s)
#     return formataddr((Header(name, 'utf-8').encode(), addr))
#
# from_addr = raw_input('From: ')
# password = raw_input('Password: ')
# to_addr = raw_input('To: ')
# smtp_server = raw_input('SMTP server: ')
#
# msg = MIMEMultipart()
# msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
# msg['To'] = _format_addr('管理员 <%s>' % to_addr)
# msg['Subject'] = Header('来自SMTP的问候……', 'utf-8').encode()
#
# # Main text is a MIMEText class.
# msg.attach(MIMEText('send with file...', 'plain', 'utf-8'))
#
# # Adding file is creating a MIMEBase class, add a picture:
# with open('/Users/breadtrip/Downloads/test.png', 'rb') as f:
#     # Set the file's name and type
#     mime = MIMEBase('image', 'png', filename='test.png')
#     # Add some important header information
#     mime.add_header('Content-Disposition', 'attachment', filename='test.png')
#     mime.add_header('Content-ID', '<0>')
#     mime.add_header('X-Attachment-Id', '0')
#     # Read the file's information
#     mime.set_payload(f.read())
#     # Decode using base64
#     encoders.encode_base64(mime)
#     # Add the file into the MIMEMultipart class
#     msg.attach(mime)
#
# server = smtplib.SMTP(smtp_server, 25)
# server.set_debuglevel(1)
# server.login(from_addr, password)
# server.sendmail(from_addr, [to_addr], msg.as_string())
# server.quit()
