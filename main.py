import handlers.amazon_handler as amazon
import handlers.mail_handler as mail
import handlers.twitch_handler as twitch
import time

def main():
    a = amazon.create_driver()
    twitch.registerPage(a)

    time.sleep(3)

    twitch.fillRegiser(a)

    input()

    twitch.fillEmail(a, "vudconisnhs@gmail.com")

    input()


def main2():
    email = mail.gen_email()

    a = amazon.create_driver()
    amazon.register_page(a)

    time.sleep(2)

    amazon.fill_register(a, {"name": "Teste Teste", "email": email, "password": "Teste1234"})

    time.sleep(2)

    if amazon.check_error(a):
        print("ERROR")
        amazon.destroy_driver(a)
        exit()

    amazon.captcha(a)

    time.sleep(2)

    inbox = mail.get_inbox(email)

    while mail.check_mail(inbox, 0):
        continue

    id = mail.get_id(inbox)

    email = mail.retrieve_email(email, id)

    c = mail.parse_otp(email)

    amazon.fill_otp(a, c)

    amazon.fill_po(a, "cvf_phone_cc_native_169", "123456789")

    input()

if __name__ == "__main__":
    main()