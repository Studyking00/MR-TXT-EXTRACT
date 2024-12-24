#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7366398941:AAF_pQNIvUrjajCZc4bM0GBW6obLd_3srGk")
    API_ID = int(os.environ.get("API_ID", "20130231"))
    API_HASH = os.environ.get("API_HASH", "695a139ecb2964273a6489b907f4ae0b")
    AUTH_USERS = os.environ.get("AUTH_USERS", "6391221938")
