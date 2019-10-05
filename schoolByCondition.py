import csv
from readCSV import *


def schoolstuff(x):

    """Main input is the substring taken from schEnquiry"""
    schEnquiry = x

    schoolDictItemsList = genDict(openCSV("Data/general-information-of-schools.csv"))

    schByConditionInfo = []
    schByAreaListNames = []

    # print schoolDictItemsList[len(schoolDictItemsList)-1]
    #
    for sch in schoolDictItemsList[len(schoolDictItemsList)-1].items():
        """change the filter condition in the 'Column you want to filter by' in sch[1][0]['Column you want to filter by']"""
        if schEnquiry.upper() in sch[1][0]['dgp_code'].upper():
            # appending the schools depending on the requested area
            schByConditionInfo.append(sch)

    # print schoolDictItemsList[0]

    """schByAreaListInfo contains all the information of the schools based on the condition given"""
    for y in schByConditionInfo:
        # print y[1][0]
        for z in y[1][0].keys():
            y[1][0][z] = y[1][0].get(z).replace('|',',')

    return schByAreaListNames
