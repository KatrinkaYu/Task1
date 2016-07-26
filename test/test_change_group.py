# -*- coding: utf-8 -*-
from model.group import Group


def test_change_first_group_name(app):
    app.group.change_first(Group(name="change_group"))

def test_change_first_group_header(app):
    app.group.change_first(Group(header="change_new_group"))