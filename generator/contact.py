from model.contact import Contact
import random
import string
import os.path
import json
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])
def random_email(maxlen):
    symbols = string.ascii_letters + string.digits
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))]) + "@qwerty.com"
def random_numbers(maxlen):
    symbols = string.digits
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Contact(name=random_string("name", 15), middle_name=random_string("middle_name", 15),
                    last_name=random_string("last_name", 15),nickname=random_string("nickname", 15),
                    title=random_string("title", 15), company=random_string("company", 15),
                    address=random_string("address", 15), home_telephone=random_numbers(10),
                    mobile_telephone=random_numbers(10), work_telephone=random_numbers(10), email=random_email(10),
                    email2=random_email(10), email3=random_email(10), year=random_numbers(4),
                    address2=random_string("address2", 15), phone2=random_numbers(10)) for i in range(n)]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)
with open(file, "w") as document:
    document.write(json.dumps(testdata, default=lambda x: x.__dict__, indent=2))