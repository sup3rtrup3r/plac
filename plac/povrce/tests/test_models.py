import pytest

from ..models import Povrce

pytestmark = pytest.mark.django_db


def test__str__():
    povrce = Povrce.objects.create(name='luk', description='od luka se fuka',
                                   vrsta=Povrce.Vrsta.LUKOVICASTO)
    assert povrce.__str__() == 'luk'
    assert str(povrce) == 'luk'
