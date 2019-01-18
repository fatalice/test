# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 16:50:57 2019

@author: jihong
"""

import pytest


@pytest.mark.parametrize("username", username)
def username(username):
    return "override-"+username


@pytest.mark.parametrize("override-hujun", username)
def test_username(username):
    assert username == "override-hujun"
    
