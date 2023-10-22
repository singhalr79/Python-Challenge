import os
import csv

csvpath = os.path.join("Resources","budget_data.csv")

count_months = 0
total_PL = 0
months = []
PL_Change = []
prev_month_PL = 0
curr_month_PL = 0
profit_loss_change = 0


with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first
    csv_header = next(csvreader)
    

    # Read each row of data after the header
    for row in csvreader:
        count_months = count_months + 1
        total_PL = total_PL + int(row[1])
        curr_month_PL = int(row[1])

        if (count_months == 1):
            # Assign value of current month to the previous month
            prev_month_PL = curr_month_PL
            continue

        else:

            # Change in profit loss 
            profit_loss_change = curr_month_PL - prev_month_PL
           

            # Append each month to the months[]
            months.append(row[0])

            # Append each profit_loss_change to the PL_Change
            PL_Change.append(profit_loss_change)

            # Assign value of current month to the previous month
            prev_month_PL = curr_month_PL

    #Average of "Profit/Loss" changes over the entire period
    average_PL = round(sum(PL_Change)/(count_months - 1), 2)
    
    # greatest increase in "Profit/Loss" 
    greatest_incr = max(PL_Change)
                         
    # greatest decrease in "Profit/Loss")
    greatest_decr = min(PL_Change)

    # Greatest Increase month
    greatest_incr_month = months[PL_Change.index(greatest_incr)]

    # Greatest Decrease month
    greatest_decr_month = months[PL_Change.index(greatest_decr)]

    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {count_months}")
    print(f"Total: {total_PL}")
    print(f"Average Change: {average_PL}")
    print(f"Greatest Increase in Profits: {greatest_incr_month} (${greatest_incr})")
    print(f"Greatest Decrease in Profits: {greatest_decr_month} (${greatest_decr})")
    
    output_file = os.path.join("Analysis","Analysis.txt")
    with open(output_file, "w") as outfile:
        outfile.write("Financial Analysis\n")
        outfile.write("----------------------------\n")
        outfile.write(f"Total Months:  {count_months}\n")
        outfile.write(f"Total:  ${total_PL}\n")
        outfile.write(f"Average Change:  ${average_PL}\n")
        outfile.write(f"Greatest Increase in Profits:  {greatest_incr_month} (${greatest_incr})\n")
        outfile.write(f"Greatest Decrease in Losses:  {greatest_decr_month} (${greatest_decr})\n")