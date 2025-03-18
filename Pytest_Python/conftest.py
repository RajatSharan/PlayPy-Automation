# Fixture is a way to setup some preconditions that are required to run the test
import pytest


@pytest.fixture(scope='session')
def preSetwork():
    print("I setup browser instance")
