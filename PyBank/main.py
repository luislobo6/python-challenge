import os
import csv

# Function to iterate to know the number of rows (length)
# def count_iterable(iter):
#     x = 0
#     for i in iter :
#         x += 1
#     return x


# Define the Path of the file to read
file_path = os.path.join("Resources","budget_data.csv")


# Read/Open the file to work with
with open(file_path, "r") as cvs_file:
    csv_reader = csv.reader(cvs_file, delimiter=",")

    # skip the header and save it
    csv_header = next(csv_reader)

    # Save the total of rows of the archive
    # total_rows = count_iterable(csv_reader)
    # print(f"Total rows: {total_rows}")

    # Retrurn to the beginning of the file and skip the header again
    # cvs_file.seek(0)
    # next(csv_reader)

    # Save first row to calculate average change, greatest increase and greatest decrease
    first_row = next(csv_reader)
    total_prof_loss = int(first_row[1])
    great_inc_month = first_row[0]
    great_dec_month = first_row[0]
    great_inc_value = 0
    great_dec_value = 0
    average_changes = 0
    average_previous = int(first_row[1])
    total_rows = 1 #starts in 1 because we read the first row above
    list_changes = []

    #iterate for each row to get the challenges
    for row in csv_reader:

        # Get the total Profit/Losses and total of rows from the file
        total_rows += 1
        actual_value = int(row[1])
        total_prof_loss = total_prof_loss + actual_value

        # Calculate the change -> add it to a list 
        average_changes = actual_value - average_previous
        list_changes.append(average_changes)

        # Search for the greatest increase in profits
        if(average_changes > great_inc_value):
            great_inc_value = average_changes
            great_inc_month = row[0]

        # Search for the greatest decrease in loss
        if(average_changes < great_dec_value):
            great_dec_value = average_changes
            great_dec_month = row[0]

        # Save the actual value as the average_previous for next cycle
        average_previous = actual_value


# Save the information in a variable to print and save it as a TXT file (results.txt)
result = f"""
Financial Analysis
----------------------------
Total Months: {total_rows}
Total: ${total_prof_loss}
Average Change: ${'{:.2f}'.format(sum(list_changes)/len(list_changes))}
Greatest Increase in Profits: {great_inc_month} $({great_inc_value})
Greatest Decrease in Profits: {great_dec_month} $({great_dec_value})
"""

# Create and open TXT file
output_file = "results.txt"
file1 = open(output_file, "w")
file1.write(result) # write the results in the file

print(result) # print to console the results




