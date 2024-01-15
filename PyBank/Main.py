import os
import csv

# Define a function in this case export_to_text with 2 arguments
def export_to_text(filename, result_text):
    with open(filename, 'w') as file:
        file.write(result_text)

# Define the path to the CSV file
csv_path = os.path.join('Resources', 'budget_data.csv')

# Initialize variables for financial analysis
total_months = 0
net_total = 0
changes = []
previous_profit_loss = None
greatest_increase = {"date": "", "amount": float("-inf")}
greatest_decrease = {"date": "", "amount": float("inf")}

# Read the CSV file and store rows in a list
rows = []
with open(csv_path, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    for row in csvreader:
        rows.append(row)

# Process the rows outside the 'with' block
for row in rows:
    # Extract date and profit/loss
    date = row[0]
    profit_loss = int(row[1])

    # Update total months and net total
    total_months += 1
    net_total += profit_loss

    # Use multiple if statement to ensure all 3 conditions are met
    # Calculate change and update changes list
    if previous_profit_loss is not None:
        change = profit_loss - previous_profit_loss
        changes.append(change)

        # Update greatest increase and decrease
        if change > greatest_increase["amount"]:
            greatest_increase["date"] = date
            greatest_increase["amount"] = change

        if change < greatest_decrease["amount"]:
            greatest_decrease["date"] = date
            greatest_decrease["amount"] = change

    # Update previous profit/loss for the next iteration
    previous_profit_loss = profit_loss

# Calculate average change
average_change = sum(changes) / len(changes)

# Print the results
result_text = (
    "Financial Analysis\n"
    "----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${net_total}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})\n"
    f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})"
)

print(result_text)

# Export the results to a text file
export_filename = "analysis/financial_analysis.txt"
export_to_text(export_filename, result_text)



