import matplotlib.pyplot as plt
import pandas as pd


def make_autopct(values):  # to display the count and percentage in the chart
    def my_autopct(pct):
        total = sum(values)
        val = int(round(pct * total / 100.0))
        return '{p:.0f}% ({v:d})'.format(p=pct, v=val)

    return my_autopct


def get1PieChart(inp, colname, title):
    # Count all the unique values in a column and display as a pie chart
    df = pd.read_csv(inp)
    series1 = df[colname].value_counts()  # Enter column name, using pandas to convert the csv into series

    # Below are for pie chart appearance
    series1.plot(kind="pie", autopct=make_autopct(series1), legend=series1.all(), figsize=[15, 9])
    plt.legend(bbox_to_anchor=(1.01, 0.53), loc="lower right", fontsize=10, bbox_transform=plt.gcf().transFigure)
    plt.axis('equal')
    plt.title(title)
    plt.ylabel('')
    plt.show()


def get1BarChart(inp, rank, title, colname, colname1):
    # Rank top x1 schools and display as a bar
    df = pd.read_csv(inp)
    df.sort_values(by=colname, ascending=False)[[colname, colname1]][:rank].plot(x=colname1, y=colname,
                                                                                 kind='barh', legend='',
                                                                                 figsize=[20, 20])
    # Below are for pie chart appearance
    plt.gcf().subplots_adjust(left=0.25)
    plt.ylabel('School Name')
    plt.legend(bbox_to_anchor=(1.0, 0.53), loc="lower right", fontsize=10, bbox_transform=plt.gcf().transFigure)
    plt.title(title)
    plt.show()


def get2PieCharts(inp, col1, col2, title):
    # Count all the unique values in a column and display as a pie chart
    df = pd.read_csv(inp)
    series1 = df[col1].value_counts()  # Enter column name, using pandas to convert the csv into series
    series2 = df[col2].value_counts()  # Enter column name, using pandas to convert the csv into series

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
    plt.show()
