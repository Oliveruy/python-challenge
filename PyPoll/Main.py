import os
import csv

def export_to_text(filename, result_text):
    with open(filename, 'w') as file:
        file.write(result_text)

# Define the path to the CSV file
csv_path = os.path.join('Resources', 'election_data.csv')

# Initialize variables for election analysis
total_votes = 0
candidates = {}
winner = {"name": "", "votes": 0}

# Read the CSV file and analyze votes
with open(csv_path, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    for row in csvreader:
        total_votes += 1
        candidate_name = row[2]

        # Update candidate's vote count
        if candidate_name not in candidates:
            candidates[candidate_name] = 1
        else:
            candidates[candidate_name] += 1

            # Update winner information
            if candidates[candidate_name] > winner["votes"]:
                winner["name"] = candidate_name
                winner["votes"] = candidates[candidate_name]

# Analysis
result_text = "Election Results\n-------------------------\n"
result_text += f"Total Votes: {total_votes}\n-------------------------\n"

for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    result_text += f"{candidate}: {percentage:.3f}% ({votes})\n"

result_text += f"-------------------------\nWinner: {winner['name']}\n"

print(result_text)

# Export the results to a text file
export_filename = "analysis/election_results.txt"
export_to_text(export_filename, result_text)



