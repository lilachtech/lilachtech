import random
import csv
import pandas as pd

# Empty lists
trail_num_list, trails_total_payoff, trails_adding_points, trails_omitted_points, trails_type, conditions_list,\
trails_type_list, enforcement_list, player_choice_list, p_inspection_list, fine_size_list, true_side_list, \
block_num_list, game_num_list, correct_side_list, trails_alternative_points, error_list, block_error_list, \
block_payoff_list, game_point_list = ([] for i in range(20))


def true_side_trail(round_type):  # The side which has more dots
    if round_type == 'clear_right' or round_type == 'amb_right':
        correct_side = 'right'
    else:
        correct_side = 'left'
    return correct_side


def random_player(correct_side):
    if random.randint(0, 1) == 1:
        choice = 'right'
    else:
        choice = 'left'

    return choice


def win_stay_lose_shift_player(choice_list, trails_payoff, alternative_points, trail_num):

    if len(choice_list) == 0 or len(choice_list) % 100 == 0:
        if random.randint(0, 1) == 0:
            choice = 'right'
            print('random - right')
        else:
            choice = 'left'
            print('random - left')
    else:
        last_choice = choice_list[trail_num - 1]
        trail_payoff = trails_payoff[trail_num - 1]
        trail_alter = alternative_points[trail_num - 1]
        print(last_choice, trail_payoff, trail_alter)
        print(choice_list)

        if trail_payoff > trail_alter:
            choice = last_choice
        else:
            if last_choice == 'right':
                choice = 'left'
            elif last_choice == 'left':
                choice = 'right'

    return choice


def small_samples(choice_list, trails_payoff, alternative_points, trail_num):

    if len(choice_list) <= 4:
        if random.randint(0, 1) == 0:
            choice = 'right'
            print('random - right')
        else:
            choice = 'left'
            print('random - left')
    else:
        last_choice = choice_list[trail_num - 1]
        trail_payoff = trails_payoff[trail_num - 1]
        trail_alter = alternative_points[trail_num - 1]
        print(last_choice, trail_payoff, trail_alter)
        print(choice_list)

        if trail_payoff > trail_alter:
            choice = last_choice
        else:
            if last_choice == 'right':
                choice = 'left'
            elif last_choice == 'left':
                choice = 'right'

    return choice

# print(win_stay_lose_shift_player([], [20, 1], [1, 20], 1, 0))


def trail_inspection(condition):  # test if there is inspection on the current side
    inspection_trail = 0
    probability = 0
    fine_size = 0

    if condition == 'high_enforcement':
        probability = 0.9
        fine_size = 20
        sample_num = random.random()
        if sample_num > probability:
            inspection_trail = 0
        else:
            inspection_trail = 1
    elif condition == 'low_enforcement':
        probability = 0.1
        fine_size = 180
        sample_num = random.random()
        if sample_num > probability:
            inspection_trail = 0
        else:
            inspection_trail = 1

    return inspection_trail, probability, fine_size


def reward_for_choice(condition, choice, correct_side, inspection):
    omitted_points = 0

    if condition == 'high_enforcement' or condition == 'low_enforcement':
        if choice == 'right':
            alternative_choice = 1
            added_points = 20
            points_for_choice = added_points
        else:
            added_points = 1
            alternative_choice = 20
            points_for_choice = added_points

        if correct_side == choice:
        # dont change the points_for_choice
        # dont change omitted_points
        # dont change added_points
        # dont change alternative

        else:  # choice is wrong
            if inspection == 1:
                if condition == 'high_enforcement':

                    omitted_points = -20
                    points_for_choice = points_for_choice + omitted_points
                    # dont change alternative
                    # dont change added_points

                elif condition == 'low_enforcement':
                    omitted_points = -180
                    points_for_choice = points_for_choice + omitted_points
                    # dont change alternative
                    # dont change added_points

    else:
        if choice == 'right':
            added_points = 2
            alternative_choice = 1
            points_for_choice = added_points

        else:
            added_points = 1
            alternative_choice = 2
            points_for_choice = added_points

    return points_for_choice, added_points, omitted_points, alternative_choice


def trail_for_block():  # create one array which contain the number of each type
    global trails_type
    for t in range(100):
        if t <= 24:
            trails_type.append('clear_right')
        elif t <= 49:
            trails_type.append('clear_left')
        elif t <= 65:
            trails_type.append('amb_right')
        else:
            trails_type.append('amb_left')

    return trails_type


def play_game():

    for condition in range(3):
        if condition == 0:
            game_condition = 'high_enforcement'
        elif condition == 1:
            game_condition = 'low_enforcement'
        elif condition == 2:
            game_condition = 'no_enforcement'

        for block in range(2):
            trails_type = trail_for_block()
            random.shuffle(trails_type)

            for trail in range(100):  # one block
                game_num_list.append(condition+1)  # list of number of game
                block_num_list.append(block + 1)  # list of block num

                trail_num_list.append(trail + 1 + block * 100)

                round_type = trails_type.pop()  # type of trail
                trails_type_list.append(round_type)  # all trails type

                true_side = true_side_trail(round_type)  # Which side has more dots
                true_side_list.append(true_side)

                # player_choice = random_player(true_side)  # Player choice
                player_choice = win_stay_lose_shift_player(player_choice_list, trails_total_payoff, trails_alternative_points, trail)
                player_choice_list.append(player_choice)

                if player_choice != true_side:
                    correct_side_list.append(0)
                    error_list.append(1)
                else:
                    correct_side_list.append(1)
                    error_list.append(0)

                # Enforcement
                enforcement_array = trail_inspection(game_condition)  # There is inspection?

                conditions_list.append(game_condition)  # list of trails condition

                enforcement = enforcement_array[0]
                enforcement_list.append(enforcement)

                p_inspection = enforcement_array[1]
                p_inspection_list.append(p_inspection)

                fine_size = enforcement_array[2]
                fine_size_list.append(fine_size)

                # Trail Payoffs
                trail_payoff = reward_for_choice(game_condition, player_choice, true_side, enforcement)  # points earned
                trail_total = trail_payoff[0]
                trail_added = trail_payoff[1]
                trail_omitted = trail_payoff[2]
                trail_alternative = trail_payoff[3]

                trails_total_payoff.append(trail_total)
                trails_adding_points.append(trail_added)
                trails_omitted_points.append(trail_omitted)
                trails_alternative_points.append(trail_alternative)

                # block errors
                if condition == 0 and block == 0 and trail == 99:
                    first_block = sum(error_list)
                    b1_points = sum(trails_total_payoff)
                elif condition == 0 and block == 1 and trail == 99:
                    second_block = sum(error_list) - first_block
                    b2_points = sum(trails_total_payoff) - b1_points
                elif condition == 1 and block == 0 and trail == 99:
                    third_block = sum(error_list) - (second_block + first_block)
                    b3_points = sum(trails_total_payoff) - (b2_points + b1_points)
                elif condition == 1 and block == 1 and trail == 99:
                    fourth_block = sum(error_list) - (third_block + second_block + first_block)
                    b4_points = sum(trails_total_payoff) - (b3_points + b2_points + b1_points)
                elif condition == 2 and block == 0 and trail == 99:
                    fifth_block = sum(error_list) - (fourth_block + third_block + second_block + first_block)
                    b5_points = sum(trails_total_payoff) - (b4_points + b3_points + b2_points + b1_points)
                elif condition == 2 and block == 1 and trail == 99:
                    sixth_block = sum(error_list) - (fifth_block + fourth_block + third_block + second_block + first_block)
                    b6_points = sum(trails_total_payoff) - (b5_points + b4_points + b3_points + b2_points + b1_points)
                    game_errors = sum(error_list)
                    for i in range(100):
                        block_error_list.append(first_block)
                        block_payoff_list.append(b1_points)
                    for i in range(100):
                        block_error_list.append(second_block)
                        block_payoff_list.append(b2_points)
                    for i in range(100):
                        block_error_list.append(third_block)
                        block_payoff_list.append(b3_points)
                    for i in range(100):
                        block_error_list.append(fourth_block)
                        block_payoff_list.append(b4_points)
                    for i in range(100):
                        block_error_list.append(fifth_block)
                        block_payoff_list.append(b5_points)
                    for i in range(100):
                        block_error_list.append(sixth_block)
                        block_payoff_list.append(b6_points)
                    for i in range(600):
                        game_point_list.append(sum(trails_total_payoff))

    return game_num_list, block_num_list, trail_num_list, conditions_list, p_inspection_list, fine_size_list,\
           trails_type_list, enforcement_list, correct_side_list, trails_total_payoff, trails_alternative_points,\
           trails_adding_points, trails_omitted_points, true_side_list, player_choice_list, block_error_list, \
           game_point_list, block_payoff_list


# print(play_game())


def save_to_csv():
    play_game()
    df = pd.DataFrame(list(zip(game_num_list, block_num_list, trail_num_list, conditions_list, p_inspection_list,
                               fine_size_list, trails_type_list, enforcement_list, correct_side_list, trails_total_payoff,
                               trails_adding_points, trails_alternative_points, trails_omitted_points, true_side_list,
                               player_choice_list, block_error_list, block_payoff_list, game_point_list)),
                      columns=['Game Num', 'Block Num', 'Trail Num', 'Condition', 'P Inspection', 'Fine Size',
                               'Trail Type', 'Inspection', 'Choice Correct', 'Trials Payoff', 'Points earned',
                               'Alternative Points', 'Points Fined', 'True Side',
                               'Choice', 'Block Errors', 'Block Points', 'Final score'])

    print(df)
    df.to_csv("output.csv", index=False)


save_to_csv()


def run_multiple_games(num_games=10):

    for num in range(num_games):  # loop that runs on the range of games number
        save_to_csv()  # insert to the variable what the function returns


# run_multiple_games()
