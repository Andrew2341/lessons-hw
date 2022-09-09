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
print(" ", "A", " ", "B", " ", "C", " ")
print("1", A1, "|", B1, "|", C1, " ")
print("2", A2, "|", B2, "|", C2, " ")
print("3", A3, "|", B3, "|", C3, " ")

list = {"A1":A1, "B1":B1, "C1":C1, "A2":A2, "B2":B2, "C2":C2, "A3":A3, "B3":B3, "C3":C3}

def first_move(add_something1):
    while list[add_something1] == "_":
        list[add_something1] = X
    else:
        if list[add_something1] == O:
            add_something2 = str(input("ход неверен, повторите попытку"))
            list[add_something1] = X
    print(" ", "A", " ", "B", " ", "C", " ")
    print("1", list["A1"], "|", list["B1"], "|", list["C1"], " ")
    print("2", list["A2"], "|", list["B2"], "|", list["C2"], " ")
    print("3", list["A3"], "|", list["B3"], "|", list["C3"], " ")
def second_move(add_something2):
    while list[add_something2] == "_":
        list[add_something2] = O
    else:
        if list[add_something2] == X:
            add_something2 = str(input("ход неверен, повторите попытку"))
            list[add_something2] = O
    print(" ", "A", " ", "B", " ", "C", " ")
    print("1", list["A1"], "|", list["B1"], "|", list["C1"], " ")
    print("2", list["A2"], "|", list["B2"], "|", list["C2"], " ")
    print("3", list["A3"], "|", list["B3"], "|", list["C3"], " ")



def main():
    for i in list:
        add_something1 = str(input("Игрок1, Ваш ход: "))
        first_move(add_something1)
        add_something2 = str(input("Игрок2, Ваш ход: "))
        second_move(add_something2)
    win()
main()
