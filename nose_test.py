#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 19:17:18 2017
A testing module as requested by Verne Global.
@author: malapradej
"""
import nose
import function

def test_check_true():
    network1 = "1.0.0.0/32"
    network2 = "192.168.1.0/24"
    networks = [network1, network2]
    ip = "192.168.1.2"
    assert function.check(networks, ip)

def test_check_false():
    network1 = "1.0.0.0/32"
    network2 = "192.168.1.0/24"
    networks = [network1, network2]
    ip = "192.168.2.0"
    assert not(function.check(networks, ip))
    
def test_subset():
    network1 = "1.0.0.0/32"
    network2 = "192.168.1.0/24"
    network3 = "192.168.0.0/16"
    networks = [network1, network2, network3]
    expected = [network1, network3]
    assert function.subset(networks) == expected