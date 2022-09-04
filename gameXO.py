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

for i in list:
#    b = list.index(str(input()))
    move1 = str(input("Игрок1, введите букву и цифру (в формате B1): "))
    list[move1] = X
    #list.insert(move1,X)
    print(" ", "A", " ", "B", " ", "C", " ")
    print("1", list["A1"], "|", list["B1"], "|", list["C1"], " ")
    print("2", list["A2"], "|", list["B2"], "|", list["C2"], " ")
    print("3", list["A3"], "|", list["B3"], "|", list["C3"], " ")

    move2 = str(input("Игрок2, введите букву и цифру (в формате B1): "))
    list[move2] = O
    #list.insert(move2,O)

    print(" ", "A", " ", "B", " ", "C", " ")
    print("1", list["A1"], "|", list["B1"], "|", list["C1"], " ")
    print("2", list["A2"], "|", list["B2"], "|", list["C2"], " ")
    print("3", list["A3"], "|", list["B3"], "|", list["C3"], " ")
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
