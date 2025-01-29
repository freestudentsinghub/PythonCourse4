from django.contrib import admin

# Register your models here.
from .models import Message, Campaign
# Register your models here.

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'topic',)
    search_fields = ('topic',)


@admin.register(Campaign)
class CampaignAdmin(admin.ModelAdmin):
    list_display = ('id', 'status',)
    search_fields = ('status',)