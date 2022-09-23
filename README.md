# Election_Analysis

# PyPoll Challenge - Election Results
Tyrone Fraley 
UC Berkley Extension 
September 7, 2022 

## Overview of Election Audit

In this analysis I was tasked to assist Tom - a member of the Colorado board of elections by with providing data based on the results of the U.S. congressional precint in Colorado. My main role within this project was to report the total number of casted votes, amount of votes per candidate, percentage of the votes for each candidate, and present the winner of the election based on highest vote count. To complete this analysis Tom and I will amalgamate the data based on mail-in ballots, direct recording electric (DRE), counting machines, and punch cards. All of which was then placed in a csv file and uploaded into Python for organization and analysis purposes.

### Purpose

The main driver in this project is to collect and analyze the election results for Denver, Jefferson, and Arapahoe county of Colorado. The three running candidates are Charles Casper Stockham, Diana DeGette, and Raymon Anthony Doane. Now that the analysis has been complete the Python script produced in this analysis will assist the Colorado board of elections in the future elections. Such automation through Python could be useful to the Colorade board of elections for possibly many years to come. 

##Resources
- Sept 7, 2022: election_results.csv
- Software: Python 3.9.12, Visual Studio Code, 1.70.1 (Universal)

##Election-Audit Results
The analysis of the election showed that:
- There were 369,711 votes cast in the election.
    -Jefferson County received 10.5% of the votes and 38,855 number of votes.
    -Denver County received 82.8% of the votes and 306,055 number of votes.
    -Arapahoe County received 6.7% of the votes and 24,801 number of votes.
-County with largest votes: Denver County (306,055 votes)
- The candidates were:
    - Charles Casper Stockham
    - Diana DeGette
    - Raymon Anthony Doane
- The candidate results were:
    - Charles Casper Stockham received 23% of the vote and 85,213 number of votes.
    - Diana DeGette received 73.8% of the vote and 272,862 number of votes.
    - Raymon Anthony Doane received 3.1% of the vote and 11.606 number of votes.
- The winner of the eleciton was:
    - Diana DeGette, who received 73.8% of the vote and 272,862 number of votes
    
## Election-Audit Summary

Overall the Python script was successful in collecting data from the election analysis csv file and then analyzing that data. Counties, candidates, vote counts, and percentages were able to be categorized and viewed through the use of Python. Knowing the success of the script the county can now tie the script into other elections or voting analysis. Two of which could be for 



## Election-Audit Summary 
In a summary statement, provide a business proposal to the election commission on how this script can be used—with some modifications—for any election. Give at least two examples of how this script can be modified to be used for other elections. Two different elections that could be analyzed in this data could be on a city level, such as an election for city mayor or for votes for state laws. On a city level the script could be adjusted by changing "county" to >city< (ie. city_votes = {}). For laws you would simply adjust >candidate< to laws (ie. law_options).
