def loveCalculator():
    print("Welcome to the Love Calculator!")
    name1 = input("Please enter your name >>>  ")
    name2 = input("Please enter their name >>>  ")
    
    uppercase_name1 = name1.upper()
    uppercase_name2 = name2.upper()
       
    T = uppercase_name1.count("T") + uppercase_name2.count("T")
    R = uppercase_name1.count("R") + uppercase_name2.count("R")
    U = uppercase_name1.count("U") + uppercase_name2.count("U")
    E = uppercase_name1.count("E") + uppercase_name2.count("E")
    true = str(T + R + U + E)
    
    L = uppercase_name1.count("L") + uppercase_name2.count("L")
    O = uppercase_name1.count("O") + uppercase_name2.count("O")
    V = uppercase_name1.count("V") + uppercase_name2.count("V")
    E = uppercase_name1.count("E") + uppercase_name2.count("E")
    love = str(L + O + V + E)
    
    score = int(true + love)
    
    if score < 10 or score > 90 :
        print(f"Your score is {score}, you go together like coke and mentos.")
    elif score >= 40 and score <= 50:
        print(f"Your score is {score}, you are alright together.")
    else:
        print(f"Your score is {score}.")


def main():
    loveCalculator()
    
main()
