import smtplib
from email.message import EmailMessage


password = "slcqlmgmvterfpma"
from_email = "jadryshnikov.artur@yandex.ru"
to_email = "yadryshnikovartour@yandex.ru"
title_message = "Тест"


message = EmailMessage()
message.set_content("Привет Python")
message["Subject"] = title_message
message["From"] = from_email
message["To"] = to_email

server = None
try:
    server = smtplib.SMTP_SSL("smtp.yandex.ru", 465)
    server.login(from_email, password)
    server.send_message(message)
    print(f"Письмо с темой \"{title_message}\" отправлено.")
except Exception as e:
    print(f"Ошибка: {e}")
finally:
    if server:
        server.quit()

