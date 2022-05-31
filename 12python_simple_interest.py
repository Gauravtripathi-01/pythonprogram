principal_amount=eval(input("Enter the principal amount : "))
rate_of_interest=eval(input("Enter the rate of interest : "))
time_given=eval(input("Enter the time in minutes : "))
simple_interest=principal_amount*rate_of_interest*time_given
print("The simple interest is = ",simple_interest)
total_amount= principal_amount+simple_interest
print("The Total amount = ",total_amount