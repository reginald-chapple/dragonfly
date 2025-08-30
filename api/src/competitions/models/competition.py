import uuid
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from core.models import BaseModel
from competitions.models import Sport, Organization, Competitor

class Competition(BaseModel):
    """
    Represents a single sports competition for which users can make predictions.
    """
    class Status(models.TextChoices):
        OPEN = 'OPEN', _('Open')
        CLOSED = 'CLOSED', _('Closed')
        RESOLVED = 'RESOLVED', _('Resolved')

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(_("name"), max_length=255, null=False, blank=False)
    description = models.TextField(_("description"), null=False, blank=False)
    date = models.DateField(_("date"), auto_now=False, auto_now_add=False)
    time = models.TimeField(_("time"), auto_now=False, auto_now_add=False)
    timezone = models.CharField(_("timezone"), max_length=50, null=False, blank=False)
    sport = models.ForeignKey(Sport, verbose_name=_("sport"), on_delete=models.CASCADE, related_name="competitions", null=False, blank=False)
    organization = models.ForeignKey(Organization, verbose_name=_("organization"), on_delete=models.CASCADE, related_name="competitions", null=False, blank=False)
    competitors = models.ManyToManyField(Competitor, verbose_name=_("competitors"), related_name="competitions", blank=True)
    status = models.CharField(
        _("status"),
        max_length=10,
        choices=Status.choices,
        default=Status.OPEN,
        help_text=_("The current status of the competition.")
    )
    winning_outcome = models.ForeignKey(
        'CompetitionOutcome',
        verbose_name=_("winning outcome"),
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="winning_competitions",
        help_text=_("The winning outcome of the competition. Only set when status is RESOLVED.")
    )

    class Meta:
        verbose_name = _("competition")
        verbose_name_plural = _("competitions")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("competition_detail", kwargs={"pk": self.pk})