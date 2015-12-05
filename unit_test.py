import pytest
import domino as dom
import boneyard
import game as gm


@pytest.fixture
def domino():
    domino = dom.domino(dots1=1, dots2=0)
    return domino

@pytest.fixture
def player():
    player = gm.player('player1')
    return player

@pytest.fixture
def game():
    game = gm.game([gm.player('player1'), gm.player('player2')], 6)
    return game

def test_domino_exists():
    assert dom.domino

def test_boneyard_dominoes_contains_dominoes():
    bones = boneyard.add_dominoes(6)
    assert len(bones) == 28

def test_boneyard_shuffles_dominoes():
    old_by = [1,2,3,4]
    new_by = boneyard.shuffle(old_by)
    assert old_by != new_by

def test_domino_has_two_sets_of_dots(domino):
    assert domino.dots

def test_domino_has_total_count_of_dots(domino):
    assert domino.value == 1

def test_game_exist():
    assert gm

def test_player_score_starts_at_0(player):
    assert player.score == 0

def test_player_has_name(player):
    assert player.name == 'player1'

def test_player_hand_is_list(player):
    assert isinstance(player.hand, list)

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

def test_dominoes_detect_equality_based_on_dots():
    first_domino = dom.domino(0, 0)
    second_domino = dom.domino(0, 0)

    assert first_domino == second_domino

def test_dominoes_can_be_equal_regardless_of_position():
    first_domino = dom.domino(2, 1)
    second_domino = dom.domino(1, 2)

    assert first_domino == second_domino

def test_unequal_dominoes_are_not_equal():
    first_domino = dom.domino(3, 0)
    second_domino = dom.domino(2, 2)

    assert first_domino != second_domino

def test_can_compare_dominoes_with_in():
    dominoes = [dom.domino(1, 2)]
    domino = dom.domino(1, 2)

    assert domino in dominoes

def test_can_compare_inverted_dominoes_with_in():
    dominoes = [dom.domino(1, 2)]
    domino = dom.domino(2, 1)

    assert domino in dominoes

def test_can_find_domino_not_in_set():
    dominoes = [dom.domino(1, 2)]
    domino = dom.domino(3, 3)

    assert domino not in dominoes

