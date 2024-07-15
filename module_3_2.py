def check_email(email):
    if  '@' in email  and ( '.com' in email or '.ru' in email or '.net' in email ):
        return True
    else:
        return False
def send_email(message, recipient, sender = 'university.help@gmail.com'):
    if check_email(recipient)  and   check_email(sender) and sender == recipient:
        print("Нельзя отправить письмо самому себе!")
        return
    if  check_email(recipient)  and   check_email(sender) and  sender == 'university.help@gmail.com':
        print('Письмо успешно отправлено с адреса', sender, 'на адрес', recipient)
        return
    if check_email(recipient) and check_email(sender) and sender != 'university.help@gmail.com':
        print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса", sender, "на адрес", recipient)
        return
    if check_email(recipient)  or  check_email(sender)   :
        print("Невозможно отправить письмо с адреса", sender, "на адрес", recipient)
        return


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')




