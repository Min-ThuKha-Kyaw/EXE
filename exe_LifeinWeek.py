def lifeinWeek():
    age = int(input("Please enter your current age : "))
    print(f"You have {(90-age)* 365} days, {(90-age)* 52} weeks, and {(90-age)* 12} months.") 


def main():
    lifeinWeek()
    
main()