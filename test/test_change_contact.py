# -*- coding: utf-8 -*-
from model.contact import Contact
import random

def test_change_some_contact_names(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(name="contact", middle_name="middle_name", last_name="last_name",
                                   nickname="nickname", title="title", company="company", address="address",
                                   home_telephone="123456", mobile_telephone="234567", work_telephone="345678",
                                   email="mail@qwerty.com", year="2000", address2="address", phone2="12"))

    old_contacts = db.get_contact_list()
    old_contact = random.choice(old_contacts)
    id = old_contact.id
    contact = Contact(name="change_new_contact", middle_name="change_contact_middle_name", last_name="change_contact_last_name")
    contact.id = id
    app.contact.change_by_id(contact.id, contact)
    new_contacts = db.get_contact_list()
    old_contacts.insert(old_contacts.index(old_contact), contact)
    old_contacts.remove(old_contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)

def test_change_first_contact_phones(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(name="contact", middle_name="middle_name", last_name="last_name",
                                   nickname="nickname", title="title", company="company", address="address",
                                   home_telephone="123456", mobile_telephone="234567", work_telephone="345678",
                                   email="mail@qwerty.com", year="2000", address2="address", phone2="12"))

    old_contacts = db.get_contact_list()
    old_contact = random.choice(old_contacts)
    id = old_contact.id
    contact = Contact(home_telephone="923456", mobile_telephone="934567", work_telephone="945678")
    contact.id = id
    contact.last_name = old_contact.last_name
    contact.name = old_contact.name
    app.contact.change_by_id(id, contact)
    new_contacts = db.get_contact_list()
    old_contacts.insert(old_contacts.index(old_contact), contact)
    old_contacts.remove(old_contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)