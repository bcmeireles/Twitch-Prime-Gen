import requests
import random, string

BASE = "https://www.1secmail.com/api/v1/"
working_domains = ["wwjmp.com",
                   "esiix.com",
                   "xojxe.com",
                   "yoggm.com"]

def random_string(length):
  return ''.join(random.choice(string.ascii_letters) for i in range(length))

def gen_email():
  return random_string(random.randint(10, 15)) + "@" + random.choice(working_domains)

def get_inbox(email):
  user, domain = email.split("@")
  return requests.get(f"{BASE}?action=getMessages&login={user}&domain={domain}").json()

def check_mail(inbox):
  if len(inbox) > 0:
    return True
  else:
    return False

def get_id(inbox):
  return inbox[0]["id"]

def retrieve_email(email, id):
  user, domain = email.split("@")
  return requests.get(f"{BASE}?action=readMessage&login={user}&domain={domain}&id={id}").json()["body"]
  

def parse_otp(content):
  locate = content.find('<p class="otp">')
  return content[locate + 15: locate + 21]
