from django.contrib import admin

from .models import Game, Player

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('uid', 'is_active', 'players')

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('token', 'x_position', 'y_position')
