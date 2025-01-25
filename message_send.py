import smtplib
from email.mime.text import MIMEText

html = '''
<h1 style="color:red">警告! 警告! 有人跌倒了</h1>
<h1 style="color:red">WARNING! SOMEONE IS FALLING</h1>
'''

mail = MIMEText(html, 'html', 'utf-8')   # plain 換成 html，就能寄送 HTML 格式的信件
mail['Subject']='WARNING! 警告'
mail['From']='creator'
mail['To']='binghantsai2008@gmail.com'

def send_mes():
    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    smtp.ehlo()
    smtp.starttls()
    smtp.login('binghantsai2008@gmail.com','skte miai pefy oadn') # 這裡的密碼是授權碼
    status = smtp.send_message(mail)
    smtp.quit()