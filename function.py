#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 17:59:22 2017
A module with functions as requested by Verne Global.
@author: malapradej
"""

def check(networks, ip):
    '''A function that checks if an ip address is found within a list of 
    networks. Returns True if ip address is in the networks list, and 
    False if not.
    eg. check(["1.0.0.0/32", "192.168.1.0/24"], "192.168.1.0") will
        return True whereas
        check((["1.0.0.0/32", "192.168.1.0/24"], "192.168.2.0") will
        return False
    ===================================================================
    Arguments: <networks> - the list of networks, <ip> - the ip address to 
    check against networks. 
    Returns: True or False
    ===================================================================
    '''
    import ipaddress
    
    ip = ipaddress.ip_address(unicode(ip, "utf-8"))
    
    for network in networks:
        if ip in ipaddress.ip_network(unicode(network, "utf-8")):
            return True
        
    return False


def subset(subnets):
    '''A function that returns a subset of networks which subsumes the 
    original list. ie. removes all subnetworks of any network in the
    original list of networks.
    =================================================================
    Argument: <subnets> - the list of networks.
    Returns: <subset> - the list of subset of networks.    
    '''
    
    import ipaddress

    subnets_ = [ipaddress.ip_network(unicode(subnet, "utf-8")) for subnet in 
               subnets]
    
    indexes = []
    
    for i, subnet_ in enumerate(subnets_):
        temp_ = subnets_[:]
        temp_.pop(i)
        for t in temp_:
            if subnet_.subnet_of(t):
                indexes.append(i)
                break
    
    result = [i for j, i in enumerate(subnets) if j not in indexes]
    
    return result
        

    

