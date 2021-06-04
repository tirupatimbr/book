from django.contrib import admin
from bookapp.models import Books,Author,Products,Cart,Mobile,Profile,BaseImage
# Register your models here.

class BooksAdmin(admin.ModelAdmin):
    list_display =['Name','Author','Created_at','Published_at','Updated_at']
 
admin.site.register(Books,BooksAdmin)


class AuthorAmin(admin.ModelAdmin):
    list_display = ['Name','Age','Place']
admin.site.register(Author,AuthorAmin) 

class ProductsAdmin(admin.ModelAdmin):
    list_display = ['Book_name','Price','Stock','Available','Created_at','Published_at']
    list_filter = ['Available','Created_at','Updated_at']
    list_editable = ['Price','Stock','Available']
admin.site.register(Products,ProductsAdmin)

class CartAdmin(admin.ModelAdmin):
    list_display = ['title','user','book']
admin.site.register(Cart,CartAdmin)

class MobileAdmin(admin.ModelAdmin):
    list_display = ['brand','mobile_model','price','stock','available']
    list_filter = ['available']
    list_editable=['price','stock','available']
admin.site.register(Mobile,MobileAdmin)
admin.site.register(Profile)
admin.site.register(BaseImage)