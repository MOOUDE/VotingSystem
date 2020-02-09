from django.contrib import admin

# Register your models here.

from .models import Question,Choice

admin.site.site_header = "Questions System Admin"
admin.site.site_title  = "Questions Adminstration"
admin.site.index_title = "Welcome to Admin Area"
 

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields':['questionText'] }),
        ('Date Info',{'fields':['pubDate'],'classes':['collapse'],}),
    ]
    inlines = [ChoiceInline]

admin.site.register(Question,QuestionAdmin)
