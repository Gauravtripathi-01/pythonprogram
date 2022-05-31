principal_amount=eval(input("Enter thr principal amount : "))
rate_of_interest=eval(input("Enter the rate of interest : "))
number_of_times_per_time_period=eval(input("Enter the number of times : "))
time_given = eval(input("Enter thr time in minutes : "))
final_amount=principal_amount*((1+(rate_of_interest/number_of_times_per_time_period))**number_of_times_per_time_period*time_given)
compound_interest=principal_amount-final_amount
print(round(compound_interest,2))