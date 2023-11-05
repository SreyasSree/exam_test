from django.contrib import admin
from .models import Question, Participant , Limit , PDF
from .admin_actions import export_participants_xlsx, export_participants_pdf

class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('user', 'answers', 'score')
    actions = [export_participants_xlsx, export_participants_pdf]

admin.site.register(Question)
admin.site.register(Participant, ParticipantAdmin)
admin.site.register(Limit)
admin.site.register(PDF)
