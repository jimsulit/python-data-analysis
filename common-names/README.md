# Data Analysis using Python (List Comprehension)

## Basic Info
<p> In this exercise, I have manipulated the data in the dataset to find the most common names among male U.S. legislators. </p>

## Functions Used

<ol>
<li> enumerate() - allows us to have two variables in the body of a for loop -- an index and the value </li>
<li> items() - allows us to iterate through keys and values at the same time </li>
</ol>

## Code Workflow

<ol>
<li> Created an empty dictionary called male_name_counts to store data</li>
<li> Looped through the dataset (legislators.csv) and counted how many times each name with "M" in the gender column and a birth year after 1940 occurs, then stored the results in the dictionary male_name_counts</li>
<li> Created code to find the highest value in male_name_counts and assign it to highest_male_count </li>
<li> Appended any keys from male_name_counts with a value equal to highest_male_count to top_male_names</li>
</ol>

<ul>
The dataset includes the following columns:

<li>last_name -- The legislator's last name</li>
<li>first_name -- The legislator's first name</li>
<li>birthday -- the legislator's birthday</li>
<li>gender -- The legislator's gender</li>
<li>type -- The chamber in which the legislator served</li>
<li>state -- The state the legislator represents</li>
<li>party -- The legislator's party affiliation</li>
<li>birth_year -- integer values for the year the legislator was born</li>
</ul>