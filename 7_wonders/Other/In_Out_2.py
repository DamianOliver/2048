def calculate(n, a):
    a -= 1
    del_index = 0
    player_list = []
    for i in range(n):
        player_list.append(i)
    
    while len(player_list) > 1:
        del_index += a

        while del_index > len(player_list) - 1:
            del_index -= len(player_list)

        del(player_list[del_index])

    return player_list

def calculate_2(input):
    return ((2 ^ input) % input) + 1

def recursive(n, a):
    if n == 1:
        return 0
    return (recursive(n-1, a) + a) % n

def print_resets():
    for i in range(1, 300):
        if calculate(i) < calculate(i-1):
            print("reset at: {}, from {} to {}".format(i, calculate(i-1), calculate(i)))

def print_calc(low, high):
    for i in range(low, high):
        print(i, calculate(i), i*3)

def check(n):
    if recursive(n, 10) == calculate(n, 10)[0]:
        return 1
    else:
        print(n, "- incorrect: ", recursive(n, 2), calculate(n, 2))

num_correct = 0
for i in range (1, 700):
    num_correct += check(i)

print(num_correct)