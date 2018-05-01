# Data Analysis using Jupyter Notebook

## Basic Info
<p> In this guided project, we explored data analysis in the Jupyter environment. Jupyter is a widely used data science environment that combines a rich text editor with a console. The Jupyter project was originally called IPython, and focused on supporting just the Python language. Over time, support for other languages like R and Julia were added and the project was renamed to Jupyter.

Jupyter notebook is built around a typical data analysis workflow and it's very different from a standard integrated development environment, such as Pycharm, which focuses more on just working with code. In Jupyter, you work with notebooks, which mix plain text, code, and code outputs in one view. </p>

## Functions Used

<ol>
<li> read()</li>
<li> split()</li>
<li> dict()</li>
</ol>

## Code Workflow

* Read the csv file
* Split the raw data using the new-line delimiter as separator  
* Create an empty dictionary
* Select all but the header row and assign to a new list object
* Iterate through this new list 
  * Split each line on the comma delimiter
  * Extract the day_of_week value and the births value for each line
  * If the day_of_week value already exists as a key in the dictionary, add the births value to the existing, associated value
  * If the day_of_week value doesn't exist as a key, add it to the dictionary and set the associated value to the births value for that line
* Outside the loop, we display the dictionary to get total number of births

The dataset includes the following columns:

<li>year -- Year</li>
<li>month -- Month</li>
<li>date of month -- Day number of the month</li>
<li>day of week -- Day of week, where 1 is Monday and 7 is Sunday</li>
<li>births -- Number of births</li>
</ul>

