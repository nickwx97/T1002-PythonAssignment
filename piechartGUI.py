from piechart import *

class insights:
    window = tkinter.Tk()
    window.title('Data Statistics')
    window.geometry("500x500+10+10")

    lbl = tkinter.Label(window, text="School Insights", fg='red', font=("Helvetica", 24))
    button1 = tkinter.Button(window, text="Types of School",
                             command=lambda: get1PieChart("Data/general-information-of-schools.csv", 'Type_Code',
                                                          "Type of Schools",
                                                          "pie_SchoolTypes.png"))
    button3 = tkinter.Button(window, text="Data/Types of Applied Learning Programmes in School",
                             command=lambda: get1PieChart("school-distinctive-programmes.csv", 'Alp_Domain',
                                                          "Types of Applied Learning Programmes in School",
                                                          'pie_ALP.png'))
    button2 = tkinter.Button(window, text="Data/Type of Elective Programmes in School",
                             command=lambda: get1PieChart("moe-programmes.csv", 'Moe_Programme_Desc',
                                                          "Type of Elective Programmes in School",
                                                          "pie_SchoolProgTypes.png"))
    button4 = tkinter.Button(window, text="Data/Types of Learning for Life Programmes in Schools",
                             command=lambda: get2PieCharts("school-distinctive-programmes.csv", "Domain 1.csv",
                                                           "Domain 2",
                                                           "Types of Learning for Life Programmes in Schools",
                                                           "pie_LLP.png"))
    button5 = tkinter.Button(window, text="Data/Which Area in Singapore has more school?",
                             command=lambda: get1PieChart("general-information-of-schools.csv", "Zone_Code",
                                                          "Which Area in Singapore has more school?",
                                                          "pie_regioncode.png"))
    button6 = tkinter.Button(window, text="Data/Level Types in School",
                             command=lambda: get1PieChart("general-information-of-schools.csv", "Mainlevel_Code",
                                                          "Level Types in School", "pie_schoollevel.png"))
    button7 = tkinter.Button(window, text="Top School Rankings in Singapore",
                             command=lambda: get1BarChart("Data/cutoff.csv", 20, "Ranking of School",
                                                          "pie_schoolrank.png"))

    lbl.place(x=80, y=50)
    button1.place(x=80, y=140)
    button2.place(x=80, y=180)
    button3.place(x=80, y=220)
    button4.place(x=80, y=260)
    button5.place(x=80, y=300)
    button6.place(x=80, y=340)
    button6.place(x=80, y=380)

    window.mainloop()
