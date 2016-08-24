
from pony.orm import *
from datetime import datetime
from model.group import Group
from model.contact import Contact
from pymysql.converters import decoders


class ORMFixture:
    db = Database()

    class ORMGroup(db.Entity):
        _table_ = 'group_list'
        id = PrimaryKey(int, column='group_id')
        name = Optional(str, column='group_name')
        header = Optional(str, column='group_header')
        footer = Optional(str, column='group_footer')

    class ORMContact(db.Entity):
        _table_ = 'addressbook'
        id = PrimaryKey(int, column='id')
        first_name = Optional(str, column='firstname')
        middle_name = Optional(str, column='middlename')
        last_name = Optional(str, column='lastname')
        nickname = Optional(str, column='nickname')
        title = Optional(str, column='title')
        company = Optional(str, column='company')
        address = Optional(str, column='address')
        home_telephone = Optional(str, column='home')
        mobile_telephone = Optional(str, column='mobile')
        work_telephone = Optional(str, column='work')
        email = Optional(str, column='email')
        email2 = Optional(str, column='email2')
        email3 = Optional(str, column='email3')
        year = Optional(str, column='byear')
        address2 = Optional(str, column='address2')
        phone2 = Optional(str, column='phone2')
        deprecated = Optional(datetime, column='deprecated')

    def __init__(self, host, name, user, password):
        self.db.bind('mysql', host = host, database = name, user = user, password = password, conv=decoders)
        self.db.generate_mapping()
        sql_debug(True)

    def convert_groups_to_model(self, groups):
        def convert(group):
            return Group(id=str(group.id), name=group.name, header=group.header, footer=group.footer)
        return list(map(convert, groups))

    def convert_contacts_to_model(self, contacts):
        def convert(contact):
            return Contact(id=str(contact.id), name=contact.first_name, middle_name=contact.middle_name,
                           last_name=contact.last_name,nickname=contact.nickname, title=contact.title,
                           company=contact.company, address=contact.address, home_telephone=contact.home_telephone,
                           mobile_telephone=contact.mobile_telephone, work_telephone=contact.work_telephone,
                           email=contact.email, email2=contact.email2, email3=contact.email3, year=contact.year,
                           address2=contact.address2, phone2=contact.phone2)

        return list(map(convert, contacts))

    @db_session
    def get_grouplist(self):
        return self.convert_groups_to_model(select(g for g in ORMFixture.ORMGroup))

    @db_session
    def get_contactlist(self):
        return self.convert_contacts_to_model(select(c for c in ORMFixture.ORMContact if c.deprecated is None))

