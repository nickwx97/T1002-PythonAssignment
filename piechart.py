import csv

import matplotlib.pyplot as plt
import pandas as pd


def make_autopct(values):  # to display the count and percentage in the chart
    def my_autopct(pct):
        total = sum(values)
        val = int(round(pct * total / 100.0))
        return '{p:.0f}% ({v:d})'.format(p=pct, v=val)

    return my_autopct


def get1PieChart(input, colname, title, picname):
    # Count all the unique values in a column and display as a pie chart and save the picture
    df = pd.read_csv(input)
    series1 = df[colname].value_counts()  # Enter column name, using pandas to convert the csv into series
    print series1

    # Below are for pie chart appearance
    series1.plot(kind="pie", autopct=make_autopct(series1), legend=series1.all(), figsize=[15, 9])
    plt.legend(bbox_to_anchor=(1.01, 0.53), loc="lower right", fontsize=10, bbox_transform=plt.gcf().transFigure)
    plt.axis('equal')
    plt.title(title)
    plt.ylabel('')
    plt.savefig(picname)
    plt.show()


def getPieChart():  # To remove at the end
    # This function is more more specific and hardcoded way of getting values and displaying as pie chart
    # Count specific values in a column and display as a pie chart and save the picture
    with open("Data/general-information-of-schools.csv", 'r') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        line_count = 0
        govern = []
        nogovern = []
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                if 'Government' in row[24]:  # Enter the specific value in the column and column index
                    line_count += 1
                    govern.append({", ".join(row)})
                else:  # Add elif, if need to find more specific values
                    line_count += 1
                    nogovern.append({", ".join(row)})

    # Below are for pie chart appearance
    types = ["Government", "Non-Government"]
    num = [len(govern), len(nogovern)]
    plt.pie(num, explode=[0, 0], labels=types, autopct=make_autopct(num), startangle=0, colors=['orange', 'lightblue'])
    plt.axis('equal')
    plt.title("Type of Schools")
    plt.savefig('pie_1.png')
    plt.show()


def get2PieCharts(input, col1, col2, title, picname):
    # Count all the unique values in a column and display as a pie chart and save the picture
    df = pd.read_csv(input)
    series1 = df[col1].value_counts()  # Enter column name, using pandas to convert the csv into series
    series2 = df[col2].value_counts()  # Enter column name, using pandas to convert the csv into series
    print series1, series2

    # Below are for pie chart appearance
    # For first pie chart
    plt.subplot(1, 2, 1)
    plt.ylabel('', fontsize=20)
    plt.legend(bbox_to_anchor=(1.1, 1.1), loc="upper right", fontsize=5, bbox_transform=plt.gcf().transFigure)
    series1.plot(kind="pie", autopct=make_autopct(series1), radius=1, labels=None, legend=series1.all())

    # For second pie chart
    plt.suptitle(title, fontsize=20)
    plt.subplot(1, 2, 2)
    plt.legend(bbox_to_anchor=(1.1, 1.1), loc="upper right", fontsize=5, bbox_transform=plt.gcf().transFigure)
    plt.ylabel('', fontsize=20)
    series2.plot(kind="pie", autopct=make_autopct(series1), radius=1, labels=None, legend=series1.all())

    # For display as one figure
    plt.axis('equal')
    fig = plt.gcf()
    fig.set_size_inches(20, 20)
    fig.savefig(picname, dpi=100)
    plt.show()


# Below is a specific function
print getPieChart()  # Edit the function

# Below are dynamic functions
# To get 1.csv pie chart
# Inputs for get1PieChart: Input csv, Column name, Title for the graph, name the picture of the graph to save as
print get1PieChart("Data/test.csv", 'Type_Code', "Type of Schools", "pie_SchoolTypes.png")
print get1PieChart("Data/school-distinctive-programmes.csv", 'Alp_Domain',
                   "Types of Applied Learning Programmes in School", 'pie_ALP.png')
print get1PieChart("Data/moe-programmes.csv", 'Moe_Programme_Desc', "Type of Programmes in School",
                   "pie_SchoolProgTypes.png")
# To get 2 pie chart in one figure
# Inputs for get2PieCharts: Input csv, Column name1, Column name2, Title for the graph, name the picture of the graph to save as
print get2PieCharts("Data/school-distinctive-programmes.csv", "Domain 1.csv", "Domain 2",
                    "Types of Learning for Life Programmes in Schools", "pie_LLP.png")
