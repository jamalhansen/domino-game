import pytest
import domino
import boneyard as by
import board as bd
import player as pl

def test_domino_exists():
    assert domino.domino

def test_boneyard_exists():
    assert by.boneyard()

@pytest.fixture
def boneyard():
    boneyard = by.boneyard()
    return boneyard

def test_boneyard_dominoes_is_set(boneyard):
    assert isinstance(boneyard.dominoes, set)

def test_boneyard_dominoes_contains_dominoes(boneyard):
    assert boneyard.dominoes()

def test_boneyard_dominoes_contains_dominoes(boneyard):
    assert len(boneyard.dominoes) == 28 
    
def test_domino_exists():
    assert by.domino(0,1)

@pytest.fixture
def domino():
    domino = by.domino(dots1=1, dots2=0)
    return domino

def test_domino_has_two_sets_of_dots(domino):
    assert domino.dots

def test_domino_has_total_count_of_dots(domino):
    assert domino.value == 1

def test_board_exist():
    assert bd.board

@pytest.fixture
def board():
    board = bd.board()
    return board

def test_board_has_boneyard(board):
    assert board.boneyard

def test_board_has_field_list(board):
    assert isinstance(board.field, list)

def test_player_exist():
    assert pl

@pytest.fixture()
def player():
    player = pl.player('player1', 3, boneyard)
    return player
    
def test_player_hand_is_set(player):
    assert isinstance(player.hand, pl.hand)

def test_player_score_starts_at_0(player):
    assert player.score == 0

def test_player_has_name(player):
    assert player.name == 'player1'

def test_player_hand_has_domninoes(player):
    assert isinstance(player.hand, pl.hand) 
