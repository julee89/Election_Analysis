# Election_Analysis
## Overview
We are assisting a Colorado Board of Elections Employee, Tom, in an election audit of tabular data for the US congressional precinct in Colorado.

This analysis is used to show the user the total number of votes cast for each candidate, percentage of votes per candidate, total number of votes for each county, and the percentage of votes for each county. Then, it will also determine the winner of the election based on popular votes by viewing the candidate with the highest vote percentage. This will also allow the user to view the county with the highest voter turnout during this audit. 

By building out this audit in Python, it will allow them to automate the auditing process for this Colorado precinct.

## Analysis
### Total Votes Cast
When we run the analysis to see how many votes were cast during this we see that there are a total of 369,711 votes cast during this election period as shown here from the analysis output from the python terminal.

[Election Count](Resources/total_votes.PNG)

#### County Analysis
In this precinct there are a total of three counties which include Jefferson, Denver, and Arapahoe county.

Countys
- Jefferson county had 38,855 votes of the 369,711 votes casted making it 10.5% of the vote count percentage

- Denver county had 306,055 votes of the 369,711 votes casted making it 82.8% of the vote count percentage

- Arapahoe county had 24,801 votes of the 369,711 votes casted making it 6.7% of the vote count percentage

We can see this same breakdown in the output produced in the terminal.

[County Votes](Resources/county_votes.PNG)

A final analysis of the county level data shows us that Denver had the highest voter count during this election period.

#### Candidate Analysis
In this precinct there are a total of three candidate which include Charles Casper Stockholm, Diana DeGette, and Raymon Anthony Doane.

Candidates
- Raymon Anthony Doane had 85,213 votes of the 369,711 votes casted making which comes to 3.1% of the vote count percentage

- Diana DeGette had 272,892 votes of the 369,711 votes casted making which comes to 73.8% of the vote count percentage

- Charles Casper Stockham had 85.213 votes of the 369,711 votes casted making which comes to 23.0% of the vote count percentage

We can see this same breakdown in the output produced in the terminal.

[Candidate Votes](Resources/candidate_votes.PNG)

A final analysis of the data, shows us the the clear winner of the popular votes is Diana DeGette.

## Summary
By using this script we can easily navigate tabular voter data for other counties, which will make the analysis of data much more efficient and error proof.

Some minor changes to the code can make it more versatile to standardize processes of data for other counties as well. One proposal would be to drill down the popular candidate votes to a county level to understand voting tendencies or trends on a county level. It can be used as preliminary indicator as who will likely be a winning contender during the election period.

Another changee that could be made to only find unique voter ID's for the counts, to prevent counting of duplicative votes in this automated process. This could help with preventing voter fruad or counting vote that have high discripancy.