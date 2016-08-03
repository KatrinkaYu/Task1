# -*- coding: utf-8 -*-
from model.group import Group


def test_change_first_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="group", header="new", footer="new_1"))
    old_groups = app.group.get_group_list()
    group = Group(name="change_group")
    group.id = old_groups[0].id
    app.group.change_first(group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

def test_change_first_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="group", header="new", footer="new_1"))
    old_groups = app.group.get_group_list()
    group = Group(header="change_new_group")
    group.id = old_groups[0].id
    group.name = old_groups[0].name
    app.group.change_first(group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)