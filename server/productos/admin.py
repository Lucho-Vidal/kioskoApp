from django.contrib import admin

# Register your models here.
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'stock', 'cod_barras', 'descripcion', 'imagen')
    search_fields = ('nombre', 'cod_barras')
    list_filter = ('nombre', 'cod_barras')
    list_per_page = 10