from django.contrib import admin

from core.models import Comment, Joke, Level, Reaction, Roast, UserProfile

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Joke)
admin.site.register(Roast)
admin.site.register(Reaction)
admin.site.register(Level)
admin.site.register(Comment)
