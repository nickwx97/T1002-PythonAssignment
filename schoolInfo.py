from myCSV import *


def schoolstuff(x):
    schEnquiry = x

    schoolDictItemsList = genDict(openCSV("Data/general-information-of-schools.csv"))

    schoolDictItemsHeader = schoolDictItemsList[0]
    schoolDictItems = schoolDictItemsList[1]

    for x in schoolDictItems.items():
        for y in schoolDictItemsHeader[1:]:
            x[1][0][y] = x[1][0].get(y).replace('|', ',')

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
    schType = schoolDictItems["type_code"] + "/" + schoolDictItems["nature_code"] + "/" + schoolDictItems[
        "session_code"] + "/" + schoolDictItems["mainlevel_code"]
    mission = schoolDictItems["missionstatement_desc"]
    vision = schoolDictItems["visionstatement_desc"]

    resultstr = "School Name: " + schoolName + "\n\nAddress: " + schoolAdd + \
                "\n\nContact No: " + schTel + "\n\nEmail: " + schEmail + \
                "\n\nNearby MRTs: " + schMRT + "\n\nBuses: " + schBus + \
                "\n\nSchool Type: " + schType + "\n\nMission: " + mission + \
                "\n\nVision: " + vision + "\n\n"

    return resultstr
