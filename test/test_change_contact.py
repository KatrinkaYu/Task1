# -*- coding: utf-8 -*-
from model.contact import Contact


def test_change_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.change_first(Contact(name="change_new_contact", middle_name="change_contact_middle_name", last_name="change_contact_last_name",
                                     nickname="change_contact_nickname", title="change_contact_title", company="change_contact_company",
                                     address="change_contact_address", home_telephone="923456", mobile_telephone="934567", work_telephone="945678",
                                     email="change_mail@qwerty.com", year="2009", address2="change_address", phone2="92"))
    app.session.logout()