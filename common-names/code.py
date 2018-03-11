top_male_names = []
male_name_counts = {}
for row in legislators:
    if row[3] == "M" and row[7] >1940:
        name = row[1]
        if name in male_name_counts:
            male_name_counts[name] += 1
        else:
            male_name_counts[name] = 1
            
highest_male_count = None
for name, count in male_name_counts.items():
    if highest_male_count is None or count > highest_male_count:
        highest_male_count = count

for name, count in male_name_counts.items():
    if count == highest_male_count:
        top_male_names.append(name)
