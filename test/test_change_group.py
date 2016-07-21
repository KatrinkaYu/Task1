# -*- coding: utf-8 -*-
from model.group import Group


def test_change_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.change_first(Group(name="change_group", header="change_new_group", footer="change_new_group"))
    app.session.logout()