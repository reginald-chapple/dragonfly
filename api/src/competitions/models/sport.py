import uuid
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from core.models import BaseModel

class Sport(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(_("name"), max_length=255, unique=True, null=False, blank=False)

    class Meta:
        verbose_name = _("sport")
        verbose_name_plural = _("sports")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("sport_detail", kwargs={"pk": self.pk})