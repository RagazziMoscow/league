from random import randint
from terminaltables import AsciiTable


TEAMS_LIST = ['Наполи', 'Ювентус', 'Интер',
              'Лацио', 'Рома', 'Милан',
              'Торино', 'Аталанта', 'Кьево',
              'Болонья', 'Фиорентина', 'Дженова']

SEASON_TABLE = {}


def simulate_match(masters, guests):
    masters_goals = randint(0, 10)
    guests_goals = randint(0, 10)

    masters_team = {"name": masters, "goals": masters_goals}
    guests_team = {"name": guests, "goals": guests_goals}
    match_results = {"home": masters_team, "away": guests_team}

    return match_results


def change_table(match_results):
    masters = match_results["home"]
    guests = match_results["away"]

    winner = max(masters, guests, key=lambda x: x["goals"])
    loser = min(masters, guests, key=lambda x: x["goals"])

    SEASON_TABLE[winner["name"]]["stat"]["matches"] += 1
    SEASON_TABLE[loser["name"]]["stat"]["matches"] += 1

    SEASON_TABLE[winner["name"]]["stat"]["goals"] += winner["goals"]
    SEASON_TABLE[winner["name"]]["stat"]["goals_conceded"] += loser["goals"]

    SEASON_TABLE[loser["name"]]["stat"]["goals"] += loser["goals"]
    SEASON_TABLE[loser["name"]]["stat"]["goals_conceded"] += winner["goals"]

    if winner["goals"] == loser["goals"]:
        SEASON_TABLE[winner["name"]]["stat"]["points"] += 1
        SEASON_TABLE[loser["name"]]["stat"]["points"] += 1
    else:
        SEASON_TABLE[winner["name"]]["stat"]["wins"] += 1
        SEASON_TABLE[loser["name"]]["stat"]["losses"] += 1
        SEASON_TABLE[winner["name"]]["stat"]["points"] += 3


def print_season_results():
    season_list = sorted(list(SEASON_TABLE.values()),
                         key=lambda x: x["stat"]["points"],
                         reverse=True)
    headers = ['N', 'Клуб', 'Игры', 'Победы',
               'Ничьи', 'Поражения', 'Мячи', 'Очки']
    table_data = [headers]

    for number, team in enumerate(season_list):
        matches_count = team["stat"]["matches"]
        wins = team["stat"]["wins"]
        losses = team["stat"]["losses"]
        drawns = matches_count - wins - losses
        goals_all = "{0} - {1}".format(team["stat"]
                                       ["goals"], team['stat']['goals_conceded'])
        points = team["stat"]["points"]
        team_point = [number + 1, team['name'], matches_count,
                      wins, drawns, losses, goals_all, points]

        table_data.append(team_point)

    table = AsciiTable(table_data)
    table.padding_left = 3
    print(table.table)


def _main():
    for number, team in enumerate(TEAMS_LIST):
        team_statistics = {"place": number, "matches": 0,
                           "wins": 0, "losses": 0, "goals": 0,
                           "goals_conceded": 0, "points": 0}
        team_point = {"name": team, "stat": team_statistics}
        SEASON_TABLE[team] = team_point

    for round, team_in_round in enumerate(TEAMS_LIST):
        if round + 1 > 12:
            break
        print('Тур {0}'.format(round + 1))

        for team in TEAMS_LIST:
            if team == team_in_round:
                continue
            print('Матч: {0}-{1}'.format(team, team_in_round))
            # Изменение в таблице после каждого матча
            match_results = simulate_match(team, team_in_round)
            change_table(match_results)
        print_season_results()

    print_season_results()  # Результаты в конце сезона


if __name__ == '__main__':
    _main()
