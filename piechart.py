import matplotlib.pyplot as plt
import pandas as pd
import csv


def make_autopct(values):  # to display the count and percentage in the chart
    def my_autopct(pct):
        total = sum(values)
        val = int(round(pct * total / 100.0))
        return '{p:.2f}%  ({v:d})'.format(p=pct, v=val)

    return my_autopct


def getPieChart(colname):
    # Count all the unique values in a column and display as a pie chart and save the picture
    df = pd.read_csv("Data/general-information-of-schools.csv")
    series1 = df[colname].value_counts()  # Enter column name, using pandas to convert the csv into series
    lis1 = series1.tolist()  # Convert series to list if required
    print series1
    # Below are for pie chart appearance
    series1.plot(kind="pie", autopct=make_autopct(series1), legend=series1.all(), figsize=[11, 9])
    plt.legend(loc="lower left")
    plt.axis('equal')
    plt.title("Type of Schools")
    plt.ylabel('')
    plt.savefig('pie_1.png')
    plt.show()


def getPieChart1():
    # Count specific values in a column and display as a bar graph and save the picture
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
                else:  # Can add elif, if need to find more specific values
                    line_count += 1
                    nogovern.append({", ".join(row)})

    # Below are for pie chart appearance
    types = ["Government", "Non-Government"]
    num = [len(govern), len(nogovern)]
    plt.pie(num, explode=[0, 0], labels=types, autopct=make_autopct(num), startangle=0, colors=['orange', 'lightblue'])
    plt.axis('equal')
    plt.title("Type of Schools")
    # plt.savefig('pie_1.png')
    plt.show()


print getPieChart('Type_Code')
print getPieChart1()
