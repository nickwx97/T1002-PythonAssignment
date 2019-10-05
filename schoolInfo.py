from csv import *


def schoolStuff(x):
    sch_enquiry = x

    school_dict_items_list = genDict(openCSV("Data/general-information-of-schools.csv"))

    school_dict_items_header = school_dict_items_list[0]
    school_dict_items = school_dict_items_list[1]

    for x in school_dict_items.items():
        for y in school_dict_items_header[1:]:
            x[1][0][y] = x[1][0].get(y).replace('|', ',')

    # schoolDictItems is the list of all the information of the requested school retrived from schoolDictItems with the school name as the key
    # schoolDictItemsItems = list(v for k, v in schoolDictItems.items() if schEnquiry in k.lower())

    school_name = ""

    temp = [i.upper() for i in school_dict_items.keys()]
    for x in temp:
        if sch_enquiry.upper() in x:
            school_name = x

    school_dict_items = school_dict_items[school_name.title()][0]

    school_add = school_dict_items["address"]
    sch_tel = school_dict_items["telephone_no"]
    sch_email = school_dict_items["email_address"]
    sch_mrt = school_dict_items["mrt station"]
    sch_bus = school_dict_items["buses"]
    sch_type = school_dict_items["type_code"] + "/" + school_dict_items["nature_code"] + "/" + school_dict_items[
        "session_code"] + "/" + school_dict_items["mainlevel_code"]

    resultstr = "School Name: " + school_name + "\n" + \
                "Address: " + school_add + "\n" + \
                "Contact No: " + sch_tel + "\n" + \
                "Email: " + sch_email + "\n" + \
                "Nearby MRTs: " + sch_mrt + "\n" + \
                "Buses: " + sch_bus + "\n" + \
                "School Type: " + sch_type + "\n"
    return resultstr


tryStr = schoolStuff('high')
print tryStr
