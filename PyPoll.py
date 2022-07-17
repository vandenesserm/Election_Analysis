# Adding dependencies
import csv
import os
from wsgiref import headers

# File to load variable
file_to_load = os.path.join('Resources', 'election_results.csv')

# File to save variable
file_to_save = os.path.join('analysis', 'election_analysis.txt')

#1. Initialize total vote counter
total_votes = 0

#A complete list of candidates who received votes
candidate_options = []

# Empty dict to store votes cast for each candidate
candidate_votes = {}

# Winning candidate
winning_candidate = ""
winning_count = 0
winning_percentage = 0


# Open election results and read file
with open(file_to_load, encoding='UTF-8') as election_data:

    # Read the file obj w/ the reader function
    file_reader = csv.reader(election_data)

    #Print the header row
    headers = next(file_reader)

    #Print each row 
    for row in file_reader:

        #Add to total vote count
        total_votes += 1

        #Print candidate name for each row
        candidate_name = row[2]

        #If the candidate does not match existing candidate
        if candidate_name not in candidate_options:
            #Add candidate name to candidate list
            candidate_options.append(candidate_name)
            #Track votes cast to each candidate
            candidate_votes[candidate_name] = 0 
        candidate_votes[candidate_name] += 1

#Save results to txt file
with open(file_to_save, "w") as txt_file:

    #print to terminal
    election_results = (
        f'\nElection Results\n'
        f'--------------------\n'
        f'Total Votes: {total_votes:,}\n'
        f'----------------------------\n')
    print(election_results, end='')

    #Save final vote count to txt file
    txt_file.write(election_results)

    
    #Percentage of votes each candidate won
    #Iterate through candidate list
    for candidate_name in candidate_votes:
        #Retrieve vote count and calculate percentages
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (f'{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n')

        #Print each candidates_results
        print(candidate_results)
        #Save final vote count to txt file
        txt_file.write(candidate_results)

        #Determine winning vote count and candidate
        if (votes>winning_count) and (vote_percentage>winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name
            
    #Print winning candidate to terminal
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)