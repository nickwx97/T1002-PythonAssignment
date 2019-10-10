from csv import *

def schoolstuff(x,y):
    """Main input is the substring taken from schEnquiry"""
    sch_enquiry = x

    school_dict_items_list = genDict(openCSV("Data/general-information-of-schools.csv"))

    sch_by_condition_info = []
    sch_by_area_list_names = []

    # print schoolDictItemsList[len(schoolDictItemsList)-1]
    #
    for sch in school_dict_items_list[len(school_dict_items_list) - 1].items():
        """change the filter condition in the 'Column you want to filter by' in sch[1][0]['Column you want to filter 
        by'] """

        if y == "school_name":
            if sch_enquiry.upper() in sch[0].upper():
                sch_by_condition_info.append(sch[0])
        else:
            if sch_enquiry.upper() in sch[1][0][y.lower()].upper():
                # appending the schools depending on the requested area
                sch_by_condition_info.append(sch)

    # print schoolDictItemsList[0]

    """schByConditionInfo contains all the information of the schools based on the condition given"""
    if y != "school_name":
        for y in sch_by_condition_info:
            # print y[1][0]
            for z in y[1][0].keys():
                y[1][0][z] = y[1][0].get(z).replace('|', ',')

    return sch_by_condition_info


