#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 14:47:31 2023

@author: alessandrorabbi
"""

from cryptography.fernet import Fernet
key= Fernet.generate_key()
# just show the key
print(key)
