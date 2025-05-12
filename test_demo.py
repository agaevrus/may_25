import pytest

#dev
@pytest.fixture()
def before_after():
    print('Before test')
    yield
    print('\nAfter test')



def test_demo1():
    assert 1 == 1



    #new

def test_demo2(before_after):
    assert 2 == 2