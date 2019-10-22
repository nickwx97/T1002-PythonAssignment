from myCSV import *


def schoolstuff(x, y):
    """Main inp is the substring taken from schEnquiry"""
    sch_enquiry = x

    school_dict_items_list = genDict(openCSV("Data/general-information-of-schools.csv"))

    sch_by_condition_info = []
    for sch in school_dict_items_list[len(school_dict_items_list) - 1].items():
        """change the filter condition in the 'Column you want to filter by' in sch[1.csv][0]['Column you want to filter 
        by'] """

        if y == "school_name":
            if sch_enquiry.upper() in sch[0].upper():
                sch_by_condition_info.append(sch[0])
        else:
            if sch_enquiry.upper() in sch[1][0][y.lower()].upper():
                sch_by_condition_info.append(sch)

    """schByConditionInfo contains all the information of the schools based on the condition given"""
    if y != "school_name":
        for y in sch_by_condition_info:
            for z in y[1][0].keys():
                y[1][0][z] = y[1][0].get(z).replace('|', ',')

    return sch_by_condition_info
