def bmi():
    weight = float(input("Enter your weight in kg : "))
    height = float(input("Enter your height in m : "))
    print(round(weight / height ** 2,2))
    
def main():
    bmi()
    
main()
                   