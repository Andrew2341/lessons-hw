from prettytable import PrettyTable


A1 = "_"
A2 = "_"
A3 = "_"
B1 = "_"
B2 = "_"
B3 = "_"
C1 = "_"
C2 = "_"
C3 = "_"
X = "X"
O = "O"
list = {"A1":A1, "B1":B1, "C1":C1, "A2":A2, "B2":B2, "C2":C2, "A3":A3, "B3":B3, "C3":C3}


def board():
    x = PrettyTable()
    x.field_names = [" ", "A", "B", "C"]
    x.add_row(["1", list["A1"], list["B1"], list["C1"]])
    x.add_row(["2", list["A2"], list["B2"], list["C2"]])
    x.add_row(["3", list["A3"], list["B3"], list["C3"]])
    print(x)
def first_move(add_something1):
    while list[add_something1] == "_":
        list[add_something1] = X
    else:
        if list[add_something1] == O:
            add_something2 = str(input("ход неверен, повторите попытку"))
            list[add_something1] = X

def second_move(add_something2):
    while list[add_something2] == "_":
        list[add_something2] = O
    else:
        if list[add_something2] == X:
            add_something2 = str(input("ход неверен, повторите попытку"))
            list[add_something2] = O
def win():
        if list["A1"] == O and list["B1"] == O and list["C1"] == O:
            print('игра окончена, победил Игрок2')
        elif list["A2"] == O and list["B2"] == O and list["C2"] == O:
            print('игра окончена, победил Игрок2')
        elif list["A3"] == O and list["B3"] == O and list["C3"] == O:
            print('игра окончена, победил Игрок2')
        elif list["A1"] == O and list["A2"] == O and list["A3"] == O:
            print('игра окончена, победил Игрок2')
        elif list["B1"] == O and list["B2"] == O and list["B3"] == O:
            print('игра окончена, победил Игрок2')
        elif list["C1"] == O and list["C2"] == O and list["C3"] == O:
            print('игра окончена, победил Игрок2')
        if list["A1"] == X and list["B1"] == X and list["C1"] == X:
            print('игра окончена, победил Игрок1')
        elif list["A2"] == X and list["B2"] == X and list["C2"] == X:
            print('игра окончена, победил Игрок1')
        elif list["A3"] == X and list["B3"] == X and list["C3"] == X:
            print('игра окончена, победил Игрок1')
        elif list["A1"] == X and list["A2"] == X and list["A3"] == X:
            print('игра окончена, победил Игрок1')
        elif list["B1"] == X and list["B2"] == X and list["B3"] == X:
            print('игра окончена, победил Игрок1')
        elif list["C1"] == X and list["C2"] == X and list["C3"] == X:
            print('игра окончена, победил Игрок1')



def main():
    for i in list:
        board()
        add_something1 = str(input("Игрок1, Ваш ход: "))
        first_move(add_something1)
        board()
        add_something2 = str(input("Игрок2, Ваш ход: "))
        second_move(add_something2)
        board()
        win()
main()
