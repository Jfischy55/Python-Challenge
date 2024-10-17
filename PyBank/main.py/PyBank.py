# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0
# Add more variables to track other necessary financial data
previous_net = 0
month_of_change = []
net_change_list = []
greatest_net_increase = ["", 0]
greatest_net_decrease = ["", 9999999999999999999]

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list


    # Track the total and net change


    # Process each row of data
    for row in reader:

        # Track the total
        total_months += 1
        total_net = total_net + int(row["Net Profit"])

        # Track the net change
        net_change = int(row["Net Profit"]) - previous_net
        # Calculating the revenue change
        previous_net - int(row["Net Profit"])
        # Updating previous revenue
        net_change_list = net_change_list + [net_change]
        # Appending revenue change to revenue change list at the end of the list
        month_of_change = month_of_change + [row["Date"]]
        # Appending month changing (i.e., tracking the months) at end of list

        # Calculate the greatest increase in profits (month and amount)
        if (net_change > greatest_net_increase[1]):
            greatest_net_increase[0] = row["Date"]
            greatest_net_increase[1] = net_change
            # Changing values of the array based one prior greatest net increase
            # And comparing it to the new net change, and continually updating 

        # Calculate the greatest decrease in losses (month and amount)
        if (net_change < greatest_net_decrease[1]):
            greatest_net_decrease[0] = row["Date"]
            greatest_net_decrease[1] = net_change
            # Doing the same for decrease as done previously for increase


# Calculate the average net change across the months
net_avg = sum(net_change_list) / len(net_change_list)

# Generate the output summary
output_summary = (
    f"Financial Analysis"
    f"----------------------------"
    f"Total Months: {total_months}"
    f"Total: ${total_net}"
    f"Average Change: ${net_avg}"
    f"Greatest Increase in Profits: {greatest_net_increase[0]} (${greatest_net_increase[1]})"
    f"Greatest Decrease in Profits: {greatest_net_decrease[0]} (${greatest_net_decrease[1]})"
)

# Print the output
print(output_summary)

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output_summary)
