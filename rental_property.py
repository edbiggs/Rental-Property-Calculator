

class RentalCalc:
    def __init__(self, income=0, expenses=0, tax=0,cash_flow=0, roi=0):
        self.income = income
        self.expenses = expenses
        self.tax = tax
        self.cash_flow = cash_flow
        self.roi = roi



    def income_calculator(self):
        while True:
            try:
                self.income += int(input("How much will you make on rental income each month?"))
            except:
                print("Please type a valid number rounded to the nearest dollar")
                continue

            other_income_prompt = input("Do you make additional money from any other sources, such as laundry, storage, etc.?(Y/N)").lower()
            if other_income_prompt == "y":
                try:
                    self.income += int(input("How much do you make from other sources?"))
                    print(self.income)
                    break
                except:
                    print("Please type a valid number rounded to the nearest dollar")
                    continue
            elif other_income_prompt == "n":
                print(f"total income: ${self.income}")
                break
            else:
                print("Input not recognized. Please type 'Y' for yes and 'N' for no")
                continue
    
    def expenses_calculator(self):
        while True:
            try:
                self.tax = float(input("How much is property tax?(As a decimal)"))
            except:
                print("Please type a valid number (Decimals only)")
                continue
            try:
                self.expenses += int(input("How much does it cost to insure the property?(Monthly)"))
            except:
                print("Please type a valid number rounded to the nearest dollar")
                continue
            if input("Do you pay for utilites?(Y/N)").lower() == 'y':
                try:
                    self.expenses += int(input("How much do you spend on gas?(Monthly)"))
                except:
                    print("Please type a valid number rounded to the nearest dollar")
                    continue
                try:
                    self.expenses += int(input("How much do you spend on water?(Monthly)"))
                except:
                    print("Please type a valid number rounded to the nearest dollar")
                    continue
                try:                
                    self.expenses += int(input("How much do you spend on electricity?(Monthly)"))
                except:
                    print("Please type a valid number rounded to the nearest dollar")
                    continue
            try:
                self.expenses += int(input("How much are HOA fees?(Monthly)"))
            except:
                print("Please type a valid number rounded to the nearest dollar")
                continue
            try:
                self.expenses += int(input("How much do you expect to spend on repairs?(Yearly)"))/12
            except:
                print("Please type a valid number rounded to the nearest dollar")
                continue
            try:
                self.expenses += int(input("How much do you spend on property management?"))
            except:
                print("Please type a valid number rounded to the nearest dollar")
                continue
            try:
                self.expenses += int(input("How much is the monthly mortgage payment?"))
            except:
                print("Please type a valid number rounded to the nearest dollar")
                continue
            print(f"Total expenses: ${round(self.expenses + (self.tax * self.expenses), 2)}")
            break

            
    def cash_flow_calculator(self):
        self.cash_flow = self.income - self.expenses
        print(f"Total cash flow: ${round(self.cash_flow, 2)}")
        

    def roi_calculator(self):
        while True:
            try:
                self.roi += int(input("How much is the down payment for this property?"))
            except:
                print("Please type a valid number rounded to the nearest dollar")
                continue
            try:
                self.roi += int(input("How much are the closing costs?"))
            except:
                print("Please type a valid number rounded to the nearest dollar")
                continue
            try:
                self.roi += int(input("How much will it cost to repair/renovate the property?"))
            except:
                print("Please type a valid number rounded to the nearest dollar")
                continue
            break

        
        
        self.roi = ((self.cash_flow * 12) / self.roi) * 100

        print(f"The estimated return on investment for this property is {round(self.roi, 2)}%.")



                
            


my_rental = RentalCalc()

def run():
    while True:
        my_rental.income_calculator()
        my_rental.expenses_calculator()
        my_rental.cash_flow_calculator()
        my_rental.roi_calculator()
        if input("Would you like to continue using the rental calculator?(Y/N)").lower() == "y":
            continue
        break
run()


