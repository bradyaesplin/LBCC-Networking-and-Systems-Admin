while True:
    cont = input("Another one? yes/no > ")
    while cont.lower() not in ("yes", "no"):
        cont = input("Another one? yes/no> ")
        if cont == "no":
            break
