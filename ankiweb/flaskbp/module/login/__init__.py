# -*- coding: utf-8 -*-
# @Author: Zengjq
# @Date:   2018-06-04 12:15:18
# @Last Modified by:   Zengjq
# @Last Modified time: 2018-06-04 14:48:22
from flask import Blueprint

bp_login = Blueprint('login', __name__)

from . import views
