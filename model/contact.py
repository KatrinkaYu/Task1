from  sys import maxsize

class Contact:
    def __init__(self, name=None, middle_name=None, last_name=None, nickname=None, title=None, company=None, address=None,
                 home_telephone=None, mobile_telephone=None, work_telephone=None, email=None, year=None, address2=None, phone2=None, id=None):
        self.name = name
        self.middle_name = middle_name
        self.last_name = last_name
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.home_telephone = home_telephone
        self.mobile_telephone = mobile_telephone
        self.work_telephone = work_telephone
        self.email = email
        self.year = year
        self.address2 = address2
        self.phone2 = phone2
        self.id = id

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.name == other.name and self.last_name == other.last_name

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize