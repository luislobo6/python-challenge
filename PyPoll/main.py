import os
import csv

# Define the Path of the file to read
file_path = os.path.join("Resources","budget_data.csv")

total_prof_loss = 0

# Read/Open the file to work with
with open(file_path, "r") as cvs_file:
    csv_reader = csv.reader(cvs_file, delimiter=",")
    
    print(csv_reader.line_num)

    # skip the header and save it
    csv_header = next(csv_reader)

    #iterate for each row
    for row in csv_reader:
        total_prof_loss = total_prof_loss + float(row[1])


print(f"Total Profit/Loss: {total_prof_loss}")