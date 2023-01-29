from django.contrib import admin
from . import models


admin.site.register(models.Tag)
admin.site.register(models.Profile)
admin.site.register(models.Project)
admin.site.register(models.Banner)

# admin.site.register(models.Comment)


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('headline', 'status', 'slug', 'author')
    prepopulated_fields = {'slug': ('headline',), }