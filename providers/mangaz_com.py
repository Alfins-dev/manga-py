#!/usr/bin/python3
# -*- coding: utf-8 -*-

from lxml.html import document_fromstring
import re
# import json


def get_main_content(url, get=None, post=None):
    """
    :param url: str
    :param get: request.get
    :param post: request.post
    :return: mixed (1)
    """
    pass


def get_volumes(content=None, url=None, get=None, post=None):
    """
    :param content: mixed (1)
    :param url: str
    :return: array (2)
    """
    pass


def get_archive_name(volume, index: int = None):
    """
    :param volume: mixed (2)
    :param index: int
    :return: str
    """
    pass


def get_images(main_content=None, volume=None, get=None, post=None):
    """
    :param main_content: mixed (1)
    :param volume: mixed (2)
    :param get: request.get
    :param post: request.post
    :return: dict(str)
    """
    pass


def get_manga_name(url, get=None):
    """
    :param url: str
    :param get: request.get
    :return: str
    """
    pass
