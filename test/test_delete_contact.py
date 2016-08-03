# -*- coding: utf-8 -*-

from model.contact import Contact

def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(name="contact", middle_name="middle_name", last_name="last_name",
                                   nickname="nickname", title="title", company="company", address="address",
                                   home_telephone="123456", mobile_telephone="234567", work_telephone="345678",
                                   email="mail@qwerty.com", year="2000", address2="address", phone2="12"))
    old_contacts = app.contact.get_contact_list()
    app.contact.delete_first()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts[0:1] = []
    assert old_contacts == new_contacts
