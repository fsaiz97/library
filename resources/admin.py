from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Subject)
admin.site.register(Character)
admin.site.register(Place)
admin.site.register(Location)
admin.site.register(Author)
admin.site.register(Resource)
#admin.site.register(LibraryUser)
admin.site.register(Loan)
