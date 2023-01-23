from random import randint
import time

logo = """
 _   _      _             _             
| | (_)    | |           | |            
| |_ _  ___| |_ __ _  ___| |_ ___   ___ 
| __| |/ __| __/ _` |/ __| __/ _ \ / _ \ 
| |_| | (__| || (_| | (__| || (_) |  __/
 \__|_|\___|\__\__,_|\___|\__\___/ \___|
"""

VALUE_USER = "X"
VALUE_COMPUTER = "O"
VALUES = ["X", "O"]


def get_computer_choice():
    if len(values_dictionary["X"] + values_dictionary["O"]) < 9:
        col_num = randint(1, 3)
        row_num = randint(1, 3)
        found = False
        for row in range(1, 4):
            for col in range(1, 4):
                for letter in VALUES:
                    for each_dict in values_dictionary[letter]:
                        if each_dict.get(row_num) == col_num:
                            found = True
        if found:
            get_computer_choice()
        else:
            values_dictionary["O"].append({row_num: col_num})
            return True
    return False


def get_user_choice():
    if len(values_dictionary["X"] + values_dictionary["O"]) < 9:
        row_num = int(input("Enter the row number you want to put your 'X':"))
        col_num = int(input("Enter the column number you want to put your 'X':"))
        found = False
        if 3 >= row_num >= 1 and 3 >= col_num >= 1:
            for row in range(1, 4):
                for col in range(1, 4):
                    for letter in VALUES:
                        for each_dict in values_dictionary[letter]:
                            if each_dict.get(row_num) == col_num:
                                found = True
            if found:
                get_user_choice()
            else:
                values_dictionary["X"].append({row_num: col_num})
            return True
        else:
            print("\nPlease Inter the column and the row number in range!!!\n")
            get_user_choice()
    return False


def fill_squares():
    print("\n")
    columns = range(1, 4)
    rows = range(1, 4)
    empty_container = """|     |"""
    dash_container = "   ---------------------"
    flag = False
    print("        1       2      3 ")
    for row in rows:
        print("    " + dash_container)
        print("    ", end="")
        for col in columns:
            for letter in VALUES:
                for each_dict in values_dictionary[letter]:
                    if each_dict.get(row) == col:
                        flag = True
                        value = letter
            if col == 1:
                print(row, end='  ')
            if flag:
                print(f"""|  {value}  |""", end="")
                flag = False
            else:
                print(empty_container, end="")
        print()


def artificial_intelligence():
    diagonal_values = []
    diagonal_values_computer = []
    diagonal_values_complete = [{1: 1}, {2: 2}, {3: 3}]
    diagonal_values_back = []
    diagonal_values_back_computer = []
    diagonal_values_back_complete = [{1: 3}, {2: 2}, {3: 1}]
    for row in range(1, 4):
        consecutive_values = []
        downward_values = []
        consecutive_values_computer = []
        downward_values_computer = []
        consecutive_values_complete = []
        downward_values_complete = []
        for col in range(1, 4):
            temp = {row: col}
            temp1 = {col: row}
            consecutive_values_complete.append(temp)
            downward_values_complete.append(temp1)
            for letter in VALUES:
                for each_dict in values_dictionary[letter]:
                    if letter == "X":
                        if each_dict.items() == temp.items():
                            consecutive_values.append(each_dict)
                        if each_dict.items() == temp1.items():
                            downward_values.append(each_dict)
                        if row == col:
                            if temp.items() == each_dict.items():
                                diagonal_values.append(temp)
                        for temp_dict in diagonal_values_back_complete:
                            if each_dict.items() == temp_dict.items() and temp_dict not in diagonal_values_back:
                                diagonal_values_back.append(temp_dict)
                    else:
                        if each_dict.items() == temp.items():
                            consecutive_values_computer.append(each_dict)
                        if each_dict.items() == temp1.items():
                            downward_values_computer.append(each_dict)
                        if row == col:
                            if temp.items() == each_dict.items():
                                diagonal_values_computer.append(temp)
                        for temp_dict in diagonal_values_back_complete:
                            if each_dict.items() == temp_dict.items() and temp_dict not in diagonal_values_back_computer:
                                diagonal_values_back_computer.append(each_dict)

        if len(consecutive_values) == 2 and len(consecutive_values_computer) == 0:
            for _ in range(len(consecutive_values_complete)):
                if consecutive_values_complete[_] not in consecutive_values:
                    must_fill_dict = consecutive_values_complete[_]
                    values_dictionary["O"].append(must_fill_dict)
                    return True
        elif len(downward_values) == 2 and len(downward_values_computer) == 0:
            for _ in range(len(downward_values_complete)):
                if downward_values_complete[_] not in downward_values:
                    must_fill_dict = downward_values_complete[_]
                    values_dictionary["O"].append(must_fill_dict)
                    return True

        elif len(diagonal_values) == 2 and len(diagonal_values_computer) == 0:
            for _ in range(len(diagonal_values_complete)):
                if diagonal_values_complete[_] not in diagonal_values:
                    must_fill_dict = diagonal_values_complete[_]
                    values_dictionary["O"].append(must_fill_dict)
                    return True

        elif len(diagonal_values_back) == 2 and len(diagonal_values_back_computer) == 0:
            for _ in range(len(diagonal_values_back_complete)):
                if diagonal_values_back_complete[_] not in diagonal_values_back:
                    must_fill_dict = diagonal_values_back_complete[_]
                    values_dictionary["O"].append(must_fill_dict)
                    return True
    return get_computer_choice()


def find_the_winner(value):
    winner = False
    diagonal_values = []
    diagonal_values_back = []
    for row in range(1, 4):
        consecutive_values = []
        downward_values = []
        for col in range(1, 4):
            for each_dict in values_dictionary[value]:
                temp = {row: col}
                temp1 = {col: row}
                if each_dict.items() == temp.items():
                    consecutive_values.append(each_dict.get(row))
                if each_dict.items() == temp1.items():
                    downward_values.append(each_dict.get(col))
                if row == col:
                    if temp.items() == each_dict.items():
                        diagonal_values.append(temp)
                temp3 = [{1: 3}, {2: 2}, {3: 1}]
                for temp_dict in temp3:
                    if each_dict.items() == temp_dict.items() and temp_dict not in diagonal_values_back:
                        diagonal_values_back.append(temp_dict)

        if len(consecutive_values) == 3:
            winner = True
        if len(downward_values) == 3:
            if downward_values[0] == downward_values[1] == downward_values[2]:
                winner = True
        if len(diagonal_values) == 3 or len(diagonal_values_back) == 3:
            winner = True
        if winner:
            if value == "X":
                print("\nYou have Won the game.Congratulations!!!")
            else:
                print("\nYou have Lost The Game. Try Again to Win.")
            return True
    return False


print("\nWELCOME TO THE TIC-TAC-TOE GAME!!!")
print(logo)
values_dictionary = {
    "X": [],
    "O": [],
}
game_is_on = True
draw = False
fill_squares()
while game_is_on:
    if get_user_choice():
        fill_squares()
    else:
        draw = True

    if find_the_winner(value="X"):
        break
    elif draw:
        print("You scored 'DRAW' Please Try Again!")
        game_is_on = False

    if artificial_intelligence():
        print("\nCOMPUTER IS CHOOSING A CELL...")
        time.sleep(.3)
        fill_squares()
    else:
        draw = True

    if find_the_winner(value="O"):
        break
    elif draw:
        print("You scored 'DRAW' Please Try Again!")
        game_is_on = False
