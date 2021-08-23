#########----------ATTENDANCE DETAILS-----------------
def searchATTENDANCE():
    def submitATTENDANCEsearch():
        usn2 = usnvar2.get()
        subcode2 = subcodevar2.get()
        sem2 = semvar2.get()
        percent = percentvar.get()
        #greater85 = greater85var.get()
        #essthan75 = lessthan75var.get()
        #between7585 = between7585.get()
        if (usn2 != ''):
            strr = 'SELECT A.USN,S.SUBCODE,S.TITLE,S.SEM,A.TOTAL_ATTENDANCE,A.TOTAL_TAKEN,A.PERCENTAGE FROM ATTENDANCE AS A,SUBJECT AS S WHERE A.SUBCODE=S.SUBCODE AND A.USN=%s;'
            mycursor.execute(strr,(usn2))
            datas = mycursor.fetchall()
            attendancetable.delete(*attendancetable.get_children())
            for i in datas:
                vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6]]
                attendancetable.insert('',END,values=vv)
        elif (subcode2 != ''):
            strr = 'SELECT A.USN,S.SUBCODE,S.TITLE,S.SEM,A.TOTAL_ATTENDANCE,A.TOTAL_TAKEN,A.PERCENTAGE FROM ATTENDANCE AS A,SUBJECT AS S WHERE A.SUBCODE=S.SUBCODE AND A.SUBCODE=%s;'
            mycursor.execute(strr,(subcode2))
            datas = mycursor.fetchall()
            attendancetable.delete(*attendancetable.get_children())
            for i in datas:
                vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6]]
                attendancetable.insert('',END,values=vv)
        elif (sem2 != ''):
            strr = 'SELECT A.USN,S.SUBCODE,S.TITLE,S.SEM,A.TOTAL_ATTENDANCE,A.TOTAL_TAKEN,A.PERCENTAGE FROM ATTENDANCE AS A,SUBJECT AS S WHERE A.SUBCODE=S.SUBCODE AND S.SEM=%s;'
            mycursor.execute(strr,(sem2))
            datas = mycursor.fetchall()
            attendancetable.delete(*attendancetable.get_children())
            for i in datas:
                vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6]]
                attendancetable.insert('',END,values=vv)

        elif (percent != '' and percent=='>=85'):
            strr = 'SELECT A.USN,S.SUBCODE,S.TITLE,S.SEM,A.TOTAL_ATTENDANCE,A.TOTAL_TAKEN,A.PERCENTAGE FROM ATTENDANCE AS A,SUBJECT AS S WHERE A.SUBCODE=S.SUBCODE AND A.PERCENTAGE>=85;'
            mycursor.execute(strr)
            datas = mycursor.fetchall()
            attendancetable.delete(*attendancetable.get_children())
            for i in datas:
                vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6]]
                attendancetable.insert('',END,values=vv)

        elif (percent != '' and percent=='<75'):
            strr = 'SELECT A.USN,S.SUBCODE,S.TITLE,S.SEM,A.TOTAL_ATTENDANCE,A.TOTAL_TAKEN,A.PERCENTAGE FROM ATTENDANCE AS A,SUBJECT AS S WHERE A.SUBCODE=S.SUBCODE AND A.PERCENTAGE<75;'
            mycursor.execute(strr)
            datas = mycursor.fetchall()
            attendancetable.delete(*attendancetable.get_children())
            for i in datas:
                vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6]]
                attendancetable.insert('',END,values=vv)

        elif (percent != '' and percent=='>=75 and <85'):
            strr = 'SELECT A.USN,S.SUBCODE,S.TITLE,S.SEM,A.TOTAL_ATTENDANCE,A.TOTAL_TAKEN,A.PERCENTAGE FROM ATTENDANCE AS A,SUBJECT AS S WHERE A.SUBCODE=S.SUBCODE AND A.PERCENTAGE>=75 AND A.PERCENTAGE<85;'
            mycursor.execute(strr)
            datas = mycursor.fetchall()
            attendancetable.delete(*attendancetable.get_children())
            for i in datas:
                vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6]]
                attendancetable.insert('',END,values=vv)


    searchATTENDANCEroot = Toplevel(master=attroot)
    searchATTENDANCEroot.grab_set()
    searchATTENDANCEroot.geometry('450x550+2+150')
    searchATTENDANCEroot.resizable(False,False)
    searchATTENDANCEroot.config(bg="#15648e")
    searchATTENDANCEroot.iconbitmap("stu.ico")
    searchATTENDANCEroot.title("Search IA Details")
    usn2label = Label(searchATTENDANCEroot,text="Enter USN : ",bg="white",font=("times",18),width=16,bd=2,anchor="w")
    usn2label.place(x=10,y=10)

    subcode2label = Label(searchATTENDANCEroot,text="Enter SUBCODE : ",bg="white",font=("times",18),width=16,bd=2,anchor="w")
    subcode2label.place(x=10,y=80)

    titlelabel = Label(searchATTENDANCEroot,text="Enter Semester : ",bg="white",font=("times",18),width=16,bd=2,anchor="w")
    titlelabel.place(x=10,y=150)

    sem2label = Label(searchATTENDANCEroot,text="Select Percentage : ",bg="white",font=("times",18),width=16,bd=2,anchor="w")
    sem2label.place(x=10,y=220)

    #creditslabel = Label(searchATTENDANCEroot,text="Select CREDITS : ",bg="white",font=("times",18),width=16,bd=2,anchor="w")
    #creditslabel.place(x=10,y=290)

    ########################################
    usnvar2 = StringVar()
    subcodevar2 = StringVar()
    semvar2 = StringVar()
    percentvar =StringVar()
    greatert85var = StringVar()
    lessthan75 = StringVar()
    between7585 = StringVar()


    usn2entry = Entry(searchATTENDANCEroot,font=('Times',14,'bold'),bg='gray73',bd=3,textvariable=usnvar2)
    usn2entry.place(x=230,y=10,width=205,height=35)

    subcode2entry = Entry(searchATTENDANCEroot,font=('Times',14,'bold'),bg='gray73',bd=3,textvariable=subcodevar2)
    subcode2entry.place(x=230,y=80,width=205,height=35)

    titleentry = Entry(searchATTENDANCEroot,font=('Times',14,'bold'),bg='gray73',bd=3,textvariable=semvar2)
    titleentry.place(x=230,y=150,width=205,height=35)

    percententry = Combobox(searchATTENDANCEroot,font=('Times',14,'bold'),textvariable=percentvar)
    percententry.place(x=230,y=220,width=205,height=35)

    percententry['values'] = ('>=85',
                              '<75',
                              '>=75 and <85')
    percententry.current()

    #creditsentry = Entry(searchATTENDANCEroot,font=('Times',14,'bold'),bg='gray73',bd=3,textvariable=creditsvar)
    #creditsentry.place(x=230,y=290,width=205,height=35)

    #genderentry1 = Radiobutton(searchroot,text="MALE",font=('Times',14,'bold'),bg='#15648e',variable=gendervar,
      #                         value='MALE',activebackground='#15648e'
                           #    )
    #genderentry1.place(x=230,y=290)

    #genderentry2 = Radiobutton(searchroot,text='FEMALE',font=('Times',14,'bold'),bg='#15648e',variable=gendervar,
     #                          value='FEMALE',activebackground='#15648e'
                          #     )
    #genderentry2.place(x=310,y=290)



    submitbtn=Button(searchATTENDANCEroot,text="Submit",font=('Times',14,'bold'),bd=3,width=15,bg="sky blue2",activebackground='royal blue3',
                     activeforeground='white',command=submitATTENDANCEsearch,cursor='hand2')
    submitbtn.place(x=135,y=450)

    searchATTENDANCEroot.mainloop()




def updateATTENDANCE():
    def submitATTENDANCEupdate():
        usn2 = usnvar2.get()
        subcode2 = subcodevar2.get()
        title = titlevar.get()
        sem2 = semvar2.get()
        attended = attendedvar.get()
        taken = takenvar.get()

        strr = 'UPDATE ATTENDANCE SET TOTAL_ATTENDANCE =%s, TOTAL_TAKEN =%s ,PERCENTAGE=(%s*100)/%s WHERE USN=%s AND SUBCODE = %s;'
        mycursor.execute(strr,(attended,taken,attended,taken,usn2,subcode2))
        con.commit()
        messagebox.showinfo('Notifications','usn  {} with subject code {} attendance Modified sucessfully...'.format(usn2,subcode2),parent=updateATTENDANCEroot)
        strr = 'SELECT A.USN,S.SUBCODE,S.TITLE,S.SEM,A.TOTAL_ATTENDANCE,A.TOTAL_TAKEN,A.PERCENTAGE FROM ATTENDANCE AS A,SUBJECT AS S WHERE A.SUBCODE=S.SUBCODE;'
        mycursor.execute(strr)
        datas = mycursor.fetchall()
        attendancetable.delete(*attendancetable.get_children())
        for i in datas:
            vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6]]
            attendancetable.insert('',END,values=vv)

    updateATTENDANCEroot = Toplevel(master=attroot)
    updateATTENDANCEroot.grab_set()
    updateATTENDANCEroot.geometry('450x690+2+90')
    updateATTENDANCEroot.resizable(False,False)
    updateATTENDANCEroot.config(bg="#15648e")
    updateATTENDANCEroot.iconbitmap("stu.ico")
    updateATTENDANCEroot.title("Update Student Details")
    usn2label=Label(updateATTENDANCEroot,text="Enter USN : ",bg="white",font=("times",18),width=16,bd=2,anchor="w")
    usn2label.place(x=10,y=10)

    subcode2label = Label(updateATTENDANCEroot,text="Enter Subjectcode : ",bg="white",font=("times",18),width=16,bd=2,anchor="w")
    subcode2label.place(x=10,y=80)

    #titlelabel = Label(updateIAroot,text="Update Title : ",bg="white",font=("times",18),width=16,bd=2,anchor="w")
    #titlelabel.place(x=10,y=150)

    #sem2label = Label(updateIAroot,text="Update Sem : ",bg="white",font=("times",18),width=16,bd=2,anchor="w")
    #sem2label.place(x=10,y=220)

    #creditslabel = Label(updateIAroot,text="Update credits : ",bg="white",font=("times",18),width=16,bd=2,anchor="w")
    #creditslabel.place(x=10,y=290)

    test1label = Label(updateATTENDANCEroot,text="Update Attendance : ",bg="white",font=("times",18),width=16,bd=2,anchor="w")
    test1label.place(x=10,y=150)

    test2label = Label(updateATTENDANCEroot,text="Update Class Taken : ",bg="white",font=("times",18),width=16,bd=2,anchor="w")
    test2label.place(x=10,y=220)

    #test3label = Label(updateATTENDANCEroot,text="Update Class Taken : ",bg="white",font=("times",18),width=16,bd=2,anchor="w")
    #test3label.place(x=10,y=290)


    ########################################
    usnvar2 = StringVar()
    subcodevar2 = StringVar()
    titlevar = StringVar()
    semvar2 = StringVar()
    creditsvar = StringVar()
    attendedvar = StringVar()
    takenvar = StringVar()


    usn2entry = Entry(updateATTENDANCEroot,font=('Times',14,'bold'),bg='gray73',bd=3,textvariable=usnvar2)
    usn2entry.place(x=230,y=10,width=205,height=35)

    subcode2entry = Entry(updateATTENDANCEroot,font=('Times',14,'bold'),bg='gray73',bd=3,textvariable=subcodevar2)
    subcode2entry.place(x=230,y=80,width=205,height=35)

    #titleentry = Entry(updateIAroot,font=('Times',14,'bold'),bg='gray73',bd=3,textvariable=titlevar)
    #titleentry.place(x=230,y=150,width=205,height=35)

    #sem2entry = Entry(updateIAroot,font=('Times',14,'bold'),bg='gray73',bd=3,textvariable=semvar2)
    #sem2entry.place(x=230,y=220,width=205,height=35)

    #creditsentry = Entry(updateIAroot,font=('Times',14,'bold'),bg='gray73',bd=3,textvariable=creditsvar)
    #creditsentry.place(x=230,y=290,width=205,height=35)

    test1entry = Entry(updateATTENDANCEroot,font=('Times',14,'bold'),bg='gray73',bd=3,textvariable=attendedvar)
    test1entry.place(x=230,y=150,width=205,height=35)

    test2entry = Entry(updateATTENDANCEroot,font=('Times',14,'bold'),bg='gray73',bd=3,textvariable=takenvar)
    test2entry.place(x=230,y=220,width=205,height=35)

    #test3entry = Entry(updateIAroot,font=('Times',14,'bold'),bg='gray73',bd=3,textvariable=testvar3)
    #test3entry.place(x=230,y=290,width=205,height=35)

    submitbtn=Button(updateATTENDANCEroot,text="Submit",font=('Times',14,'bold'),bd=3,width=15,bg="sky blue2",activebackground='royal blue3',
                     activeforeground='white',command=submitATTENDANCEupdate,cursor='hand2')
    submitbtn.place(x=135,y=620)
    cc = attendancetable.focus()
    content = attendancetable.item(cc)
    pp = content['values']
    if (len(pp) != 0):
        usnvar2.set(pp[0])
        subcodevar2.set(pp[1])
        attendedvar.set(pp[4])
        takenvar.set(pp[5])

    updateATTENDANCEroot.mainloop()



def deleteATTENDANCE():
    cc = attendancetable.focus()
    content = attendancetable.item(cc)
    pp = content['values'][0]
    pq = content['values'][1]
    strr = 'DELETE FROM ATTENDANCE WHERE USN=%s AND SUBCODE=%s;'
    mycursor.execute(strr,(pp,pq))
    con.commit()
    messagebox.showinfo('Notifications','usn  {} with subcode {} deleted sucessfully...'.format(pp,pq))
    strr = 'SELECT A.USN,S.SUBCODE,S.TITLE,S.SEM,A.TOTAL_ATTENDANCE,A.TOTAL_TAKEN,A.PERCENTAGE FROM ATTENDANCE AS A,SUBJECT AS S WHERE A.SUBCODE=S.SUBCODE;'
    mycursor.execute(strr)
    datas = mycursor.fetchall()
    attendancetable.delete(*attendancetable.get_children())
    for i in datas:
        vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6]]
        attendancetable.insert('',END,values=vv)


def showATTENDANCE():
    strr = 'SELECT A.USN,S.SUBCODE,S.TITLE,S.SEM,A.TOTAL_ATTENDANCE,A.TOTAL_TAKEN,A.PERCENTAGE FROM ATTENDANCE AS A,SUBJECT AS S WHERE A.SUBCODE=S.SUBCODE;'
    mycursor.execute(strr)
    datas = mycursor.fetchall()
    attendancetable.delete(*attendancetable.get_children())
    for i in datas:
        vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6]]
        attendancetable.insert('',END,values=vv)


def addATTENDANCE():
    def submitaddATTENDACE():
        usn2 = usnvar2.get()
        subcode2 = subcodevar2.get()
        attended = attendedvar.get()
        taken = takenvar.get()
        percentage = percentagevar.get()
        try:
            strr = 'insert into attendance values(%s,%s,%s,%s,(%s*100/%s))'
            mycursor.execute(strr,(usn2,subcode2,attended,taken,attended,taken))
            con.commit()
            res = messagebox.askyesnocancel('Notificatrions',
                                            'usn {} subcode {} Added sucessfully.. and want to clean the form'.format(
                                                usn2,subcode2),parent=attroot)
            if (res == True):
                usnvar2.set('')
                subcodevar2.set('')
                attended.set('')
                taken.set('')
                percentage.set('')
        except:
            messagebox.showerror('Notifications','SUBJECT NOT ADDED YET PLEASE ADD AND TRY AGAIN...',parent=attroot)

        strr = 'SELECT A.USN,S.SUBCODE,S.TITLE,S.SEM,A.TOTAL_ATTENDANCE,A.TOTAL_TAKEN,A.PERCENTAGE FROM ATTENDANCE AS A,SUBJECT AS S WHERE A.SUBCODE=S.SUBCODE;'
        mycursor.execute(strr)
        datas = mycursor.fetchall()
        attendancetable.delete(*attendancetable.get_children())
        for i in datas:
            vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6]]
            attendancetable.insert('',END,values=vv)

    addattroot = Toplevel(master=attroot)
    addattroot.grab_set()
    addattroot.geometry('400x570+5+175')
    addattroot.resizable(False,False)
    addattroot.config(bg="#15648e")
    addattroot.iconbitmap("stu.ico")
    addattroot.title("STUDENT DATABASE MANAGEMENT SYSTEM")
    usnlabel = Label(addattroot,text="Enter USN : ",bg="white",font=("times",18),width=12,bd=2,anchor="w")
    usnlabel.place(x=10,y=10)

    subcodelabel = Label(addattroot,text="Enter Subcode : ",bg="white",font=("times",18),width=12,bd=2,anchor="w")
    subcodelabel.place(x=10,y=80)

    test1label = Label(addattroot,text="Enter Attended : ",bg="white",font=("times",18),width=12,bd=2,anchor="w")
    test1label.place(x=10,y=150)

    test2label = Label(addattroot,text="Enter Taken : ",bg="white",font=("times",18),width=12,bd=2,anchor="w")
    test2label.place(x=10,y=220)

    #test3label = Label(addattroot,text="Enter percentage : ",bg="white",font=("times",18),width=12,bd=2,anchor="w")
    #test3label.place(x=10,y=290)

    ########################################
    usnvar2 = StringVar()
    subcodevar2 = StringVar()
    attendedvar = StringVar()
    takenvar = StringVar()
    percentagevar = StringVar()

    usnentry = Entry(addattroot,font=('Times',14,'bold'),bd=3,textvariable=usnvar2)
    usnentry.place(x=180,y=10,width=200,height=35)

    subcodeentry = Entry(addattroot,font=('Times',14,'bold'),bd=3,textvariable=subcodevar2)
    subcodeentry.place(x=180,y=80,width=200,height=35)

    test1entry = Entry(addattroot,font=('Times',14,'bold'),bd=3,textvariable=attendedvar)
    test1entry.place(x=180,y=150,width=200,height=35)

    test2entry = Entry(addattroot,font=('Times',14,'bold'),bd=3,textvariable=takenvar)
    test2entry.place(x=180,y=220,width=200,height=35)

    #test3entry = Entry(addattroot,font=('Times',14,'bold'),bd=3,textvariable=percentagevar)
    #test3entry.place(x=180,y=290,width=200,height=35)


    submitbtn = Button(addattroot,text="Submit",font=('Times',14,'bold'),bd=3,width=15,bg="sky blue2",
                       activebackground='royal blue3',
                       activeforeground='white',command=submitaddATTENDACE)
    submitbtn.place(x=100,y=500)

    addattroot.mainloop()


########-----------IA MARKS-----------------------
def deleteIA():
    cc = iatable.focus()
    content = iatable.item(cc)
    pp = content['values'][0]
    pq = content['values'][1]
    strr = 'DELETE FROM IAMARKS WHERE USN=%s AND SUBCODE=%s;'
    mycursor.execute(strr,(pp,pq))
    con.commit()
    messagebox.showinfo('Notifications','usn  {} with subcode {} deleted sucessfully...'.format(pp,pq))
    strr = 'SELECT I.USN,S.SUBCODE,S.TITLE,S.SEM,S.CREDITS,I.TEST1,I.TEST2,I.TEST3,I.FINALIA FROM IAMARKS AS I,SUBJECT AS S WHERE I.SUBCODE=S.SUBCODE;'
    mycursor.execute(strr)
    datas = mycursor.fetchall()
    iatable.delete(*iatable.get_children())
    for i in datas:
        vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],[7],i[8]]
        iatable.insert('',END,values=vv)


def updateIAMARKS():
    def submitIAupdate():
        usn2 = usnvar2.get()
        subcode2 = subcodevar2.get()
        title = titlevar.get()
        sem2 = semvar2.get()
        credits = creditsvar.get()
        test1 = testvar1.get()
        test2 = testvar2.get()
        test3 = testvar3.get()

        strr = 'UPDATE IAMARKS SET TEST1 =%s, TEST2=%s, TEST3= %s ,FINALIA=(%s+%s+%s)/3 WHERE USN=%s AND SUBCODE = %s;'
        mycursor.execute(strr,(test1,test2,test3,test1,test2,test3,usn2,subcode2))
        con.commit()
        messagebox.showinfo('Notifications','usn  {} with subject code {} marks Modified sucessfully...'.format(usn2,subcode2),parent=updateIAroot)
        strr = 'SELECT I.USN,S.SUBCODE,S.TITLE,S.SEM,S.CREDITS,I.TEST1,I.TEST2,I.TEST3,I.FINALIA FROM IAMARKS AS I,SUBJECT AS S WHERE I.SUBCODE=S.SUBCODE;'
        mycursor.execute(strr)
        datas = mycursor.fetchall()
        iatable.delete(*iatable.get_children())
        for i in datas:
            vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
            iatable.insert('',END,values=vv)

    updateIAroot=Toplevel(master=iaroot)
    updateIAroot.grab_set()
    updateIAroot.geometry('450x690+2+90')
    updateIAroot.resizable(False,False)
    updateIAroot.config(bg="#15648e")
    updateIAroot.iconbitmap("stu.ico")
    updateIAroot.title("Update Student Details")
    usn2label=Label(updateIAroot,text="Enter USN : ",bg="white",font=("times",18),width=16,bd=2,anchor="w")
    usn2label.place(x=10,y=10)

    subcode2label = Label(updateIAroot,text="Enter SUBCODE : ",bg="white",font=("times",18),width=16,bd=2,anchor="w")
    subcode2label.place(x=10,y=80)

    #titlelabel = Label(updateIAroot,text="Update Title : ",bg="white",font=("times",18),width=16,bd=2,anchor="w")
    #titlelabel.place(x=10,y=150)

    #sem2label = Label(updateIAroot,text="Update Sem : ",bg="white",font=("times",18),width=16,bd=2,anchor="w")
    #sem2label.place(x=10,y=220)

    #creditslabel = Label(updateIAroot,text="Update credits : ",bg="white",font=("times",18),width=16,bd=2,anchor="w")
    #creditslabel.place(x=10,y=290)

    test1label = Label(updateIAroot,text="Update TEST1 : ",bg="white",font=("times",18),width=16,bd=2,anchor="w")
    test1label.place(x=10,y=150)

    test2label = Label(updateIAroot,text="Update TEST2 : ",bg="white",font=("times",18),width=16,bd=2,anchor="w")
    test2label.place(x=10,y=220)

    test3label = Label(updateIAroot,text="Update TEST3 : ",bg="white",font=("times",18),width=16,bd=2,anchor="w")
    test3label.place(x=10,y=290)


    ########################################
    usnvar2 = StringVar()
    subcodevar2 = StringVar()
    titlevar = StringVar()
    semvar2 = StringVar()
    creditsvar = StringVar()
    testvar1 = StringVar()
    testvar2 = StringVar()
    testvar3 = StringVar()

    usn2entry = Entry(updateIAroot,font=('Times',14,'bold'),bg='gray73',bd=3,textvariable=usnvar2)
    usn2entry.place(x=230,y=10,width=205,height=35)

    subcode2entry = Entry(updateIAroot,font=('Times',14,'bold'),bg='gray73',bd=3,textvariable=subcodevar2)
    subcode2entry.place(x=230,y=80,width=205,height=35)

    #titleentry = Entry(updateIAroot,font=('Times',14,'bold'),bg='gray73',bd=3,textvariable=titlevar)
    #titleentry.place(x=230,y=150,width=205,height=35)

    #sem2entry = Entry(updateIAroot,font=('Times',14,'bold'),bg='gray73',bd=3,textvariable=semvar2)
    #sem2entry.place(x=230,y=220,width=205,height=35)

    #creditsentry = Entry(updateIAroot,font=('Times',14,'bold'),bg='gray73',bd=3,textvariable=creditsvar)
    #creditsentry.place(x=230,y=290,width=205,height=35)

    test1entry = Entry(updateIAroot,font=('Times',14,'bold'),bg='gray73',bd=3,textvariable=testvar1)
    test1entry.place(x=230,y=150,width=205,height=35)

    test2entry = Entry(updateIAroot,font=('Times',14,'bold'),bg='gray73',bd=3,textvariable=testvar2)
    test2entry.place(x=230,y=220,width=205,height=35)

    test3entry = Entry(updateIAroot,font=('Times',14,'bold'),bg='gray73',bd=3,textvariable=testvar3)
    test3entry.place(x=230,y=290,width=205,height=35)

    submitbtn=Button(updateIAroot,text="Submit",font=('Times',14,'bold'),bd=3,width=15,bg="sky blue2",activebackground='royal blue3',
                     activeforeground='white',command=submitIAupdate,cursor='hand2')
    submitbtn.place(x=135,y=620)
    cc = iatable.focus()
    content = iatable.item(cc)
    pp = content['values']
    if (len(pp) != 0):
        usnvar2.set(pp[0])
        subcodevar2.set(pp[1])
        testvar1.set(pp[5])
        testvar2.set(pp[6])
        testvar3.set(pp[7])

    updateIAroot.mainloop()

def searchIA():
    def submitIAsearch():
        usn2 = usnvar2.get()
        subcode2 = subcodevar2.get()
        sem2 = semvar2.get()
        title = titlevar.get()
        credits= creditsvar.get()
        if (usn2 != ''):
            strr = 'SELECT I.USN,S.SUBCODE,S.TITLE,S.SEM,S.CREDITS,I.TEST1,I.TEST2,I.TEST3,I.FINALIA FROM IAMARKS AS I,SUBJECT AS S WHERE I.SUBCODE=S.SUBCODE AND I.USN=%s;'
            mycursor.execute(strr,(usn2))
            datas = mycursor.fetchall()
            iatable.delete(*iatable.get_children())
            for i in datas:
                vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                iatable.insert('',END,values=vv)
        elif (subcode2 != ''):
            strr = 'SELECT I.USN,S.SUBCODE,S.TITLE,S.SEM,S.CREDITS,I.TEST1,I.TEST2,I.TEST3,I.FINALIA FROM IAMARKS AS I,SUBJECT AS S WHERE I.SUBCODE=S.SUBCODE AND I.SUBCODE=%s;'
            mycursor.execute(strr,(subcode2))
            datas = mycursor.fetchall()
            iatable.delete(*iatable.get_children())
            for i in datas:
                vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                iatable.insert('',END,values=vv)
        elif (title != ''):
            strr = 'SELECT I.USN,S.SUBCODE,S.TITLE,S.SEM,S.CREDITS,I.TEST1,I.TEST2,I.TEST3,I.FINALIA FROM IAMARKS AS I,SUBJECT AS S WHERE I.SUBCODE=S.SUBCODE AND S.TITLE=%s;'
            mycursor.execute(strr,(title))
            datas = mycursor.fetchall()
            iatable.delete(*iatable.get_children())
            for i in datas:
                vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                iatable.insert('',END,values=vv)

        elif (sem2 != ''):
            strr = 'SELECT I.USN,S.SUBCODE,S.TITLE,S.SEM,S.CREDITS,I.TEST1,I.TEST2,I.TEST3,I.FINALIA FROM IAMARKS AS I,SUBJECT AS S WHERE I.SUBCODE=S.SUBCODE AND S.SEM=%s;'
            mycursor.execute(strr,(sem2))
            datas = mycursor.fetchall()
            iatable.delete(*iatable.get_children())
            for i in datas:
                vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                iatable.insert('',END,values=vv)

        elif (credits != ''):
            strr = 'SELECT I.USN,S.SUBCODE,S.TITLE,S.SEM,S.CREDITS,I.TEST1,I.TEST2,I.TEST3,I.FINALIA FROM IAMARKS AS I,SUBJECT AS S WHERE I.SUBCODE=S.SUBCODE AND S.CREDITS=%s'
            mycursor.execute(strr,(credits))
            datas = mycursor.fetchall()
            iatable.delete(*iatable.get_children())
            for i in datas:
                vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                iatable.insert('',END,values=vv)


    searchIAroot = Toplevel(master=iaroot)
    searchIAroot.grab_set()
    searchIAroot.geometry('450x550+2+150')
    searchIAroot.resizable(False,False)
    searchIAroot.config(bg="#15648e")
    searchIAroot.iconbitmap("stu.ico")
    searchIAroot.title("Search IA Details")
    usn2label = Label(searchIAroot,text="Enter USN : ",bg="white",font=("times",18),width=16,bd=2,anchor="w")
    usn2label.place(x=10,y=10)

    subcode2label = Label(searchIAroot,text="Enter SUBCODE : ",bg="white",font=("times",18),width=16,bd=2,anchor="w")
    subcode2label.place(x=10,y=80)

    titlelabel = Label(searchIAroot,text="Enter TITLE : ",bg="white",font=("times",18),width=16,bd=2,anchor="w")
    titlelabel.place(x=10,y=150)

    sem2label = Label(searchIAroot,text="Enter SEMESTER : ",bg="white",font=("times",18),width=16,bd=2,anchor="w")
    sem2label.place(x=10,y=220)

    creditslabel = Label(searchIAroot,text="Select CREDITS : ",bg="white",font=("times",18),width=16,bd=2,anchor="w")
    creditslabel.place(x=10,y=290)

    ########################################
    usnvar2 = StringVar()
    subcodevar2 = StringVar()
    titlevar = StringVar()
    semvar2 = StringVar()
    creditsvar = StringVar()


    usn2entry = Entry(searchIAroot,font=('Times',14,'bold'),bg='gray73',bd=3,textvariable=usnvar2)
    usn2entry.place(x=230,y=10,width=205,height=35)

    subcode2entry = Entry(searchIAroot,font=('Times',14,'bold'),bg='gray73',bd=3,textvariable=subcodevar2)
    subcode2entry.place(x=230,y=80,width=205,height=35)

    titleentry = Entry(searchIAroot,font=('Times',14,'bold'),bg='gray73',bd=3,textvariable=titlevar)
    titleentry.place(x=230,y=150,width=205,height=35)

    sem2entry = Entry(searchIAroot,font=('Times',14,'bold'),bg='gray73',bd=3,textvariable=semvar2)
    sem2entry.place(x=230,y=220,width=205,height=35)

    creditsentry = Entry(searchIAroot,font=('Times',14,'bold'),bg='gray73',bd=3,textvariable=creditsvar)
    creditsentry.place(x=230,y=290,width=205,height=35)

    #genderentry1 = Radiobutton(searchroot,text="MALE",font=('Times',14,'bold'),bg='#15648e',variable=gendervar,
      #                         value='MALE',activebackground='#15648e'
                           #    )
    #genderentry1.place(x=230,y=290)

    #genderentry2 = Radiobutton(searchroot,text='FEMALE',font=('Times',14,'bold'),bg='#15648e',variable=gendervar,
     #                          value='FEMALE',activebackground='#15648e'
                          #     )
    #genderentry2.place(x=310,y=290)



    submitbtn=Button(searchIAroot,text="Submit",font=('Times',14,'bold'),bd=3,width=15,bg="sky blue2",activebackground='royal blue3',
                     activeforeground='white',command=submitIAsearch,cursor='hand2')
    submitbtn.place(x=135,y=450)

    searchIAroot.mainloop()

def showIA():
    print("hh")
    strr = 'SELECT I.USN,S.SUBCODE,S.TITLE,S.SEM,S.CREDITS,I.TEST1,I.TEST2,I.TEST3,I.FINALIA FROM IAMARKS AS I,SUBJECT AS S WHERE I.SUBCODE=S.SUBCODE;'
    mycursor.execute(strr)
    datas = mycursor.fetchall()
    iatable.delete(*iatable.get_children())
    for i in datas:
        vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
        iatable.insert('',END,values=vv)



def addia():
    def submitaddia():
        usn2 = usnvar2.get()
        subcode2 = subcodevar2.get()
        test1 = testvar1.get()
        test2 = testvar2.get()
        test3 = testvar3.get()
        finalia = finaliavar.get()
        try:
            strr = 'insert into iamarks values(%s,%s,%s,%s,%s,(%s+%s+%s)/3)'
            mycursor.execute(strr,(usn2,subcode2,test1,test2,test3,test1,test2,test3))
            con.commit()
            res = messagebox.askyesnocancel('Notificatrions','usn {} subcode {} Added sucessfully.. and want to clean the form'.format(usn2, subcode2),parent=iaroot)
            if (res == True):
                usnvar2.set('')
                subcodevar2.set('')
                testvar1.set('')
                testvar2.set('')
                testvar3.set('')
                finaliavar.set('')
        except:
            messagebox.showerror('Notifications','SUBJECT NOT ADDED YET PLEASE ADD AND TRY AGAIN...',parent=iaroot)
        strr = 'SELECT I.USN,S.SUBCODE,S.TITLE,S.SEM,S.CREDITS,I.TEST1,I.TEST2,I.TEST3,I.FINALIA FROM IAMARKS AS I,SUBJECT AS S WHERE I.SUBCODE=S.SUBCODE;'
        mycursor.execute(strr)
        datas = mycursor.fetchall()
        iatable.delete(*iatable.get_children())
        for i in datas:
            vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
            iatable.insert('',END,values=vv)
    addiaroot=Toplevel(master=iaroot)
    addiaroot.grab_set()
    addiaroot.geometry('400x570+5+175')
    addiaroot.resizable(False,False)
    addiaroot.config(bg="#15648e")
    addiaroot.iconbitmap("stu.ico")
    addiaroot.title("STUDENT DATABASE MANAGEMENT SYSTEM")
    usnlabel=Label(addiaroot,text="Enter USN : ",bg="white",font=("times",18),width=12,bd=2,anchor="w")
    usnlabel.place(x=10,y=10)

    subcodelabel=Label(addiaroot,text="Enter Subcode : ",bg="white",font=("times",18),width=12,bd=2,anchor="w")
    subcodelabel.place(x=10,y=80)

    test1label=Label(addiaroot,text="Enter Test1 : ",bg="white",font=("times",18),width=12,bd=2,anchor="w")
    test1label.place(x=10,y=150)

    test2label=Label(addiaroot,text="Enter Test2 : ",bg="white",font=("times",18),width=12,bd=2,anchor="w")
    test2label.place(x=10,y=220)

    test3label=Label(addiaroot,text="Enter Test3 : ",bg="white",font=("times",18),width=12,bd=2,anchor="w")
    test3label.place(x=10,y=290)

    #finalialabel=Label(addiaroot,text="Enter FinalIA : ",bg="white",font=("times",18),width=12,bd=2,anchor="w")
    #finalialabel.place(x=10,y=360)
    ########################################
    usnvar2 = StringVar()
    subcodevar2 = StringVar()
    testvar1 = StringVar()
    testvar2 = StringVar()
    testvar3 = StringVar()
    finaliavar = StringVar()
    usnentry = Entry(addiaroot,font=('Times',14,'bold'),bd=3,textvariable=usnvar2)
    usnentry.place(x=180,y=10,width=200,height=35)

    subcodeentry = Entry(addiaroot,font=('Times',14,'bold'),bd=3,textvariable=subcodevar2)
    subcodeentry.place(x=180,y=80,width=200,height=35)

    test1entry = Entry(addiaroot,font=('Times',14,'bold'),bd=3,textvariable=testvar1)
    test1entry.place(x=180,y=150,width=200,height=35)

    test2entry = Entry(addiaroot,font=('Times',14,'bold'),bd=3,textvariable=testvar2)
    test2entry.place(x=180,y=220,width=200,height=35)

    test3entry = Entry(addiaroot,font=('Times',14,'bold'),bd=3,textvariable=testvar3)
    test3entry.place(x=180,y=290,width=200,height=35)

    #finaliaentry = Entry(addiaroot,font=('Times',14,'bold'),bd=3,textvariable=finaliavar)
    #finaliaentry.place(x=180,y=360,width=200,height=35)

    submitbtn = Button(addiaroot,text="Submit",font=('Times',14,'bold'),bd=3,width=15,bg="sky blue2",activebackground='royal blue3',
                     activeforeground='white',command=submitaddia)
    submitbtn.place(x=100,y=500)

    addiaroot.mainloop()
        



###########-------------CLASS AND SEMSEC ACTION---------
"""def deleteclass():
    cc = classsemtable.focus()
    content = classsemtable.item(cc)
    pp = content['values'][0]
    strr = 'delete from SEMSEC where SSID=%s'
    mycursor.execute(strr,(pp))
    con.commit()
    messagebox.showinfo('Notifications','SSID {} deleted sucessfully...'.format(pp))
    strr = 'SELECT DISTINCT(SE.SSID),S.USN,S.NAME,SE.SEM,SE.SEC,SE.PROCTOR FROM STUDENTGENINFO AS S,SEMSEC AS SE,CLASS AS C WHERE S.USN=C.USN AND SE.SSID=C.SSID'
    mycursor.execute(strr)
    datas = mycursor.fetchall()
    classsemtable.delete(*classsemtable.get_children())
    for i in datas:
        vv = [i[0],i[1],i[2],i[3],i[4],i[5]]
        classsemtable.insert('',END,values=vv)"""


def updateclass():
    def submitclassupdate():
        usn = usnvar.get()
        name = namevar.get()
        ssid = ssidvar.get()
        sem = semvar.get()
        sec = secvar.get()
        proctor = proctorvar.get()

        strr = 'update semsec set sem=%s,sec=%s,proctor=%s where ssid=%s'
        mycursor.execute(strr,(sem,sec,proctor,ssid))
        con.commit()
        messagebox.showinfo('Notifications','Id {} Modified sucessfully...'.format(ssid),parent=classupdateroot)
        strr = 'SELECT DISTINCT(SE.SSID),S.USN,S.NAME,SE.SEM,SE.SEC,SE.PROCTOR FROM STUDENTGENINFO AS S,SEMSEC AS SE,CLASS AS C WHERE S.USN=C.USN AND SE.SSID=C.SSID'
        mycursor.execute(strr)
        datas = mycursor.fetchall()
        classsemtable.delete(*classsemtable.get_children())
        for i in datas:
            vv = [i[0],i[1],i[2],i[3],i[4],i[5]]
            classsemtable.insert('',END,values=vv)

    classupdateroot = Toplevel(master=classroot)
    classupdateroot.grab_set()
    classupdateroot.geometry('450x550+2+150')
    classupdateroot.resizable(False,False)
    classupdateroot.config(bg="#15648e")
    classupdateroot.iconbitmap("stu.ico")
    classupdateroot.title("Update class Details")
    ssidlabel = Label(classupdateroot,text="Enter SSID : ",bg="white",font=("times",18),width=16,bd=2,anchor="w")
    ssidlabel.place(x=10,y=10)

    usnlabel = Label(classupdateroot,text="Enter USN : ",bg="white",font=("times",18),width=16,bd=2,anchor="w")
    usnlabel.place(x=10,y=80)

    namelabel = Label(classupdateroot,text="Enter NAME : ",bg="white",font=("times",18),width=16,bd=2,anchor="w")
    namelabel.place(x=10,y=150)

    semlabel = Label(classupdateroot,text="Enter SEMESTER : ",bg="white",font=("times",18),width=16,bd=2,anchor="w")
    semlabel.place(x=10,y=220)

    seclabel = Label(classupdateroot,text="Select SECTION : ",bg="white",font=("times",18),width=16,bd=2,anchor="w")
    seclabel.place(x=10,y=290)

    proctorlabel = Label(classupdateroot,text="Enter PROCTOR : ",bg="white",font=("times",18),width=16,bd=2,anchor="w")
    proctorlabel.place(x=10,y=360)

    ########################################
    usnvar = StringVar()
    namevar = StringVar()
    ssidvar = StringVar()
    semvar = StringVar()
    secvar = StringVar()
    proctorvar = StringVar()

    ssidentry = Entry(classupdateroot,font=('Times',14,'bold'),bg='gray73',bd=3,textvariable=ssidvar)
    ssidentry.place(x=230,y=10,width=205,height=35)

    usnentry = Entry(classupdateroot,font=('Times',14,'bold'),bg='gray73',bd=3,textvariable=usnvar)
    usnentry.place(x=230,y=80,width=205,height=35)

    nameentry = Entry(classupdateroot,font=('Times',14,'bold'),bg='gray73',bd=3,textvariable=namevar)
    nameentry.place(x=230,y=150,width=205,height=35)

    sementry = Entry(classupdateroot,font=('Times',14,'bold'),bg='gray73',bd=3,textvariable=semvar)
    sementry.place(x=230,y=220,width=205,height=35)

    secentry = Entry(classupdateroot,font=('Times',14,'bold'),bg='gray73',bd=3,textvariable=secvar)
    secentry.place(x=230,y=290,width=205,height=35)

    proctorentry = Entry(classupdateroot,font=('Times',14,'bold'),bg='gray73',bd=3,textvariable=proctorvar)
    proctorentry.place(x=230,y=360,width=205,height=35)

    submitbtn = Button(classupdateroot,text="Submit",font=('Times',14,'bold'),bd=3,width=15,bg="sky blue2",
                       activebackground='royal blue3',
                       activeforeground='white',command=submitclassupdate,cursor='hand2')
    submitbtn.place(x=135,y=450)


    #submitbtn.place(x=135,y=620)
    cc = classsemtable.focus()
    content = classsemtable.item(cc)
    pp = content['values']
    if (len(pp) != 0):
        ssidvar.set(pp[0])
        usnvar.set(pp[1])
        namevar.set(pp[2])
        semvar.set(pp[3])
        secvar.set(pp[4])
        proctorvar.set(pp[5])

    classupdateroot.mainloop()


def showclass():
    strr = 'SELECT DISTINCT(SE.SSID),S.USN,S.NAME,SE.SEM,SE.SEC,SE.PROCTOR FROM STUDENTGENINFO AS S,SEMSEC AS SE,CLASS AS C WHERE S.USN=C.USN AND SE.SSID=C.SSID'
    mycursor.execute(strr)
    datas = mycursor.fetchall()
    classsemtable.delete(*classsemtable.get_children())
    for i in datas:
        vv = [i[0],i[1],i[2],i[3],i[4],i[5]]
        classsemtable.insert('',END,values=vv)

def searchclass():
    def submitclasssearch():
        usn = usnvar.get()
        name = namevar.get()
        ssid = ssidvar.get()
        sem = semvar.get()
        sec = secvar.get()
        proctor = proctorvar.get()
        if (usn != ''):
            strr = 'SELECT SE.SSID,S.USN,S.NAME,SE.SEM,SE.SEC,SE.PROCTOR FROM STUDENTGENINFO AS S,SEMSEC AS SE,CLASS AS C WHERE S.USN=C.USN AND SE.SSID=C.SSID AND C.USN=%s'
            mycursor.execute(strr,(usn))
            datas = mycursor.fetchall()
            classsemtable.delete(*classsemtable.get_children())
            for i in datas:
                vv = [i[0],i[1],i[2],i[3],i[4],i[5]]
                classsemtable.insert('',END,values=vv)
        elif (name != ''):
            strr = 'SELECT SE.SSID,S.USN,S.NAME,SE.SEM,SE.SEC,SE.PROCTOR FROM STUDENTGENINFO AS S,SEMSEC AS SE,CLASS AS C WHERE S.USN=C.USN AND SE.SSID=C.SSID AND S.NAME=%s;'
            mycursor.execute(strr,(name))
            datas = mycursor.fetchall()
            classsemtable.delete(*classsemtable.get_children())
            for i in datas:
                vv = [i[0],i[1],i[2],i[3],i[4],i[5]]
                classsemtable.insert('',END,values=vv)
        elif (ssid != ''):
            strr = 'SELECT SE.SSID,S.USN,S.NAME,SE.SEM,SE.SEC,SE.PROCTOR FROM STUDENTGENINFO AS S,SEMSEC AS SE,CLASS AS C WHERE S.USN=C.USN AND SE.SSID=C.SSID AND SE.SSID=%s;'
            mycursor.execute(strr,(ssid))
            datas = mycursor.fetchall()
            classsemtable.delete(*classsemtable.get_children())
            for i in datas:
                vv = [i[0],i[1],i[2],i[3],i[4],i[5]]
                classsemtable.insert('',END,values=vv)

        elif (sem != ''):
            strr = 'SELECT SE.SSID,S.USN,S.NAME,SE.SEM,SE.SEC,SE.PROCTOR FROM STUDENTGENINFO AS S,SEMSEC AS SE,CLASS AS C WHERE S.USN=C.USN AND SE.SSID=C.SSID AND SE.SEM=%s'
            mycursor.execute(strr,(sem))
            datas = mycursor.fetchall()
            classsemtable.delete(*classsemtable.get_children())
            for i in datas:
                vv = [i[0],i[1],i[2],i[3],i[4],i[5]]
                classsemtable.insert('',END,values=vv)

        elif (sec != ''):
            strr = 'SELECT SE.SSID,S.USN,S.NAME,SE.SEM,SE.SEC,SE.PROCTOR FROM STUDENTGENINFO AS S,SEMSEC AS SE,CLASS AS C WHERE S.USN=C.USN AND SE.SSID=C.SSID AND SE.SEC=%s'
            mycursor.execute(strr,(sec))
            datas = mycursor.fetchall()
            classsemtable.delete(*classsemtable.get_children())
            for i in datas:
                vv = [i[0],i[1],i[2],i[3],i[4],i[5]]
                classsemtable.insert('',END,values=vv)


        elif (proctor != ''):
            strr = 'SELECT SE.SSID,S.USN,S.NAME,SE.SEM,SE.SEC,SE.PROCTOR FROM STUDENTGENINFO AS S,SEMSEC AS SE,CLASS AS C WHERE S.USN=C.USN AND SE.SSID=C.SSID AND SE.PROCTOR=%s'
            mycursor.execute(strr,(proctor))
            datas = mycursor.fetchall()
            classsemtable.delete(*classsemtable.get_children())
            for i in datas:
                vv = [i[0],i[1],i[2],i[3],i[4],i[5]]
                classsemtable.insert('',END,values=vv)

    searchroot = Toplevel(master=classroot)
    searchroot.grab_set()
    searchroot.geometry('450x550+2+150')
    searchroot.resizable(False,False)
    searchroot.config(bg="#15648e")
    searchroot.iconbitmap("stu.ico")
    searchroot.title("Search class Details")
    usnlabel = Label(searchroot,text="Enter USN : ",bg="white",font=("times",18),width=16,bd=2,anchor="w")
    usnlabel.place(x=10,y=10)

    namelabel = Label(searchroot,text="Enter Name : ",bg="white",font=("times",18),width=16,bd=2,anchor="w")
    namelabel.place(x=10,y=80)

    ssidlabel = Label(searchroot,text="Enter SSID : ",bg="white",font=("times",18),width=16,bd=2,anchor="w")
    ssidlabel.place(x=10,y=150)

    semlabel = Label(searchroot,text="Enter Sem : ",bg="white",font=("times",18),width=16,bd=2,anchor="w")
    semlabel.place(x=10,y=220)

    seclabel = Label(searchroot,text="Select Sec : ",bg="white",font=("times",18),width=16,bd=2,anchor="w")
    seclabel.place(x=10,y=290)

    proctorlabel = Label(searchroot,text="Enter Proctor : ",bg="white",font=("times",18),width=16,bd=2,anchor="w")
    proctorlabel.place(x=10,y=360)

    ########################################
    usnvar = StringVar()
    namevar = StringVar()
    ssidvar = StringVar()
    semvar = StringVar()
    secvar = StringVar()
    proctorvar = StringVar()

    usnentry = Entry(searchroot,font=('Times',14,'bold'),bg='gray73',bd=3,textvariable=usnvar)
    usnentry.place(x=230,y=10,width=205,height=35)

    nameentry = Entry(searchroot,font=('Times',14,'bold'),bg='gray73',bd=3,textvariable=namevar)
    nameentry.place(x=230,y=80,width=205,height=35)

    ssidentry = Entry(searchroot,font=('Times',14,'bold'),bg='gray73',bd=3,textvariable=ssidvar)
    ssidentry.place(x=230,y=150,width=205,height=35)

    sementry = Entry(searchroot,font=('Times',14,'bold'),bg='gray73',bd=3,textvariable=semvar)
    sementry.place(x=230,y=220,width=205,height=35)

    secentry = Entry(searchroot,font=('Times',14,'bold'),bg='gray73',bd=3,textvariable=secvar)
    secentry.place(x=230,y=290,width=205,height=35)

    #genderentry1 = Radiobutton(searchroot,text="MALE",font=('Times',14,'bold'),bg='#15648e',variable=gendervar,
      #                         value='MALE',activebackground='#15648e'
                           #    )
    #genderentry1.place(x=230,y=290)

    #genderentry2 = Radiobutton(searchroot,text='FEMALE',font=('Times',14,'bold'),bg='#15648e',variable=gendervar,
     #                          value='FEMALE',activebackground='#15648e'
                          #     )
    #genderentry2.place(x=310,y=290)

    proctorentry = Entry(searchroot,font=('Times',14,'bold'),bg='gray73',bd=3,textvariable=proctorvar)
    proctorentry.place(x=230,y=360,width=205,height=35)


    submitbtn=Button(searchroot,text="Submit",font=('Times',14,'bold'),bd=3,width=15,bg="sky blue2",activebackground='royal blue3',
                     activeforeground='white',command=submitclasssearch,cursor='hand2')
    submitbtn.place(x=135,y=450)

    searchroot.mainloop()
#######-------------STUDENT DETAILS ACTION--------------
"""def addstudent():
    def submitadd():
        usn = usnvar.get()
        name = namevar.get()
        address = addressvar.get()
        mobile = mobilevar.get()
        gender = gendervar.get()
        email = emailvar.get()
        dob = dobvar.get()
        parent_name = parnamvar.get()
        parent_num = parnumvar.get()
        addedtime = time.strftime("%H:%M:%S")
        addeddate = time.strftime("%d/%m/%Y")
        try:
            strr = 'insert into studentgeninfo values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            mycursor.execute(strr,(usn,name,address,mobile,gender,email,dob,parent_name,parent_num,addeddate,addedtime))
            strr = 'insert into CLASS values(%s,%s)'
            mycursor.execute(strr,('1MJ18IS001','1234'))
            con.commit()
            res = messagebox.askyesnocancel('Notificatrions','usn {} Name {} Added sucessfully.. and want to clean the form'.format(usn, name),parent=addroot)
            if (res == True):
                usnvar.set('')
                namevar.set('')
                addressvar.set('')
                mobilevar.set('')
                gendervar.set('')
                emailvar.set('')
                dobvar.set('')
                parnamvar.set('')
                parnumvar.set('')
        except:
            messagebox.showerror('Notifications','usn Already Exist try another usn...',parent=addroot)
        strr = 'select * from studentgeninfo'
        mycursor.execute(strr)
        datas = mycursor.fetchall()
        studenttable.delete(*studenttable.get_children())
        for i in datas:
            vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10]]
            studenttable.insert('',END,values=vv)
    addroot = Toplevel(master=studroot)
    addroot.grab_set()
    addroot.geometry('450x690+2+90')
    addroot.resizable(False,False)
    addroot.config(bg="#15648e")
    addroot.iconbitmap("stu.ico")
    addroot.title("Add Student Details")
    usnlabel=Label(addroot,text="Enter USN : ",bg="white",font=("times",18),width=16,bd=2,anchor="w")
    usnlabel.place(x=10,y=10)

    namelabel=Label(addroot,text="Enter Name : ",bg="white",font=("times",18),width=16,bd=2,anchor="w")
    namelabel.place(x=10,y=80)

    addresslabel = Label(addroot,text="Enter Address : ",bg="white",font=("times",18),width=16,bd=2,anchor="w")
    addresslabel.place(x=10,y=150)

    mobilelabel=Label(addroot,text="Enter Mobile : ",bg="white",font=("times",18),width=16,bd=2,anchor="w")
    mobilelabel.place(x=10,y=220)

    genderlabel = Label(addroot,text="Select Gender : ",bg="white",font=("times",18),width=16,bd=2,anchor="w")
    genderlabel.place(x=10,y=290)

    emaillabel=Label(addroot,text="Enter Email : ",bg="white",font=("times",18),width=16,bd=2,anchor="w")
    emaillabel.place(x=10,y=360)

    doblabel=Label(addroot,text="Enter D.O.B : ",bg="white",font=("times",18),width=16,bd=2,anchor="w")
    doblabel.place(x=10,y=430)

    parent_namelabel = Label(addroot,text="Enter Parent Name  : ",bg="white",font=("times",18),width=16,bd=2,anchor="w")
    parent_namelabel.place(x=10,y=500)

    parent_numlabel = Label(addroot,text="Enter Parent No : ",bg="white",font=("times",18),width=16,bd=2,anchor="w")
    parent_numlabel.place(x=10,y=570)

    ########################################
    usnvar=StringVar()
    namevar = StringVar()
    mobilevar = StringVar()
    addressvar = StringVar()
    emailvar = StringVar()
    gendervar = StringVar()
    dobvar = StringVar()
    parnamvar = StringVar()
    parnumvar = StringVar()

    usnentry = Entry(addroot,font=('Times',14,'bold'),bg='gray73',bd=3,textvariable=usnvar)
    usnentry.place(x=230,y=10,width=205,height=35)

    nameentry = Entry(addroot,font=('Times',14,'bold'),bg='gray73',bd=3,textvariable=namevar)
    nameentry.place(x=230,y=80,width=205,height=35)

    addressentry = Entry(addroot,font=('Times',14,'bold'),bg='gray73',bd=3,textvariable=addressvar)
    addressentry.place(x=230,y=150,width=205,height=35)

    mobileentry = Entry(addroot,font=('Times',14,'bold'),bg='gray73',bd=3,textvariable=mobilevar)
    mobileentry.place(x=230,y=220,width=205,height=35)

    #genderentry = Entry(addroot,font=('Times',14,'bold'),bg='gray73',bd=3,textvariable=gendervar)
    #genderentry.place(x=230,y=290,width=205,height=35)
    genderentry1= Radiobutton(addroot,text="MALE",font=('Times',14,'bold'),bg='#15648e',variable=gendervar,value='MALE',activebackground='#15648e'
                     )
    genderentry1.place(x=230,y=290)

    genderentry2 = Radiobutton(addroot,text='FEMALE',font=('Times',14,'bold'),bg='#15648e',variable=gendervar,value='FEMALE',activebackground='#15648e'
                     )
    genderentry2.place(x=310,y=290)

    emailentry = Entry(addroot,font=('Times',14,'bold'),bg='gray73',bd=3,textvariable=emailvar)
    emailentry.place(x=230,y=360,width=205,height=35)

    dobentry = Entry(addroot,font=('Times',14,'bold'),bg='gray73',bd=3,textvariable=dobvar)
    dobentry.place(x=230,y=430,width=205,height=35)

    parent_nameentry = Entry(addroot,font=('Times',14,'bold'),bg='gray73',bd=3,textvariable=parnamvar)
    parent_nameentry.place(x=230,y=500,width=205,height=35)

    parent_numentry = Entry(addroot,font=('Times',14,'bold'),bg='gray73',bd=3,textvariable=parnumvar)
    parent_numentry.place(x=230,y=570,width=205,height=35)

    submitbtn=Button(addroot,text="Submit",font=('Times',14,'bold'),bd=3,width=15,bg="sky blue2",activebackground='royal blue3',
                     activeforeground='white',command=submitadd,cursor='hand2')
    submitbtn.place(x=135,y=640)

    addroot.mainloop()

"""
def updatestudent():
    def submitupdate():
        usn = usnvar.get()
        name = namevar.get()
        address = addressvar.get()
        mobile = mobilevar.get()
        gender = gendervar.get()
        email = emailvar.get()
        dob = dobvar.get()
        parent_name = parnamvar.get()
        parent_num = parnumvar.get()
        #addedtime = time.strftime("%H:%M:%S")
        #addeddate = time.strftime("%d/%m/%Y")

        strr = 'update studentgeninfo set name=%s,address=%s,mobile=%s,gender=%s,email=%s,dob=%s,parent_name=%s,parent_no=%s where usn=%s'
        mycursor.execute(strr,(name,address,mobile,gender,email,dob,parent_name,parent_num,usn))
        con.commit()
        messagebox.showinfo('Notifications','Id {} Modified sucessfully...'.format(usn),parent=updateroot)
        strr = 'select *from studentgeninfo'
        mycursor.execute(strr)
        datas = mycursor.fetchall()
        studenttable.delete(*studenttable.get_children())
        for i in datas:
            vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10]]
            studenttable.insert('',END,values=vv)

    updateroot=Toplevel(master=studroot)
    updateroot.grab_set()
    updateroot.geometry('450x690+2+90')
    updateroot.resizable(False,False)
    updateroot.config(bg="#15648e")
    updateroot.iconbitmap("stu.ico")
    updateroot.title("Update Student Details")
    usnlabel=Label(updateroot,text="Update USN : ",bg="white",font=("times",18),width=16,bd=2,anchor="w")
    usnlabel.place(x=10,y=10)

    namelabel = Label(updateroot,text="Update Name : ",bg="white",font=("times",18),width=16,bd=2,anchor="w")
    namelabel.place(x=10,y=80)

    addresslabel = Label(updateroot,text="Update Address : ",bg="white",font=("times",18),width=16,bd=2,anchor="w")
    addresslabel.place(x=10,y=150)

    mobilelabel = Label(updateroot,text="Update Mobile : ",bg="white",font=("times",18),width=16,bd=2,anchor="w")
    mobilelabel.place(x=10,y=220)

    genderlabel = Label(updateroot,text="Update Gender : ",bg="white",font=("times",18),width=16,bd=2,anchor="w")
    genderlabel.place(x=10,y=290)

    emaillabel = Label(updateroot,text="Update Email : ",bg="white",font=("times",18),width=16,bd=2,anchor="w")
    emaillabel.place(x=10,y=360)

    doblabel = Label(updateroot,text="Update D.O.B : ",bg="white",font=("times",18),width=16,bd=2,anchor="w")
    doblabel.place(x=10,y=430)

    parent_namelabel = Label(updateroot,text="Update Parent Name  : ",bg="white",font=("times",18),width=16,bd=2,anchor="w")
    parent_namelabel.place(x=10,y=500)

    parent_numlabel = Label(updateroot,text="Update Parent No : ",bg="white",font=("times",18),width=16,bd=2,anchor="w")
    parent_numlabel.place(x=10,y=570)

    ########################################
    usnvar = StringVar()
    namevar = StringVar()
    mobilevar = StringVar()
    addressvar = StringVar()
    emailvar = StringVar()
    gendervar = StringVar()
    dobvar = StringVar()
    parnamvar = StringVar()
    parnumvar = StringVar()

    usnentry = Entry(updateroot,font=('Times',14,'bold'),bg='gray73',bd=3,textvariable=usnvar)
    usnentry.place(x=230,y=10,width=205,height=35)

    nameentry = Entry(updateroot,font=('Times',14,'bold'),bg='gray73',bd=3,textvariable=namevar)
    nameentry.place(x=230,y=80,width=205,height=35)

    addressentry = Entry(updateroot,font=('Times',14,'bold'),bg='gray73',bd=3,textvariable=addressvar)
    addressentry.place(x=230,y=150,width=205,height=35)

    mobileentry = Entry(updateroot,font=('Times',14,'bold'),bg='gray73',bd=3,textvariable=mobilevar)
    mobileentry.place(x=230,y=220,width=205,height=35)

    #genderentry = Entry(updateroot,font=('Times',14,'bold'),bg='gray73',bd=3,textvariable=gendervar)
    #genderentry.place(x=230,y=290,width=205,height=35)

    genderentry1 = Radiobutton(updateroot,text="MALE",font=('Times',14,'bold'),bg='#15648e',variable=gendervar,
                               value='MALE',activebackground='#15648e'
                               )
    genderentry1.place(x=230,y=290)

    genderentry2 = Radiobutton(updateroot,text='FEMALE',font=('Times',14,'bold'),bg='#15648e',variable=gendervar,
                               value='FEMALE',activebackground='#15648e'
                               )
    genderentry2.place(x=310,y=290)

    emailentry = Entry(updateroot,font=('Times',14,'bold'),bg='gray73',bd=3,textvariable=emailvar)
    emailentry.place(x=230,y=360,width=205,height=35)

    dobentry = Entry(updateroot,font=('Times',14,'bold'),bg='gray73',bd=3,textvariable=dobvar)
    dobentry.place(x=230,y=430,width=205,height=35)

    parent_nameentry = Entry(updateroot,font=('Times',14,'bold'),bg='gray73',bd=3,textvariable=parnamvar)
    parent_nameentry.place(x=230,y=500,width=205,height=35)

    parent_numentry = Entry(updateroot,font=('Times',14,'bold'),bg='gray73',bd=3,textvariable=parnumvar)
    parent_numentry.place(x=230,y=570,width=205,height=35)

    submitbtn=Button(updateroot,text="Submit",font=('Times',14,'bold'),bd=3,width=15,bg="sky blue2",activebackground='royal blue3',
                     activeforeground='white',command=submitupdate,cursor='hand2')
    submitbtn.place(x=135,y=620)
    cc = studenttable.focus()
    content = studenttable.item(cc)
    pp = content['values']
    if (len(pp) != 0):
        usnvar.set(pp[0])
        namevar.set(pp[1])
        addressvar.set(pp[2])
        mobilevar.set(pp[3])
        gendervar.set(pp[4])
        emailvar.set(pp[5])
        dobvar.set(pp[6])
        parnamvar.set(pp[7])
        parnumvar.set(pp[8])

    updateroot.mainloop()

def showstudent():
    strr = 'select *from studentgeninfo'
    mycursor.execute(strr)
    datas = mycursor.fetchall()
    studenttable.delete(*studenttable.get_children())
    for i in datas:
        vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10]]
        studenttable.insert('',END,values=vv)

def deletestudent():
    cc = studenttable.focus()
    content = studenttable.item(cc)
    pp = content['values'][0]
    strr = 'delete from studentgeninfo where usn=%s'
    mycursor.execute(strr,(pp))
    con.commit()
    messagebox.showinfo('Notifications','Id {} deleted sucessfully...'.format(pp))
    strr = 'select *from studentgeninfo'
    mycursor.execute(strr)
    datas = mycursor.fetchall()
    studenttable.delete(*studenttable.get_children())
    for i in datas:
        vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10]]
        studenttable.insert('',END,values=vv)

def searchstudent():
    def submitsearch():
        usn = usnvar.get()
        name = namevar.get()
        address = addressvar.get()
        mobile = mobilevar.get()
        gender = gendervar.get()
        email = emailvar.get()
        dob = dobvar.get()
        parent_name = parnamvar.get()
        parent_num = parnumvar.get()
        addeddate = datevar.get()
        if (usn != ''):
            strr = 'select *from studentgeninfo where usn=%s'
            mycursor.execute(strr,(usn))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10]]
                studenttable.insert('',END,values=vv)
        elif (name != ''):
            strr = 'select *from studentgeninfo where name=%s'
            mycursor.execute(strr,(name))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10]]
                studenttable.insert('',END,values=vv)
        elif (address != ''):
            strr = 'select *from studentgeninfo where address=%s'
            mycursor.execute(strr,(address))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10]]
                studenttable.insert('',END,values=vv)

        elif (mobile != ''):
            strr = 'select *from studentgeninfo where mobile=%s'
            mycursor.execute(strr,(mobile))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10]]
                studenttable.insert('',END,values=vv)

        elif (gender != ''):
            strr = 'select *from studentgeninfo where gender=%s'
            mycursor.execute(strr,(gender))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10]]
                studenttable.insert('',END,values=vv)


        elif (email != ''):
            strr = 'select *from studentgeninfo where email=%s'
            mycursor.execute(strr,(email))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10]]
                studenttable.insert('',END,values=vv)


        elif (dob != ''):
            strr = 'select *from studentgeninfo where dob=%s'
            mycursor.execute(strr,(dob))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10]]
                studenttable.insert('',END,values=vv)

        elif (parent_name != ''):
            strr = 'select *from studentgeninfo where parent_name=%s'
            mycursor.execute(strr,(parent_name))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10]]
                studenttable.insert('',END,values=vv)

        elif (parent_num != ''):
            strr = 'select *from studentgeninfo where parent_no=%s'
            mycursor.execute(strr,(parent_num))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10]]
                studenttable.insert('',END,values=vv)

        elif (addeddate != ''):
            strr = 'select *from studentgeninfo where date=%s'
            mycursor.execute(strr,(addeddate))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10]]
                studenttable.insert('',END,values=vv)

    searchroot = Toplevel(master=studroot)
    searchroot.grab_set()
    searchroot.geometry('450x750+2+70')
    searchroot.resizable(False,False)
    searchroot.config(bg="#15648e")
    searchroot.iconbitmap("stu.ico")
    searchroot.title("Search Student Details")
    usnlabel = Label(searchroot,text="Enter USN : ",bg="white",font=("times",18),width=16,bd=2,anchor="w")
    usnlabel.place(x=10,y=10)

    namelabel = Label(searchroot,text="Enter Name : ",bg="white",font=("times",18),width=16,bd=2,anchor="w")
    namelabel.place(x=10,y=80)

    addresslabel = Label(searchroot,text="Enter Address : ",bg="white",font=("times",18),width=16,bd=2,anchor="w")
    addresslabel.place(x=10,y=150)

    mobilelabel = Label(searchroot,text="Enter Mobile : ",bg="white",font=("times",18),width=16,bd=2,anchor="w")
    mobilelabel.place(x=10,y=220)

    genderlabel = Label(searchroot,text="Select Gender : ",bg="white",font=("times",18),width=16,bd=2,anchor="w")
    genderlabel.place(x=10,y=290)

    emaillabel = Label(searchroot,text="Enter Email : ",bg="white",font=("times",18),width=16,bd=2,anchor="w")
    emaillabel.place(x=10,y=360)

    doblabel = Label(searchroot,text="Enter D.O.B : ",bg="white",font=("times",18),width=16,bd=2,anchor="w")
    doblabel.place(x=10,y=430)

    parent_namelabel = Label(searchroot,text="Enter Parent Name  : ",bg="white",font=("times",18),width=16,bd=2,anchor="w")
    parent_namelabel.place(x=10,y=500)

    parent_numlabel = Label(searchroot,text="Enter Parent No : ",bg="white",font=("times",18),width=16,bd=2,anchor="w")
    parent_numlabel.place(x=10,y=570)

    datelabel = Label(searchroot,text="Enter Date : ",bg="white",font=("times",18),width=16,bd=2,anchor="w")
    datelabel.place(x=10,y=640)
    ########################################
    usnvar = StringVar()
    namevar = StringVar()
    mobilevar = StringVar()
    addressvar = StringVar()
    emailvar = StringVar()
    gendervar = StringVar()
    dobvar = StringVar()
    parnamvar = StringVar()
    parnumvar = StringVar()
    datevar = StringVar()

    usnentry = Entry(searchroot,font=('Times',14,'bold'),bg='gray73',bd=3,textvariable=usnvar)
    usnentry.place(x=230,y=10,width=205,height=35)

    nameentry = Entry(searchroot,font=('Times',14,'bold'),bg='gray73',bd=3,textvariable=namevar)
    nameentry.place(x=230,y=80,width=205,height=35)

    addressentry = Entry(searchroot,font=('Times',14,'bold'),bg='gray73',bd=3,textvariable=addressvar)
    addressentry.place(x=230,y=150,width=205,height=35)

    mobileentry = Entry(searchroot,font=('Times',14,'bold'),bg='gray73',bd=3,textvariable=mobilevar)
    mobileentry.place(x=230,y=220,width=205,height=35)

    #genderentry = Entry(searchroot,font=('Times',14,'bold'),bg='gray73',bd=3,textvariable=gendervar)
    #genderentry.place(x=230,y=290,width=205,height=35)

    genderentry1 = Radiobutton(searchroot,text="MALE",font=('Times',14,'bold'),bg='#15648e',variable=gendervar,
                               value='MALE',activebackground='#15648e'
                               )
    genderentry1.place(x=230,y=290)

    genderentry2 = Radiobutton(searchroot,text='FEMALE',font=('Times',14,'bold'),bg='#15648e',variable=gendervar,
                               value='FEMALE',activebackground='#15648e'
                               )
    genderentry2.place(x=310,y=290)

    emailentry = Entry(searchroot,font=('Times',14,'bold'),bg='gray73',bd=3,textvariable=emailvar)
    emailentry.place(x=230,y=360,width=205,height=35)

    dobentry = Entry(searchroot,font=('Times',14,'bold'),bg='gray73',bd=3,textvariable=dobvar)
    dobentry.place(x=230,y=430,width=205,height=35)

    parent_nameentry = Entry(searchroot,font=('Times',14,'bold'),bg='gray73',bd=3,textvariable=parnamvar)
    parent_nameentry.place(x=230,y=500,width=205,height=35)

    parent_numentry = Entry(searchroot,font=('Times',14,'bold'),bg='gray73',bd=3,textvariable=parnumvar)
    parent_numentry.place(x=230,y=570,width=205,height=35)

    dateentry = Entry(searchroot,font=('Times',14,'bold'),bg='gray73',bd=3,textvariable=datevar)
    dateentry.place(x=230,y=640,width=205,height=35)

    submitbtn=Button(searchroot,text="Submit",font=('Times',14,'bold'),bd=3,width=15,bg="sky blue2",activebackground='royal blue3',
                     activeforeground='white',command=submitsearch,cursor='hand2')
    submitbtn.place(x=135,y=680)

    searchroot.mainloop()


def tm():
    time_string = time.strftime("%H:%M:%S")
    date_string = time.strftime("%d/%m/%Y")
    clock.config(text="Time-" + time_string + "\nDate-" + date_string)
    clock.after(200,tm)


def back_fun1():
    mycursor.close()
    con.close()
    print("disconnected")
    newwind.destroy()
    root.update()
    root.deiconify()

def login_fun( ):

    def student_back():
        studroot.withdraw()
        menu_window()

    def class_back():
        classroot.destroy()
        menu_window()

    def ia_back():
        iaroot.destroy()
        menu_window()

    def attendance_back():
        attroot.destroy()
        menu_window()

    def addmission_back():
        admin.destroy()
        menu_window()

    def subjectregistration_back():
        subreg.destroy()
        menu_window()

    def subjectaddition():
        def submitsubject():
            subcode1 = subcodevar1.get()
            title1 = titlevar1.get()
            sem1 = semvar1.get()
            credits1 = creditsvar1.get()
            try:
                strr = 'insert into SUBJECT values(%s,%s,%s,%s)'
                mycursor.execute(strr,(subcode1,title1,sem1,credits1))
                con.commit()
                res = messagebox.askyesnocancel('Notificatrions',
                                                    'subject code {} sem {} Registered sucessfully.. and want to clean the form'.format(
                                                      subcode1,sem1),parent=subreg)
                if (res == True):
                    subcodevar1.set('')
                    titlevar1.set('')
                    semvar1.set('')
                    creditsvar1.set('')
                        
            except:
                messagebox.showerror('Notifications','Subcode Already Exist try another usn...',parent=subreg)
            #strr = 'select * from studentgeninfo'
            #mycursor.execute(strr)
            #datas = mycursor.fetchall()
            #studenttable.delete(*studenttable.get_children())
            #for i in datas:
            #    vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10]]
            #   studenttable.insert('',END,values=vv)

        def tm():
            time_string = time.strftime("%H:%M:%S")
            date_string = time.strftime("%d/%m/%Y")
            clock.config(text="Time-" + time_string + "\nDate-" + date_string)
            clock.after(200,tm)

        global subreg
        subreg = Toplevel()
            # newwind.attributes('-fullscreen',True)
        w,h = subreg.winfo_screenwidth(),subreg.winfo_screenheight()
        subreg.geometry("%dx%d+0+0" % (w,h))
            # admin.geometry('1199x600+160+80')
        subreg.grab_set()
        subreg.title("Add Subjects")
            # admin.resizable(False,False)
        subreg.iconbitmap("stu.ico")

        screenlabel = Label(subreg,font=("times",25,"bold"),relief=RIDGE,bg="#15648e",bd=0,).place(x=0,y=0,
                                                                                                      relwidth=1,
                                                                                                      relheight=1)

        heading1 = Label(subreg,font=("Helvetica 9 italic",20,"bold"),fg="white",relief=RIDGE,bg="#15648e",bd=0,
                             text="Add Subjects").place(x=350,y=80,width=850,height=60)

        basic_details_frame1 = Frame(subreg,bg='#15648e',borderwidth=0)
        basic_details_frame1.place(x=575,y=165,width=150,height=300)

        basic_details_frame2 = Frame(subreg,bg="#15648e",borderwidth=0)
        basic_details_frame2.place(x=725,y=165,width=250,height=300)

            # -----------------label in frame-----------#
        subcodevar1 = StringVar()
        titlevar1 = StringVar()
        semvar1 = StringVar()
        creditsvar1 = StringVar()
        subcodelabel = Label(basic_details_frame1,text="Subjectcode : ",bg="white",font=("times",16),width=16,bd=2,anchor="w")
        subcodelabel.pack(side=TOP,expand=True)

        subcodeentry = Entry(basic_details_frame2,font=("times",15),bg='lightgray',textvariable=subcodevar1)
        subcodeentry.pack(side=TOP,expand=True)

        titlelabel = Label(basic_details_frame1,text="Title : ",bg="white",font=("times",16),width=16,bd=2,anchor="w")
        titlelabel.pack(side=TOP,expand=True)

        titleentry = Entry(basic_details_frame2,font=("times",15),bg='lightgray',textvariable=titlevar1)
        titleentry.pack(side=TOP,expand=True)

        semlabel = Label(basic_details_frame1,text="Semister : ",bg="white",font=("times",16),width=16,bd=2,
                               anchor="w")
        semlabel.pack(side=TOP,expand=True)

        sementry = Entry(basic_details_frame2,font=("times",15),bg='lightgray',textvariable=semvar1)
        sementry.pack(side=TOP,expand=True)

        creditslabel = Label(basic_details_frame1,text="Credits : ",bg="white",font=("times",16),width=16,bd=2,
                                 anchor="w")
        creditslabel.pack(side=TOP,expand=True)

        creditsentry = Entry(basic_details_frame2,font=("times",15),bg='lightgray',textvariable=creditsvar1)
        creditsentry.pack(side=TOP,expand=True)


        # ---------------------------------------------------------------
        reg_btn = Button(subreg,text="ADD SUBJECT",font=("times",15,"bold"),bg="firebrick1",activebackground="white",
                             bd=3,
                             cursor="hand2",command=submitsubject)
        reg_btn.place(x=700,y=550,width=150,height=50)

        heading1 = Label(subreg,font=("times",25,"bold"),fg="white",relief=RIDGE,bg="#15648e",bd=0,anchor="w",
                             text="STUDENT DATABASE MANAGEMENT SYSTEM").place(x=350,y=0,width=850,height=60)
        clock = Label(subreg,fg='white',bg="firebrick2",font=("Times",10,'bold'),relief=RIDGE)
        clock.place(x=1385,y=0,width=150,height=50)
        tm()

        exit_btn = Button(subreg,image=exit_im,bg="#15648e",activebackground="#15648e",bd=0,
                              cursor="hand2",command=subjectregistration_back)
        exit_btn.place(x=0,y=0,width=45,height=45)
        newwind.withdraw()
        subreg.mainloop()




    def admission():
        def submitadd():
            usn = usnvar.get()
            name = namevar.get()
            address = addressvar.get()
            mobile = mobilevar.get()
            gender = gendervar.get()
            email = emailvar.get()
            dob = dobvar.get()
            parent_name = parnamvar.get()
            parent_num = parnumvar.get()
            addedtime = time.strftime("%H:%M:%S")
            addeddate = time.strftime("%d/%m/%Y")
            ssid = ssidvar.get()
            sem = semvar.get()
            sec = secvar.get()
            proctor = proctorvar.get()

            try:
                strr = 'insert into studentgeninfo values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                mycursor.execute(strr,(usn,name,address,mobile,gender,email,dob,parent_name,parent_num,addeddate,addedtime))
                strr = 'insert into SEMSEC values(%s,%s,%s,%s)'
                mycursor.execute(strr,(ssid,sem,sec,proctor))
                strr = 'insert into CLASS values(%s,%s)'
                mycursor.execute(strr,(usn,ssid))
                #strr = 'insert into subject values(%s,%s,%s,%s)'
                #mycursor.execute(strr,('18CS51','MANAGEMENT AND','5','3'))
                #strr = 'insert into IAMARKS values(%s,%s,%s,%s,%s,%s,%s)'
                #mycursor.execute(strr,('1MJ18IS001','18CS51','1234','00','00','00','00'))
                con.commit()
                res = messagebox.askyesnocancel('Notificatrions',
                                                'usn {} Name {} Registered sucessfully.. and want to clean the form'.format(
                                                    usn,name),parent=admin)
                if (res == True):
                    usnvar.set('')
                    namevar.set('')
                    addressvar.set('')
                    mobilevar.set('')
                    gendervar.set('')
                    emailvar.set('')
                    dobvar.set('')
                    parnamvar.set('')
                    parnumvar.set('')
                    ssidvar.set('')
                    semvar.set('')
                    secvar.set('')
                    proctorvar.set('')
            except:
                messagebox.showerror('Notifications','usn Already Exist try another usn...',parent=admin)
            strr = 'select * from studentgeninfo'
            mycursor.execute(strr)
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10]]
                studenttable.insert('',END,values=vv)



        def tm():
            time_string = time.strftime("%H:%M:%S")
            date_string = time.strftime("%d/%m/%Y")
            clock.config(text="Time-" + time_string + "\nDate-" + date_string)
            clock.after(200,tm)

        global admin
        admin = Toplevel()
        # newwind.attributes('-fullscreen',True)
        w,h = admin.winfo_screenwidth(),admin.winfo_screenheight()
        admin.geometry("%dx%d+0+0" % (w,h))
        # admin.geometry('1199x600+160+80')
        admin.grab_set()
        admin.title("Student registration")
        # admin.resizable(False,False)
        admin.iconbitmap("stu.ico")

        screenlabel = Label(admin,font=("times",25,"bold"),relief=RIDGE,bg="#15648e",bd=0,).place(x=0,y=0,relwidth=1,
                                                                                                  relheight=1)

        heading1 = Label(admin,font=("Helvetica 9 italic",20,"bold"),fg="white",relief=RIDGE,bg="#15648e",bd=0,
                         text="Student Registration").place(x=350,y=80,width=850,height=60)

        heading1 = Label(admin,font=("Helvetica 16 bold italic"),fg="white",relief=RIDGE,bg="#15648e",bd=0,
                         text="1.Student Basic details").place(x=10,y=130,width=250,height=50)

        heading1 = Label(admin,font=("Helvetica 16 bold italic"),fg="white",relief=RIDGE,bg="#15648e",bd=0,anchor="w",
                         text="2.class details").place(x=10,y=450,width=250,height=50)

        #heading1 = Label(admin,font=("Helvetica 16 bold italic"),fg="white",relief=RIDGE,bg="#15648e",bd=0,anchor="w",
         #                text="3.Academics").place(x=1000,y=250,width=250,height=50)

        basic_details_frame1 = Frame(admin,bg='#15648e',borderwidth=0)
        basic_details_frame1.place(x=10,y=165,width=150,height=300)

        basic_details_frame2 = Frame(admin,bg="#15648e",borderwidth=0)
        basic_details_frame2.place(x=150,y=165,width=250,height=300)

        basic_details_frame3 = Frame(admin,bg="#15648e",borderwidth=0)
        basic_details_frame3.place(x=500,y=165,width=150,height=300)

        basic_details_frame4 = Frame(admin,bg="#15648e",borderwidth=0)
        basic_details_frame4.place(x=650,y=165,width=250,height=300)
        # -----------------------------------------------------------#
        basic_details_frame11 = Frame(admin,bg="#15648e",borderwidth=0)
        basic_details_frame11.place(x=10,y=495,width=150,height=150)

        basic_details_frame22 = Frame(admin,bg="#15648e",borderwidth=0)
        basic_details_frame22.place(x=150,y=495,width=250,height=150)

        basic_details_frame33 = Frame(admin,bg="#15648e",borderwidth=0)
        basic_details_frame33.place(x=500,y=495,width=150,height=150)

        basic_details_frame44 = Frame(admin,bg="#15648e",borderwidth=0)
        basic_details_frame44.place(x=650,y=495,width=250,height=150)
        # ------------------------------------------------------------#
        #basic_details_frame15 = Frame(admin,bg="#15648e",borderwidth=0)
        #basic_details_frame15.place(x=170,y=685,width=1300,height=30)
        #basic_details_frame15 = Frame(admin,bg="#15648e",borderwidth=0)
        #basic_details_frame15.place(x=1000,y=340,width=150,height=300)

        #basic_details_frame16 = Frame(admin,bg="#15648e",borderwidth=0)
        #basic_details_frame16.place(x=1200,y=340,width=150,height=300)

        # -----------------label in frame-----------#
        ssidvar = StringVar()
        semvar = StringVar()
        secvar = StringVar()
        proctorvar = StringVar()
        usnvar = StringVar()
        namevar = StringVar()
        mobilevar = StringVar()
        addressvar = StringVar()
        emailvar = StringVar()
        gendervar = StringVar()
        dobvar = StringVar()
        parnamvar = StringVar()
        parnumvar = StringVar()

        namelabel = Label(basic_details_frame1,text="Name : ",bg="white",font=("times",16),width=16,bd=2,anchor="w")
        namelabel.pack(side=TOP,expand=True)

        nameentry = Entry(basic_details_frame2,font=("times",15),bg='lightgray',textvariable=namevar)
        nameentry.pack(side=TOP,expand=True)

        usnlabel = Label(basic_details_frame1,text="USN : ",bg="white",font=("times",16),width=16,bd=2,anchor="w")
        usnlabel.pack(side=TOP,expand=True)

        usnentry = Entry(basic_details_frame2,font=("times",15),bg='lightgray',textvariable=usnvar)
        usnentry.pack(side=TOP,expand=True)

        phonelabel = Label(basic_details_frame1,text="Phone : ",bg="white",font=("times",16),width=16,bd=2,anchor="w")
        phonelabel.pack(side=TOP,expand=True)

        phoneentry = Entry(basic_details_frame2,font=("times",15),bg='lightgray',textvariable=mobilevar)
        phoneentry.pack(side=TOP,expand=True)

        addresslabel = Label(basic_details_frame1,text="address : ",bg="white",font=("times",16),width=16,bd=2,anchor="w")
        addresslabel.pack(side=TOP,expand=True)

        addressentry = Entry(basic_details_frame2,font=("times",15),bg='lightgray',textvariable=addressvar)
        addressentry.pack(side=TOP,expand=True)

        datelabel = Label(basic_details_frame3,text="Date of Birth : ",bg="white",font=("times",16),width=16,bd=2,
                         anchor="w")
        datelabel.pack(side=TOP,expand=True)

        dateentry = Entry(basic_details_frame4,font=("times",15),bg='lightgray',textvariable=dobvar)
        dateentry.pack(side=TOP,expand=True)

        emaillabel = Label(basic_details_frame3,text="Email : ",bg="white",font=("times",16),width=16,bd=2,anchor="w")
        emaillabel.pack(side=TOP,expand=True)

        emailentry = Entry(basic_details_frame4,font=("times",15),bg='lightgray',textvariable=emailvar)
        emailentry.pack(side=TOP,expand=True)

        parentnamelabel = Label(basic_details_frame3,text="Parent Name : ",bg="white",font=("times",16),width=16,bd=2,
                          anchor="w")
        parentnamelabel.pack(side=TOP,expand=True)

        parentnameentry = Entry(basic_details_frame4,font=("times",15),bg='lightgray',textvariable=parnamvar)
        parentnameentry.pack(side=TOP,expand=True)

        parentphonelabel = Label(basic_details_frame3,text="Parent Phone : ",bg="white",font=("times",16),width=16,bd=2,
                         anchor="w")
        parentphonelabel.pack(side=TOP,expand=True)

        parenumentry = Entry(basic_details_frame4,font=("times",15),bg='lightgray',textvariable=parnumvar)
        parenumentry.pack(side=TOP,expand=True)

        genderlabel = Label(admin,text="Gender : ",bg="white",font=("times",16),width=15,bd=2,anchor="w")
        genderlabel.place(x=1000,y=188,width=150)

        genderentry1 = Radiobutton(admin,text="MALE",font=('Times',14,'bold'),bg='#15648e',variable=gendervar,
                                   value='MALE',activebackground='#15648e',
                                   )
        genderentry1.place(x=1170,y=188)

        genderentry2 = Radiobutton(admin,text='FEMALE',font=('Times',14,'bold'),bg='#15648e',variable=gendervar,
                                   value='FEMALE',activebackground='#15648e'
                                   )
        genderentry2.place(x=1270,y=188)
        # --------------------------------------------------#
        ssidlabel = Label(basic_details_frame11,text="SSID : ",bg="white",font=("times",16),width=16,bd=2,anchor="w")
        ssidlabel.pack(side=TOP,expand=True)

        ssidentry = Entry(basic_details_frame22,font=("times",15),bg='lightgray',textvariable=ssidvar)
        ssidentry.pack(side=TOP,expand=True)

        seclabel = Label(basic_details_frame11,text="Section : ",bg="white",font=("times",16),width=16,bd=2,anchor="w")
        seclabel.pack(side=TOP,expand=True)

        secentry = Entry(basic_details_frame22,font=("times",15),bg='lightgray',textvariable=secvar)
        secentry.pack(side=TOP,expand=True)

        semlabel = Label(basic_details_frame33,text="Semester : ",bg="white",font=("times",16),width=16,bd=2,
                          anchor="w")
        semlabel.pack(side=TOP,expand=True)

        sementry = Entry(basic_details_frame44,font=("times",15),bg='lightgray',textvariable=semvar)
        sementry.pack(side=TOP,expand=True)

        proctorlabel = Label(basic_details_frame33,text="Proctor : ",bg="white",font=("times",16),width=16,bd=2,anchor="w")
        proctorlabel.pack(side=TOP,expand=True)

        proctorentry = Entry(basic_details_frame44,font=("times",15),bg='lightgray',textvariable=proctorvar)
        proctorentry.pack(side=TOP,expand=True)

#---------------------------------------------------------------
        reg_btn = Button(admin,text="register",font=("times",15,"bold"),bg="firebrick1",activebackground="white",bd=3,
                         cursor="hand2",command=submitadd)
        reg_btn.place(x=700,y=680,width=150,height=50)

        heading1 = Label(admin,font=("times",25,"bold"),fg="white",relief=RIDGE,bg="#15648e",bd=0,anchor="w",
                         text="STUDENT DATABASE MANAGEMENT SYSTEM").place(x=350,y=0,width=850,height=60)
        clock = Label(admin,fg='white',bg="firebrick2",font=("Times",10,'bold'),relief=RIDGE)
        clock.place(x=1385,y=0,width=150,height=50)
        tm()

        exit_btn = Button(admin,image=exit_im,bg="#15648e",activebackground="#15648e",bd=0,
                          cursor="hand2",command=addmission_back)
        exit_btn.place(x=0,y=0,width=45,height=45)
        newwind.withdraw()
        admin.mainloop()


    def student_details():
        def tm():
            time_string = time.strftime("%H:%M:%S")
            date_string = time.strftime("%d/%m/%Y")
            clock1.config(text="Time-" + time_string + "\nDate-" + date_string)
            clock1.after(200,tm)

        global studroot

        studroot =Toplevel()
        w,h = studroot.winfo_screenwidth(),studroot.winfo_screenheight()
        studroot.geometry("%dx%d+0+0" % (w,h))
        #studroot.focus()
        #studroot.geometry('1199x600+100+50')
        studroot.grab_set()
        studroot.title("student details")
        # studroot.resizable(False,False)
        studroot.iconbitmap("stu.ico")
        screenlabel = Label(studroot,font=("times",25,"bold"),relief=RIDGE,bg="#15648e",bd=0,).place(x=0,y=0,relwidth=1,
                                                                                                    relheight=1)

        heading1 = Label(studroot,font=("times",25,"bold"),fg="white",relief=RIDGE,bg="#15648e",bd=0,
                         text="STUDENT DATABASE MANAGEMENT SYSTEM").place(x=350,y=0,width=850,height=60)

        heading2 = Label(studroot,font=("times",20,"bold",'underline'),fg="yellow",relief=RIDGE,bg="#15648e",bd=0,
                         text="STUDENT GENERAL INFORMATION").place(x=600,y=100,width=750,height=30)

        clock1 = Label(studroot,fg='white',bg="firebrick2",font=("Times",10,'bold'),relief=RIDGE)
        clock1.place(x=1385,y=0,width=150,height=50)
        tm()

        exit_btn = Button(studroot,image=exit_im,bg="#15648e",activebackground="#15648e",bd=0,command=student_back,
                          cursor="hand2")
        exit_btn.place(x=0,y=0,width=45,height=45)

        #------data entry frame--------------

        DataEntryFrame = Frame(studroot,bg="#15648e",borderwidth=0)
        DataEntryFrame.place(x=60,y=130,width=300,height=600)

        datatext = Label(DataEntryFrame,text="Choose Any Option",font=("arial",20,"bold"),bg='#15648e',fg='white')
        datatext.place(x=5,y=20,width=360,height=30)
        datatext.pack(side=TOP,expand=True)

        #addbut = Button(DataEntryFrame,text="ADD STUDENT",font=("times new roman",18),width=25,bd=3,bg='sky blue2',
         #               activebackground='royal blue3',activeforeground='white',command=addstudent,cursor='hand2')
        #addbut.pack(side=TOP,expand=True)

        searchbut = Button(DataEntryFrame,text="SEARCH STUDENT",font=("times new roman",18,),width=25,bd=3,
                           bg='sky blue2',activebackground='royal blue3',activeforeground='white',command=searchstudent,cursor='hand2')
        searchbut.pack(side=TOP,expand=True)

        deletebut = Button(DataEntryFrame,text="DELETE STUDENT",font=("times new roman",18,),width=25,bd=3,
                          bg='sky blue2',activebackground='royal blue3',activeforeground='white',command=deletestudent,cursor='hand2')
        deletebut.pack(side=TOP,expand=True)

        updatebut = Button(DataEntryFrame,text="UPDATE STUDENT",font=("times new roman",18,),width=25,bd=3,
                           bg='sky blue2',activebackground='royal blue3',activeforeground='white',command=updatestudent,cursor='hand2')
        updatebut.pack(side=TOP,expand=True)

        showallbut = Button(DataEntryFrame,text="SHOW ALL",font=("times new roman",18,),width=25,bd=3,bg='sky blue2',
                            activebackground='royal blue3',activeforeground='white',command=showstudent,cursor='hand2')
        showallbut.pack(side=TOP,expand=True)

        #exportbut = Button(DataEntryFrame,text="EXPORT DATA",font=("times new roman",18,),width=25,bd=3,bg='sky blue2',
         #                  activebackground='royal blue3',activeforeground='white',command=exportstudent)
        #exportbut.pack(side=TOP,expand=True)

        #exitbut = Button(DataEntryFrame,text="EXIT",font=("times new roman",18,),width=25,bd=3,bg='sky blue2',
         #                activebackground='royal blue3',activeforeground='white',command=exitstudent)
        #exitbut.pack(side=TOP,expand=True)


        #-------data show frame--------------

        ShowData = Frame(studroot,bg='white',relief=GROOVE,borderwidth=4)
        ShowData.place(x=470,y=150,width=1000,height=600)

        scroll_x = Scrollbar(ShowData,orient=HORIZONTAL)
        scroll_y = Scrollbar(ShowData,orient=VERTICAL)

        global studenttable
        studenttable = Treeview(ShowData,columns=(
        'USN','NAME','ADDRESS','MOBILE NO','GENDER','EMAIL','D.O.B','PARENT NAME','PARENT NO','ADDED DATE','ADDED TIME'),
                                yscrollcommand=scroll_y.set,xscrollcommand=scroll_x.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=studenttable.xview)
        scroll_y.config(command=studenttable.yview)
        studenttable.heading('USN',text='USN')
        studenttable.heading('NAME',text='NAME')
        studenttable.heading('MOBILE NO',text='MOBILE NO')
        studenttable.heading('EMAIL',text='EMAIL')
        studenttable.heading('ADDRESS',text='ADDRESS')
        studenttable.heading('GENDER',text='GENDER')
        studenttable.heading('D.O.B',text='D.O.B')
        studenttable.heading('PARENT NAME',text='PARENT NAME')
        studenttable.heading('PARENT NO',text='PARENT NO')
        studenttable.heading('ADDED DATE',text='ADDED DATE')
        studenttable.heading('ADDED TIME',text='ADDED TIME')
        studenttable['show'] = 'headings'
        style = ttk.Style()
        style.configure('Treeview.Heading',font=("times",14,'bold'),background='gray40')
        style.configure('Treeview',font=("times",12,'bold'),background='gray92')
        studenttable.pack(fill=BOTH,expand=1)

        newwind.destroy()

    def student_class():
        def tm():
            time_string = time.strftime("%H:%M:%S")
            date_string = time.strftime("%d/%m/%Y")
            clock2.config(text="Time-" + time_string + "\nDate-" + date_string)
            clock2.after(200,tm)

        global classroot
        classroot =Toplevel()
        w,h = classroot.winfo_screenwidth(),classroot.winfo_screenheight()
        classroot.geometry("%dx%d+0+0" % (w,h))
        #classroot.geometry('1199x600+100+50')
        classroot.grab_set()
        classroot.title("student class details")
        # studroot.resizable(False,False)
        classroot.iconbitmap("stu.ico")
        screenlabel = Label(classroot,font=("times",25,"bold"),relief=RIDGE,bg="#15648e",bd=0,).place(x=0,y=0,relwidth=1,
                                                                                                    relheight=1)

        heading1 = Label(classroot,font=("times",25,"bold"),fg="white",relief=RIDGE,bg="#15648e",bd=0,
                         text="STUDENT DATABASE MANAGEMENT SYSTEM").place(x=350,y=0,width=850,height=60)
        heading2 = Label(classroot,font=("times",20,"bold",'underline'),fg="yellow",relief=RIDGE,bg="#15648e",bd=0,
                         text="STUDENT CLASS INFORMATION").place(x=600,y=100,width=750,height=30)

        clock2 = Label(classroot,fg='white',bg="firebrick2",font=("Times",10,'bold'),relief=RIDGE)
        clock2.place(x=1385,y=0,width=150,height=50)
        tm()

        exit_btn = Button(classroot,image=exit_im,bg="#15648e",activebackground="#15648e",bd=0,command=class_back,
                          cursor="hand2")
        exit_btn.place(x=0,y=0,width=45,height=45)

        # ------data entry frame--------------

        DataEntryFrame = Frame(classroot,bg="#15648e",relief=GROOVE,borderwidth=0)
        DataEntryFrame.place(x=60,y=130,width=300,height=600)

        datatext = Label(DataEntryFrame,text="Choose Any Option",font=("arial",20,"bold"),bg='#15648e',fg='white')
        datatext.place(x=5,y=20,width=360,height=30)
        datatext.pack(side=TOP,expand=True)

        #addbut = Button(DataEntryFrame,text="ADD USN And SSID",font=("times new roman",18,),width=25,bd=3,bg='sky blue2',
        #                activebackground='royal blue3',activeforeground='white',command=addstudent,cursor='hand2')
        #addbut.pack(side=TOP,expand=True)

        searchbut = Button(DataEntryFrame,text="SEARCH USN",font=("times new roman",18,),width=25,bd=3,
                           bg='sky blue2',activebackground='royal blue3',activeforeground='white',command=searchclass,cursor='hand2')
        searchbut.pack(side=TOP,expand=True)

        #deletebut = Button(DataEntryFrame,text="DELETE USN",font=("times new roman",18,),width=25,bd=3,
         #                  bg='sky blue2',activebackground='royal blue3',activeforeground='white',command=deleteclass,cursor='hand2')
        #deletebut.pack(side=TOP,expand=True)

        updatebut = Button(DataEntryFrame,text="UPDATE STUDENT",font=("times new roman",18,),width=25,bd=3,
                           bg='sky blue2',activebackground='royal blue3',activeforeground='white',command=updateclass,cursor='hand2')
        updatebut.pack(side=TOP,expand=True)

        showallbut = Button(DataEntryFrame,text="SHOW ALL",font=("times new roman",18,),width=25,bd=3,bg='sky blue2',
                            activebackground='royal blue3',activeforeground='white',command=showclass,cursor='hand2')
        showallbut.pack(side=TOP,expand=True)

        # -------data show frame--------------

        ShowData = Frame(classroot,bg='white',relief=GROOVE,borderwidth=4)
        ShowData.place(x=470,y=150,width=1000,height=600)

        scroll_x = Scrollbar(ShowData,orient=HORIZONTAL)
        scroll_y = Scrollbar(ShowData,orient=VERTICAL)
        global classsemtable
        classsemtable = Treeview(ShowData,columns=(
            'SSID','USN','NAME','SEMESTER','SECTION','PROCTOR'),yscrollcommand=scroll_y.set,xscrollcommand=scroll_x.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=classsemtable.xview)
        scroll_y.config(command=classsemtable.yview)
        classsemtable.heading('SSID',text='SSID')
        classsemtable.heading('USN',text='USN')
        classsemtable.heading('NAME',text='NAME')
        classsemtable.heading('SEMESTER',text='SEMESTER')
        classsemtable.heading('SECTION',text='SECTION')
        classsemtable.heading('PROCTOR',text='PROCTOR')
        classsemtable['show'] = 'headings'
        style = ttk.Style()
        style.configure('Treeview.Heading',font=("times",14,'bold'),background='gray40')
        style.configure('Treeview',font=("times",12,'bold'),background='gray92')
        classsemtable.pack(fill=BOTH,expand=1)

        newwind.destroy()


    def student_ia():
        def tm():
            time_string = time.strftime("%H:%M:%S")
            date_string = time.strftime("%d/%m/%Y")
            clock3.config(text="Time-" + time_string + "\nDate-" + date_string)
            clock3.after(200,tm)

        global iaroot
        iaroot =Toplevel()
        w,h = iaroot.winfo_screenwidth(),iaroot.winfo_screenheight()
        #iaroot.geometry("%dx%d+0+0" % (w,h))
        #iaroot.geometry('1199x600+100+50')
        iaroot.geometry('2000x2000')
        #iaroot.grab_set()
        iaroot.title("student IA marks")
        # studroot.resizable(False,False)
        iaroot.iconbitmap("stu.ico")
        screenlabel = Label(iaroot,font=("times",25,"bold"),relief=RIDGE,bg="#15648e",bd=0,).place(x=0,y=0,relwidth=1,
                                                                                                    relheight=1)

        heading1 = Label(iaroot,font=("times",25,"bold"),fg="white",relief=RIDGE,bg="#15648e",bd=0,
                         text="STUDENT DATABASE MANAGEMENT SYSTEM").place(x=350,y=0,width=850,height=60)
        heading2 = Label(iaroot,font=("times",20,"bold",'underline'),fg="yellow",relief=RIDGE,bg="#15648e",bd=0,
                         text="STUDENT IA DETAILS").place(x=600,y=100,width=750,height=30)

        clock3 = Label(iaroot,fg='white',bg="firebrick2",font=("Times",10,'bold'),relief=RIDGE)
        clock3.place(x=1385,y=0,width=150,height=50)
        tm()

        exit_btn = Button(iaroot,image=exit_im,bg="#15648e",activebackground="#15648e",bd=0,command=ia_back,
                          cursor="hand2")
        exit_btn.place(x=0,y=0,width=45,height=45)

        # ------data entry frame--------------
        DataEntryFrame = Frame(iaroot,bg="#15648e",relief=GROOVE,borderwidth=0)
        DataEntryFrame.place(x=60,y=130,width=300,height=600)

        datatext = Label(DataEntryFrame,text="Choose Any Option",font=("arial",20,"bold"),bg='#15648e',fg='white')
        datatext.place(x=5,y=20,width=360,height=30)
        datatext.pack(side=TOP,expand=True)


        # addbut = Button(DataEntryFrame,text="ADD STUDENT",font=("times new roman",18),width=25,bd=3,bg='sky blue2',
        #               activebackground='royal blue3',activeforeground='white',command=addstudent,cursor='hand2')
        # addbut.pack(side=TOP,expand=True)

        addbut = Button(DataEntryFrame,text="ADD STUDENT",font=("times new roman",18,),width=25,bd=3,bg='sky blue2',
                        activebackground='royal blue3',activeforeground='white',command=addia,cursor='hand2')
        addbut.pack(side=TOP,expand=True)

        searchbut = Button(DataEntryFrame,text="SEARCH STUDENT",font=("times new roman",18,),width=25,bd=3,
                           bg='sky blue2',activebackground='royal blue3',activeforeground='white',command=searchIA,
                           cursor='hand2')
        searchbut.pack(side=TOP,expand=True)

        deletebut = Button(DataEntryFrame,text="DELETE STUDENT",font=("times new roman",18,),width=25,bd=3,
                           bg='sky blue2',activebackground='royal blue3',activeforeground='white',command=deleteIA,
                           cursor='hand2')
        deletebut.pack(side=TOP,expand=True)

        updatebut = Button(DataEntryFrame,text="UPDATE STUDENT",font=("times new roman",18,),width=25,bd=3,
                           bg='sky blue2',activebackground='royal blue3',activeforeground='white',command=updateIAMARKS,
                           cursor='hand2')
        updatebut.pack(side=TOP,expand=True)

        showallbut = Button(DataEntryFrame,text="SHOW ALL",font=("times new roman",18,),width=25,bd=3,bg='sky blue2',
                            activebackground='royal blue3',activeforeground='white',command=showIA,cursor='hand2')
        showallbut.pack(side=TOP,expand=True)



        # -------data show frame--------------

        ShowData = Frame(iaroot,bg='white',relief=GROOVE,borderwidth=4)
        ShowData.place(x=470,y=150,width=1000,height=600)

        scroll_x = Scrollbar(ShowData,orient=HORIZONTAL)
        scroll_y = Scrollbar(ShowData,orient=VERTICAL)
        global iatable

        iatable = Treeview(ShowData,columns=(
            'USN','SUBCODE','TITLE','SEMESTER','CREDITS','TEST1','TEST2','TEST3','FINALIA'),yscrollcommand=scroll_y.set,xscrollcommand=scroll_x.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=iatable.xview)
        scroll_y.config(command=iatable.yview)
        iatable.heading('USN',text='USN')
        iatable.heading('SUBCODE',text='SUBCODE')
        #iatable.heading('NAME',text='NAME')
        iatable.heading('TITLE',text='TITLE')
        iatable.heading('SEMESTER',text='SEMESTER')
        iatable.heading('CREDITS',text='CREDITS')
        iatable.heading('TEST1',text='TEST1')
        iatable.heading('TEST2',text='TEST2')
        iatable.heading('TEST3',text='TEST3')
        iatable.heading('FINALIA',text='FINALIA')
        iatable['show'] = 'headings'
        style = ttk.Style()
        style.configure('Treeview.Heading',font=("times",14,'bold'),background='gray40')
        style.configure('Treeview',font=("times",12,'bold'),background='gray92')
        iatable.pack(fill=BOTH,expand=1)

        newwind.destroy()

    def student_attendance():
        def tm():
            time_string = time.strftime("%H:%M:%S")
            date_string = time.strftime("%d/%m/%Y")
            clock4.config(text="Time-" + time_string + "\nDate-" + date_string)
            clock4.after(200,tm)

        global attroot
        attroot = Toplevel()
        w,h = attroot.winfo_screenwidth(),attroot.winfo_screenheight()
        attroot.geometry("%dx%d+0+0" % (w,h))
        #attroot.geometry('1199x600+100+50')
        attroot.grab_set()
        attroot.title("student Attendance")
        #attroot.resizable(False,False)
        attroot.iconbitmap("stu.ico")
        screenlabel = Label(attroot,font=("times",25,"bold"),relief=RIDGE,bg="#15648e",bd=0,).place(x=0,y=0,relwidth=1,
                                                                                                    relheight=1)

        heading1 = Label(attroot,font=("times",25,"bold"),fg="white",relief=RIDGE,bg="#15648e",bd=0,
                         text="STUDENT DATABASE MANAGEMENT SYSTEM").place(x=350,y=0,width=850,height=60)
        heading2 = Label(attroot,font=("times",20,"bold",'underline'),fg="yellow",relief=RIDGE,bg="#15648e",bd=0,
                         text="STUDENT ATTENDANCE DETAILS").place(x=600,y=100,width=750,height=30)

        clock4 = Label(attroot,fg='white',bg="firebrick2",font=("Times",10,'bold'),relief=RIDGE)
        clock4.place(x=1385,y=0,width=150,height=50)
        tm()

        exit_btn = Button(attroot,image=exit_im,bg="#15648e",activebackground="#15648e",bd=0,command=attendance_back,
                          cursor="hand2")
        exit_btn.place(x=0,y=0,width=45,height=45)

        # ------data entry frame--------------

        DataEntryFrame = Frame(attroot,bg="#15648e",relief=GROOVE,borderwidth=0)
        DataEntryFrame.place(x=10,y=150,width=400,height=600)

        datatext = Label(DataEntryFrame,text="Choose Any Option",font=("arial",20,"bold"),bg='#15648e',fg='white')
        datatext.place(x=5,y=20,width=360,height=30)
        datatext.pack(side=TOP,expand=True)
        addbut = Button(DataEntryFrame,text="ADD STUDENT",font=("times new roman",18,),width=25,bd=3,bg='sky blue2',
                        activebackground='royal blue3',activeforeground='white',command=addATTENDANCE,cursor='hand2')
        addbut.pack(side=TOP,expand=True)

        searchbut = Button(DataEntryFrame,text="SEARCH STUDENT",font=("times new roman",18,),width=25,bd=3,
                           bg='sky blue2',activebackground='royal blue3',activeforeground='white',command=searchATTENDANCE,
                           cursor='hand2')
        searchbut.pack(side=TOP,expand=True)

        deletebut = Button(DataEntryFrame,text="DELETE STUDENT",font=("times new roman",18,),width=25,bd=3,
                           bg='sky blue2',activebackground='royal blue3',activeforeground='white',command=deleteATTENDANCE,
                           cursor='hand2')
        deletebut.pack(side=TOP,expand=True)

        updatebut = Button(DataEntryFrame,text="UPDATE STUDENT",font=("times new roman",18,),width=25,bd=3,
                           bg='sky blue2',activebackground='royal blue3',activeforeground='white',command=updateATTENDANCE,
                           cursor='hand2')
        updatebut.pack(side=TOP,expand=True)

        showallbut = Button(DataEntryFrame,text="SHOW ALL",font=("times new roman",18,),width=25,bd=3,bg='sky blue2',
                            activebackground='royal blue3',activeforeground='white',command=showATTENDANCE,cursor='hand2')
        showallbut.pack(side=TOP,expand=True)

        # -------data show frame--------------

        ShowData = Frame(attroot,bg='white',relief=GROOVE,borderwidth=4)
        ShowData.place(x=470,y=150,width=1000,height=600)

        scroll_x = Scrollbar(ShowData,orient=HORIZONTAL)
        scroll_y = Scrollbar(ShowData,orient=VERTICAL)

        global attendancetable

        attendancetable = Treeview(ShowData,columns=(
            'USN','SUBCODE','TITLE','SEMESTER','TOTAL ATTENDED','TOTAL CLASS TAKEN','PERCENTAGE'),yscrollcommand=scroll_y.set,xscrollcommand=scroll_x.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=attendancetable.xview)
        scroll_y.config(command=attendancetable.yview)
        attendancetable.heading('USN',text='USN')
        attendancetable.heading('SUBCODE',text='SUBCODE')
        attendancetable.heading('TITLE',text='TITLE')
        attendancetable.heading('SEMESTER',text='SEMESTER')
        attendancetable.heading('TOTAL ATTENDED',text='TOTAL ATTENDED')
        attendancetable.heading('TOTAL CLASS TAKEN',text='TOTAL CLASS TAKEN')
        attendancetable.heading('PERCENTAGE',text='PERCENTAGE')
        attendancetable['show'] = 'headings'
        style = ttk.Style()
        style.configure('Treeview.Heading',font=("times",14,'bold'),background='gray40')
        style.configure('Treeview',font=("times",12,'bold'),background='gray92')
        attendancetable.pack(fill=BOTH,expand=1)

        newwind.destroy()

    def delete():
        txt_password.delete(0,'end')
        txt_user.delete(0,'end')
    global con,mycursor
    dbuser = userval.get()
    dbpassword = passwordval.get()
    try:
        con = pymysql.connect(host='localhost',user=dbuser,password=dbpassword)
        mycursor = con.cursor()
        print("connected")
    except:
        messagebox.showerror('notification','invalid data please try again..')
        return
    try:
        strr = 'create database studentmanagementsystem1;'
        mycursor.execute(strr)
        strr = 'use studentmanagementsystem1;'
        mycursor.execute(strr)
        strr = 'create table studentgeninfo(usn varchar(10),name varchar(20),address varchar(12),mobile varchar(10),gender varchar(10),email varchar(50),dob varchar(50),parent_name varchar(30),parent_no varchar(10),date varchar(50),time varchar(50));'
        mycursor.execute(strr)
        strr = 'alter table studentgeninfo modify column usn varchar(10) not null;'
        mycursor.execute(strr)
        strr = 'alter table studentgeninfo modify column usn varchar(10) primary key;'
        mycursor.execute(strr)
        strr = 'CREATE TABLE SEMSEC (SSID VARCHAR(10) PRIMARY KEY,SEM INTEGER NOT NULL, SEC VARCHAR(20) NOT NULL,PROCTOR VARCHAR(30) NOT NULL);'
        mycursor.execute(strr)
        strr = 'CREATE TABLE CLASS (USN VARCHAR(10) NOT NULL,SSID VARCHAR(10) NOT NULL,FOREIGN KEY (USN) REFERENCES STUDENTGENINFO(USN) ON DELETE CASCADE,FOREIGN KEY (SSID) REFERENCES SEMSEC(SSID) ON DELETE CASCADE);'
        mycursor.execute(strr)
        strr = 'CREATE TABLE SUBJECT( SUBCODE VARCHAR(20) PRIMARY KEY,TITLE VARCHAR(20) NOT NULL, SEM INTEGER NOT NULL,CREDITS INTEGER NOT NULL);'
        mycursor.execute(strr)

        strr = 'CREATE TABLE IAMARKS( USN VARCHAR(10) NOT NULL, SUBCODE VARCHAR(20) NOT NULL, TEST1 INTEGER NOT NULL,TEST2 INTEGER NOT NULL, TEST3 INTEGER NOT NULL,FINALIA INTEGER NOT NULL,FOREIGN KEY(SUBCODE) REFERENCES SUBJECT(SUBCODE) ON DELETE CASCADE);'
        mycursor.execute(strr)

        strr = 'CREATE TABLE ATTENDANCE( USN VARCHAR(10) NOT NULL, SUBCODE VARCHAR(20) NOT NULL, TOTAL_ATTENDANCE INTEGER NOT NULL, TOTAL_TAKEN INTEGER NOT NULL, PERCENTAGE INTEGER NOT NULL, FOREIGN KEY(SUBCODE) REFERENCES SUBJECT(SUBCODE) ON DELETE CASCADE);'
        mycursor.execute(strr)

        strr = 'CREATE TRIGGER NAMEUPPER BEFORE INSERT ON STUDENTGENINFO FOR EACH ROW SET NEW.NAME=UPPER(NEW.NAME);'
        mycursor.execute(strr)

        strr = 'CREATE TRIGGER NAMEUPPER1 BEFORE UPDATE ON STUDENTGENINFO FOR EACH ROW SET NEW.NAME=UPPER(NEW.NAME);'
        mycursor.execute(strr)

        strr = 'CREATE TRIGGER PARUPPER BEFORE INSERT ON STUDENTGENINFO FOR EACH ROW SET NEW.parent_name=UPPER(NEW.parent_name);'
        mycursor.execute(strr)

        strr = 'CREATE TRIGGER PARUPPER1 BEFORE INSERT ON STUDENTGENINFO FOR EACH ROW SET NEW.parent_name=UPPER(NEW.parent_name);'
        mycursor.execute(strr)


        # messagebox.showinfo('Notification',
            # 'database created and now you are connected connected to the database ....',
            # parent=root)
        delete()
    except:
        strr = 'use studentmanagementsystem1;'
        mycursor.execute(strr)
        #messagebox.showinfo('Notification','Now you are connected to the database ....',parent=root)
        delete()


    def menu_window():
        root.withdraw()
        def tm():
            time_string = time.strftime("%H:%M:%S")
            date_string = time.strftime("%d/%m/%Y")
            clock.config(text="Time-" + time_string + "\nDate-" + date_string)
            clock.after(200,tm)
        global newwind
        newwind =Toplevel()
        #newwind.attributes('-fullscreen',True)
        newwind.geometry('1199x600+160+80')
        newwind.grab_set()
        newwind.title("Menu page")
        newwind.resizable(False,False)
        newwind.iconbitmap("stu.ico")

        # ----placing labels
        screenlabel = Label(newwind,font=("times",25,"bold"),relief=RIDGE,bg="#15648e",bd=0,).place(x=0,y=0,relwidth=1,relheight=1)

        heading1 = Label(newwind,font=("times",25,"bold"),fg="white",relief=RIDGE,bg="#15648e",bd=0,
                        text="STUDENT DATABASE MANAGEMENT SYSTEM").place(x=180,y=0,width=850,height=60)
        clock = Label(newwind,fg='white',bg="firebrick2",font=("Times",10,'bold'),relief=RIDGE)
        clock.place(x=1050,y=0,width=150,height=50)
        tm()

        exit_btn = Button(newwind,image=exit_im,bg="#15648e",activebackground="#15648e",bd=0,command=back_fun1,cursor="hand2")
        exit_btn.place(x=0,y=0,width=45,height=45)

        #------menu frame------

        menuoption = Label(newwind,font=("times",20,"bold"),fg="floral white",relief=RIDGE,bg="#15648e",bd=0,
                            text="Choose your option below").place(x=150,y=80,width=850,height=60)

        Frame_menu1 = Frame(newwind,bg="#15648e")
        Frame_menu1.place(x=730,y=150,height=450,width=70)

        Frame_menu2 = Frame(newwind,bg="#15648e")
        Frame_menu2.place(x=380,y=150,height=450,width=350)

       #-----menu buttons-----------
        global menu_go
        menu_go = ImageTk.PhotoImage(file="menugo.png")


        btn1 = Button(Frame_menu1,image=menu_go,fg='#15648e',bg='#15648e',activebackground='#15648e',bd=2,
                           font=("times",20),cursor="hand2",command=student_details)
        btn1.pack(side=TOP,expand=True)

        btn2 = Button(Frame_menu1,image=menu_go,fg='#15648e',bg='#15648e',activebackground='#15648e',bd=2,
                      font=("times",20),cursor="hand2",command=student_class)
        btn2.pack(side=TOP,expand=True)

        btn3 = Button(Frame_menu1,image=menu_go,fg='#15648e',bg='#15648e',activebackground='#15648e',bd=2,
                           font=("times",20),cursor="hand2",command=student_ia)
        btn3.pack(side=TOP,expand=True)

        btn4 = Button(Frame_menu1,image=menu_go,fg='#15648e',bg='#15648e',activebackground='#15648e',bd=2,
                      font=("times",20),cursor="hand2",command=student_attendance)
        btn4.pack(side=TOP,expand=True)
        global admit
        admit = ImageTk.PhotoImage(file="add.gif")
        registerlabel = Label(newwind,font=("times",16,"bold"),fg="floral white",relief=RIDGE,bg="#15648e",bd=0,
                           text="Register student").place(x=890,y=100,width=150,height=60)

        registerlabel = Label(newwind,font=("times",16,"bold"),fg="floral white",relief=RIDGE,bg="#15648e",bd=0,
                              text="Add subjects").place(x=890,y=250,width=150,height=60)

        admit_btn = Button(newwind,image=admit,bd=0,fg='#15648e',bg='#15648e',activebackground='#15648e',
                           font=("times",20),cursor="hand2",command=admission).place(x=1050,y=100)

        admit_btn1 = Button(newwind,image=admit,bd=0,fg='#15648e',bg='#15648e',activebackground='#15648e',
                           font=("times",20),cursor="hand2",command=subjectaddition).place(x=1050,y=250)
        #----------menu labels---------

        menuoption1 = Label(Frame_menu2,font=("times",25,"bold"),fg="floral white",anchor='center',relief=RIDGE,bg="firebrick2",bd=0,
                            text="Student general info").place(x=20,y=30,width=330,height=50)

        menuoption2 = Label(Frame_menu2,font=("times",25,"bold"),fg="floral white",anchor='center',relief=RIDGE,bg="firebrick2",bd=0,
                            text="Student class info").place(x=20,y=140,width=330,height=50)

        menuoption3 = Label(Frame_menu2,font=("times",25,"bold"),fg="floral white",anchor='center',relief=RIDGE,bg="firebrick2",bd=0,
                            text="Student IA marks").place(x=20,y=255,width=330,height=50)

        menuoption4 = Label(Frame_menu2,font=("times",25,"bold"),fg="floral white",anchor='center',relief=RIDGE,bg="firebrick2",bd=0,
                      text="Student Attendance ").place(x=20,y=370,width=330,height=50)






    menu_window()

#-----root----------

from tkinter import *
from PIL import ImageTk
from tkinter import messagebox,ttk
from tkinter.ttk import Treeview,Combobox
import pymysql
import time

def root_fun():
    global root
    root = Tk()
    root.title("Login page")
    #root.attributes('-fullscreen',True)
    root.geometry('1199x600+160+80')
    root.resizable(False,False)
    root.grab_set()
    root.iconbitmap("stu.ico")


    #----placing main image
    bg = ImageTk.PhotoImage(file="students.jpg")
   # bg_image = Label(root,image=bg).place(x=0,y=0,relwidth=1,relheight=1)
    screenlabel = Label(root,font=("times",25,"bold"),fg="white",relief=RIDGE,bg="#15648e",bd=0,).place(x=0,y=0,
                                                                                                       relwidth=1,
                                                                                                    relheight=1)

    #----placing main
    heading = Label(root,font=("times",25,"bold"),fg="white",relief=RIDGE,bg="#15648e",bd=0,text="STUDENT DATABASE MANAGEMENT SYSTEM").place(x=180,y=0,width=845,height=60)
    #-----

    global clock
    clock = Label(root,fg='white',bg="firebrick2",font=("Times",10,'bold'),relief=RIDGE)
    clock.place(x=1050,y=0,width=150,height=50)
    tm()
    #------back button
    global exit_im
    exit_im = ImageTk.PhotoImage(file="back.gif")
    exit_btn = Button(root,image=exit_im,bg="#15648e",activebackground="#15648e",bd=0,command=root.destroy,cursor="hand2")
    exit_btn.place(x=0,y=0,width=45,height=45)


    #----placing second image------
    stuim = ImageTk.PhotoImage(file="studentlogin.jpg")
    stu_image = Label(root,image=stuim,bd=0).place(x=800,y=225)

    #-----login frame-------
    Frame_login = Frame(root,bg="white")
    Frame_login.place(x=250,y=150,height=340,width=500)
    title = Label(Frame_login,text="System Login",font=('Impack',25,'bold'),bg='white',fg='firebrick1').place(x=135,y=30)

    #-----login fields
    global userval,passwordval
    userval = StringVar()
    passwordval = StringVar()

    global txt_user,txt_password

    user = Label(Frame_login,text="Username",font=('Goudy old style',15,'bold'),bg='white',fg='gray').place(x=75,y=120)
    txt_user = Entry(Frame_login,font=("times",15),bg='lightgray',textvariable=userval)
    txt_user.place(x=75,y=150,width=350,height=35)

    password = Label(Frame_login,text="password",font=('Goudy old style',15,'bold'),bg='white',fg='gray').place(x=75,y=190)
    txt_password = Entry(Frame_login,font=("times",15),bg='lightgray',show='*',textvariable=passwordval)
    txt_password.place(x=75,y=220,width=350,height=35)

    login_btn = Button(Frame_login,text="Login",fg='white',bg='firebrick1',activebackground='sky blue1',bd=5,font=("times",20),command=login_fun,cursor="hand2")
    login_btn.place(x=165,y=280,width=180,height=40)


    root.mainloop()
root_fun()