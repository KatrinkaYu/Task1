# -*- coding: utf-8 -*-
from model.contact import Contact
from random import randrange


def test_change_some_contact_names(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(name="contact", middle_name="middle_name", last_name="last_name",
                                   nickname="nickname", title="title", company="company", address="address",
                                   home_telephone="123456", mobile_telephone="234567", work_telephone="345678",
                                   email="mail@qwerty.com", year="2000", address2="address", phone2="12"))

    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(name="change_new_contact", middle_name="change_contact_middle_name", last_name="change_contact_last_name")
    contact.id = old_contacts[index].id
    app.contact.change_by_index(index, contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

def test_change_first_contact_phones(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(name="contact", middle_name="middle_name", last_name="last_name",
                                   nickname="nickname", title="title", company="company", address="address",
                                   home_telephone="123456", mobile_telephone="234567", work_telephone="345678",
                                   email="mail@qwerty.com", year="2000", address2="address", phone2="12"))

    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(home_telephone="923456", mobile_telephone="934567", work_telephone="945678")
    contact.id = old_contacts[index].id
    contact.last_name = old_contacts[index].last_name
    contact.name = old_contacts[index].name
    app.contact.change_by_index(index, contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)