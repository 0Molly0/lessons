import pytest
import random

from base import Library


@pytest.fixture(scope='function')
# @pytest.fixture(scope='session')
# @pytest.fixture(scope='module')
# @pytest.fixture(scope='class')
def library():
    address = 'Sadova, 14'
    helmet = random.choice(['Musienko', 'Buyler'])
    return Library(address, helmet=helmet)


@pytest.fixture
def books():
    return ['aaa', 'bbb']
