import uuid
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from users.managers import AppUserManager
from core.validators import LowercaseValidator

def get_profile_image_filepath(instance, filename):
    """
    Generates a unique filename for a user's profile image using a UUID.
    """
    extension = filename.split('.')[-1]
    # Creates a path like: profile_images/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.jpg
    return f'members/{uuid.uuid4()}.{extension}'

class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(
        _('user name'),
        max_length=30,
        unique=True,
        help_text=_('Required. 30 characters or fewer. Letters, numbers, and @/./+/-/_ only.'),
        validators=[LowercaseValidator()],
         error_messages={
            'unique': _("A user with that username already exists."),
        },
         null=False,
         blank=True
    )
    email = models.EmailField(_('email address'), unique=True, blank=True)
    first_name = models.CharField(max_length=150, null=False, blank=False)
    last_name = models.CharField(max_length=150, null=False, blank=False)
    is_member = models.BooleanField(_('member status'), default=False)
    photo = models.ImageField(
        _("photo"), 
        upload_to=get_profile_image_filepath, # Use the function here
        null=True, 
        blank=True
    )
    phone_number = models.CharField(
        _("phone number"),
        max_length=16,
        blank=True,
        null=True,
        validators=[
            RegexValidator(
                regex=r'^1?\d{9,15}$',
                message="Phone number must be entered in the format '123456789'. Up to 15 digits allowed."
            ),
        ],
    )
    birthdate = models.DateField(_("birthdate"), auto_now=False, auto_now_add=False, null=True, blank=True)
    address = models.CharField(_("address"), max_length=50, null=True, blank=True)
    city = models.CharField(_("city"), max_length=50, null=True, blank=True)
    country = models.CharField(_("country"), max_length=50, null=True, blank=True)
    state = models.CharField(_("state"), max_length=50, null=True, blank=True)
    zip = models.CharField(_("zip"), max_length=12, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email']

    objects = AppUserManager()

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def __str__(self):
        return self.username

    @property
    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """
        Returns the short name for the user.
        """
        return self.first_name

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})