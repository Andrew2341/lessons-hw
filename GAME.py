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



x = PrettyTable()
x.field_names = [" ", "A", "B", "C"]
x.add_row(["1", A1, B1, C1])
x.add_row(["2", A2, B2, C2])
x.add_row(["3", A3, B3, C3])
print(x)
def first_move(add_something1):
    while list[add_something1] == "_":
        list[add_something1] = X
    else:
        if list[add_something1] == O:
            add_something2 = str(input("ход неверен, повторите попытку"))
            list[add_something1] = X
    print(PrettyTable())
def second_move(add_something2):
    while list[add_something2] == "_":
        list[add_something2] = O
    else:
        if list[add_something2] == X:
            add_something2 = str(input("ход неверен, повторите попытку"))
            list[add_something2] = O
    print(x)



def main():
    for i in list:
        add_something1 = str(input("Игрок1, Ваш ход: "))
        first_move(add_something1)
        add_something2 = str(input("Игрок2, Ваш ход: "))
        second_move(add_something2)
    win()
main()
