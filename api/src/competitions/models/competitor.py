import uuid
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from core.models import BaseModel
from competitions.models import Sport, Organization

class Competitor(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(_("name"), max_length=50, null=False, blank=False)
    wins = models.PositiveIntegerField(_("wins"), default=0, null=False, blank=False)
    losses = models.PositiveIntegerField(_("losses"), default=0, null=False, blank=False)
    organization = models.ForeignKey(Organization, verbose_name=_("organization"), on_delete=models.CASCADE, related_name="competitors", null=False, blank=False)

    class Meta:
        verbose_name = _("competitor")
        verbose_name_plural = _("competitors")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("competitor_detail", kwargs={"pk": self.pk})