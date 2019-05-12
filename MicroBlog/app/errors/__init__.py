#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# filename: .py
# author: jiangheng
# description:
# questions:
from flask import Blueprint

bp = Blueprint('errors', __name__)

from app.errors import handlers