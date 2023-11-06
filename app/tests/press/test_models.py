import pytest

from press.models import *

def test_press_model(db):
    press_sample = Press.objects.create(
        name='조선일보',
        press_id='123'
    )

    assert Press.objects.count() == 1