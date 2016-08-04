# -*- coding: utf-8 -*-
from model.group import Group
from random import randrange

def test_change_some_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="group", header="new", footer="new_1"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="change_group")
    group.id = old_groups[index].id
    app.group.change_by_index(index, group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

def test_change_some_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="group", header="new", footer="new_1"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(header="change_new_group")
    group.id = old_groups[index].id
    group.name = old_groups[index].name
    app.group.change_by_index(index, group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)