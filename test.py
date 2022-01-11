from numberwords import NumberWord

entry = input("Enter an integer: ")
while entry != "":

    try:
        number = int(entry)
    except:
        print("Enter an integer!")

    nw = NumberWord(number)
    print(nw.word_number)

    entry = input("Enter an integer: ")
