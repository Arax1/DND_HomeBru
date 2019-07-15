from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Race)
admin.site.register(Class)
admin.site.register(Background)
admin.site.register(Character)
admin.site.register(Trait)
admin.site.register(RaceTrait)
admin.site.register(BackgroundTrait)
