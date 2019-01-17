# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 16:52:28 2019

@author: jihong
"""

import pytest

def username(username):
    return "override-else-"+username

def test_username(username):
    return username == "override-else-hujun"

