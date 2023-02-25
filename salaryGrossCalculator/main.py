
#Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.
#Rewrite your pay program using try and except so that your program handles non-numeric input gracefully by printing a message and exiting the program. The following shows two executions of the program:

def salaryGrossCalculator(hours, rates):
    hours = input("How many hours have you worked?")
    rates = input("how much do you earn per hour?")
    try:
        fhours = float(hours)
        frates = float(rates)
    except:
        print("Please, enter numeric input")
        quit()
    if fhours > 40:
        pay = fhours * frates + (fhours - 40) * frates * 0.5
    else:
        pay = fhours * frates
    print("You earn: ", pay)


salaryGrossCalculator()