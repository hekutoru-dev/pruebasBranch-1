import os
import csv

# Path to collect data from the Resources folder
file = os.path.join('.', 'budget2.csv')

# Function Definition
def sum_av(numbers):
    lenght = len(numbers)
    total = 0
    for number in numbers:
        total = total - number
    return round(total / lenght, 2)

with open(file, 'r') as csvfile:
    
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Skip header for calculations
    header = next(csvreader)
    
    # Initialization of variables
    count = 0
    total = 0
    Max_Month = ' '
    Max_Amount = 0
    Min_Month = ' '
    Min_Amount = 0    
    f_row = True
    chg_list = []
    prev_v = 0

    
    # Review all the calculations
    for row in csvreader:
    
        # Total months
        count = count + 1

        # Total amount
        total = total + int(row[2])
        
        # Validation of Max and Min
        if(Max_Amount < int(row[2])):
            Max_Amount = int(row[2])
            Max_Month = row[1]
        if(Min_Amount > int(row[2])):
            Min_Amount = int(row[2])
            Min_Month = row[1]
        if(f_row):
            f_row = False
        else:
            chg_list.append(prev_v - int(row[2]))

        prev_v = int(row[2])
    
    sum_ave = 0
    sum_ave = sum_av(chg_list)

        # Print results
    lines = "Financial Analysis\r\n"    
    lines += "----------------------------\r\n"
    lines += f"Total Months: {count}\r\n"
    lines += f"Total: ${total}\r\n"
    lines += f"Average  Change: {sum_ave}\r\n"
    lines += f"Greatest Increase in Profits: {Max_Month} ${Max_Amount}\r\n"
    lines += f"reatest Decrease in Profits: {Min_Month} ${Min_Amount}\r\n"
    
    print(lines)

    # Specify the file to write to
output_path = os.path.join(".", "Bank.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as text_file:
    text_file.write(lines)    