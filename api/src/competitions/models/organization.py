import uuid
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from core.models import BaseModel
from competitions.models import Sport

class Organization(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(_("name"), max_length=255, null=False, blank=False)
    initials = models.CharField(_("initials"), max_length=10, null=False, blank=False)
    sport = models.ForeignKey(Sport, verbose_name=_("sport"), on_delete=models.CASCADE, related_name="organizations", null=False, blank=False)

    class Meta:
        verbose_name = _("organization")
        verbose_name_plural = _("organizations")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("organization_detail", kwargs={"pk": self.pk})