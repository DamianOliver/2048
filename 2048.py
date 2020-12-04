from random import randrange, shuffle
import pygame as pg
from time import sleep
import collections as cl

pg.init()


score = 0

background_color = (250, 248, 239)
background_board = (187, 173, 160)

unhover = (200,200,200)
hover = (100,100,100)
button_color = unhover
new_game_hovered = False
tile_hovered = 0

game_end = False

board_size = 650
margin = 200
padding = 20
cell_size = (board_size - padding * 5) / 4
score_x = .75
score_y = 0.1
button_size = (200, 50)
score_size = (150, 50)
button_bar_size = (
    button_size[0] + score_size[0] + padding,
    button_size[1] + score_size[1] + padding
    )
button_bar_pos = (margin + board_size - button_bar_size[0], margin * 0.1)
screen_dimension = board_size + margin*2

cheat_pos = (margin + padding, margin + board_size - padding)
cheat_button_size = (150,150)
cheat_button_location_x = ((screen_dimension/5) - cheat_button_size[0]/2)
cheat_button_location_y = (margin*1.5 + board_size - cheat_button_size[0]/2)
cheat_button_color = (150,150,150)
cheat_button_border_color = (70,70,70)
options_rect_size = (screen_dimension/5, screen_dimension/5)
no_number_button_location = ((screen_dimension/5) - cheat_button_size[0]/2, cheat_button_location_y)
add_number_button_location = ((screen_dimension/5)*2.5 - cheat_button_size[0]/2, cheat_button_location_y)
possible_values_button_location = ((screen_dimension/5)*4 - cheat_button_size[0]/2, cheat_button_location_y)
cheat_padding = 10
add_options_location = (screen_dimension/2 - options_rect_size[0]/2, screen_dimension/2 - cheat_button_size[1]/2)
submit_button_size = (200,50)
submit_button_color = (30, 150, 30)
submit_button_location = (add_options_location[0] + screen_dimension/3, add_options_location[1] + options_rect_size[1]/4)
cancel_button_size = (200,50)
cancel_button_color = (150, 30, 30)
cancel_button_location = (add_options_location[0] - screen_dimension/3, add_options_location[1] + options_rect_size[1]/4)
add_value_button_size = (400,50)
add_value_button_color = (170,170,170)
add_value_button_hovered_color = (100,100,100)
add_value_button_location = (screen_dimension/2 - add_value_button_size[0]/2, add_options_location[1] + options_rect_size[1] + 50)

new_possible_values = []

highlight_color = (230, 230, 0)

add_instructions_location = (screen_dimension/2, 170)

cheat_font = pg.font.Font(None, 30)
new_numbers_clicked = False
add_number_clicked = False
possible_values_clicked = False
cheat_mode = False



screen = pg.display.set_mode((screen_dimension, screen_dimension))

print(cheat_pos)

colors = {
    0 : (238/1.15, 228/1.15, 218/1.15),
    2 : (238, 228, 218),
    4 : (238, 225, 201),
    8 : (243, 178, 122),
    16 : (246, 150, 100),
    32 : (247, 124, 95),
    64 : (247, 95, 59),
    128 : (237, 208, 115),
    256 : (237, 204, 98),
    512 : (237, 201, 80),
    1024 : (237, 197, 63),
    2048 : (237, 194, 46),
    4096 : (0,0,0),
    8192 : (0,0,0),
    16384 : (0,0,0),
    32768 : (0,0,0),
    65536 : (0,0,0),
}

tile_locations = {
    i : (margin + padding + (i%4) * (padding + cell_size),
         margin + padding + int(i/4) * (padding + cell_size))
    for i in range(0, 16)
}

end_screen_color = (100,100,100,80)
def right():
    print("RIGHT")
    global new_locations
    new_locations = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    print(new_locations)
    y = 0
    while y <= 15:
        new_locations[y] = locations[y]
        y += 1
    print(new_locations)
    move1c(start=2, increment=1, step=4)

    print(new_locations, "1c")

    move2c(1,1,4)

    print(new_locations, "2c")

    move3c(0,1,4)

    print(new_locations, "3c")

    copy_locations()
    board_create(locations)
    game_loss()

def left():
    print("LEFT")
    global new_locations
    new_locations = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    print(new_locations)
    y = 0
    while y <= 15:
        new_locations[y] = locations[y]
        y += 1
    print(new_locations)
    move1c(start=1, increment=-1, step=4)

    print("1c", new_locations)

    move2c(2,-1,4)

    print("2c", new_locations)

    move3c(3,-1,4)

    print("3c", new_locations)
    print(locations, "3c")

    copy_locations()
    board_create(locations)
    game_loss()

def up():
    print("UP")
    global new_locations
    global locations
    new_locations = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    print(new_locations)
    y = 0
    while y <= 15:
        new_locations[y] = locations[y]
        y += 1
    print(new_locations)
    move1c(start=4, increment=-4, step=1)

    move2c(8,-4,1)

    move3c(12,-4,1)

    print(locations, "3c")

    copy_locations()
    board_create(locations)
    game_loss()

def down():
    print("DOWN")
    global new_locations
    global locations
    new_locations = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    print(new_locations)
    y = 0
    while y <= 15:
        new_locations[y] = locations[y]
        y += 1
    print(new_locations)
    move1c(start=8, increment=4, step=1)

    move2c(4,4,1)

    move3c(0,4,1)

    copy_locations()
    board_create(locations)
    game_loss()

def copy_locations():
    global new_locations
    global locations
    x = 0
    while x <= len(locations):
        print(locations[x], "locations", new_locations[x], "new_locations", new_locations, "full new list", locations, "full locations")
        if locations[x] != new_locations[x]:
            break
        else:
            x += 1
            if x == 15:
                print("how did I get here?")
                return

    print("I did it")
    z = 0
    while z <= 15:
        locations[z] = new_locations[z]
        z += 1

    new_number()

def draw_number(a):
    global new_locations
    new_locations = locations
    number_value = locations[a]
    number_color = colors[locations[a]]
    cell_x = margin + padding + (cell_size + padding) * (a % 4)
    cell_y = margin + padding + int(a / 4) * (cell_size + padding)
    cell_font_size = 100
    if number_value > 1000:
        cell_font_size = 70
        if number_value > 10000:
            cell_font_size = 50
    pg.draw.rect((screen), (number_color), (cell_x, cell_y, cell_size, cell_size))
    cell_font = pg.font.Font(None, cell_font_size)
    text_color = (255,255,255)
    text = str(locations[a])
    if locations[a] == 0:
        text = ' '
    if locations[a] < 8:
        text_color = (40,40,40)
    text_x, text_y = text_pos(cell_font, text, cell_x, cell_y)
    cell_text = cell_font.render(text, True, (text_color))
    screen.blit(cell_text, (text_x, text_y))

def text_pos(cell_font, text, cell_x, cell_y):
    text_size = cell_font.size(text)
    text_x = cell_x + cell_size/2 - text_size[0]/2
    text_y = cell_y +  cell_size/2 - text_size[1]/2
    return text_x, text_y

def draw_button_bar():
    board_font = pg.font.Font(None, 40)
    pg.draw.rect((screen), background_color, (button_bar_pos[0], button_bar_pos[1], 600, 150))
    global button_pos
    button_pos = button_bar_pos
    button_text = board_font.render("New Game", True, (50,50,50))
    button_text_rect = button_text.get_rect(center = (button_pos[0] + button_size[0]/2, button_pos[1] + button_size[1]/2))
    new_button = pg.Surface(button_size)
    new_button.fill((button_color))
    screen.blit(new_button, button_pos)
    screen.blit(button_text, button_text_rect)

    global board_score_text

    board_score_text = board_font.render("Score: " + str(score), True, (50,50,50))
    score_x = button_bar_pos[0] + button_size[0] + padding
    score_center_y = button_bar_pos[1] + button_size[1]/2
    board_score_text_rect = board_score_text.get_rect(x = score_x, centery = score_center_y)
    screen.blit(board_score_text, board_score_text_rect)

    pg.display.update()

def board_create(locations):
    print("                                        ")
    print("| {} | {} | {} | {} |".format(*locations[0:4]))
    print("| {} | {} | {} | {} |".format(*locations[4:8]))
    print("| {} | {} | {} | {} |".format(*locations[8:12]))
    print("| {} | {} | {} | {} |".format(*locations[12:16]))

    pg.draw.rect(screen, background_board, (margin, margin, board_size, board_size))

    a = 0
    for i in locations:
        draw_number(a)
        a += 1
    pg.mouse.set_visible(True)

    draw_button_bar()
    background = pg.Surface(screen.get_size())
    pg.display.update()

def draw_border(border_size_x, border_size_y, border_x, border_y, padding, border_color, rect_color):
     pg.draw.rect(screen, border_color, (border_x, border_y, border_size_x, border_size_y))
     pg.draw.rect(screen, rect_color, (border_x + padding, border_y + padding, border_size_x - padding*2, border_size_y - padding*2))

def new_number():
    if new_numbers:
        global locations
        possible_locations = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
        i = 0
        shuffle(possible_locations)
        while i <= len(locations) - 1:
            new_location = possible_locations[i]
            print("new_location: ", new_location)
            if locations[new_location] == 0:
                locations[new_location] = possible_values[(randrange(0,len(possible_values)))]
                print(new_location)
                break
            i += 1

# this is here that I can find find this spot more easily
# this is here that I can find find this spot more easily
# this is here that I can find find this spot more easily
# this is here that I can find find this spot more easily

def draw_cheat():
    global new_numbers
    global new_numbers_clicked
    global add_number_clicked
    global possible_values_clicked
    global new_possible_values
    global possible_values
    global add_value_button_color
    if new_numbers_clicked:
        new_numbers_clicked = False
        if not new_numbers:
            no_number_3 = "Off"
            no_number_button = pg.Surface(cheat_button_size)
            no_number_button.fill(cheat_button_color)
            screen.blit(no_number_button, no_number_button_location)

            no_number_button_text_1 = cheat_font.render("No", True, (50,50,50))
            no_number_button_text_rect_1 = no_number_button_text_1.get_rect(center = (cheat_button_location_x + cheat_button_size[0]/2, cheat_button_location_y + cheat_button_size[1]/2 - 25))
            screen.blit(no_number_button_text_1, no_number_button_text_rect_1)

            no_number_button_text_2 = cheat_font.render("Numbers", True, (50,50,50))
            no_number_button_text_rect_2 = no_number_button_text_2.get_rect(center = (cheat_button_location_x + cheat_button_size[0]/2, cheat_button_location_y + cheat_button_size[1]/2))
            screen.blit(no_number_button_text_2, no_number_button_text_rect_2)

            no_number_button_text_3 = cheat_font.render(no_number_3, True, (50,50,50))
            no_number_button_text_rect_3 = no_number_button_text_3.get_rect(center = (cheat_button_location_x + cheat_button_size[0]/2, cheat_button_location_y + cheat_button_size[1]/2 + 25))
            screen.blit(no_number_button_text_3, no_number_button_text_rect_3)
            new_numbers = True
            pg.display.update()

        elif new_numbers:
            no_number_3 = "On"
            draw_border(cheat_button_size[0], cheat_button_size[1], no_number_button_location[0], no_number_button_location[1], cheat_padding, cheat_button_border_color, cheat_button_color)
            no_number_button_text_1 = cheat_font.render("No", True, (50,50,50))
            no_number_button_text_rect_1 = no_number_button_text_1.get_rect(center = (cheat_button_location_x + cheat_button_size[0]/2, cheat_button_location_y + cheat_button_size[1]/2 - 25))
            screen.blit(no_number_button_text_1, no_number_button_text_rect_1)

            no_number_button_text_2 = cheat_font.render("Numbers", True, (50,50,50))
            no_number_button_text_rect_2 = no_number_button_text_2.get_rect(center = (cheat_button_location_x + cheat_button_size[0]/2, cheat_button_location_y + cheat_button_size[1]/2))
            screen.blit(no_number_button_text_2, no_number_button_text_rect_2)

            no_number_button_text_3 = cheat_font.render(no_number_3, True, (50,50,50))
            no_number_button_text_rect_3 = no_number_button_text_3.get_rect(center = (cheat_button_location_x + cheat_button_size[0]/2, cheat_button_location_y + cheat_button_size[1]/2 + 25))
            screen.blit(no_number_button_text_3, no_number_button_text_rect_3)
            new_numbers = False
            pg.display.update()

    elif add_number_clicked:
        add_number_clicked = False
        options_font_size = 150
        pg.draw.rect(screen, (150,150,150), (0, screen_dimension/3, screen_dimension, screen_dimension/3))
        add_number_message_font = pg.font.Font(None, 80)
        add_number_message = add_number_message_font.render("Click to Increase Value", True, (50,50,50))
        add_number_message_rect = add_number_message.get_rect(center = (screen_dimension/2, screen_dimension/3 + 40))
        screen.blit(add_number_message, add_number_message_rect)

        add_options_value = 2
        add_options_rect = pg.Surface((options_rect_size))
        options_value_font = pg.font.Font(None, options_font_size)
        options_value_text = options_value_font.render(str(add_options_value), True, (50,50,50))
        options_value_text_rect = options_value_text.get_rect(center = (add_options_location[0] + options_rect_size[0]/2, add_options_location[1] + options_rect_size[1]/2))
        add_options_rect.fill(colors[add_options_value])
        screen.blit(add_options_rect, add_options_location)
        screen.blit(options_value_text, options_value_text_rect)

        submit_number_button = pg.Surface(submit_button_size)
        submit_number_button.fill(submit_button_color)
        screen.blit(submit_number_button, submit_button_location)

        submit_font = pg.font.Font(None, 40)
        submit_text = submit_font.render("Submit", True, (50,50,50))
        submit_text_rect = submit_text.get_rect(center = (submit_button_location[0] + submit_button_size[0]/2, submit_button_location[1] + submit_button_size[1]/2))
        screen.blit(submit_text, submit_text_rect)

        cancel_number_button = pg.Surface(cancel_button_size)
        cancel_number_button.fill(cancel_button_color)
        screen.blit(cancel_number_button, cancel_button_location)

        cancel_font = pg.font.Font(None, 40)
        cancel_text = cancel_font.render("Cancel", True, (0,0,0))
        cancel_text_rect = cancel_text.get_rect(center = (cancel_button_location[0] + cancel_button_size[0]/2, cancel_button_location[1] + cancel_button_size[1]/2))
        screen.blit(cancel_text, cancel_text_rect)
        pg.display.update()
        while True:
            global tile_hovered
            for event in pg.event.get():
                if event.type == pg.MOUSEBUTTONDOWN:
                    if pg.mouse.get_pos()[0] > add_options_location[0] and pg.mouse.get_pos()[0] < add_options_location[0] + options_rect_size[0] and pg.mouse.get_pos()[1] > add_options_location[1] and pg.mouse.get_pos()[1] < add_options_location[1] + options_rect_size[1]:
                        if add_options_value == 2048:
                            add_options_value = 2
                        else:
                            add_options_value = add_options_value * 2
                        if add_options_value >= 1000:
                            options_font_size = 110
                        else:
                            options_font_size = 150
                        print(options_font_size)
                        options_color = (50,50,50)
                        if add_options_value >= 8:
                            options_color = (255,255,255)
                        options_value_font = pg.font.Font(None, options_font_size)
                        options_value_text = options_value_font.render(str(add_options_value), True, (options_color))
                        options_value_text_rect = options_value_text.get_rect(center = (add_options_location[0] + options_rect_size[0]/2, add_options_location[1] + options_rect_size[1]/2))
                        add_options_rect.fill(colors[add_options_value])
                        screen.blit(add_options_rect, add_options_location)
                        screen.blit(options_value_text, options_value_text_rect)
                        pg.display.update()
                    elif pg.mouse.get_pos()[0] > submit_button_location[0] and pg.mouse.get_pos()[0] < submit_button_location[0] + submit_button_size[0] and pg.mouse.get_pos()[1] > submit_button_location[1] and pg.mouse.get_pos()[1] < submit_button_location[1] + submit_button_size[1]:
                        pg.draw.rect(screen, background_color, ( 0, screen_dimension/3, screen_dimension, screen_dimension/3))
                        board_create(locations)

                        add_instructions_text_variable = "Click an Empty Location to Place Your Tile"
                        add_instructions_font = pg.font.Font(None, 40)
                        add_instructions_text = add_instructions_font.render(add_instructions_text_variable, True, (50,50,50))
                        add_instructions_text_rect = add_instructions_text.get_rect(center = (add_instructions_location[0], add_instructions_location[1]))
                        screen.blit(add_instructions_text, add_instructions_text_rect)
                        pg.display.update()

                        while True:
                            for event in pg.event.get():
                                if event.type == pg.MOUSEBUTTONDOWN:
                                    current_square = which_square()
                                    print(current_square)
                                    if current_square < 20:
                                        if locations[current_square] == 0:
                                            locations[current_square] = add_options_value
                                            draw_border(cell_size + padding, cell_size + padding, tile_locations[tile_hovered][0] - padding/2, tile_locations[tile_hovered][1] - padding/2, padding/2, (background_board), colors[0])
                                            draw_number(tile_hovered)
                                            draw_number(current_square)
                                            pg.draw.rect(screen, background_color, (0, margin - 70, screen_dimension, 70))
                                            pg.display.update()
                                            return
                                current_square = 20
                                if event.type == pg.MOUSEMOTION:
                                    current_square = which_square()
                                    print(current_square)
                                    if current_square != tile_hovered:
                                        draw_border(cell_size + padding, cell_size + padding, tile_locations[tile_hovered][0] - padding/2, tile_locations[tile_hovered][1] - padding/2, padding/2, (background_board), colors[0])
                                        draw_number(tile_hovered)
                                        pg.display.update()
                                        if current_square != 20:
                                            if current_square < 20:
                                                draw_border(cell_size + padding, cell_size + padding, tile_locations[current_square][0] - padding/2, tile_locations[current_square][1] - padding/2, padding/2, (255,255,0), colors[0])
                                                draw_number(current_square)
                                                pg.display.update()
                                                tile_hovered = current_square
                                elif event.type == pg.QUIT:
                                    pg.quit()

                    elif pg.mouse.get_pos()[0] > cancel_button_location[0] and pg.mouse.get_pos()[0] < cancel_button_location[0] + cancel_button_size[0] and pg.mouse.get_pos()[1] > cancel_button_location[1] and pg.mouse.get_pos()[1] < cancel_button_location[1] + cancel_button_size[1]:
                        pg.draw.rect(screen, background_color, (0, screen_dimension/3, screen_dimension, screen_dimension/3))
                        board_create(locations)
                        return("cancel")
                elif event.type == pg.QUIT:
                    pg.quit()



    elif possible_values_clicked:
        print("It vas clicked")
        add_number_clicked = False
        options_font_size = 150
        pg.draw.rect(screen, (150,150,150), (0, screen_dimension/2 - screen_dimension/4, screen_dimension, screen_dimension/2))
        add_number_message_font = pg.font.Font(None, 80)
        add_number_text = "Click to Increase Value"
        add_number_message = add_number_message_font.render(add_number_text, True, (50,50,50))
        add_number_message_rect = add_number_message.get_rect(center = (screen_dimension/2, screen_dimension/3 + 40))
        screen.blit(add_number_message, add_number_message_rect)

        add_options_value = 2
        add_options_rect = pg.Surface((options_rect_size))
        options_value_font = pg.font.Font(None, options_font_size)
        options_value_text = options_value_font.render(str(add_options_value), True, (50,50,50))
        options_value_text_rect = options_value_text.get_rect(center = (add_options_location[0] + options_rect_size[0]/2, add_options_location[1] + options_rect_size[1]/2))
        add_options_rect.fill(colors[add_options_value])
        screen.blit(add_options_rect, add_options_location)
        screen.blit(options_value_text, options_value_text_rect)

        submit_number_button = pg.Surface(submit_button_size)
        submit_number_button.fill(submit_button_color)
        screen.blit(submit_number_button, submit_button_location)

        submit_font = pg.font.Font(None, 40)
        submit_text = submit_font.render("Submit", True, (50,50,50))
        submit_text_rect = submit_text.get_rect(center = (submit_button_location[0] + submit_button_size[0]/2, submit_button_location[1] + submit_button_size[1]/2))
        screen.blit(submit_text, submit_text_rect)

        cancel_number_button = pg.Surface(cancel_button_size)
        cancel_number_button.fill(cancel_button_color)
        screen.blit(cancel_number_button, cancel_button_location)

        cancel_font = pg.font.Font(None, 40)
        cancel_text = cancel_font.render("Cancel", True, (0,0,0))
        cancel_text_rect = cancel_text.get_rect(center = (cancel_button_location[0] + cancel_button_size[0]/2, cancel_button_location[1] + cancel_button_size[1]/2))
        screen.blit(cancel_text, cancel_text_rect)
        pg.display.update()

        add_value_button = pg.Surface(add_value_button_size)
        add_value_button.fill(add_value_button_color)
        screen.blit(add_value_button, add_value_button_location)

        add_value_font = pg.font.Font(None, 40)
        add_value_text = cancel_font.render("Add To Possible Values", True, (50,50,50))
        add_value_text_rect = cancel_text.get_rect(center = (add_value_button_location[0] + add_value_button_size[0]/4, add_value_button_location[1] + add_value_button_size[1]/2))
        screen.blit(add_value_text, add_value_text_rect)
        pg.display.update()

        new_possible_values = []

        while True:
            for event in pg.event.get():
                if event.type == pg.MOUSEBUTTONDOWN:
                    if pg.mouse.get_pos()[0] > add_options_location[0] and pg.mouse.get_pos()[0] < add_options_location[0] + options_rect_size[0] and pg.mouse.get_pos()[1] > add_options_location[1] and pg.mouse.get_pos()[1] < add_options_location[1] + options_rect_size[1]:
                        if add_options_value == 2048:
                            add_options_value = 2
                        else:
                            add_options_value = add_options_value * 2
                        if add_options_value >= 1000:
                            options_font_size = 110
                        else:
                            options_font_size = 150
                        print(options_font_size)
                        options_color = (50,50,50)
                        if add_options_value >= 8:
                            options_color = (255,255,255)
                        options_value_font = pg.font.Font(None, options_font_size)
                        options_value_text = options_value_font.render(str(add_options_value), True, (options_color))
                        options_value_text_rect = options_value_text.get_rect(center = (add_options_location[0] + options_rect_size[0]/2, add_options_location[1] + options_rect_size[1]/2))
                        print(add_options_value)
                        add_options_rect.fill(colors[add_options_value])
                        screen.blit(add_options_rect, add_options_location)
                        screen.blit(options_value_text, options_value_text_rect)
                        pg.display.update()
                    elif pg.mouse.get_pos()[0] > submit_button_location[0] and pg.mouse.get_pos()[0] < submit_button_location[0] + submit_button_size[0] and pg.mouse.get_pos()[1] > submit_button_location[1] and pg.mouse.get_pos()[1] < submit_button_location[1] + submit_button_size[1]:
                        if len(new_possible_values) > 0:
                            pg.draw.rect(screen, (background_color), (0, screen_dimension/2 - screen_dimension/4, screen_dimension, screen_dimension/2))
                            board_create(locations)
                            possible_values = []
                            for i in range(len(new_possible_values)):
                                possible_values.append(new_possible_values[i])
                            print(possible_values)
                            return
                            pg.display.update()
                        else:
                            add_number_text = "Please Add Your Values Before Submitting"
                            add_number_message_font = pg.font.Font(None, 60)
                            pg.draw.rect(screen, (150,150,150), (0, screen_dimension/2 - screen_dimension/4, screen_dimension, 150))
                            add_number_message = add_number_message_font.render(add_number_text, True, (240,50,50))
                            add_number_message_rect = add_number_message.get_rect(center = (screen_dimension/2, screen_dimension/3 + 40))
                            screen.blit(add_number_message, add_number_message_rect)
                            pg.display.update()
                    elif pg.mouse.get_pos()[0] > add_value_button_location[0] and pg.mouse.get_pos()[0] < add_value_button_location[0] + add_value_button_size[0] and pg.mouse.get_pos()[1] > add_value_button_location[1] and pg.mouse.get_pos()[1] < add_value_button_location[1] + add_value_button_size[1]:
                        if add_number_text != "Click to Increase Value":
                            add_number_text = "Click to Increase Value"
                            pg.draw.rect(screen, (150,150,150), (0, screen_dimension/2 - screen_dimension/4, screen_dimension, 150))
                            add_number_message = add_number_message_font.render(add_number_text, True, (50,50,50))
                            add_number_message_rect = add_number_message.get_rect(center = (screen_dimension/2, screen_dimension/3 + 40))
                            screen.blit(add_number_message, add_number_message_rect)
                            pg.display.update()

                        clicked_add_value_button = pg.Surface(add_value_button_size)
                        clicked_add_value_button.fill((70,70,70))
                        screen.blit(clicked_add_value_button, add_value_button_location)

                        add_value_font = pg.font.Font(None, 40)
                        add_value_text = cancel_font.render("Add To Possible Values", True, (50,50,50))
                        add_value_text_rect = cancel_text.get_rect(center = (add_value_button_location[0] + add_value_button_size[0]/4, add_value_button_location[1] + add_value_button_size[1]/2))
                        screen.blit(add_value_text, add_value_text_rect)
                        pg.display.update()

                        pg.time.wait(100)

                        add_value_button_color = (add_value_button_color)
                        add_value_button = pg.Surface(    add_value_button_size)
                        add_value_button.fill(add_value_button_color)
                        screen.blit(add_value_button, add_value_button_location)

                        add_value_font = pg.font.Font(None, 40)
                        add_value_text = cancel_font.render("Add To Possible Values", True, (50,50,50))
                        add_value_text_rect = cancel_text.get_rect(center = (add_value_button_location[0] + add_value_button_size[0]/4, add_value_button_location[1] + add_value_button_size[1]/2))
                        screen.blit(add_value_text, add_value_text_rect)
                        pg.display.update()
                        new_possible_values.append(add_options_value)
                    elif pg.mouse.get_pos()[0] > cancel_button_location[0] and pg.mouse.get_pos()[0] < cancel_button_location[0] + cancel_button_size[0] and pg.mouse.get_pos()[1] > cancel_button_location[1] and pg.mouse.get_pos()[1] < cancel_button_location[1] + cancel_button_size[1]:
                        pg.draw.rect(screen, (background_color), (0, screen_dimension/2 - screen_dimension/4, screen_dimension, screen_dimension/2))
                        board_create(locations)
                        return("cancel")
                elif event.type == pg.QUIT:
                    pg.quit()

def draw_start_cheat():
    no_number_3 = "Off"
    no_number_button = pg.Surface(cheat_button_size)
    no_number_button.fill(cheat_button_color)
    screen.blit(no_number_button, no_number_button_location)

    no_number_button_text_1 = cheat_font.render("No", True, (50,50,50))
    no_number_button_text_rect_1 = no_number_button_text_1.get_rect(center = (cheat_button_location_x + cheat_button_size[0]/2, cheat_button_location_y + cheat_button_size[1]/2 - 25))
    screen.blit(no_number_button_text_1, no_number_button_text_rect_1)

    no_number_button_text_2 = cheat_font.render("Numbers", True, (50,50,50))
    no_number_button_text_rect_2 = no_number_button_text_2.get_rect(center = (cheat_button_location_x + cheat_button_size[0]/2, cheat_button_location_y + cheat_button_size[1]/2))
    screen.blit(no_number_button_text_2, no_number_button_text_rect_2)

    no_number_button_text_3 = cheat_font.render(no_number_3, True, (50,50,50))
    no_number_button_text_rect_3 = no_number_button_text_3.get_rect(center = (cheat_button_location_x + cheat_button_size[0]/2, cheat_button_location_y + cheat_button_size[1]/2 + 25))
    screen.blit(no_number_button_text_3, no_number_button_text_rect_3)

    add_number_button = pg.Surface(cheat_button_size)
    add_number_button.fill(cheat_button_color)
    screen.blit(add_number_button, ((screen_dimension/5)*2.5 - cheat_button_size[0]/2, cheat_button_location_y))

    add_number_button_text_1 = cheat_font.render("Add", True, (50,50,50))
    add_number_button_text_rect_1 = add_number_button_text_1.get_rect(center = (add_number_button_location[0] + cheat_button_size[0]/2, cheat_button_location_y + cheat_button_size[1]/2 - 12))
    screen.blit(add_number_button_text_1, add_number_button_text_rect_1)

    add_number_button_text_2 = cheat_font.render("Numbers", True, (50,50,50))
    add_number_button_text_rect_2 = add_number_button_text_2.get_rect(center = (add_number_button_location[0] + cheat_button_size[0]/2, cheat_button_location_y + cheat_button_size[1]/2 + 12))
    screen.blit(add_number_button_text_2, add_number_button_text_rect_2)

    possible_values_button = pg.Surface(cheat_button_size)
    possible_values_button.fill(cheat_button_color)
    screen.blit(possible_values_button, ((screen_dimension/5)*4 - cheat_button_size[0]/2, cheat_button_location_y))

    possible_values_button_text_1 = cheat_font.render("Edit", True, (50,50,50))
    add_number_button_text_rect_1 = add_number_button_text_1.get_rect(center = (possible_values_button_location[0] + cheat_button_size[0]/2, cheat_button_location_y + cheat_button_size[1]/2 - 25))
    screen.blit(add_number_button_text_1, add_number_button_text_rect_1)

    possible_values_button_text_2 = cheat_font.render("Possible", True, (50,50,50))
    possible_values_button_text_rect_2 = possible_values_button_text_2.get_rect(center = (possible_values_button_location[0] + cheat_button_size[0]/2, cheat_button_location_y + cheat_button_size[1]/2))
    screen.blit(possible_values_button_text_2, possible_values_button_text_rect_2)

    possible_values_button_text_2 = cheat_font.render("Values", True, (50,50,50))
    possible_values_button_text_rect_2 = possible_values_button_text_2.get_rect(center = (possible_values_button_location[0] + cheat_button_size[0]/2, cheat_button_location_y + cheat_button_size[1]/2 + 25))
    screen.blit(possible_values_button_text_2, possible_values_button_text_rect_2)

    pg.display.update()

def move1c(start, increment, step):
    for i in range(0, 4):
        move1c_step(start + i * step, start + i * step + increment)

def move1c_step(a, b):
    global score
    global new_locations
    if new_locations[a] != 0:
        print("move1c called")
        if new_locations[a] == new_locations[b]:
            new_locations[b] = new_locations[a]+new_locations[b]
            new_locations[a] = 0
            score += new_locations[b]
        elif new_locations[b] == 0:
            new_locations[b] = new_locations[a]
            new_locations[a] = 0

def move2c(start, increment, step):
    for i in range(0,4):
        move2c_step(start + i * step, start + i * step + increment, start + i * step + increment*2)

def move2c_step(a,b,c):
    print(a, b, c)
    global score
    if new_locations[a] != 0:
        print("move2c called")
        if new_locations[a] == new_locations[b]:
            new_locations[b] = new_locations[a]+new_locations[b]
            score += new_locations[b]
            new_locations[a] = 0
        elif new_locations[b] == 0:
            if new_locations[a] == new_locations[c]:
                new_locations[c] = new_locations[a]+new_locations[c]
                score += new_locations[c]
                new_locations[a] = 0
            elif new_locations[c] == 0:
                new_locations[c] = new_locations[a]
                new_locations[a] = 0
            else:
                new_locations[b] = new_locations[a]
                new_locations[a] = 0

def move3c(start, increment, step):
    for i in range(0,4):
        move3c_step(start + i * step, start + i * step + increment, start + i * step + increment*2, start + i * step + increment*3)


def move3c_step(a,b,c,d):
    global score
    if new_locations[a] != 0:
        print("move3c called")
        if new_locations[a] == new_locations[b]:
            new_locations[b] = new_locations[a]+new_locations[b]
            score += new_locations[b]
            new_locations[a] = 0
        elif new_locations[b] == 0:
            if new_locations[a] == new_locations[c]:
                new_locations[c] = new_locations[a]+new_locations[c]
                score += new_locations[c]
                new_locations[a] = 0
            elif new_locations[c] == 0:
                if new_locations[a] == new_locations[d]:
                    new_locations[d] = new_locations[a]+new_locations[d]
                    score += new_locations[d]
                    new_locations[a] = 0
                elif new_locations[d] == 0:
                    new_locations[d] = new_locations[a]
                    new_locations[a] = 0
                else:
                    new_locations[c] = new_locations[a]
                    new_locations[a] = 0
            else:
                new_locations[b] = new_locations[a]
                new_locations[a] = 0

def which_square():
    if pg.mouse.get_pos()[0] > margin + padding and pg.mouse.get_pos()[0] < margin + padding + cell_size:
        if pg.mouse.get_pos()[1] > margin + padding and pg.mouse.get_pos()[1] < margin + padding + cell_size:
            return 0
        elif pg.mouse.get_pos()[1] > margin + padding + cell_size + padding and pg.mouse.get_pos()[1] < margin + padding + padding + cell_size + cell_size:
            return 4
        elif pg.mouse.get_pos()[1] > margin + padding + (cell_size + padding)*2 and pg.mouse.get_pos()[1] < margin + padding + cell_size + (cell_size + padding)*2:
            return 8
        elif pg.mouse.get_pos()[1] > margin + padding + (cell_size + padding)*3 and pg.mouse.get_pos()[1] < margin + padding + cell_size + (cell_size + padding)*3:
            return 12
        else:
            return 20
    elif pg.mouse.get_pos()[0] > margin + padding + cell_size + padding and pg.mouse.get_pos()[0] < margin + padding + padding + cell_size + cell_size:
        if pg.mouse.get_pos()[1] > margin + padding and pg.mouse.get_pos()[1] < margin + padding + cell_size:
            return 1
        elif pg.mouse.get_pos()[1] > margin + padding + cell_size + padding and pg.mouse.get_pos()[1] < margin + padding + padding + cell_size + cell_size:
            return 5
        elif pg.mouse.get_pos()[1] > margin + padding + (cell_size + padding)*2 and pg.mouse.get_pos()[1] < margin + padding + cell_size + (cell_size + padding)*2:
            return 9
        elif pg.mouse.get_pos()[1] > margin + padding + (cell_size + padding)*3 and pg.mouse.get_pos()[1] < margin + padding + cell_size + (cell_size + padding)*3:
            return 13
        else:
            return 20
    elif pg.mouse.get_pos()[0] > margin + padding + (cell_size + padding)*2 and pg.mouse.get_pos()[0] < margin + padding + cell_size + (cell_size + padding)*2:
        if pg.mouse.get_pos()[1] > margin + padding and pg.mouse.get_pos()[1] < margin + padding + cell_size:
            return 2
        elif pg.mouse.get_pos()[1] > margin + padding + cell_size + padding and pg.mouse.get_pos()[1] < margin + padding + padding + cell_size + cell_size:
            return 6
        elif pg.mouse.get_pos()[1] > margin + padding + (cell_size + padding)*2 and pg.mouse.get_pos()[1] < margin + padding + cell_size + (cell_size + padding)*2:
            return 10
        elif pg.mouse.get_pos()[1] > margin + padding + (cell_size + padding)*3 and pg.mouse.get_pos()[1] < margin + padding + cell_size + (cell_size + padding)*3:
            return 14
        else:
            return 20
    elif pg.mouse.get_pos()[0] > margin + padding + (cell_size + padding)*3 and pg.mouse.get_pos()[0] < margin + padding + cell_size + (cell_size + padding)*3:
        if pg.mouse.get_pos()[1] > margin + padding and pg.mouse.get_pos()[1] < margin + padding + cell_size:
            return 3
        elif pg.mouse.get_pos()[1] > margin + padding + cell_size + padding and pg.mouse.get_pos()[1] < margin + padding + padding + cell_size + cell_size:
            return 7
        elif pg.mouse.get_pos()[1] > margin + padding + (cell_size + padding)*2 and pg.mouse.get_pos()[1] < margin + padding + cell_size + (cell_size + padding)*2:
            return 11
        elif pg.mouse.get_pos()[1] > margin + padding + (cell_size + padding)*3 and pg.mouse.get_pos()[1] < margin + padding + cell_size + (cell_size + padding)*3:
            return 15
        else:
            return 20
    else:
        return 20


def game_start():
    global game_end
    global cheat_mode
    global new_numbers
    game_end = False
    new_numbers = True
    global possible_values
    possible_values = [2,2,2,2,2,2,2,2,2,4]
    global locations
    locations = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    global score
    score = 0
    print("game start")
    new_number()
    new_number()
    screen = pg.display.set_mode([board_size + margin*2, board_size + margin * 2], pg.DOUBLEBUF, 32)
    screen.fill(background_color)
    pg.display.set_caption("2048")
    board_create(locations)
    if cheat_mode:
        draw_start_cheat()

def game_over():
    print("game over")
    global screen
    draw_button_bar()
    end_screen = pg.Surface((board_size, board_size))
    end_screen.set_alpha(190)
    end_screen.fill((210,210,210))
    screen.blit(end_screen, (margin, margin))
    font_score = pg.font.Font(None, 100)
    font_score_text = pg.font.Font(None, 75)
    end_score_text = font_score.render("Final Score:", True, (100,100,100))
    end_score_text_rect = end_score_text.get_rect(center = ((board_size/2 + margin), ((board_size/5.5 + margin))))
    end_score = font_score.render(str(score), True, (100,100,100))
    screen.blit(end_score_text, end_score_text_rect)
    end_score_rect = end_score.get_rect(center = ((board_size/2 + margin), ((board_size/3.5 + margin))))
    screen.blit(end_score, end_score_rect)
    pg.display.update()
    global game_end
    game_end = True



def game_loss():
    print("game loss")
    piece_check = ['true','true','true','true','true','true','true','true','true','true','true','true','true','true','true','true']
    a = 0
    while a <= len(locations) -1:
        if locations[a] != 0:
            if a == 0:
                if locations[a+1] != locations[a] and locations[a+4] != locations[a]:
                    piece_check[a] = 'false'
            elif a == 1 or a == 2:
                if locations[a+1] != locations[a] and locations[a+4] != locations[a] and locations[a-1] != locations[a]:
                    piece_check[a] = 'false'
            elif a == 3:
                if locations[a+4] != locations[a] and locations[a-1] != locations[a]:
                    piece_check[a] = 'false'
            elif a == 4 or a == 8:
                if locations[a+4] != locations[a] and locations[a+1] != locations[a] and locations[a-4] != locations[a]:
                    piece_check[a] = 'false'
            elif a == 5 or a == 6 or a == 9 or a == 10:
                if locations[a+1] != locations[a] and locations[a-1] != locations[a] and locations[a+4] != locations[a] and locations[a-4] != locations[a]:
                    piece_check[a] = 'false'
            elif a == 7 or a == 11:
                if locations[a+4] != locations[a] and locations[a-4] != locations[a] and locations[a-1]:
                    piece_check[a] = 'false'
            elif a == 12:
                if locations[a-4] != locations[a] and locations[a+1] != locations[a]:
                     piece_check[a] = 'false'
            elif a == 13 or a == 14:
                if locations[a-1] != locations[a] and locations[a+1] != locations[a] and locations[a-4] != locations[a]:
                    piece_check[a] = 'false'
            elif a == 15:
                if locations[a-1] != locations[a] and locations[a-4] != locations[a]:
                    piece_check[a] = 'false'
        a += 1
    print(piece_check)
    a = 0
    while a <= len(piece_check) - 1:
        if piece_check[a] == 'true':
            return 'you good'
        a += 1
    game_over()


game_start()

while (True):
    sleep(0.05)
    for event in pg.event.get():
        if event.type == pg.MOUSEMOTION:
            if pg.mouse.get_pos()[0] > button_pos[0] and pg.mouse.get_pos()[0] < button_pos[0] + button_size[0] and pg.mouse.get_pos()[1] > button_pos[1] and pg.mouse.get_pos()[1] < button_pos[1] + button_size[1]:
                if not new_game_hovered:
                    new_game_hovered = True
                    button_color = hover
                    print(button_color)
                    draw_button_bar()
            else:
                if new_game_hovered:
                    new_game_hovered = False
                    button_color = unhover
                    draw_button_bar()
        if event.type == pg.MOUSEBUTTONDOWN:
            if pg.mouse.get_pos()[0] > button_pos[0] and pg.mouse.get_pos()[0] < button_pos[0] + button_size[0] and pg.mouse.get_pos()[1] > button_pos[1] and pg.mouse.get_pos()[1] < button_pos[1] + button_size[1]:
                game_start()
            elif cheat_mode:
                if pg.mouse.get_pos()[0] > no_number_button_location[0] and pg.mouse.get_pos()[0] < no_number_button_location[0] + cheat_button_size[0] and pg.mouse.get_pos()[1] > no_number_button_location[1] and pg.mouse.get_pos()[1] < no_number_button_location[1] + cheat_button_size[1]:
                    new_numbers_clicked = True
                    draw_cheat()
                elif pg.mouse.get_pos()[0] > add_number_button_location[0] and pg.mouse.get_pos()[0] < add_number_button_location[0] + cheat_button_size[0] and pg.mouse.get_pos()[1] > add_number_button_location[1] and pg.mouse.get_pos()[1] < add_number_button_location[1] + cheat_button_size[1]:
                    add_number_clicked = True
                    draw_cheat()
                elif pg.mouse.get_pos()[0] > possible_values_button_location[0] - cheat_button_size[0]/2 and pg.mouse.get_pos()[0] < possible_values_button_location[0] + cheat_button_size[0] and pg.mouse.get_pos()[1] > possible_values_button_location[1] and pg.mouse.get_pos()[1] < possible_values_button_location[1] + cheat_button_size[1]:
                    possible_values_clicked = True
                    draw_cheat()

        if event.type == pg.QUIT:
            pg.quit()
        if not game_end:
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_UP:
                        up()
                elif event.key == pg.K_DOWN:
                        down()
                elif event.key == pg.K_RIGHT:
                        right()
                elif event.key == pg.K_LEFT:
                        left()
                elif event.key == pg.K_y:
                        if pg.mouse.get_pos()[0] > cheat_pos[0] and pg.mouse.get_pos()[0] < cheat_pos[0] + cell_size and pg.mouse.get_pos()[1] < cheat_pos[1] - cell_size and pg.mouse.get_pos()[1] > button_pos[1]:
                            cheat_mode = True
                            draw_start_cheat()
