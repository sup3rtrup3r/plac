import pytest

from .factories import VegetablesFactory

pytestmark = pytest.mark.django_db


def test__str__():
    povrce = VegetablesFactory()
    assert povrce.__str__() == povrce.name
    assert str(povrce) == povrce.name
