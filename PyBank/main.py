import os
import csv                  #imports libraries for use in this script

      

totalPL = 0                 #Total Profit/Loss
row_count = 0               #Variable to count rows of data set
total_months = 0            #Adds 1 for every month in data set
last_monthPL = 0            #The profit or loss from the previous month                 
mtm = 0                     #Month to month change in profit/loss
mtm_pool = []               #List to store all the month to month changes
mtm_change = {}             #Dictionary to store month to month changes paired with their respective months
gr_inc = 0                  #Greatest increase
gr_dec = 0                  #Greatest decrease


input_path = os.path.join(r"C:\Users\Ben\python-challenge\PyBank\Resources\budget_data.csv")    #sets my budget csv as input_path, for reading the csv
output_path = os.path.join(r"C:\Users\Ben\python-challenge\PyBank\Analysis\Analysis.txt")       #sets my output path and file

with open(input_path) as csvfile:                                                               #opens my csv

    csvreader = csv.reader(csvfile, delimiter=',')                                              #reads my csv

    
    #The following is done outside of the loop, as to only be done once
    
    header = next(csvreader)                                                                    #skips header row of budget_data
    firstline = next(csvreader)                                                                 #saves the first line 
    last_monthPL = int(firstline[1])                                                            #saves the Jan-2010 value as the first last_month to be used in the loop
    totalPL = int(firstline[1])                                                                 #starts the running total with the first profit/loss in the data





    
    for row in csvreader:                                                                       #loop to look through each row
            
        #Sets the current Profit/Loss amount to the value in the row
        currentPL = int(row[1])
            
        #Adds the current Profit/Loss to the total
        totalPL = currentPL + totalPL
            

        #Calculates the change in profit/loss from the previous month and stores that value into the mtm list as well as
        #storing it into a dictionary paired with its month/year
        mtm = currentPL - last_monthPL
        mtm_pool.append(mtm)
        mtm_change[row[0]] = mtm


        #Sets the current row value as the last months value, so when the loop starts over it has access to the last month
        last_monthPL = int(row[1])

        #increments total months
        total_months = total_months + 1
        


#Calculates the average change in profit or loss from the list of month to month profits/losses.  Uses one less than the total months to account 
#for first month when there is no change.  Also grabs the biggest and smallest values in that list as greatest increase and decrease and
#also finds the min/max in the dictionary, so I can grab the month that corresponds to min and max.  

total_months = total_months + 1
avgPL = round(sum(mtm_pool) / (total_months - 1), 2)
gr_inc = max(mtm_pool)
gr_dec = min(mtm_pool)
gr_inc_m = max(mtm_change, key=mtm_change.get)
gr_dec_m = min(mtm_change, key=mtm_change.get)


#Prints results to terminal

print("\nFinancial Analysis")
print("-------------------------")
print(f"Total Months: {total_months}")
print(f"Grand Total: ${totalPL}")
print(f"Average Change: ${avgPL}")
print(f"Greatest Increase: {gr_inc_m} (${gr_inc})")
print(f"Greatest Decrease: {gr_dec_m} (${gr_dec})")


#Creates an output file at the out put path, writes all info to the file as text

with open(output_path, 'w', newline='') as datafile:

    csvwriter = csv.writer(datafile)

    csvwriter.writerow(["Financial Analysis"])
    csvwriter.writerow(["-------------------------"])
    csvwriter.writerow([f'Total Months: {total_months}'])
    csvwriter.writerow([f'Grand Total: ${totalPL}'])
    csvwriter.writerow([f'Average Change: ${avgPL}'])
    csvwriter.writerow([f'Greatest Increase: {gr_inc_m} (${gr_inc})'])
    csvwriter.writerow([f'Greatest Decrease: {gr_dec_m} (${gr_dec})'])
    csvwriter.writerow(["-------------------------"])








