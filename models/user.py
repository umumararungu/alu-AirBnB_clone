#!/usr/bin/python3
"""
Module for the User Class.
"""
from models.base_model import BaseModel

class User(BaseModel):
    """
    Class User that handles users' information
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""