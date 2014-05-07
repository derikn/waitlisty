from django.contrib import admin
from waitlisty.models import Family
from waitlisty.models import Parent
from waitlisty.models import Centre
from waitlisty.models import Child
from waitlisty.models import Application


class CentreAdmin(admin.ModelAdmin):
    fieldsets = [
        ('General Information', {'fields': ['name',
        									'address',
        									'hours',
        									'phone_number',
        									'services',
        									'supervisor',
        									'info']}),

        ('Date Information', {'fields': ['pub_date']}),
    ]

admin.site.register(Family)
admin.site.register(Parent)
admin.site.register(Centre, CentreAdmin)
admin.site.register(Child)
admin.site.register(Application)
