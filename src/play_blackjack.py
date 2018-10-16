from Game import Game
from Hand import Hand

# Prompts
main_menu_prompt = 'Press "n" to start a new game or "q" to quit: '
player_menu_prompt = 'Press "c" to check the current hand, "h" to hit, or "s" to stay: '
num_players_prompt = 'Enter the number of players (integer > 0): '
# Messages
intro_msg = 'Welcome to Black Jack! A multi-player game where you can face off against a friend in the classic card game of 21!'
game_over_msg = 'The game is over! Here is the list of players in order of ranking (first place -> last place)'
goodbye_msg = 'Thanks for playing!'
# Input flag detectors
is_x = lambda x, user_in: user_in.lower() == x
is_yes = lambda user_in: is_x('y', user_in)
is_newgame = lambda user_in: is_x('n', user_in)
is_quit = lambda user_in: is_x('q', user_in)
is_stay = lambda user_in: is_x('s', user_in)
is_check = lambda user_in: is_x('c', user_in)
is_hit = lambda user_in: is_x('h', user_in)

# Command getters
def get_command(valid_cmd: str, prompt: str):
    next_cmd = input(prompt)
    while next_cmd not in valid_cmd:
        print('Invalid command')
        next_cmd = input(prompt)
    return next_cmd

get_player_command = lambda: get_command(['s', 'S', 'c', 'C', 'h', 'H'], player_menu_prompt)
get_main_menu_command = lambda: get_command(['q', 'Q', 'n', 'N'], main_menu_prompt)

# Turn management
def print_player_status(hand: Hand):
    current_cards = ', '.join(map(str, hand.get_cards()))
    possible_scores = ', '.join(map(str, hand.get_possible_scores()))
    print('Cards: {0}'.format(current_cards))
    print('Possible Scores: {0}'.format(possible_scores))

def play_turn(current_game: Game):
    print('\nIt is {0}\'s turn'.format(current_game.get_current_player_name()))
    current_hand = current_game.get_current_hand()
    print_player_status(current_hand)
    next_cmd = get_player_command()
    while not is_stay(next_cmd):
        if is_check(next_cmd):
            print_player_status(current_hand)
        else:
            try:
                hit_result = current_game.hit()
            except ValueError:
                print('Out of cards, cannot hit')
                break
            print('Hit: {0}'.format(current_hand.get_most_recent_card()))
            if not hit_result:
                print('Oh no! Busted with {0}....'.format(current_hand.get_best_score()))
                return
        next_cmd = get_player_command()
    current_game.stay()

# Game management
def play_game(current_game: Game):
    while not current_game.is_game_over():
        play_turn(current_game)
    print(game_over_msg)
    for player in current_game.get_rankings():
        print('\t{0}'.format(player))

def start_newgame():
    num_players = input(num_players_prompt)
    while not str.isdigit(num_players) and (int(num_players) <= 0) or (int(num_players) > 26):
        print('Invalid number of players')
        num_players = input(num_players_prompt)
    num_players = int(num_players)
    player_names = ['Player {0}'.format(i) for i in range(1, num_players + 1)]
    play_game(Game(player_names, True))

# Main process
if __name__ == '__main__':
    print(intro_msg)
    main_menu_cmd = get_main_menu_command()
    while not is_quit(main_menu_cmd):
        start_newgame()
        main_menu_cmd = get_main_menu_command()
    print(goodbye_msg)