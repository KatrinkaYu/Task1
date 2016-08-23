import mysql.connector
from model.group import Group
from model.contact import Contact

class DbFixture:
    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = mysql.connector.connect(host=host, database=name, user=user, password=password)
        self.connection.autocommit = True

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, middlename, lastname, nickname, company, title, address, home, mobile, work, email, email2, email3, byear, address2, phone2, created, modified, deprecated from addressbook")
            for row in cursor:
                (id, firstname, middlename, lastname, nickname, company, title, address, home, mobile, work, email, email2, email3, byear, address2, phone2, created, modified, deprecated) = row
                if not deprecated:
                    list.append(Contact(id=str(id), name=firstname, middle_name=middlename,last_name=lastname,nickname=nickname,
                                    title=title, company=company, address=address, home_telephone=home,mobile_telephone=mobile,
                                    work_telephone=work, email=email, email2=email2, email3=email3, year=byear,
                                    address2=address2, phone2=phone2, modified=modified))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()