import csv

schEnquiry = raw_input("Put school name")
schoolDict = {}
schCCAList = []
schoolName = ""

with open('Data/co-curricular-activities-ccas.csv', 'rb') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # schoolDict called to store information of school from csv file with the school name as the key
        schoolDict[row['school_name']] = row
        #print row['cca_generic_name']

        if schEnquiry.upper() in row['school_name']:
            schCCAList.append(row['cca_generic_name'])
            schoolName = row['school_name']

ccaStr = str(schCCAList)[1:-1]


print schoolName + " CCAs are" + ccaStr





# schInfoArr is the list of all the information of the requested school retrived from schoolDict with the school name as the key
#schInfoArr = list(v for k, v in schoolDict.items() if schEnquiry in k.lower())[0]


#print schInfoArr.values()


