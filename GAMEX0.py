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

def first_move(add_something):
    if list[add_something] == "_":
         list[add_something] = X
     else:
        if list[add_something] == O:
            first_move()
        print(" ", "A", " ", "B", " ", "C", " ")
        print("1", list["A1"], "|", list["B1"], "|", list["C1"], " ")
        print("2", list["A2"], "|", list["B2"], "|", list["C2"], " ")
        print("3", list["A3"], "|", list["B3"], "|", list["C3"], " ")
move1 = str(input("Ваш ход .."))
first_move(move1)
