
from model.contact import Contact
import re

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        self.go_to_page_add_new()
        # fill contact form
        self.fill_form(contact)
        # submit contact creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.contact_cache = None

    def go_to_page_add_new(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/edit.php") and len(wd.find_elements_by_name("submit")) > 0):
            wd.find_element_by_link_text("add new").click()

    def change_first(self, new_contact_data):
        self.change_by_index(0, new_contact_data)

    def change_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.go_to_homepage()
        # submit change
        text = "//table[@id='maintable']/tbody/tr[%s]/td[8]/a/img" %(2+index)
        wd.find_element_by_xpath(text).click()
        # fill contact form
        self.fill_form(new_contact_data)
        # submit contact change
        wd.find_element_by_name("update").click()
        self.go_to_homepage()
        self.contact_cache = None

    def delete_first(self):
        self.delete_by_index(0)

    def delete_by_index(self, index):
        wd = self.app.wd
        self.go_to_homepage()
        self.select_contact_by_index(index)
        # submit deletion
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        self.go_to_homepage()
        self.contact_cache = None

    def select_contact_by_index(self, index):
        wd = self.app.wd
        # select first group
        wd.find_elements_by_name("selected[]")[index].click()

    def go_to_homepage(self):
        wd = self.app.wd
        # go to home page
        if not (wd.current_url.endswith("/addressbook/") and len(wd.find_elements_by_name("add")) > 0):
            wd.find_element_by_link_text("home").click()

    def fill_form(self, contact):
        wd = self.app.wd
        # fill contact form
        self.change_field_value("firstname",contact.name)
        self.change_field_value("middlename", contact.middle_name)
        self.change_field_value("lastname", contact.last_name)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.home_telephone)
        self.change_field_value("mobile", contact.mobile_telephone)
        self.change_field_value("work", contact.work_telephone)
        self.change_field_value("email", contact.email)
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[3]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[3]").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[2]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[2]").click()
        self.change_field_value("byear", contact.year)
        self.change_field_value("address2", contact.address2)
        self.change_field_value("phone2", contact.phone2)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def count(self):
        wd = self.app.wd
        self.go_to_homepage()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.go_to_homepage()
            self.contact_cache = []
            for element in wd.find_elements_by_name("entry"):
                info = element.find_elements_by_tag_name("td")
                name = info[2].text
                last_name = info[1].text
                address = info[3].text
                id = info[0].find_element_by_tag_name("input").get_attribute("value")
                all_emails = info[4].text
                all_phones = info[5].text
                self.contact_cache.append(Contact(last_name=last_name, name=name, address=address,
                                                  all_emails_from_homepage=all_emails,
                                                  all_phones_from_homepage=all_phones, id=id))
        return list(self.contact_cache)

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        name = wd.find_element_by_name("firstname").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        last_name = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        home_telephone = wd.find_element_by_name("home").get_attribute("value")
        mobile_telephone = wd.find_element_by_name("mobile").get_attribute("value")
        work_telephone = wd.find_element_by_name("work").get_attribute("value")
        phone2 = wd.find_element_by_name("phone2").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        return Contact(name=name, last_name=last_name, id=id, address=address, home_telephone=home_telephone,
                       mobile_telephone=mobile_telephone,work_telephone=work_telephone,phone2=phone2,
                       email=email, email2=email2, email3=email3)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.go_to_homepage()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        home_telephone = re.search("H: (.*)", text).group(1)
        work_telephone = re.search("W: (.*)", text).group(1)
        mobile_telephone = re.search("M: (.*)", text).group(1)
        phone2 = re.search("P: (.*)", text).group(1)
        return Contact(home_telephone=home_telephone, mobile_telephone=mobile_telephone,
                       work_telephone=work_telephone, phone2=phone2)

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.go_to_homepage()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

