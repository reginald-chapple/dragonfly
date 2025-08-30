import uuid

from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from core.models import BaseModel
from competitions.models import Competition

class Group(BaseModel):
    """
    Represents a user-created group for private competitions.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(_("name"), max_length=255, unique=True, null=False, blank=False)
    description = models.TextField(_("description"), null=True, blank=True)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_("creator"), on_delete=models.CASCADE, related_name="created_groups", null=False, blank=False)
    members = models.ManyToManyField(settings.AUTH_USER_MODEL, verbose_name=_("members"), related_name="groups", through='GroupMember')
    competitions = models.ManyToManyField(Competition, verbose_name=_("competitions"), related_name="groups", through='GroupCompetition')

    class Meta:
        verbose_name = _("group")
        verbose_name_plural = _("groups")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("group_detail", kwargs={"pk": self.pk})
    
class GroupMember(BaseModel):
    """
    Through model for the Group's many-to-many relationship with users.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("group member")
        verbose_name_plural = _("group members")
        unique_together = ('group', 'user')

    def __str__(self):
        return f"{self.user.username} in {self.group.name}"
    
class GroupCompetition(BaseModel):
    group = models.ForeignKey(Group, verbose_name=_("group"), on_delete=models.CASCADE, related_name="group_competitions", null=False, blank=False)
    competition = models.ForeignKey(Competition, verbose_name=_("competition"), on_delete=models.CASCADE, related_name="group_competitions", null=False, blank=False)

    class Meta:
        verbose_name = _("group competition")
        verbose_name_plural = _("group competitions")

    def __str__(self):
        return f"{self.group.name} - {self.competition.name}"

    def get_absolute_url(self):
        return reverse("group_competition_detail", kwargs={"pk": self.pk})