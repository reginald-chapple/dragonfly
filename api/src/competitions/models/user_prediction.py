import uuid
from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from core.models import BaseModel
from competitions.models import CompetitionOutcome, Competition

class UserPrediction(BaseModel):
    """
    Represents a user's prediction on a specific competition outcome.
    """
    class Status(models.TextChoices):
        PENDING = 'PENDING', _('Pending')
        CORRECT = 'CORRECT', _('Correct')
        INCORRECT = 'INCORRECT', _('Incorrect')
        CANCELLED = 'CANCELLED', _('Cancelled')

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_("user"), on_delete=models.CASCADE, related_name="predictions", null=False, blank=False)
    competition = models.ForeignKey(Competition, verbose_name=_("competition"), on_delete=models.CASCADE, related_name="user_predictions", null=False, blank=False)
    predicted_outcome = models.ForeignKey(CompetitionOutcome, verbose_name=_("predicted outcome"), on_delete=models.CASCADE, related_name="user_predictions", null=False, blank=False)
    points_awarded = models.IntegerField(_("points awarded"), default=0, null=False, blank=False)
    credit_cost = models.PositiveIntegerField(_("credit cost"), default=0, help_text=_("The number of credits spent on this prediction."))
    credits_awarded = models.PositiveIntegerField(_("credits awarded"), default=0, help_text=_("The number of credits awarded for this prediction."))
    status = models.CharField(
        _("status"),
        max_length=10,
        choices=Status.choices,
        default=Status.PENDING,
        help_text=_("The status of the user's prediction.")
    )

    class Meta:
        verbose_name = _("user prediction")
        verbose_name_plural = _("user predictions")
        unique_together = ('user', 'competition')

    def __str__(self):
        return f"{self.user.username}'s prediction on {self.competition.name}"

    def get_absolute_url(self):
        return reverse("user_prediction_detail", kwargs={"pk": self.pk})

    @property
    def awarded_points(self):
        """
        Calculates the points to be awarded based on the prediction's status.
        """
        if self.status == self.Status.CORRECT:
            return self.predicted_outcome.points_value
        elif self.status == self.Status.INCORRECT:
            return -self.predicted_outcome.points_value
        return 0