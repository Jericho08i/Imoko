def echo():
    ONE = int(input("1st no.: "))
    TWO = int(input("2nd no.: "))
    THREE = int(input("3rd no.: "))
    FOUR = int(input("4th no.: "))
    FIVE = int(input("5th no.: "))
    SIX = int(input("6th no.: "))
    SEVEN = int(input("7th no.: "))
    EIGHT = int(input("8th no.: "))
    NINE = int(input("9th no.: "))
    TEN = int(input("10th no.: "))
    for a in range(ONE):
        for b in range(TWO):
            for c in range(THREE):
                for d in range(FOUR):
                    for e in range(FIVE):
                        for f in range(SIX):
                            for g in range(SEVEN):
                                for h in range(EIGHT):
                                    for i in range(NINE):
                                       for j in range(TEN):
                                           print(f"a={a}, b={b}, c={c}, d={d}, e={e}, f={f}, g={g}, h={i},j={j}")
                                           
                                           



usernamemo = input("Ibagam so ngaran mo:")
passwordmoey = input("ibagam so password mo:")
username = "echo"
password =  "logyy"

while True:
    if usernamemo == username and passwordmoey == password:
        print("Maong")
        echo()
    else:
        print("iiyak ako")
        break                                
                                       
              