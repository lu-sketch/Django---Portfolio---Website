from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Poll, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3  # Provide space for adding three choices

class PollAdmin(admin.ModelAdmin):
    list_display = ('question', 'pub_date')
    inlines = [ChoiceInline]

admin.site.register(Poll, PollAdmin)
admin.site.register(Choice)
