from website.models import *
from django.contrib import admin

class PageAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

class TourAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Page, PageAdmin)    
admin.site.register(Tour, TourAdmin)
admin.site.register(GalleryImage)



