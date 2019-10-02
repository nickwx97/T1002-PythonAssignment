import csv


def schoolstuff(x):


    schEnquiry = x
    schoolDict = {}

    with open('Data/general-information-of-schools.csv','rb') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # schoolDict called to store information of school from csv file with the school name as the key
            schoolDict[row['school_name']] = row

    # schInfoArr is the list of all the information of the requested school retrived from schoolDict with the school name as the key
    schInfoArr = list(v for k, v in schoolDict.items() if schEnquiry in k.lower())[0]


    schoolName = schInfoArr["school_name"].title()
    schoolAdd = schInfoArr["address"]
    schTel = schInfoArr["telephone_no"]
    schEmail = schInfoArr["email_address"]
    schMRT = schInfoArr["mrt_desc"]
    schBus = schInfoArr["bus_desc"]
    schType = schInfoArr["type_code"] + "/" + schInfoArr["nature_code"] + "/" + schInfoArr["session_code"] + "/" + schInfoArr["mainlevel_code"]

    resultstr = "Name of School: " + schoolName + "\n" \
                "Address: " + schoolAdd + "\n" \
                "Contact No: " + schTel + "\n" \
                "Email: " + schEmail + "\n" \
                "Nearby MRTs: " + schMRT + "\n" \
                "Buses: " + schBus + "\n" \
                "School Type: " + schType + "\n" \

    return resultstr
