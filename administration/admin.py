from django.contrib import admin

from .models import RT, RW, Anggota, Pengurus

# Register your models here.
admin.site.register(RT)
admin.site.register(RW)
admin.site.register(Anggota)
admin.site.register(Pengurus)