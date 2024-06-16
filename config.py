#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7288707966:AAE7WE5T77QJ7P-Mto9E2v_bRG7ejXR7vF8")
    API_ID = int(os.environ.get("API_ID", "27560342"))
    API_HASH = os.environ.get("API_HASH", "cd10f0b290f53f7c9a3f22c6cd788b60")
    AUTH_USERS = os.environ.get("AUTH_USERS", "7166894131")
