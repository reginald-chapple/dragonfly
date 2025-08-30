import uuid
from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from core.models import BaseModel

class UserCredit(BaseModel):
    """
    Represents a user's virtual credit balance for making predictions.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, verbose_name=_("user"), on_delete=models.CASCADE, related_name="credits", null=False, blank=False)
    balance = models.PositiveIntegerField(_("balance"), default=0, help_text=_("The user's current credit balance."))

    class Meta:
        verbose_name = _("user credit")
        verbose_name_plural = _("user credits")

    def __str__(self):
        return f"{self.user.username}'s credits: {self.balance}"

    def get_absolute_url(self):
        return reverse("user_credit_detail", kwargs={"pk": self.pk})