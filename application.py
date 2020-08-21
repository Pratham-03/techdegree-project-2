import copy
from constants import PLAYERS, TEAMS


team_copy = copy.deepcopy(TEAMS)
players_copy = copy.deepcopy(PLAYERS)
PLAYER_PER_TEAM = len(PLAYERS) // len(TEAMS)
balance_team = {key: [] for key in TEAMS}
experience = []
no_experience = []


def welcome():  # To display the welcome message
    print("""
        <<<----------------------->>>
            𝐁𝐀𝐒𝐊𝐄𝐓𝐁𝐀𝐋𝐋 𝐒𝐓𝐀𝐓𝐒 𝐓𝐎𝐎𝐋
        <<<----------------------->>>
    """)


def clear_data():  # To clear the data from the copy of constants.py
    for player in players_copy:
        if player.get('experience') == 'NO':
            player['experience'] = False
        else:
            player['experience'] = True
        player['height'] = int(player['height'][:2])
        player['guardians'] = player['guardians'].split(' and ')


def experience_splitter():  # To split the experience, so that it can be used later
    for player in players_copy:
        if player.get('experience') == True:
            experience.append(player)
        else:
            no_experience.append(player)


def balance_teams():  # To balance the teams with equal number of players
    counter = 0
    while len(balance_team.get('Panthers')) < PLAYER_PER_TEAM:
        for key, value in balance_team.items():
            experienced_player = experience[counter]
            not_experienced_player = no_experience[counter]
            items = {key: value.append(experienced_player)}
            items = {key: value.append(not_experienced_player)}
            counter += 1

    for key, value in balance_team.items():
        if len(value) > PLAYER_PER_TEAM:
            items = {key: value.pop()}


def menu():  # To display the option-menu in order to proceed
    print('\t----------Menu--------\n')
    print('\tChoose an option\n')
    print('\t> teams -- Display the Team Stats')
    print('\t> quit  -- Quit\n')
    choice = input('\tEnter your choice [teams/quit]:  ').lower()
    while True:
        if choice == 'teams':
            team_menu()
            break
        elif choice == 'quit':
            print('\t--Thank You, Have a Good Day!--\n')
            break
        else:
            choice = input(
                '\tERROR: Please choose from the given option. Enter your choice [teams/quit]:  ')


def team_menu():  # To display the team names and further selection of team
    print('\n\t--Teams--\n')
    print('\t> Panthers')
    print('\t> Bandits')
    print('\t> Warriors\n')
    print('')
    choice = input(
        '\tEnter your choice [panthers/bandits/warriors]:  ').lower()
    while True:
        if choice == 'panthers':
            stats('panthers')
            break
        elif choice == 'bandits':
            stats('bandits')
            break
        elif choice == 'warriors':
            stats('warriors')
            break
        else:
            print('\tERROR: Please choose from the given options. Try again!\n')
            choice = str(
                input('\tEnter your choice [panthers/bandits/warriors]:  ')).lower()


def stats(choice):  # To display the option-menu the selected team stats
    if choice == 'panthers'.lower():
        stats_info('Panthers')
    elif choice == 'bandits'.lower():
        stats_info('Bandits')
    elif choice == ('warriors').lower():
        stats_info('Warriors')


def stats_info(team):  # To show the team stats, such as number of player, their names, etc
    print(f'\n\tTeam {team} stats:')
    print('\t----------------------------------\n')
    print(f'\tTotal Players on the team:  {str(PLAYER_PER_TEAM)}')
    print('\tPlayers:')
    list_of_players = []
    for player in balance_team.get(team):
        list_of_players.append(player.get('name'))
    print('\t')
    for index, ply in enumerate(list_of_players, 1):
        print(f'\t{index}.) {ply}')
    total_experienced_player(team)
    average_height_players(team)
    guardians_player(team)
    stats_again()


# To show the total number of experienced players
def total_experienced_player(team):
    experienced_player = 0
    not_experienced_player = 0
    for player in balance_team.get(team):
        if player.get('experience') == True:
            experienced_player += 1
        not_experienced_player += 1
    print(
        f'\n\tTotal number of experienced players are {experienced_player} and not experienced player are {not_experienced_player} on the team')


# To show the average height of the players in the selected team
def average_height_players(team):
    avg_total_height = 0
    for player in balance_team.get(team):
        avg_total_height += player.get('height')
    avg_height = round(avg_total_height / PLAYER_PER_TEAM)
    print(f'\tAverage height of players on this team is {avg_height} inch\n')


def guardians_player(team):  # To show the gurdians of the selected team
    guardians = []
    for player in balance_team.get(team):
        guardians += player.get('guardians')
    total_num_guardians = ", ".join(guardians)
    print(
        f'\tThe guradians on this on this team are:\n\t{total_num_guardians}')


def stats_again():  # To give an option of going again from the menu
    print('\t----------------------------------')
    choice = input('\n\tWould you like to go again? [y/n]:  ').lower()
    while True:
        if choice == 'y':
            print('\n\n')
            menu()
            break
        elif choice == 'n':
            print('\t--Thank You. Have a Good Day!--\n\n')
            break
        else:
            choice = input(
                '\tInvalid option, please try again! Enter your choice:  ').lower()


if __name__ == "__main__":
    clear_data()
    welcome()
    experience_splitter()
    balance_teams()
    menu()
