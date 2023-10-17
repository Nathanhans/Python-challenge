#### Nathan Hanns
#### Python challenge

#PyBank

#Import the os module to create file paths

import os

# Module for reading CSV files
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')


# # Method 1: Plain Reading of CSV files
# with open(csvpath, 'r') as file_handler:
#     lines = file_handler.read()
#     print(lines)
#     print(type(lines))


# Read csv file and calculate necessary information from file

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    #print(csvreader)

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    Total_months = 0
    Total = 0
    Max_increase = 0
    Max_decrease = 0
    Max_increase_month = 0
    Max_decrease_month = 0
    Average_change = 0
    # Read each row of data after the header
    for row in csvreader:
        print(row)
        #increment months
        Total_months = Total_months+1
        #add to total
        Total = Total + int(row[1])
        #conditional to determine min and max
        if int(row[1]) < Max_decrease:
            Max_decrease = int(row[1])
            Max_decrease_month = (row[0])
        else:
            Max_decrease = Max_decrease
        #conditional to determine min and max
        if int(row[1]) > Max_increase:
            Max_increase = int(row[1])
            Max_increase_month = (row[0])
        else:
            Max_increase = Max_increase    
    Average_change = Total/Total_months
    
    print(f"Financial Analysis \n---------------------")
    print(f"Total Months: {Total_months}")
    print(f"Total: ${Total}")
    print(f"Average Change: ${Average_change}")
    print(f"Greatest Increase in Profits: {Max_increase_month} (${Max_increase})")
    print(f"Greatest Decrease in Profits: {Max_decrease_month} (${Max_decrease})")
          
# Specify the file to write to
output_path = os.path.join('output', 'new.csv')     

          
     # Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the first row (column headers)
    csvwriter.writerow(['Total Months', 'Total Amount', 'Average Change','Greatest Increase Month'
                        ,'Greatest Increase','Greatest Decrease Month','Greatest Decrease'])

    # Write the second row
    csvwriter.writerow([Total_months,Total,Average_change, Max_increase_month, Max_increase,Max_decrease_month,Max_decrease])     
          
          