from django.contrib import admin
from my_app.models import RecetasItalianas, RecetasColombianas, RecetasMar
# Register your models here.


class RecetasAdmin(admin.ModelAdmin):
    pass

admin.site.register([RecetasItalianas, RecetasMar, RecetasColombianas])