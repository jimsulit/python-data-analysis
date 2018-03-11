# Data Analysis using Python (List Comprehension)

## Basic Info
<p> In this exercise, I have manipulated the data in the dataset to find the most common names among male U.S. legislators. </p>

## Functions Used

<ol>
<li> enumerate() - allows us to have two variables in the body of a for loop -- an index and the value </li>
<li> items() - allows us to iterate through keys and values at the same time </li>

## Code Workflow

<ol>
<li> Create an empty dictinary called male_name_counts to store data</li>
<li> Loop through the dataset (legislators.csv) and count how many times each name with "M" in the gender column and a birth year after 1940 occurs, then store the results in the dictionary male_name_counts</li>
<li> Find the highest value in male_name_counts and assign it to highest_male_count </li>
<li> Append any keys from male_name_counts with a value equal to highest_male_count to top_male_names</li>

The dataset includes the following columns:

last_name -- The legislator's last name
first_name -- The legislator's first name
birthday -- the legislator's birthday
gender -- The legislator's gender
type -- The chamber in which the legislator served - either Senate (sen) or House of Representatives (rep)
state -- The state the legislator represents
party -- The legislator's party affiliation
birth_year -- integer values for the year the legislator was born
In this mission, we'll use the data to find the most common names among U.S. legislators of each gender.