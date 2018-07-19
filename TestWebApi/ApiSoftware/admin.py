from django.contrib import admin

from  ApiSoftware.modes import login_models

# Register your models here.
admin.site.register(login_models.tbl_user)
admin.site.register(login_models.tbl_verCode)
