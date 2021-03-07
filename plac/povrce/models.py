from django.db import models

from autoslug import AutoSlugField
from model_utils.models import TimeStampedModel


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

    def __str__(self):
        return self.name
