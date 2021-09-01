"""
Project: Ethical Automation
Name: Josh Bridges

Functionality:
Has four "analyze_applicant" methods that are used to evaluate a student's grades at 
unique criteria. The code executes all four tests on each applicant in "applicants.csv"
and writes the results in a file named "results.csv". 
"""
import csv

def analyze_applicant1(applicant):
    """
    Given the GPAs of a single applicant, return "ACCEPT" if they are qualified 
    Qualification: An applicant is qualified if...
    −The average of all their grades is above 85

    @param applicant: a list of GPAs(integers)
    @return "ACCEPT" if the applicant qualifies
    """

    av = (int(applicant[0]) + int(applicant[1]) + int(applicant[2]) + int(applicant[3]))/4
    if(av > 85):
        return "ACCEPT"
    else:
        return "REJECT"
    

def analyze_applicant2(applicant):
    """
    Given the GPAs of a single applicant, return "ACCEPT" if they are qualified 
    Qualification: An applicant is qualified if...
    −The lowest grade is above a 65

    @param applicant: a list of GPAs(integers)
    @return "ACCEPT if the applicant qualifies
    """

    low = 100
    for i in applicant:
        if(int(i) < low):
            low = int(i)

    if(low > 65):
        return "ACCEPT"
    else:
        return "REJECT"

def analyze_applicant3(applicant):
    """
    Given the GPAs of a single applicant, return "ACCEPT" if they are qualified 
    Qualification: An applicant is qualified if...
    −Applicant has at least 4 grades above 85

    @param applicant: a list of GPAs(integers)
    @return "ACCEPT if the applicant qualifies
    """
    count = 0
    for i in applicant:
        if(int(i) > 85):
            count += int(1)

    if(count >= 4):
        return "ACCEPT"
    else:
        return "REJECT"

def analyze_applicant4(applicant):
    """
    Given the GPAs of a single applicant, return "ACCEPT" if they are qualified 
    Qualification: An applicant is qualified if...
    −The average of all CS grades(columns 0-4) is above 85

    @param applicant: a list of GPAs(integers)
    @return "ACCEPT if the applicant qualifies
    """

    av = (int(applicant[0]) + int(applicant[1]) + int(applicant[2]) + int(applicant[3])) / 4
    if(av > 85):
        return "ACCEPT"
    else:
        return "REJECT"


with open('applicants.csv', 'r') as gpas:   # Open the applicants file to read in provided data
    with open('results.csv', 'w', newline = '') as results: # Open the results file to write output to

        ar = csv.reader(gpas)       # Create reader for inputs
        rw = csv.writer(results)    # Writer for Output


        # Skip first titles row
        skip = True

        # Iterate over each applicant in csv
        for row in ar:
            if(skip):
                skip = False
            else:
                rw.writerow([analyze_applicant1(row), analyze_applicant2(row), analyze_applicant3(row), analyze_applicant4(row)]) # Write results to the output csv

        
