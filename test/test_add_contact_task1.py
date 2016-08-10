# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string

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
                    address2=random_string("address2", 15), phone2=random_numbers(10)) for i in range(5)]

@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])

def test_add_contact_task1(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)



