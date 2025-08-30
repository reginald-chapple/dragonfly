import uuid
from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from core.models import BaseModel

class Prize(BaseModel):
    """
    Represents a prize that can be awarded to top-ranking users.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(_("name"), max_length=255, null=False, blank=False)
    description = models.TextField(_("description"), null=True, blank=True)
    winner = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_("winner"), on_delete=models.SET_NULL, related_name="won_prizes", null=True, blank=True)

    class Meta:
        verbose_name = _("prize")
        verbose_name_plural = _("prizes")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("prize_detail", kwargs={"pk": self.pk})
