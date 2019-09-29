import csv

try:
    schEnquiry = raw_input("Which school do you want to research on?")
    schoolDict = {}

    with open('general-information-of-schools.csv','rb') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # schoolDict called to store information of school from csv file with the school name as the key
            schoolDict[row['school_name']] = row

    # schInfoArr is the list of all the information of the requested school retrived from schoolDict with the school name as the key
    schInfoArr = schoolDict[schEnquiry.upper()]


except KeyError:
    print("No such school exists!")