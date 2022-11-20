import sys
import matplotlib.pyplot as plt

# def find_next_number(list, start):
#     del_index += 1 # keep track of each next number we look at in the list, including how many times we went around in the circle
#             if player_list[(del_index - 1) % input] != -1: 
#                 skipped += 1 # increment skipped only when the number at del_index has not been deleted yet

def make_list_with_values(len, value):
    list = []
    for i in range(len):
        list.append(value)
    return list

def calculate(input, del_spacing):
    counter = 0
    player_list = list(range(input))
    deleted_player_list = make_list_with_values(input, -1)
    last_seen_number_index = -1

    while True:
        skipped = 0
        start_skip_loop_index = counter

        def found_next_player():
            return skipped >= del_spacing

        def no_players_left():
            return (counter - start_skip_loop_index) > input

        while True: # go around the loop no more than twice, stop when we skip enough numbers
            if player_list[(counter) % input] != -1: 
                skipped += 1 # increment skipped only when the number at counter has not been deleted yet
                last_seen_number_index = counter

            # Save the last player number and return
            if no_players_left():
                deleted_player_list[last_seen_number_index % input] = last_seen_number_index 
                return deleted_player_list

            if found_next_player():
                player_index = (counter) % input
                player_list[player_index] = -1 # Mark player as deleted
                deleted_player_list[player_index] = counter # Save counter at which player was deleted
                break

            counter += 1 # keep track of each next number we look at in the list, including how many times we went around in the circle


for i in range(2, 257):
    # print(max(calculate(i, 2)))
    print(i, max(calculate(i, 2)), max(calculate(i, 2)) - max(calculate(i-1, 2)))


# num_players = 3
# x = range(num_players)
# y = calculate(num_players, 2)

# print(int(max(y)) % num_players) 

# print(y)

# plt.scatter(x, y)
# plt.show()