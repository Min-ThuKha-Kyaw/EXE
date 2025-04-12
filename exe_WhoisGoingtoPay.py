import random

def whoisgoingtopay():
    names_string = input("Give me everybody's name, seperated by a comma >>>  ")
    names = names_string.split(",")
    result = random.randint(0, len(names)-1)
    print(result)
    whopay = names[result]
    print(f"{whopay} is going to buy for meal today!")

def main():
    whoisgoingtopay()
    
main()