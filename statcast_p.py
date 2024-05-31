from pybaseball import statcast_single_game
import pandas as pd
from pybaseball import statcast
from pybaseball import cache
from datetime import datetime
from pybaseball import playerid_reverse_lookup
# this should get the current one inning cycles for current season


def hit_value_column(value):
    value_dict = {
        'single': 1,
        'double': 2,
        'triple': 3,
        'home_run': 4
    }

    return value_dict.get(value, 0)


if __name__ == '__main__':
    cache.enable()
    # # get all play by play data
    data = statcast('2024-03-20', datetime.now().strftime('%Y-%m-%d'))

    play_by_play_2024 = data[
        ['game_date', 'home_team', 'away_team', 'inning', 'inning_topbot', 'pitcher', 'events']].dropna()

    play_by_play_2024['hit_value'] = play_by_play_2024['events'].apply(hit_value_column)

    play_by_play_2024.to_csv(
        '<enter filename>.csv',
        index=False)

    # data = playerid_reverse_lookup([641927, 607259,676775], key_type='mlbam')
    # print(data)

    #
    # data = playerid_reverse_lookup(['yelic001', 'bauej001', 'barnb002', 'gomec002', 'younr001', 'robif103', 'doerb101', 'gehrl101', 'robed103'], key_type='retro')
    # print(data[['name_first', 'name_last']])

