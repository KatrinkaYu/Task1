import re
from random import randrange

def test_some_contact_on_homepage(app):
    index = randrange(app.contact.count())
    contact_from_homepage = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_homepage.name == contact_from_edit_page.name
    assert contact_from_homepage.last_name == contact_from_edit_page.last_name
    assert contact_from_homepage.address == contact_from_edit_page.address
    assert contact_from_homepage.all_phones_from_homepage == merge_phones_like_on_homepage(contact_from_edit_page)
    assert contact_from_homepage.all_emails_from_homepage == merge_emails_like_on_homepage(contact_from_edit_page)

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