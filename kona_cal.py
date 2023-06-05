def main():
    print(" This is a monthly payment loan calculator ")
    print("")

    principal = float(input("Write down the loan ammount:        "))
    apr = float(input("Write down the annual interest rate:      "))
    years = int(input("Write down th e amount of years:          "))



    monthly_interest_rate = apr / 1200
    amount_of_months = years * 12
    monthly_payment = principal * monthly_interest_rate / (1-(1+monthly_interest_rate) ** (-amount_of_months))


    print(" The monthly pament if this loan is: " + monthly_payment)

main()    