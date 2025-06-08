name = str(input("What's your name?"))

match name:
    case "Peter" | "Parker" | "John":
        print("English")
    case "Ahmed" | "Mohamed":
        print("Arabic")
    case _:
        print("Who?")