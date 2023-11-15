replit link: https://replit.com/join/ruakzoldxz-soniavillanueva


"""
Salary. File name as: Salary - tuition.
Objective. Algorithm to calculate the salary of “n” salespeople.
Each salary is made up of a base salary and a sales commission.
Total Salary = Base salary + sales commission
The sales commission is calculated by taking a percentage of the sales made, according to the following table:
Sales Commission percentage
1. Less than 3,500 7%
2. 3,500 – 7,000 10%
3. Greater than 7000 15%
The algorithm must ask as input: if there is another seller (yes/no response), the name of each seller, the base salary of each one, and the total sales made per seller. 
Tip: use the lower function to validate yes and no
The output must have the seller's name and their total salary
"""
print("What's the salary of the first person?: ")
salary = int(input())

sales_commission = 0

sales = int(input("How many sales has that person made? Give me a percentage: "))
if sales < 3500:
    sales_commission = sales * (7/100)
elif sales >= 3500 and sales <= 7000:
    sales_commission = sales * (10/100)
else:
    sales_commission = sales * (15/100)

sales_people = input("Do you wanna register another salesperson? (yes/no)")
total_sales_people = 0 #counter of attendees
while sales_people == "yes":
  total_sales_people += 1

while sales_people == "no":
  print("okay :D")
