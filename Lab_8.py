#Nathan Raia

def main():
    temperatures = input("Enter the average daily temperature ")
    temperatures = temperatures.split(" ")
    coolingDegreeDays = 0
    heatingDegreeDays = 0

    for i in temperatures:
        if int(i) > 80 or int(i) < 60:
            if int(i) > 80:
                coolingDegreeDays += int(i) - 80
            else:
                heatingDegreeDays += 60 - int(i)

    print("There are" , coolingDegreeDays , "cooling degree days")
    print("There are" , heatingDegreeDays , "heating degree days")
    
main()