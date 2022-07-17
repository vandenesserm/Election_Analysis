# Election_Analysis
## Project Overview
The following data was requested for an election audit by the election commission. Besides the results directly related to each candidate, voter turnout by county, percentage of votes for each county, and the county with the highest turnout were also requested. To fulfill this request, a county list and county_votes dictionary were created. This is the final product as printed on a .txt file:

        Election Results
    -------------------------
    Total Votes: 369,711
    -------------------------

    County Votes:
    Jefferson: 10.5% (10.509560169970598)
    Denver: 82.8% (82.78222719908253)
    Arapahoe: 6.7% (6.708212630946875)

    -------------------------
    Largest County Turnout: Denver
    -------------------------

    Charles Casper Stockham: 23.0% (85,213)
    Diana DeGette: 73.8% (272,892)
    Raymon Anthony Doane: 3.1% (11,606)

    -------------------------
    Winner: Diana DeGette
    Winning Vote Count: 272,892
    Winning Percentage: 73.8%
    -------------------------


## Resources
Data Source: election_results.csv
Tools and Software: Visual Studio Code, Python 3.7.6, Gitbash, and Github.

## Election Results
- How many votes were cast in this congressional election?
    A total of 369,711 votes were cast in the election. The result was calculated using the total_votes and election_results variables and a for loop iterating through the rows. The final result was printed to the terminal using the following code:

        election_results = (
            f"\nElection Results\n"
            f"-------------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"-------------------------\n\n"
            f"County Votes:\n")
        print(election_results, end="")
        txt_file.write(election_results)

    These are the final results as printed in the election_results.txt file:

        Election Results
        -------------------------
        Total Votes: 369,711
        -------------------------

- Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct:

        County Votes:
        Jefferson: 10.5% (10.509560169970598)
        Denver: 82.8% (82.78222719908253)
        Arapahoe: 6.7% (6.708212630946875)

- Which county had the largest number of votes?

    The county with the largest turnout was Denver.

        -------------------------
        Largest County Turnout: Denver
        -------------------------

- Provide a breakdown of the number of votes and the percentage of the total votes each candidate received:

        Charles Casper Stockham: 23.0% (85,213)
        Diana DeGette: 73.8% (272,892)
        Raymon Anthony Doane: 3.1% (11,606)

 - Which candidate won the election, what was their vote count, and what was their percentage of the total votes?
    Diana DeGetter was the winner candidate with 272,892 votes, which is equivalent to 73.8% of the total votes cast.
    
        -------------------------
        Winner: Diana DeGette
        Winning Vote Count: 272,892
        Winning Percentage: 73.8%
        -------------------------

## Summary

As seen from the results presented, this script has the potential to provide up-to-date, accurate, electoral information, within seconds. This is of the utmost importance when trying to give voters updates on election night. This script can help the election commission and news outlets complete this task. With minor updates, this scrip could handle not only congressional races for other localities but also district races.
