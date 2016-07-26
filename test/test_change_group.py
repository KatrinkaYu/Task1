# -*- coding: utf-8 -*-
from model.group import Group


def test_change_first_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="group", header="new", footer="new_1"))
    app.group.change_first(Group(name="change_group"))

def test_change_first_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="group", header="new", footer="new_1"))
    app.group.change_first(Group(header="change_new_group"))