#file = open("homework2.txt", "w")
#file.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus imperdiet venenatis tellus, in lobortis turpis hendrerit vitae. Quisque porta orci sit amet eros venenatis, dignissim sodales augue finibus. Quisque sed finibus sem. Sed a elit odio. Quisque aliquam nisl libero, sit amet scelerisque turpis mattis at. Nunc nec interdum orci. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent purus nibh, placerat sed dolor eget, volutpat porttitor urna. Nulla mattis sapien sapien, vel ornare odio pharetra id. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer ullamcorper massa et nulla elementum, id ornare turpis porttitor. Nam gravida tempor nibh, vitae tempor felis ultricies pharetra. Integer dictum vestibulum convallis. Donec quis metus a arcu elementum tempor. Quisque rutrum at tortor nec congue. Nulla faucibus aliquam ligula, id rhoncus lorem. Nam eros est, interdum eu purus id, laoreet maximus risus. Suspendisse eu mollis ex. Ut dictum quis eros nec sollicitudin. Nunc dolor mi, porttitor nec mi id, molestie viverra ante. Praesent eleifend, nibh sit amet sodales rutrum, urna justo dictum velit, sed lobortis ligula mauris pretium nisi. Pellentesque sit amet ligula sed dolor egestas consectetur. Sed viverra dolor eu nulla sollicitudin facilisis. Praesent vulputate nibh varius felis mollis tempus. Nam posuere dignissim ligula, hendrerit commodo metus. Nulla in hendrerit lorem. Aliquam erat volutpat. Integer ac ante vel ipsum hendrerit luctus. Mauris luctus iaculis nunc, vitae pulvinar ante iaculis et. Duis dolor erat, vehicula vitae maximus at, ullamcorper nec orci. Aenean sed quam ante. Ut sed sollicitudin metus. Phasellus diam elit, malesuada quis viverra a, facilisis sit amet massa. Nullam interdum, sem eget volutpat placerat, quam urna tempor enim, vitae tempus mauris urna quis risus. Morbi arcu ante, sodales eget tortor vitae, finibus finibus quam. Aenean varius a neque bibendum eleifend. Ut blandit non ante in efficitur. Phasellus sed iaculis nisl. In et viverra nibh. Nunc et scelerisque mi. Integer sagittis condimentum malesuada. Nunc est ipsum, fringilla a imperdiet sed, commodo a ligula. Maecenas commodo justo id nisi posuere porta. Fusce convallis, sem ut aliquam faucibus, lacus arcu consequat tortor, ac imperdiet erat sem in erat. Quisque dolor mi, varius sed fringilla eget, egestas nec mi. Nulla vitae ante eget eros ultrices ultrices. Nunc in hendrerit magna. Morbi commodo volutpat eros quis commodo. Pellentesque tempor rutrum massa, a gravida arcu ullamcorper ac. Praesent in velit rutrum, pellentesque quam ac, blandit purus. Ut vestibulum orci ac eros euismod, nec faucibus purus convallis. Ut ornare eros eros, in pharetra ex placerat nec. Sed dictum est neque, at vestibulum purus elementum consectetur. Nunc non vestibulum sem. Ut a libero ut lacus ornare mattis. Nulla auctor tincidunt blandit. Donec tempor hendrerit leo, ut semper urna volutpat in. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. ")
#def new_operations_with_functions():


def number_of_words(file_name):
    file = open(file_name,"r")
    a = file.read()
    spaces = a.split(" ")
    return len(spaces)

def number_of_marks(file_name):
    file = open(file_name,"r")
    reading_file = file.read()
    find_1 = reading_file.count(".")
    find_2 = reading_file.count(",")
    return (find_1 + find_2)

def replacing(file_name):
    file = open(file_name,"r")
    new_file = open("new_file.txt","w")
    a = file.read().replace(" ","_").replace(",_",";_")
    new_file.write(a)
    new_file.close()
    new_file = open("new_file.txt","r")
    return new_file.read()

def main():
    file_name = str(input("Введите название файла: "))
    a = print("Что вы хотите выбрать\n","1 - Посчитать количество слов\n", "2 - Посчитать количество знако препинаний\n", "3 - Заменить ' ' на '_' и ',_' на ';_'")
    b = str(input("Ваш вариант: "))
    if b == "1":
        print(number_of_words(file_name))
    elif b == "2":
        print(number_of_marks(file_name))
    else:
        print(replacing(file_name))

main()
