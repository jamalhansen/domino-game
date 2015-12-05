import pytest
import domino as dom
import boneyard
import game as gm

def test_domino_exists():
    assert dom.domino

def test_boneyard_dominoes_contains_dominoes():
    bones = boneyard.add_dominoes(6)
    assert len(bones) == 28 
    
def test_boneyard_shuffles_dominoes():
    old_by = [1,2,3,4] 
    new_by = boneyard.shuffle(old_by)
    assert old_by != new_by

@pytest.fixture
def domino():
    domino = dom.domino(dots1=1, dots2=0)
    return domino

def test_domino_has_two_sets_of_dots(domino):
    assert domino.dots

def test_domino_has_total_count_of_dots(domino):
    assert domino.value == 1

def test_game_exist():
    assert gm

@pytest.fixture()
def player():
    player = gm.player('player1')
    return player
    
def test_player_score_starts_at_0(player):
    assert player.score == 0

def test_player_has_name(player):
    assert player.name == 'player1'

def test_player_hand_is_list(player):
    assert isinstance(player.hand, list) 

@pytest.fixture
def game():
    game = gm.game([gm.player('player1'), gm.player('player2')], 6)
    return game

def test_game_has_boneyard(game):
    assert game.boneyard

def test_game_has_players(game):
    assert game.players

def test_player_picks_dominoes(game):
    game.pickup_dominoes(6, game.players[0])
    assert len(game.players[0].hand) == 6

def test_player_picks_domines_from_boneyard(game):
    original_length = len(game.boneyard)
    game.pickup_dominoes(7, game.players[0])
    assert len(game.boneyard) == original_length - 7

def test_game_board_is_list(game):
    assert isinstance(game.board, list)

def test_game_boneyard_has_dominoes(game):
    for domino in game.boneyard:
        assert isinstance (domino, dom.domino)
