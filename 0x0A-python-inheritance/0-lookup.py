#!/usr/bin/python3
"""Lookup module"""


def lookup(obj):
    """returns the list of available attributes and methods of an object"""
    return obj.__dict__
