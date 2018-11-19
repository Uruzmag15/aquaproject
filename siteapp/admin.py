from django.contrib import admin
from .models import Brand, Tara, Drink


class TaraAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields': ['brand', 'material', 'volume', 'photo', 'storage']}),
		('Информация об упаковке', {'fields': ['pack_length', 'pack_width', 'pack_height', 'pack_quant', 'pack_weight']}),
		('Информация о поддонах', {'fields': ['pallet_length', 'pallet_width', 'pallet_quant', 'pallet_weight_bru',
			'pallet_weight_net']})
	]

	list_display = ('brand', 'material', 'volume')
	list_display_links = ('brand', 'material', 'volume')
	list_filter = ('brand', 'material', 'volume')
	ordering = ('brand', 'volume')


class DrinkAdmin(admin.ModelAdmin):
	list_display = ('brand', 'tara', 'taste')
	list_display_links = ('brand', 'tara', 'taste')
	list_filter = ('brand', 'tara', 'taste')
	ordering = ('brand', 'tara')

admin.site.register(Brand)
admin.site.register(Tara, TaraAdmin)
admin.site.register(Drink, DrinkAdmin)
