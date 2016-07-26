# -*- coding: utf-8 -*-
from model.contact import Contact


def test_change_first_contact_names(app):
    app.contact.change_first(Contact(name="change_new_contact", middle_name="change_contact_middle_name", last_name="change_contact_last_name"))

def test_change_first_contact_phones(app):
    app.contact.change_first(Contact(home_telephone="923456", mobile_telephone="934567", work_telephone="945678"))