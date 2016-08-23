# -*- coding: utf-8 -*-
from model.group import Group
import random


def test_change_some_group_name(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="group", header="new", footer="new_1"))
    old_groups = db.get_group_list()
    old_group = random.choice(old_groups)
    id = old_group.id
    group = Group(name="change_group")
    app.group.change_by_id(id, group)
    new_groups = db.get_group_list()
    group.id = id
    old_groups.insert(old_groups.index(old_group), group)
    old_groups.remove(old_group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

def test_change_some_group_header(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="group", header="new", footer="new_1"))
    old_groups = db.get_group_list()
    old_group = random.choice(old_groups)
    id = old_group.id
    group = Group(header="change_new_group")
    app.group.change_by_id(id, group)
    group.id =id
    group.name = old_group.name
    new_groups = db.get_group_list()
    old_groups.insert(old_groups.index(old_group), group)
    old_groups.remove(old_group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)