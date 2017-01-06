from django.contrib import admin

# Register your models here
from .models import Content, Article, Company

class ContentAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}

class ArticleAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, { 'fields': ['title']}),
        (None, { 'fields': ['subtitle']}),
        (None, { 'fields': ['pub_date']}),
        ('Company', { 'fields': ['company'], 'classes': ['collapse']}),
        (None, { 'fields': ['text']}),
        (None, { 'fields': ['image']}),
        (None, { 'fields': ['style']}),
        (None, { 'fields': ['imagefile']})
    ]
    list_display = ('title', 'subtitle', 'pub_date', 'imagefile')
    list_filter = ['pub_date']
    search_fields = ['title', 'subtitle']
class CompanyAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, { 'fields': ['name']}),
    ]
    list_display = ['name']

admin.site.register(Content, ContentAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Company, CompanyAdmin)