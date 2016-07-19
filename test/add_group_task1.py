# -*- coding: utf-8 -*-
import pytest
from fixture.application import Application
from model.group import Group


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_group_task1(app):
        app.session.login(username="admin", password="secret")
        app.group.create(Group(name="group_task1", header="new_group", footer="new_group"))
        app.session.logout()

def test_add_empty_group_task1(app):
        app.session.login(username="admin", password="secret")
        app.group.create(Group(name="", header="", footer=""))
        app.session.logout()
