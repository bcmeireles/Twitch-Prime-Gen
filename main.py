import handlers.amazon_handler as amazon
import handlers.mail_handler as mail
import time

def main():
    email = mail.gen_email()

    a = amazon.create_driver()
    amazon.register_page(a)

    time.sleep(2)

    amazon.fill_register(a, {"name": "Magoz Puta", "email": email, "password": "Pila1234"})

    time.sleep(2)

    amazon.captcha(a)

    time.sleep(2)

    inbox = mail.get_inbox(email)

    time.sleep(3)

    id = mail.get_id(inbox)

    email = mail.retrieve_email(email, id)

    c = mail.parse_otp(email)

    print(c)

    input()

    amazon.fill_po(a, "cvf_phone_cc_native_169", "123456789")

    input()

if __name__ == "__main__":
    main()
