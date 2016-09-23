# Code Reference: https://github.com/buckyroberts/Viberr
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Photo
# Register Photo Module so that it is available for population from admin panel as well
admin.site.register(Photo)