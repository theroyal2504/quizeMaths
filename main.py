con = input("can you play with quiz game? = ")
if con.lower() == "yas":
    score = 0
    print("first qustion")
    while True:
        qtn = input("how many days are in  week = ")
        if len(qtn) == 0:
            print("pls enter answer")
        else:
            if qtn == "7":
                print("correct")
                score += 1
                break
            else:
                print("wrongh")
                break
    print(" ")
    print("second qustion")
    while True:
        qtn = input("Sun rise in the ..........")
        if len(qtn) == 0:
            print("pls enter answer")
        else:
            if qtn.lower() == "east":
                print("correct")
                score += 1
                break
            else:
                print("wrongh")
                break
    print(" ")
    print("third qustion")
    while True:
        qtn = input("Name the national animal of india = ")
        if len(qtn) == 0:
            print("pls enter answer")
        else:
            if qtn.lower() == "lion":
                print("correct")
                score += 1
                break
            else:
                print("wrongh")
                break
    print(" ")
    print("fourth qustion")
    while True:
        qtn = input("Name the smallest continent = ")
        if len(qtn) == 0:
            print("pls enter answer")
        else:
            if qtn.lower() == "australia":
                print("correct")
                score += 1
                break
            else:
                print("wrongh")
                break
    print(" ")
    print("five")
    while True:
        qtn = input("The largest planet of our solar system = ")
        if len(qtn) == 0:
            print("pls enter answer")
        else:
            if qtn.lower() == "jupiter":
                print("correct")
                score += 1
                break
            else:
                print("wrongh")
                break
    print(" ")
    print("six")
    while True:
        qtn = input("which is the country with the most people =  ")
        if len(qtn) == 0:
            print("pls enter answer")
        else:
            if qtn.lower() == "china":
                print("correct")
                score += 1
                break
            else:
                print("wrongh")
                break
    print(" ")
    print("seven")
    while True:
        qtn = input("Name of the national game = ")
        if len(qtn) == 0:
            print("pls enter answer")
        else:
            if qtn.lower() == "hockey":
                print("correct")
                score += 1
                break
            else:
                print("wrongh")
                break
    print(" ")
    print("eight")
    while True:
        qtn = input("which cricket team are win 2011 worldcup cricket = ")
        if len(qtn) == 0:
            print("pls enter answer")
        else:
            if qtn.lower() == "india":
                print("correct")
                score += 1
                break
            else:
                print("wrongh")
                break
    print(" ")
    print("nine ")
    while True:
        qtn = input("how many months do you have in a year = ")
        if len(qtn) == 0:
            print("pls enter answer")
        else:
            if qtn == "12":
                print("correct")
                score += 1
                break
            else:
                print("wrongh")
                break
    print(" ")
    print("ten")
    while True :
        qtn = input("which day in holiday a week in india  = ")
        if len(qtn) == 0:
            print("pls enter answer")
        else:
            if qtn.lower() == "sunday":
                print("correct")
                score += 1
                break
            else:
                print("wrongh")
                break
    print("\n <*************  Result  ****************>")
    print("you got " + str(score) + " qustion  given answer correct")
    res = str((score/10) * 100)
    print(res + "%")
    if res >= "80":
        print("first division")
        print("           excellent            ")
    elif res >= "60":
        print("second division")
        print("           good                  ")
    elif res > "40" == "40":
        print("third division")
        print("      Ok  but work your study    ")
    elif res < "40":
        print("faill")
        print("     ja pad bhaiiiiii..........  ")
else:
    print("by")
