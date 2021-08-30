"""
Project: Ethical Automation
Name: Josh Bridges

Functionality:

"""
import csv

def analyze_applicant1(applicant):

    """
    Given the GPAs of a single applicant, return True if they are qualified 
    Qualification: Anapplicant is qualified if...
    −The average of all their grades is above 85

    @param applicant: a list of GPAs(int ege rs)
    @return True if the applicant qualifies
    """

    av = (applicant[0] + applicant[1] + applicant[2] + applicant[3])/4
    if(av > 85):
        return True
    else:
        return False
    

def analyze_applicant2(applicant):
    low = 100
    for i in appplicant:
        if(i < low):
            low = i

    if(low < 65):
        return True
    else:
        return False

def analyze_applicant3(applicant):
    count = 0
    for i in applicant:
        if(i > 85):
            count += 1

    if(count >= 4):
        return True
    else:
        return False

def analyze_applicant4(applicant):
    return True


with open('applicants.csv') as gpas:
    with open('results.csv', 'w') as results:

        ar = csv.reader(gpas)
        rw = csv.writer(results)

        rw.writerow(["Analysis #1, Analysis #2, Analysis #3, Analysis #4"])

        skip = True
        for row in ar:
            if(skip):
                print(row)
                skip = False
            else:
                rw.writerow([analyze_applicant1(row), analyze_applicant2(row), analyze_applicant3(row), analyze_applicant4(row)])
