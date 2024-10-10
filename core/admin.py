from django.contrib import admin
from core.models import category
from core.models import product
from core.models import author
from core.models import genre






# Register your models here.
admin.site.register(category)
admin.site.register(product)
admin.site.register(author)
admin.site.register(genre)
