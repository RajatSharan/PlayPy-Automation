# Fixture is a way to setup some preconditions that are required to run the test
import pytest


@pytest.fixture(scope='module')  # scope='module' will run only once before the test
# @pytest.fixture(scope='session')    #scope='function' will run before every test
def prework():
    print("I setup browser instance 1")
    return "Pass"


@pytest.fixture(scope='function')  # scope='module' will run only once before the test
def secondwork():
    print("I setup browser instance")
    yield
    print("I close browser instance")

@pytest.mark.smoke
def test_inital_check(prework,secondwork):  # pytest will look for any function with test_ in the begining
    print("Intial Check")
    assert prework == "Pass"

@pytest.mark.skip
def test_inital_Note(preSetwork):  # pytest will look for any function with test_ in the begining
    print("Second Check")
