top_male_names = []
# create a dictionary to store count of male names
male_name_counts = {}
# loop through the dataset, legislators.csv, and count how many times names with "M" in gender column and birth year after 1940 occurs; store result in male_name_counts
for row in legislators:
    if row[3] == "M" and row[7] >1940:
        name = row[1]
        if name in male_name_counts:
            male_name_counts[name] += 1
        else:
            male_name_counts[name] = 1

# find highest value in male_name_counts             
highest_male_count = None
for name, count in male_name_counts.items():
    if highest_male_count is None or count > highest_male_count:
        highest_male_count = count

# append any keys from male_name_counts with a value equal to highest_male_count to top_male_names
for name, count in male_name_counts.items():
    if count == highest_male_count:
        top_male_names.append(name)
