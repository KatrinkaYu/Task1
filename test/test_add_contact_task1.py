# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact_task1(app):

    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(name="new_contact", middle_name="contact_middle_name", last_name="contact_last_name",
                               nickname="contact_nickname", title="contact_title", company="contact_company",
                               address="contact_address", home_telephone="123456", mobile_telephone="234567",
                               work_telephone="345678", email="mail@qwerty.com", year="2000", address2="address", phone2="12"))
    app.session.logout()


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(name="new_contact_1", middle_name="contact_middle_name_1", last_name="contact_last_name_1",
                               nickname="contact_nickname_1", title="contact_title_1", company="contact_company_1",
                               address="contact_address_1", home_telephone="1234567", mobile_telephone="2345678",
                               work_telephone="3456789", email="mail_1@qwerty.com", year="2001", address2="address_1",
                               phone2="123"))
    app.session.logout()

