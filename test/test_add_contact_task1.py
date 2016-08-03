# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact_task1(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(name="new_contact", middle_name="contact_middle_name", last_name="contact_last_name",
                               nickname="contact_nickname", title="contact_title", company="contact_company",
                               address="contact_address", home_telephone="123456", mobile_telephone="234567",
                               work_telephone="345678", email="mail@qwerty.com", year="2000", address2="address", phone2="12")
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(name="new_contact_1", middle_name="contact_middle_name_1", last_name="contact_last_name_1",
                               nickname="contact_nickname_1", title="contact_title_1", company="contact_company_1",
                               address="contact_address_1", home_telephone="1234567", mobile_telephone="2345678",
                               work_telephone="3456789", email="mail_1@qwerty.com", year="2001", address2="address_1",
                               phone2="123")
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

