from django.contrib import admin
from .models import Competition, Ticket, TicketSize, Winner

# Register your models here.
admin.site.register(Competition)
admin.site.register(Ticket)
admin.site.register(TicketSize)
admin.site.register(Winner)
