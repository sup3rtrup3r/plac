from django.template.defaultfilters import slugify
from plac.users.tests.factories import UserFactory

import factory
import factory.fuzzy

from ..models import Povrce


class VegetablesFactory(factory.django.DjangoModelFactory):
    name = factory.fuzzy.FuzzyText()
    slug = factory.LazyAttribute(lambda obj: slugify(obj.name))
    description = factory.Faker(
        'paragraph', nb_sentences=3, variable_nb_sentences=True
    )
    vrsta = factory.fuzzy.FuzzyChoice(
        [x[0] for x in Povrce.Vrsta.choices]
    )
    creator = factory.SubFactory(UserFactory)

    class Meta:
        model = Povrce
