#Expence Tracker Project

expences = [] # list of expences in form of dictionaries
print("welcome to Expence Tracker : Kahrcha km kr mittar")


while True:
     print("=====MENU=====")
     print("1. Add Expence")
     print("2. View all Expences")
     print("3. View all Kharcha")
     print("4. Exit")

     choice = int(input("Please Enter Your Choice : "))
#add expence
     if(choice == 1):
          date = input("Enter the date of spending in DD-MM formate :")
          category = input("Enter the type of catgories of spending(Food, Travel, Backup, Trip) :")
          description = input("Any other details: ")
          amount = float(input("Enter the amount of sepnding: "))

          expence = {
               "date": date,
               "categories":category,
               "description":description,
               "amount": amount
          }

          expences.append(expence)
          print("\nDone Bro Expences is added sucesfully")

    #View all Expences
     if(choice == 2):
        if(len(expences))==0:
            print("No expenses is added. go back and add expense")
        else:
          print("=== this is your Total expense")
          count =1
          for eachexpence in expences:
               print(f"Expence Number {count} -> {eachexpence["date"]}, {eachexpence["categories"]}, {eachexpence["amount"]}")
               count = count+1

     #View all spending
     if(choice == 3):
          total = 0
          for eachexpence in expences:
             total = total + eachexpence["amount"]
          print("\n Total Spending = ",total)

#4 Exit
     elif(choice == 4):
         print("Thanks For Using our system")
         break

     else:
         print("Invalid Choice. Try Again")


