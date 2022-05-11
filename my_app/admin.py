from django.contrib import admin

from my_app.models import Friend


@admin.register(Friend)
class FriendAdmin(admin.ModelAdmin):
    list_display = [
        'nick_name',
        'first_name',
        'last_name',
        'likes',
        'dob',
        'lives_in',
    ]
    list_filter = [
        'nick_name',
        'first_name',
        'last_name',
        'likes',
        'dob',
        'lives_in',
    ]
    search_filter = [
        'nick_name',
        'first_name',
        'last_name',
        'likes',
        'dob',
        'lives_in',
    ]