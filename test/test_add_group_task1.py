# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group_task1(app):
    app.group.create(Group(name="group_task1", header="new_group", footer="new_group"))

def test_add_empty_group_task1(app):
    app.group.create(Group(name="", header="", footer=""))
