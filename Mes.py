import smtplib
from email.message import EmailMessage
from tkinter import *
from tkinter import messagebox as mb

#password = "slcqlmgmvterfpma"
#from_email = "jadryshnikov.artur@yandex.ru"
#to_email = "yadryshnikovartour@yandex.ru"

def send_message():
    password = pass_entry.get()
    from_email = from_email_entry.get()
    to_email = to_email_entry.get()
    title_message = subject_entry.get()
    text_message = message_entry.get(1.0, END)

    message = EmailMessage()
    message.set_content(text_message)
    message["Subject"] = title_message
    message["From"] = from_email
    message["To"] = to_email

    server = None
    try:
        server = smtplib.SMTP_SSL("smtp.yandex.ru", 465)
        server.login(from_email, password)
        server.send_message(message)
        mb.showinfo(title="Отправка Email", message=f"Сообщение с темой \"{title_message}\" успешно отправлено")
    except Exception as e:
        mb.showerror(title="Ошибка", message=f"Ошибка: {e}")
    finally:
        if server:
            server.quit()

window = Tk()
window.title("Отправка сообщений")
window.geometry("600x420")

text_from = Label(window, text="Отправитель:", font=("Arial", 16))
text_from.grid(row=0, column=0, pady=10)
from_email_entry = Entry(window, font=("Arial", 16), width=30)
from_email_entry.grid(row=0, column=1, pady=10)

text_to = Label(window, text="Получатель:", font=("Arial", 16))
text_to.grid(row=1, column=0, pady=10)
to_email_entry = Entry(window, font=("Arial", 16), width=30)
to_email_entry.grid(row=1, column=1, pady=10)

text_pass = Label(window, text="Пароль для связи:", font=("Arial", 16))
text_pass.grid(row=2, column=0, pady=10)
pass_entry = Entry(window, font=("Arial", 16), width=30)
pass_entry.grid(row=2, column=1, pady=10)

text_subject = Label(window, text="Тема сообщения:", font=("Arial", 16))
text_subject.grid(row=3, column=0, pady=10)
subject_entry = Entry(window, font=("Arial", 16), width=30)
subject_entry.grid(row=3, column=1, pady=10)

text_message = Label(window, text="Введите сообщение: ", font=("Arial", 16))
text_message.grid(row=4, column=0, pady=10)
message_entry = Text(window, width=30, height=6, font=("Arial", 16))
message_entry.grid(row=4, column=1, pady=10)

btn = Button(window, text="Отправить", font=("Arial", 16), command=send_message)
btn.grid(row=5, column=1)

window.mainloop()
