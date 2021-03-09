from django.db import models
from django.urls import reverse

from autoslug import AutoSlugField
from model_utils.models import TimeStampedModel

from django_countries.fields import CountryField


class Povrce(TimeStampedModel):
    name = models.CharField("Name of vegetable", max_length=255)
    slug = AutoSlugField("Vegetables Address", unique=True, always_update=False,
                         populate_from="name")
    description = models.TextField("Description", blank=True)

    class Vrsta(models.TextChoices):
        NEDEFINIRANO = "nedefinirano", "Nedefinirano"
        PLODASTO = "plodasto", "Plodasto"
        CVJETASTO = "cvjetasto", "Cvjetasto"
        LISNATO = "lisnato", "Lisnato"
        STABLJICASTO = "stabljicasto", "Stabljicasto"
        LUKOVICASTO = "lukovicasto", "Lukovicasto"
        KORJENASTO = "korjenasto", "Korjenasto"
        MAHUNASTO = "mahunasto", "Mahunasto"
        GOMOLJASTO = "gomoljasto", "Gomoljasto"

    vrsta = models.CharField("Vegetable species", max_length=30,
                             choices=Vrsta.choices, default=Vrsta.NEDEFINIRANO)
    country_of_origin = CountryField("Country of Origin", blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """Return absolute URL to the Vegetables Detail page."""
        return reverse(
            'povrce:detail', kwargs={"slug": self.slug}
        )
