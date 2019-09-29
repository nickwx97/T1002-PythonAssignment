import csv

schEnquiry = raw_input("Which school do you want to research on?")
schoolDict = {}

with open('Data/general-information-of-schools.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # schoolDict called to store information of school from csv file with the school name as the key
        schoolDict[row['school_name']] = row

# schInfoArr is the list of all the information of the requested school with the school name as the key
schInfoArr = list(v for k, v in schoolDict.iteritems() if schEnquiry in k.lower())
# START test result print
for row in schInfoArr:
    print "%50s%40s" % (row['school_name'], row['address'])
# END test result print
