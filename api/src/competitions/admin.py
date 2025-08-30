from django.contrib import admin

from competitions.models import (
    Competition, 
    CompetitionOutcome, 
    Competitor,
    Group,
    GroupMember,
    GroupCompetition,
    Organization,
    Prize,
    Sport,
    UserCredit,
    UserPrediction,
    UserScore
)

admin.site.register(Competition)
admin.site.register(CompetitionOutcome)
admin.site.register(Competitor)
admin.site.register(Group)
admin.site.register(GroupMember)
admin.site.register(GroupCompetition)
admin.site.register(Organization)
admin.site.register(Prize)
admin.site.register(Sport)
admin.site.register(UserCredit)
admin.site.register(UserPrediction)
admin.site.register(UserScore)