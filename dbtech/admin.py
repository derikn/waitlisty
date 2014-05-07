from django.contrib import admin
from dbtech.models import Asset, Ticket, models
from django.forms import TextInput, Textarea

class TicketInline(admin.TabularInline):
	model = Ticket
	extra = 1
	fields = ('title','content','resolved','position')
	formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'20'})},	
        models.TextField: {'widget': Textarea(attrs={'rows':2, 'cols':40})},
	}
	classes = ('grp-collapse grp-open',)
	inline_classes = ('grp-collapse grp-open',)

class TicketAdmin(admin.ModelAdmin):
	list_display = ('title', 'content','resolved','created_date')
	
class AssetAdmin(admin.ModelAdmin):
	list_filter = ('model','model_details')
	fieldsets = [
		('General Information',	{'fields': ['model','model_details','colour']}),
		('User Information', {'fields': ['assigned_to','program']}),
		('Purchase Information', {'fields': ['purchase_date','purchase_price','bought_from','warranty_info']}),
		(None,	{'fields': ['status']}),
	]
	list_display = ('model','model_details','assigned_to','program','purchase_date','status')
	inlines = [TicketInline]
	search_fields = ['model','model_details','colour']
	date_hierarchy = 'created_date'
	
admin.site.register(Asset, AssetAdmin)
admin.site.register(Ticket, TicketAdmin)
