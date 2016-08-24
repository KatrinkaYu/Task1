import re
from fixture.orm import ORMFixture
from model.contact import Contact

db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

def test_contacts_on_homepage(app):
    contacts_from_homepage = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    contacts_from_db = sorted(get_contacts_from_db(), key=Contact.id_or_max)
    if len(contacts_from_homepage)==len(contacts_from_db):
        for all in range(len(contacts_from_homepage)):
            assert contacts_from_homepage[all].name == contacts_from_db[all].name
            assert contacts_from_homepage[all].last_name == contacts_from_db[all].last_name
            assert contacts_from_homepage[all].address == contacts_from_db[all].address
            assert contacts_from_homepage[all].all_phones_from_homepage == contacts_from_db[all].all_phones_from_homepage
            assert contacts_from_homepage[all].all_emails_from_homepage == contacts_from_db[all].all_emails_from_homepage
    else:
        False

def clear(s):
    return re.sub("[() -]", "", s)

def merge_phones_like_on_homepage(contact):
    return "\n".join(filter(lambda x: x!="",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None, [contact.home_telephone, contact.mobile_telephone,
                                                                 contact.work_telephone, contact.phone2]))))

def merge_emails_like_on_homepage(contact):
    return "\n".join(filter(lambda x: x!="",
                                filter(lambda x: x is not None, [contact.email, contact.email2,
                                                                 contact.email3])))
def get_contacts_from_db():
    contacts_db = []
    for i in db.get_contactlist():
        contacts_db.append(Contact(last_name=i.last_name, name=i.name, address=i.address,
                                          all_emails_from_homepage=merge_emails_like_on_homepage(i),
                                          all_phones_from_homepage=merge_phones_like_on_homepage(i), id=i.id))
    return list(contacts_db)