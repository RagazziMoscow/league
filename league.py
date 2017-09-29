from random import randint

TEAMS_LIST = ['Наполи', 'Ювентус', 'Интер',
              'Лацио', 'Рома', 'Милан',
              'Сампдория', 'Торино', 'Аталанта',
              'Кьево', 'Болонья', 'Фиорентина',
              'Дженова']

SEASON_TABLE = []

def change_table():
  pass

def simulate_match(masters, guests):
    masters_team = {"name": masters, "goals": randint(0, 10)}
    guests_team = {"name": guests, "goals": randint(0, 10)}
    match = {"home": masters_team, "away": guests_team}
    return match


def print_season_results():
    print("N  Клуб Игры Победы Ничьи Поражения Мячи Очки")
    for number, team in enumerate(SEASON_TABLE):
        matches_count = team["matches"]
        wins = team["wins"]
        losses = team["losses"]
        drawns = matches_count - wins - losses
        goals_count = team["goals"]
        points = team["points"]
        print("{0} {1} {2} {3} {4} {5} {6} {7}".format(
            number, team["name"], matches_count, wins, drawns, losses, goals_count, points))


def _main():
    for number, team in enumerate(TEAMS_LIST):
        team_point = {"place": number, "name": team, "matches": 0,
                      "wins": 0, "losses": 0, "goals": 0,
                      "goals_conceded": 0, "points": 0}
        SEASON_TABLE.append(team_point)
    print(simulate_match(TEAMS_LIST[3], TEAMS_LIST[6]))
    print_season_results()


if __name__ == '__main__':
    _main()
