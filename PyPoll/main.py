import os
import csv          #imports libraries for use in this script


vote_total = 0      #Total vote variable
all_votes = []      #List which will be populated with every vote, then used to count


input_path = os.path.join(r"C:\Users\Ben\python-challenge\PyPoll\Resources\election_data.csv")  #sets my election_data csv as input_path, for reading the csv
output_path = os.path.join(r"C:\Users\Ben\python-challenge\PyPoll\Analysis\Analysis.txt")       #sets the output path for the file I will export

with open(input_path) as csvfile:                                                               #opens my csv

    csvreader = csv.reader(csvfile, delimiter=',')                                              #reads my csv

    header = next(csvreader)                                                                    #skips header row of election_data csv

    for row in csvreader:                                                                       #loop to look through each row

        vote_total = vote_total + 1                                                             #Adds 1 for each vote to form a vote total
        all_votes.append(row[2])                                                                #Adds the vote (name of candidate) into a list to be counted


#Counts every instance of a candidates name and saves it as their number of votes

kvote = all_votes.count("Khan")
cvote = all_votes.count("Correy")
lvote = all_votes.count("Li")
ovote = all_votes.count("O'Tooley")


#Calculates the percentage of each candidates individual vote

kPer = round(kvote / vote_total * 100, 3)
cPer = round(cvote / vote_total * 100, 3)
lPer = round(lvote / vote_total * 100, 3)
oPer = round(ovote / vote_total * 100, 3)


#Conditional logic to determine which candidate has the most votes, then stores that candidate's name as 'winnner'

if(kvote > cvote and kvote > lvote and kvote > ovote):
    winner = "Khan"
if(cvote > kvote and cvote > lvote and cvote > ovote):
    winner = "Correy"
if(lvote > cvote and lvote > kvote and lvote > ovote):
    winner = "Li"
if(ovote > cvote and ovote > lvote and ovote > kvote):
    winner = "O'Tooley"



#Outputs text to terminal containing total, each vote count and its percentage of the total, and the winner

print("\nElection Results")
print("-------------------------")
print(f"Total Votes: {vote_total}")
print("-------------------------")
print(f"Khan: {kPer}% ({kvote})")
print(f"Correy: {cPer}% ({cvote})")
print(f"Li: {lPer}% ({lvote})")
print(f"O'Tooley: {oPer}% ({ovote})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")


#Creates an output file at the out put path, writes all info to the file in csv format

with open(output_path, 'w', newline='') as datafile:

    csvwriter = csv.writer(datafile)

    csvwriter.writerow(["Election Results"])
    csvwriter.writerow(["-------------------------"])
    csvwriter.writerow(['Candidate--Vote Percentage--Votes'])
    csvwriter.writerow([f'Khan {kPer}% {kvote}'])
    csvwriter.writerow([f'Correy {cPer}% {cvote}'])
    csvwriter.writerow([f'Li {lPer}% {lvote}'])
    csvwriter.writerow([f"O'Tooley {oPer}% {ovote}"])
    csvwriter.writerow(["-------------------------"])
    csvwriter.writerow([f"Winner: {winner}"])
    csvwriter.writerow(["-------------------------"])
