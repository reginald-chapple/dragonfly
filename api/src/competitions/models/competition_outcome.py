import uuid
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from core.models import BaseModel
from competitions.models import Competition, Group

class CompetitionOutcome(BaseModel):
    """
    Represents a single possible outcome for a competition.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    competition = models.ForeignKey(
        Competition,
        verbose_name=_("competition"),
        on_delete=models.CASCADE,
        related_name="outcomes",
        null=False,
        blank=False
    )
    name = models.CharField(_("name"), max_length=128, null=False, blank=False)
    points_value = models.PositiveIntegerField(
        _("points value"),
        default=10,
        help_text=_("The number of points awarded for a correct prediction.")
    )
    credit_cost = models.PositiveIntegerField(
        _("credit cost"),
        default=1,
        help_text=_("The number of credits required to make this prediction.")
    )
    credit_prize = models.PositiveIntegerField(
        _("credit prize"),
        default=0,
        help_text=_("The number of credits awarded for a correct prediction.")
    )
    group = models.ForeignKey(Group, verbose_name=_("group"), on_delete=models.CASCADE, related_name="competition_outcomes", null=True, blank=True)


    class Meta:
        verbose_name = _("competition outcome")
        verbose_name_plural = _("competition outcomes")
        unique_together = ('competition', 'name')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("competition_outcome_detail", kwargs={"pk": self.pk})