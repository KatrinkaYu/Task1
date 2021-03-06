from model.contact import Contact
from model.group import Group
from fixture.orm import ORMFixture
import random

db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

group = Group(id="69")
def test_delete_contact_from_group(app):
    if len(db.get_contactlist()) == 0:
        app.contact.create(Contact(name="contact", middle_name="middle_name", last_name="last_name",
                                   nickname="nickname", title="title", company="company", address="address",
                                   home_telephone="123456", mobile_telephone="234567", work_telephone="345678",
                                   email="mail@qwerty.com", year="2000", address2="address", phone2="12"))
        new_contact = db.get_contactlist()[0]
        app.contact.add_contact_in_group(new_contact, group)
    elif len(db.get_contacts_in_group(group)) == 0:
        add_contact = random.choice(db.get_contacts_not_in_group(group))
        app.contact.add_contact_in_group(add_contact, group)

    old_contacts = db.get_contacts_in_group(group)
    contact = random.choice(db.get_contacts_in_group(group))
    app.contact.delete_contact_from_group(contact, group)
    new_contacts = db.get_contacts_in_group(group)
    old_contacts.remove(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)