import uuid
from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from core.models import BaseModel

class UserScore(BaseModel):
    """
    Represents a user's total points for leaderboards.
    This provides a direct way to view a user's points without a complex query.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, verbose_name=_("user"), on_delete=models.CASCADE, related_name="score", null=False, blank=False)
    points = models.PositiveIntegerField(_("points"), default=0, help_text=_("The user's current point balance."))

    class Meta:
        verbose_name = _("user score")
        verbose_name_plural = _("user scores")

    def __str__(self):
        return f"{self.user.username}'s points: {self.points}"

    def get_absolute_url(self):
        return reverse("user_score_detail", kwargs={"pk": self.pk})