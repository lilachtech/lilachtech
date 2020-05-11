import random
import csv
import pandas as pd

# Empty lists
trail_num_list, trails_total_payoff, trails_adding_points, trails_omitted_points, trails_type, conditions_list,\
trails_type_list, enforcement_list, player_choice_list, p_inspection_list, fine_size_list, \
true_side_list, block_num_list, game_num_list = ([] for i in range(14))

points_counter = 0


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
    global points_counter

    if condition == 'high_enforcement' or condition == 'low_enforcement':
        if choice == 'right':
            points_counter += 20
            added_points = 20
            points_for_choice = added_points

        else:
            points_counter += 1
            added_points = 1
            points_for_choice = added_points

        if condition == 'high_enforcement' and correct_side != choice and inspection == 1:
            points_counter -= 20
            omitted_points = -20
            points_for_choice = added_points + omitted_points

        elif condition == 'low_enforcement' and correct_side != choice and inspection == 1:
            points_counter -= 180
            omitted_points = -180
            points_for_choice = added_points + omitted_points

    else:
        if choice == 'right':
            points_counter += 2
            added_points = 2
            points_for_choice = added_points

        else:
            points_counter += 1
            added_points = 1
            points_for_choice = added_points

    return points_for_choice, added_points, omitted_points


# print(reward_for_choice('low_enforcement', 'right', 'left', 1))


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

                if block == 0:  # list with trail number
                    trail_num_list.append(trail+1)
                else:
                    trail_num_list.append(trail + 101)

                round_type = trails_type.pop()  # type of trail
                trails_type_list.append(round_type)  # all trails type

                true_side = true_side_trail(round_type)  # Which side has more dots
                true_side_list.append(true_side)

                player_choice = random_player(true_side)  # Player choice
                player_choice_list.append(player_choice)

                enforcement_array = trail_inspection(game_condition)  # There is inspection?

                conditions_list.append(game_condition)  # list of trails condition

                enforcement = enforcement_array[0]
                enforcement_list.append(enforcement)

                p_inspection = enforcement_array[1]
                p_inspection_list.append(p_inspection)

                fine_size = enforcement_array[2]
                fine_size_list.append(fine_size)

                trail_payoff = reward_for_choice(game_condition, player_choice, true_side, enforcement)  # points earned
                # trails_unit_payoff = []
                # trails_unit_payoff.extend(trail_payoff)  # unit all together
                print(trail_payoff)
                total_added = trail_payoff[0]
                total = trail_payoff[1]  # the total payoff for the trail
                total_omitted = trail_payoff[2]

                # trails_total_payoff.append(total)  # array that contain total payoff for each trail
                trails_adding_points.append(total_added)  # earned points
                # trails_omitted_points.append(total_omitted)  # punishment omitted points

                if player_choice != true_side:  # check if needed to omit points
                    if enforcement == 1:
                        final_trail_payoff = total - total_omitted
                        trails_total_payoff.append(final_trail_payoff)
                        trails_omitted_points.append(total_omitted)
                        enforcement_list.append(1)
                    else:
                        final_trail_payoff = total
                        trails_total_payoff.append(final_trail_payoff)
                        trails_omitted_points.append(0)
                        enforcement_list.append(0)
                else:
                    trails_total_payoff.append(total)
                    trails_omitted_points.append(0)
                    enforcement_list.append(0)

    return game_num_list, block_num_list, trail_num_list, conditions_list, p_inspection_list, fine_size_list,\
           trails_type_list, enforcement_list, trails_total_payoff, trails_adding_points, trails_omitted_points, true_side_list, \
           player_choice_list


# print(play_game())


def save_to_csv():
    play_game()
    df = pd.DataFrame(list(zip(game_num_list, block_num_list, trail_num_list, conditions_list, p_inspection_list,
                               fine_size_list, trails_type_list, enforcement_list, trails_total_payoff,
                               trails_adding_points, trails_omitted_points, true_side_list, player_choice_list)),
                      columns=['Game Num', 'Block Num', 'Trail Num', 'Condition', 'P Inspection', 'Fine Size',
                               'Trail Type', 'Inspection', 'Trials Payoff', 'Points earned', 'Points Fined', 'True Side',
                               'Choice'])

    print(df)
    df.to_csv("output.csv", index=False)


save_to_csv()


def run_multiple_games(num_games=1):

    for num in range(num_games):  # loop that runs on the range of games number
        save_to_csv()  # insert to the variable what the function returns


# run_multiple_games()
