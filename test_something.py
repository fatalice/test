# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 16:50:57 2019

@author: jihong
"""

import pytest

def username(username):
    return "override-"+username

def test_username(username):
    assert username == "override-hujun"
    
