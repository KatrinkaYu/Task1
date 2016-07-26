
class GroupHelper:

    def __init__(self, app):
        self.app = app

    def create(self, group):
        wd = self.app.wd
        # go to group page
        wd.find_element_by_link_text("groups").click()
        # init group creation
        wd.find_element_by_name("new").click()
        # fill group form
        self.fill_form(group)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_group_page()

    def delete_first(self):
        wd = self.app.wd
        # go to group page
        wd.find_element_by_link_text("groups").click()
        #select first group
        wd.find_element_by_name("selected[]").click()
        #submit deletion
        wd.find_element_by_name("delete").click()
        self.return_to_group_page()

    def change_first(self, new_group_data):
        wd = self.app.wd
        # go to group page
        wd.find_element_by_link_text("groups").click()
        self.select_first_group()
        # open change form
        wd.find_element_by_name("edit").click()
        # fill group form
        self.fill_form(new_group_data)
        # submit group change
        wd.find_element_by_name("update").click()
        self.return_to_group_page()

    def select_first_group(self):
        wd = self.app.wd
        # select first group
        wd.find_element_by_name("selected[]").click()

    def fill_form(self, group):
        wd = self.app.wd
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def return_to_group_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()


