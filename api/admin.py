from django.contrib import admin

# Register your models here.
from .models import TrainDetails, PnrDetails

admin.site.register(TrainDetails)
admin.site.register(PnrDetails)
