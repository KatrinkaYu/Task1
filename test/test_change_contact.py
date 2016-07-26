# -*- coding: utf-8 -*-
from model.contact import Contact


def test_change_first_contact_names(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(name="contact", middle_name="middle_name", last_name="last_name",
                                   nickname="nickname", title="title", company="company", address="address",
                                   home_telephone="123456", mobile_telephone="234567", work_telephone="345678",
                                   email="mail@qwerty.com", year="2000", address2="address", phone2="12"))
    app.contact.change_first(Contact(name="change_new_contact", middle_name="change_contact_middle_name", last_name="change_contact_last_name"))

def test_change_first_contact_phones(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(name="contact", middle_name="middle_name", last_name="last_name",
                                   nickname="nickname", title="title", company="company", address="address",
                                   home_telephone="123456", mobile_telephone="234567", work_telephone="345678",
                                   email="mail@qwerty.com", year="2000", address2="address", phone2="12"))
    app.contact.change_first(Contact(home_telephone="923456", mobile_telephone="934567", work_telephone="945678"))