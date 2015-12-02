import pytest
import boneyard as b

def test_boneyard_exists():
    assert b.boneyard()

@pytest.fixture
def boneyard():
    boneyard = b.boneyard()
    return boneyard

def test_boneyard_dominoes_is_set(boneyard):
    assert isinstance(boneyard.dominoes, set)

def test_boneyard_dominoes_contains_dominoes(boneyard):
    assert boneyard.dominoes()

def test_boneyard_dominoes_contains_dominoes(boneyard):
    boneyard.shuffle()
    assert len(boneyard.dominoes) == 28 
    
def test_domino_exists():
    assert b.domino(0,1)

@pytest.fixture
def domino():
    domino = b.domino(x=1, y=0)
    return domino

def test_domino_has_two_sets_of_dots(domino):
    assert domino.dots


def test_domino_has_total_count_of_dots(domino):
    assert domino.value


