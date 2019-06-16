from django.contrib import admin
from . import models

# Register your models here.

from main.helpers import auto_admin
auto_admin(models)