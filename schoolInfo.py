import csv
from readCSV import *


def schoolstuff(x):


    schEnquiry = x

    schoolDictItemsList = genDict(openCSV("Data/general-information-of-schools.csv"))

    schoolDictItemsHeader = schoolDictItemsList[0]
    schoolDictItems = schoolDictItemsList[1]

    for x in schoolDictItems.items():
        for y in schoolDictItemsHeader[1:]:
            x[1][0][y] = x[1][0].get(y).replace('|',',')



    # schoolDictItems is the list of all the information of the requested school retrived from schoolDictItems with the school name as the key
    #schoolDictItemsItems = list(v for k, v in schoolDictItems.items() if schEnquiry in k.lower())



    schoolName = ""

    temp = [i.upper() for i in schoolDictItems.keys()]
    for x in temp:

        if schEnquiry.upper() in x:
            schoolName = x

    schoolDictItems = schoolDictItems[schoolName.title()][0]


    schoolAdd = schoolDictItems["address"]
    schTel = schoolDictItems["telephone_no"]
    schEmail = schoolDictItems["email_address"]
    schMRT = schoolDictItems["mrt station"]
    schBus = schoolDictItems["buses"]
    schType = schoolDictItems["type_code"] + "/" + schoolDictItems["nature_code"] + "/" + schoolDictItems["session_code"] + "/" + schoolDictItems["mainlevel_code"]

    resultstr = "School Name: " + schoolName + "\n\n" \
                "Address: " + schoolAdd + "\n\n" \
                "Contact No: " + schTel + "\n\n" \
                "Email: " + schEmail + "\n\n" \
                "Nearby MRTs: " + schMRT + "\n\n" \
                "Buses: " + schBus + "\n\n" \
                "School Type: " + schType + "\n\n" \

    return resultstr
