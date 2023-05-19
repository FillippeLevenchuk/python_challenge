# Importing the os module
import os
# Module for reading CSV files
import csv

#Create a path
csvpath = os.path.join("Resources", "budget_data.csv")

with open (csvpath) as csvfile:
    csvreader =csv.reader(csvfile, delimiter=",")
    #Read the first row
    header = next(csvreader)

    #Prepare Variables
    months = [] #Making a list named "months" for the "date" column
    prof_loss = [] #Making a list for "Profit/Losses" column
    changes = []#Making a list for changes of values in profit/losses column

    previous_profit_loss = 0 #last profit/loss value used in loop
    total_profit_loss = 0 #total amount of profit/loss

    for row in csvreader: #Loop to go through rows in csv file
        month= (row[0]) #first row
        profit_loss = int(row[1]) #second row
        months.append(month) #adding a new month found in row to months list
        prof_loss.append(profit_loss) #adding a new profit/loss to our prof_loss list
        total_profit_loss += profit_loss #total is adding all profits and losses

        #if function to calculate changes
        if csvreader.line_num != 2:
            change = profit_loss - previous_profit_loss
            changes.append(change)

        previous_profit_loss = profit_loss
        
#Financial analysis variables
month_count = len(months)
net_total = total_profit_loss
avg_change = sum(changes) / len(changes)
greatest_increase = max(changes)
greatest_increase_index = changes.index(greatest_increase)
greatest_increase_month = months[greatest_increase_index]
greatest_decrease = min (changes)
greatest_decrease_index = changes.index(greatest_decrease)
greatest_decrease_month = months[greatest_decrease_index]
        

#Store the financial analysis
Analysis = f"\
Financial Analysis\n\
-----------------------\n\
Total Months: {month_count}\n\
Total: ${net_total}\n\
Average Change: ${avg_change: .2f}\n\
Greatest Increase in Profits: {greatest_increase_month} ${greatest_increase}\n\
Greatest Decrease in Profits: {greatest_decrease_month} ${greatest_decrease}"

print(Analysis)

#Exporting results
PBOUT = os.path.join("Analysis", "pybank.txt")
with open(PBOUT, "w") as outfile:
    outfile.write(Analysis)
