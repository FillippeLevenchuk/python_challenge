#Imports
import os
import csv
import collections
from collections import Counter

#Create a path
csvpath = os.path.join("Resources", "election_data.csv")

#Open and read csv file
with open (csvpath) as csvfile:
    csvreader =csv.reader(csvfile, delimiter=",")
    #Read the first row
    header = next(csvreader)

    #Variables
    candidates=[] #list with number of times a candidate has been voted for
    candidatenames=[] #list of unique name of candidates
    totalpercandidate={} #dictionary with the name of candidate and the votes
    candidateresults={} #dictionary with the name of candidate and the votes
    results_list=[]#text version of the candidateresults
    

    for row in csvreader: #goes row by row through csv file

        Candidate= row[2] #third column on csv file
        candidates.append(Candidate) #adds to candidate list values in third column
        
        #if function to add unique candidate names into list
        if Candidate not in candidatenames:
            candidatenames.append(Candidate)
        #if fuction to add candidate name to dictionary and the number of votes
        if Candidate not in totalpercandidate:
            totalpercandidate[Candidate] =1
            
        totalpercandidate[Candidate] +=1

votes = totalpercandidate[Candidate] #determining the name for dictionary value
totalvotes= int(len(candidates)) #calculating the total amount of votes 

for candidate, votes in totalpercandidate.items(): #loop through all candidates in dictionary to find percentage
    percentage = (votes / totalvotes)*100 #calculating percentage of votes
    candidateresults[candidate] = (percentage, votes) #creating a new dictionary with the number of votes and their respective percentage

for candidate, (percentage, votes) in candidateresults.items(): #loop throught dictionary to create a text list with values from dictionary
    result = f"{candidate}: {percentage: .3f}% ({votes})"
    results_list.append(result)

result_text = "\n".join(results_list) #formatting results for printing
winner = max(candidateresults, key=lambda x: candidateresults[x][1]) #calculating winner

#print(totalvoters) #test
#print(totalpercandidate) #test
#print(winner) #test
#print(result_text) #test


#Analysis
Analysis = f"Election Results\n\
------------------------\n\
Total Voters: {totalvotes}\n\
------------------------\n\
{result_text}\n\
------------------------\n\
Winner: {winner}\n\
------------------------"

print(Analysis)

#Exporting results
PPOUT = os.path.join("Analysis", "pypoll.txt")
with open(PPOUT, "w") as outfile:
    outfile.write(Analysis)