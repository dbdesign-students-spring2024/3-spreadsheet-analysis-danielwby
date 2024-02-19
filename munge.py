import csv

# read data
with open('data/DOHMH_Dog_Bite.tsv', 'r') as file:
    reader = csv.reader(file, delimiter='\t')
    data = list(reader)

# Get column names
headers = data[0]

# Remove duplicate rows
unique_data = []
for row in data[1:]:
    if row not in unique_data:
        unique_data.append(row)

# Handle missing values and data transformations
for row in unique_data:
    # fill in missing age values
    if row[4] == '':
        row[4] = 'Unknown'

    # handle gender abbreviations
    if row[5] == 'U':
        row[5] = 'Unknown'
    elif row[5] == 'M':
        row[5] = 'Male'
    elif row[5] == 'F':
        row[5] = 'Female'

    # Fill in the missing zip codes
    if row[8] == '':
        row[8] = 'Unknown'

# Write the cleaned data to a new file
with open('data/clean_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(headers)
    writer.writerows(unique_data)
