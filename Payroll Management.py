import random
import os
from tkinter import *
from playsound import playsound
from gtts import gTTS
import string
import time
import random
import webbrowser
import tkinter as tk 
from fpdf import FPDF
import datetime as dt




global frame1
main=tk.Tk()
main.geometry("1000x450")
main.title("Payroll Management System")
img=PhotoImage(file="icoleg.png")
main.iconphoto(False,img)
bg = PhotoImage(file = "hell.png")
label1 = Label( main, image = bg)
label1.place(x = 0, y = 0)
main.resizable(0,0)
main.config(bg="#003b41")


#----AI BACK END--------
def __f__():
    def get_random_string(length):
        letters=string.ascii_lowercase
        result_str=''.join(random.choice(letters)for i in range(length))
        return result_str

    def bigkas(args):
        tts=gTTS(text=args)
        random_string=get_random_string(4).lower()
        audio_file=os.path.dirname(random_string)+'-audio.mp3'
        tts.save(audio_file)
        playsound(audio_file)
        print(args)
        os.remove(audio_file)
    bigkas("Hi, welcome to payroll management! This app currently have three functions, why don't you try and click one ")


def __clear__():
    for_file = "Employees.txt"
    os.remove(for_file)


title_Frame = LabelFrame(main, font= ("arial",50,"bold"),width=300, height=100,bg='black',relief='raised',bd= 5 )
title_Frame.grid(row= 0, column = 0, pady = 40)
title_Label=Label(title_Frame,text="                   PAYROLL MANAGEMENT SYSTEM                           ",fg="white", font =('buffalo',20,'bold',),bg='black')
title_Label.grid(row=0, column=0,padx =7)
title_Frame.place(x=150, y=5)

#-----------------AI BUTTON---------------------
icon = PhotoImage(file = "gask.png")
icon1 = Button( main, image = icon,relief="groove",bd=0,bg="#003b41",command=__f__)
icon1.place(x = 960, y = 19,height=28,width=30)


icon_delete = PhotoImage(file = "dlete.png")
icon_delete1 = Button( main, image = icon_delete,relief="groove",bd=5,bg="#003b41",command=__clear__)
icon_delete1.place(x = 790, y = 415,height=32,width=30)


#--------------CLOCK FRAME----------------
clock_Frame= LabelFrame(main, bg="#003b41", relief='ridge', bd= 5)
clock_Frame.grid( column = 0, padx= 100,pady=0)
clock_Frame.place(x=820,y=405,width=180,height=45)
label=Label(clock_Frame)
label.pack()

#-------------------CLOCK BACKEND--------------

color_list = ['#00918f','#00ccd3','#aaf2ef','white','maroon','#061829']

def clock():
    global TL
    global hr
    shuffling_color_list=random.shuffle(color_list)
    ti=time.strftime("%I:%M:%S %p")
    lbl.config(text=ti,fg=color_list[0])
    lbl.after(200,clock)
    TL=time.strftime("%a/%b/%d %I:%M %p")
    hr=time.strftime("%H")
lbl=Label(main,font=("ds-digital",15,'bold'),bg="#003b41",bd=5,foreground="cyan")
lbl.pack(anchor="center")
lbl.place(x=848,y=408)
clock()



#------------------EMPLOYEES LIST FOR BACKEND--------------
def __employees__():
    global frame1
    frame1=Frame(main,width=650,height=400,bg="#003b41")
    frame1.grid( column = 1, padx= 100,pady=0)
    frame1.place(x=350,y=53)

    listbox=Listbox(width=70,bg="#6bd1db")
    listbox.place(x=490,y=120)
    #----for add button------backend


    def fillout(e):
        entry_Firstame.delete(0,END)
        entry_Firstame.insert(END, listbox.get(ACTIVE))




    listbox.bind("<<ListboxSelect>>",fillout)














    def __add__():
        global index
        firstname=entry_Firstame.get()
        lastname=entry_Lastname.get()
        pos=entry_Position.get()
        hrate=entry_Salary.get()
        

    
        filename=str("Employees.txt")
        f=open(filename,"a")
        f.write("EMPLOYEES LIST\n")
        f.write("   Fistname: "+firstname+"\n")
        f.write("   Lastname: "+lastname+"\n")
        f.write("   Position: "+pos+"\n")
        f.write("   HRs/Rate: "+hrate+"\n")
        f.write("\n")
        f.write("\n")
        
        n=entry_Firstame.get()
        l=entry_Lastname.get()
        p=entry_Position.get()
        h=entry_Salary.get() 
        listbox.insert(END,"       "+n+"                              "+l+"                           "+p+"                       "+h)
        t=listbox.get(0,END)
        index=str(t)
        entry_Firstame.delete(0,END)
        entry_Lastname.delete(0,END)
        entry_Position.delete(0,END)
        entry_Salary.delete(0,END)

    #-----for update button-----backend
    def __update__():
        firstname=entry_Firstame.get()
        lastname=entry_Lastname.get()
        pos=entry_Position.get()
        hrate=entry_Salary.get()

        n=entry_Firstame.get()
        l=entry_Lastname.get()
        p=entry_Position.get()
        h=entry_Salary.get() 


        filename=str("Employees.txt")
        f=open(filename,"w")
        f.write("EMPLOYEES LIST\n")
        f.write("   Fistname: "+firstname+"\n")
        f.write("   Lastname: "+lastname+"\n")
        f.write("   Position: "+pos+"\n")
        f.write("   HRs/Rate: "+hrate+"\n")
        f.write("\n")
        f.write("\n")
        listbox.delete(0,END)
        listbox.insert(END,"       "+n+"                              "+l+"                           "+p+"                       "+h)

        




        entry_Firstame.delete(0,END)
        entry_Lastname.delete(0,END)
        entry_Position.delete(0,END)
        entry_Salary.delete(0,END)



    #----for delete button----backend
    def __delete__():
        listbox.delete(ANCHOR)

    def __history__():
        for_file="Employees.txt"
        os.startfile(for_file)

    def __exit__():
        frame1.destroy()
        listbox.place_forget()
    def __undo__():
        global index
        listbox.insert(END, index)


 


    Title_Frame = LabelFrame(frame1, font= ("arial",10,"bold"),width=400, height=100,bg='#003b41',relief= 'flat',bd= 2,)
    Title_Frame.grid(row= 0, column = 0, pady = 40)
    Firstname_Label=Label(Title_Frame,text="EMPLOYEES LIST",fg='white', font =('Times New Roman',20,'bold',),bg='#003b41')
    Firstname_Label.grid(row=0, column=0,padx =7)
    Title_Frame.place(x=205,y=0)

    Firstname_Frame = LabelFrame(frame1, font= ("arial",10,"bold"),width=100, height=100,bg='#003b41',relief= 'flat',bd= 2,)
    Firstname_Frame.grid(row= 0, column = 0, pady = 40)
    Firstname_Label=Label(Firstname_Frame,text="FirstName",fg='white', font =('Times New Roman',10,'bold',),bg='#003b41')
    Firstname_Label.grid(row=0, column=0,padx =7)
    Firstname_Frame.place(x=15,y=250)

    Firstname_Frame = LabelFrame(frame1, font= ("arial",10,"bold"),width=100, height=100,bg='#003b41',relief= 'flat',bd= 2,)
    Firstname_Frame.grid(row= 0, column = 0, pady = 40)
    Firstname_Label=Label(Firstname_Frame,text="FIRSTNAME",fg='white', font =('Times New Roman',10,'bold',),bg='#003b41')
    Firstname_Label.grid(row=0, column=0,padx =7)
    Firstname_Frame.place(x=140,y=45)




    Lastname_Frame = LabelFrame(frame1, font= ("arial",10,"bold"),width=100, height=100,bg='#003b41',relief= 'flat',bd= 2,)
    Lastname_Frame.grid(row= 0, column = 0, pady = 40)
    Lastname_Label=Label(Lastname_Frame,text="LastName",fg='white', font =('Times New Roman',10,'bold',),bg='#003b41')
    Lastname_Label.grid(row=0, column=0,padx =7)
    Lastname_Frame.place(x=15,y=290)


    Lastname_Frame = LabelFrame(frame1, font= ("arial",10,"bold"),width=100, height=100,bg='#003b41',relief= 'flat',bd= 0)
    Lastname_Frame.grid(row= 0, column = 0, pady = 40)
    Lastname_Label=Label(Lastname_Frame,text="LASTNAME",fg='white', font =('Times New Roman',10,'bold',),bg='#003b41')
    Lastname_Label.grid(row=0, column=0,padx =7)
    Lastname_Frame.place(x=260,y=45)

    Position_Frame = LabelFrame(frame1, font= ("arial",10,"bold"),width=100, height=100,bg='#003b41',relief= 'flat',bd= 0,)
    Position_Frame.grid(row= 0, column = 0, pady = 40)
    Position_Label=Label( Position_Frame,text="POSITION",fg='white', font =('Times New Roman',10,'bold',),bg='#003b41')
    Position_Label.grid(row=0, column=0,padx =7)
    Position_Frame.place(x=350,y=250)

    Position_Frame = LabelFrame(frame1, font= ("arial",10,"bold"),width=100, height=100,bg='#003b41',relief= 'flat',bd= 2,)
    Position_Frame.grid(row= 0, column = 0, pady = 40)
    Position_Label=Label( Position_Frame,text="POSITION",fg='white', font =('Times New Roman',10,'bold',),bg='#003b41')
    Position_Label.grid(row=0, column=0,padx =7)
    Position_Frame.place(x=380,y=45)

    Hr_rate_Frame = LabelFrame(frame1, font= ("arial",10,"bold"),width=100, height=100,bg='#003b41',relief= 'flat',bd= 2,)
    Hr_rate_Frame.grid(row= 0, column = 0, pady = 40)
    Hr_rate_Label=Label( Hr_rate_Frame,text="HR/RATE",fg='white', font =('Times New Roman',10,'bold',),bg='#003b41')
    Hr_rate_Label.grid(row=0, column=0,padx =7)
    Hr_rate_Frame.place(x=350,y=290)

    Hr_rate_Frame = LabelFrame(frame1, font= ("arial",10,"bold"),width=100, height=100,bg='#003b41',relief= 'flat',bd= 2,)
    Hr_rate_Frame.grid(row= 0, column = 0, pady = 40)
    Hr_rate_Label=Label( Hr_rate_Frame,text="HR/RATE",fg='white', font =('Times New Roman',10,'bold',),bg='#003b41')
    Hr_rate_Label.grid(row=0, column=0,padx =7)
    Hr_rate_Frame.place(x=486,y=45)


    row1= LabelFrame(frame1, bg="#003b41", relief='ridge', bd= 2)
    row1.grid(row = 1, column = 0, padx= 100,pady=7)
    entry_Firstame=Entry(row1,width=31)
    row1.place(x=100,y=250)
    entry_Firstame.pack()

    row2= LabelFrame(frame1, bg="#003b41", relief='ridge', bd= 2)
    row2.grid(row = 1, column = 0, padx= 100,pady=7)
    entry_Lastname=Entry(row2,width=31)
    row2.place(x=100,y=290)
    entry_Lastname.pack()

    row3= LabelFrame(frame1, bg="#003b41", relief='ridge', bd= 2)
    row3.grid(row = 1, column = 0, padx= 100,pady=7)
    entry_Position=Entry(row3,width=31)
    row3.place(x=450,y=250)
    entry_Position.pack()

    row4= LabelFrame(frame1, bg="#003b41", relief='ridge', bd= 2)
    row4.grid(row = 1, column = 0, padx= 100,pady=7)
    entry_Salary=Entry(row4,width=31)
    row4.place(x=450,y=290)
    entry_Salary.pack()

    def on_Enteradd(e):
        add_image.configure(file="onadd.png")
    def on_leaveadd(e):
        add_image.configure(file="offadd.png")
    
    add_image=PhotoImage(file="offadd.png")
    add_button = Button(frame1,image=add_image,border=2,command=__add__)
    add_button.place(x=50,y=345,width=90)
    add_button.bind("<Enter>",on_Enteradd)
    add_button.bind("<Leave>",on_leaveadd)

    def on_Enterupdate(e):
        update_image.configure(file="onupdate.png")
    def on_leaveupdate(e):
        update_image.configure(file="offupdate.png")
    
    update_image=PhotoImage(file="offupdate.png")
    update_button = Button(frame1,image=update_image,border=2,command=__update__)
    update_button.place(x=280,y=345,width=90)
    update_button.bind("<Enter>",on_Enterupdate)
    update_button.bind("<Leave>",on_leaveupdate)

    def on_Enterdelete(e):
        delete_image.configure(file="ondelete.png")
    def on_leavedelete(e):
        delete_image.configure(file="offdelete.png")
    
    delete_image=PhotoImage(file="offdelete.png")
    delete_button = Button(frame1,image=delete_image,border=2,command=__delete__)
    delete_button.place(x=500,y=345,width=90)
    delete_button.bind("<Enter>",on_Enterdelete)
    delete_button.bind("<Leave>",on_leavedelete)

    undo = Button(frame1,text = 'exit',fg='white',font=('arial',10,'bold'),width=8,bg='maroon', command = __exit__,borderwidth=5,relief="groove")
    undo.grid(row=0, column= 3, padx=50)
    undo.place(x=570,y=0,height=30,width=80)


    undo1 = Button(frame1,text = 'STORE',fg='white',font=('arial',10,'bold'),width=8,bg='maroon', command = __undo__,borderwidth=5,relief="groove")
    undo1.grid(row=0, column= 3, padx=50)
    undo1.place(x=570,y=50,height=30,width=80)




    def on_Enterview(e):
        history_image.configure(file="onview.png")
    def on_leaveview(e):
        history_image.configure(file="offview.png")
    
    history_image=PhotoImage(file="offview.png")
    history_button = Button(frame1,image=history_image,border=2,command=__history__)
    history_button.place(x=0,y=0,width=105)
    history_button.bind("<Enter>",on_Enterview)
    history_button.bind("<Leave>",on_leaveview)


#-----------------ATTENDANCE FOR BACKEND----------------
def __attendance__():
    global frame2
    frame2=Frame(main,width=650,height=400,bg="#003b41")
    frame2.grid( column = 1, padx= 100,pady=0)
    frame2.pack()
    frame2.place(x=350,y=53)


    def __TIMEIN__():
        global TIME
        fullname=entry_Fullname.get()
        entry_TIME=hr
        TIME=entry_TIME

        if (int(TIME) <= 8):
            p="NOT LATE"
            screen3 = Toplevel(main)
            screen3.title("Success")
            screen3.geometry("230x40") 
            screen3.resizable(0,0)
            Button(screen3, text = "PROCEED",font= ("arial",30,"bold"),fg="white", bg="green",command=screen3.destroy).pack()


            #btn1 = Button(screen3,text = 'ok',fg='white',font=('arial',16,'bold'),width=8,bg='#003b41', command = __delete__,borderwidth=10)
            
            def disable_event():
                pass
            screen3.protocol("WM_DELETE_WINDOW", disable_event)

        elif(int(TIME) > 8):
            l="LATE"
            screen3 = Toplevel(main)
            screen3.title("Success")
            screen3.geometry("290x40") 
            screen3.resizable(0,0)

            Button(screen3, text = "YOU'RE LATE!",font= ("arial",30,"bold"),fg="white", bg="green",command=screen3.destroy).pack()


            #btn1 = Button(screen3,text = 'ok',fg='white',font=('arial',16,'bold'),width=8,bg='#003b41', command = __delete__,borderwidth=10)
                    
            def disable_event():
                pass
            screen3.protocol("WM_DELETE_WINDOW", disable_event)

        elif(int(TIME) > 5 or int(TIME) <=24):
            o="OUT OF TIME"
            screen3 = Toplevel(main)
            screen3.title("Success")
            screen3.geometry("490x40") 
            screen3.resizable(0,0)

            Button(screen3, text = "COMBACK TOMORROW!",font= ("arial",30,"bold"),fg="white", bg="green",command=screen3.destroy).pack()


            def disable_event():
                pass
            screen3.protocol("WM_DELETE_WINDOW", disable_event)


        fname=str("Employees.txt")
        f=open(fname,"a")
        f.write("\n")
        f.write("\n")
        f.write("ATTENDANCE LIST\n")
        f.write("   Fullname: "+fullname+"\n")           
        f.write("   TIME-IN : "+TIME+"\n")
        if (int(TIME) <= 8):
            f.write(" STATUS: "+p+"\n") 
            f.write(" TODAYTIME:  "+TL+'\n')  
            f.write("\n")
        elif(int(TIME) > 8):
            f.write("  STATUS: "+l+"\n")  
            f.write(" TODAYTIME:  "+TL+"\n")  
            f.write("\n")


        elif(int(TIME) > 5 and int(TIME) <=24):
            f.write("  STATUS: "+o+"\n")  
            f.write(" TODAYTIME:  "+TL)  
            f.write("\n")    
            
        f.write("\n")           
        f.write("\n")      

        
        entry_Fullname.delete(0,END)

    def __history__():
        for_file="Employees.txt"
        os.startfile(for_file)


    def __TIMEOUT__():
        global hr
        n=entry_Fullname.get()
        fname1=str("Employees.txt")
        f=open(fname1,"a")
        f.write("\n")
        f.write("=========TIME OUT============\n")
        if (int(hr) >=8) or (int(hr) <= 17):
            ito= (17 - int(hr))
            f.write("Fullname: "+str(n)+"\n")
            f.write("You have only "+str(ito)+" hour/s to work!\n")
            
            
        else:
            itos=((int(hr)) - 5)
            f.write("Fullname: "+str(n)+"\n")
            f.write("You have "+str(itos)+" hour/s to start your work!\n")   

        entry_Fullname.delete(0,END)
            


            




        '''''
        default = dt.time(8)
        time2=datetime.now().strftime("%H:%M:%S")
        if (int(time2)) >= (int(default)):
            print("kahit ano")
        else:
            print("bahala ka")
        '''


    def __exit__():
        frame2.destroy()
    undo = Button(frame2,text = 'exit',fg='white',font=('arial',10,'bold'),width=8,bg='maroon', command = __exit__,borderwidth=5,relief="groove")
    undo.grid(row=0, column= 3, padx=50)
    undo.place(x=570,y=0,height=30,width=80)

    Title_Frame = LabelFrame(frame2, font= ("arial",10,"bold"),width=400, height=100,bg='#003b41',relief= 'flat',bd= 2,)
    Title_Frame.grid(row= 0, column = 0, pady = 40)
    Firstname_Label=Label(Title_Frame,text="ATTENDANCE",fg='white', font =('Times New Roman',20,'bold',),bg='#003b41')
    Firstname_Label.grid(row=0, column=0,padx =7)
    Title_Frame.place(x=245,y=5)

    Name_Frame = LabelFrame(frame2, font= ("arial",10,"bold"),width=100, height=100,bg='#003b41',relief= 'groove',bd= 2,)
    Name_Frame.grid(row= 0, column = 0, pady = 40)
    Name_Label=Label( Name_Frame,text="FullName",fg='white', font =('Times New Roman',10,'bold',),bg='#003b41')
    Name_Label.grid(row=0, column=0,padx =7)
    Name_Frame.place(x=160,y=120)


    Time_Frame = LabelFrame(frame2, font= ("arial",10,"bold"),width=100, height=100,bg='#003b41',relief= 'groove',bd= 2,)
    Time_Frame.grid(row= 0, column = 0, pady = 40)
    Time_Label=Label(  Time_Frame,text="LOG_TIME",fg='white', font =('Times New Roman',10,'bold',),bg='#003b41')
    Time_Label.grid(row=0, column=0,padx =7)
    Time_Frame.place(x=160,y=200)


    row1= LabelFrame(frame2, bg="#003b41", relief='ridge', bd= 2)
    row1.grid(row = 1, column = 0, padx= 100,pady=7)
    entry_Fullname=Entry(row1,width=31)
    row1.place(x=250,y=120)
    entry_Fullname.pack()

    row3= LabelFrame(frame2,bg="#003b41", relief='ridge', bd= 2)
    row3.grid(row = 1, column = 0, padx= 100,pady=7)
    entry_TIME=Entry(row3,width=31)
    row3.place(x=250,y=200)
    entry_TIME.pack()
    entry_TIME.insert(END,"Automatic")
    entry_TIME.configure(state=DISABLED)

    def on_Enterview(e):
        history_image.configure(file="onview.png")
    def on_leaveview(e):
        history_image.configure(file="offview.png")
    
    history_image=PhotoImage(file="offview.png")
    history_button = Button(frame2,image=history_image,border=2,command=__history__)
    history_button.place(x=0,y=0,width=105)
    history_button.bind("<Enter>",on_Enterview)
    history_button.bind("<Leave>",on_leaveview)


    submit1 = Button(frame2,text = 'TIME IN',fg='white',font=('arial',15,'bold'),width=8,bg='#003b41', command = __TIMEIN__,borderwidth=5,relief="groove")
    submit1.grid(row=0, column= 3, padx=50)
    submit1.place(x=150,y=350,height=30,width=130)

    
    submit2 = Button(frame2,text = 'TIME OUT',fg='white',font=('arial',15,'bold'),width=8,bg='#003b41', command = __TIMEOUT__,borderwidth=5,relief="groove")
    submit2.grid(row=0, column= 3, padx=50)
    submit2.place(x=300,y=350,height=30,width=130)
    



#-----------------TRANSACTION FOR BACKEND-----------------
def __transaction__():
    global frame3
    frame3=Frame(main,width=650,height=400,bg="#003b41")
    frame3.grid( column = 1, padx= 100,pady=0)
    frame3.pack()
    frame3.place(x=350,y=53)

    # fname= entry_Fname.get()
    # pname= entry_Pname.get()
    # hrname= entry_hr.get()
    #dname= entry_day.get()
    #tname= entry_time.get()
    

    def __MONTHLYSALARY__():
        Fulln=entry_Fname.get()
        Posn=entry_Pname.get()
        dname= entry_hrRate.get()
        hrATTname= entry_hrATT.get()
        Dayatt=entry_day.get()
        Daysalary=(int(dname))*(int(hrATTname))
        Mothlysalary=(int(Dayatt)*(int(Daysalary)))

        fname=str("Employees.txt")
        f=open(fname,"a")
        f.write("\n")
        f.write("\n")
        f.write("----------PAYROLL MANAGEMENT  SYSTEM---------\n")
        f.write("----------TRANSACTION RECIEPT---------\n")
        f.write("   FULLNAME: "+Fulln+"\n")    
        f.write("   POSITION: "+Posn+"\n")  
        f.write("   HR/RATE: PHP "+str(dname)+" /HR\n")
        f.write("   HR/ATTEND: "+str(hrATTname)+" TOTAL HR/S\n")    
        f.write("   DAYS/ATTEND: "+str(Dayatt)+" TOTAL DAY/S\n") 
        f.write("   MONTHLYSALARY: "+str(Mothlysalary)+"\n") 
        f.write("   ACCURATE-DATE RECIEPT : "+TL+"\n")
        print('\n')
        print('\n')

        entry_day.delete(0,END)
        entry_Fname.delete(0,END)
        entry_hrATT.delete(0,END)
        entry_Pname.delete(0,END)
        entry_hrRate.delete(0,END)



    def __DAYSALARY__():
        Fulln1=entry_Fname.get()
        Posn1=entry_Pname.get()
        dname1= entry_hrRate.get()
        hrATTname1= entry_hrATT.get()
        Dayatt1=entry_day.get()
        Daysalary1=((int(dname1))*(int(hrATTname1)))
        fname1=str("Employees.txt")
        f=open(fname1,"a")
        f.write("\n")
        f.write("\n")
        f.write("----------PAYROLL MANAGEMENT  SYSTEM---------\n")
        f.write("----------TRANSACTION RECIEPT---------\n")
        f.write("   FULLNAME: "+Fulln1+"\n")    
        f.write("   POSITION: "+Posn1+"\n")  
        f.write("   HR/RATE: PHP "+dname1+" /HR/S"+"\n")
        f.write("   HR/ATTEND: "+hrATTname1+" HR/S"+"\n")    
        f.write("   DAILYSALARY: "+str(Daysalary1)+"\n")
        f.write("   ACCURATE-DATE RECIEPT : "+TL+"\n")
        print('\n')
        print('\n')

        entry_day.delete(0,END)
        entry_Fname.delete(0,END)
        entry_hrATT.delete(0,END)
        entry_Pname.delete(0,END)
        entry_hrRate.delete(0,END)



    Title_Frame = LabelFrame(frame3, font= ("arial",10,"bold"),width=400, height=100,bg='#003b41',relief= 'groove',bd= 0,)
    Title_Frame.grid(row= 0, column = 0, pady = 40)
    Firstname_Label=Label(Title_Frame,text="TRANSACTION",fg='white', font =('Times New Roman',20,'bold',),bg='#003b41')
    Firstname_Label.grid(row=0, column=0,padx =7)
    Title_Frame.place(x=235,y=5)

    Fname_Frame = LabelFrame(frame3, font= ("arial",10,"bold"),width=100, height=100,bg='#003b41',relief= 'groove',bd= 0,)
    Fname_Frame.grid(row= 0, column = 0, pady = 40)
    Name_Label=Label( Fname_Frame,text="FULLNAME",fg='white', font =('Times New Roman',10,'bold',),bg='#003b41')
    Name_Label.grid(row=0, column=0,padx =7)
    Fname_Frame.place(x=150,y=100)

    Pname_Frame = LabelFrame(frame3, font= ("arial",10,"bold"),width=100, height=100,bg='#003b41',relief= 'groove',bd= 0,)
    Pname_Frame.grid(row= 0, column = 0, pady = 40)
    Name_Label=Label( Pname_Frame,text="POSITION",fg='white', font =('Times New Roman',10,'bold',),bg='#003b41')
    Name_Label.grid(row=0, column=0,padx =7)
    Pname_Frame.place(x=150,y=140)

    Hname_Frame = LabelFrame(frame3, font= ("arial",10,"bold"),width=100, height=100,bg='#003b41',relief= 'groove',bd= 0,)
    Hname_Frame.grid(row= 0, column = 0, pady = 40)
    Name_Label=Label( Hname_Frame,text="HR/RATE",fg='white', font =('Times New Roman',10,'bold',),bg='#003b41')
    Name_Label.grid(row=0, column=0,padx =7)
    Hname_Frame.place(x=150,y=180)

    Dname_Frame = LabelFrame(frame3, font= ("arial",10,"bold"),width=100, height=100,bg='#003b41',relief= 'groove',bd= 0,)
    Dname_Frame.grid(row= 0, column = 0, pady = 40)
    Name_Label=Label( Dname_Frame,text="DAY/ATT",fg='white', font =('Times New Roman',10,'bold',),bg='#003b41')
    Name_Label.grid(row=0, column=0,padx =7)
    Dname_Frame.place(x=150,y=220)

    hname_Frame = LabelFrame(frame3, font= ("arial",10,"bold"),width=100, height=100,bg='#003b41',relief= 'groove',bd= 0,)
    hname_Frame.grid(row= 0, column = 0, pady = 40)
    Name_Label=Label( hname_Frame,text="HR/ATT",fg='white', font =('Times New Roman',10,'bold',),bg='#003b41')
    Name_Label.grid(row=0, column=0,padx =7)
    hname_Frame.place(x=150,y=260)


    row3= LabelFrame(frame3,bg="#003b41", relief='ridge', bd= 2)
    row3.grid(row = 1, column = 0, padx= 100,pady=7)
    entry_time=Entry(row3,width=31)
    row3.place(x=250,y=300)
    entry_time.pack()
    entry_time.insert(END,"Date_of_Transac")
    entry_time.configure(state=DISABLED)



    row1= LabelFrame(frame3, bg="#003b41", relief='ridge', bd= 2)
    row1.grid(row = 1, column = 0, padx= 100,pady=7)
    entry_Fname=Entry(row1,width=31)
    row1.place(x=250,y=100)
    entry_Fname.pack()

    row2= LabelFrame(frame3, bg="#003b41", relief='ridge', bd= 2)
    row2.grid(row = 1, column = 0, padx= 100,pady=7)
    entry_Pname=Entry(row2,width=31)
    row2.place(x=250,y=140)
    entry_Pname.pack()

    row3= LabelFrame(frame3, bg="#003b41", relief='ridge', bd= 2)
    row3.grid(row = 1, column = 0, padx= 100,pady=7)
    entry_hrRate=Entry(row3,width=31)
    row3.place(x=250,y=180)
    entry_hrRate.pack()

    row4= LabelFrame(frame3, bg="#003b41", relief='ridge', bd= 2)
    row4.grid(row = 1, column = 0, padx= 100,pady=7)
    entry_day=Entry(row4,width=31)
    row4.place(x=250,y=220)
    entry_day.pack()

    row5= LabelFrame(frame3, bg="#003b41", relief='ridge', bd= 2)
    row5.grid(row = 1, column = 0, padx= 100,pady=7)
    entry_hrATT=Entry(row5,width=31)
    row5.place(x=250,y=260)
    entry_hrATT.pack()

    def __exit__():
        frame3.destroy()
    undo = Button(frame3,text = 'exit',fg='white',font=('arial',10,'bold'),width=8,bg='maroon', command = __exit__,borderwidth=5,relief="groove")
    undo.grid(row=0, column= 3, padx=50)
    undo.place(x=570,y=0,height=30,width=80)



    def __receipt__():
        # save FPDF() class into
        # a variable pdf
        pdf = FPDF()

        # Add a page
        pdf.add_page()

        # set style and size of font
        # that you want in the pdf
        pdf.set_font("Arial", size = 15)
        
        # open the text file in read mode
        f = open("Employees.txt", "r")
        
        # insert the texts in pdf
        for x in f:
            pdf.cell(200, 10, txt = x, ln = 1, align = 'C')

        # save the pdf with name .pdf
        pdf.output("eeceipt.pdf")
        webbrowser.open("eeceipt.pdf")
        

    print1= Button(frame3,text = 'RECIEPT',fg='white',font=('arial',10,'bold'),width=8,bg='maroon', command = __receipt__,borderwidth=5,relief="groove")
    print1.grid(row=0, column= 3, padx=50)
    print1.place(x=10,y=0,height=30,width=80)



    submit1 = Button(frame3,text = 'MONTLYSALARY',fg='white',font=('arial',15,'bold'),width=8,bg='#003b41', command = __MONTHLYSALARY__,borderwidth=5,relief="groove")
    submit1.grid(row=0, column= 3, padx=50)
    submit1.place(x=380,y=350,height=30,width=190)

    submit2 = Button(frame3,text = 'DAYSALARY',fg='white',font=('arial',15,'bold'),width=8,bg='#003b41', command = __DAYSALARY__,borderwidth=5,relief="groove")
    submit2.grid(row=0, column= 3, padx=50)
    submit2.place(x=120,y=350,height=30,width=150)


#----------------USER 1 ACCOUNT ------------------

def __user1__():
    webbrowser.open("https://www.facebook.com/CJayzzz.com.ph/")


def on_Enter(e):
    payroll_image.configure(file="hov1.png")
def on_leave(e):
    payroll_image.configure(file="emplo icon.png")


payroll_image=PhotoImage(file="emplo icon.png")
label_button = Button(main,image=payroll_image,border=0,command=__employees__)
label_button.place(x=50,y=165)


label_button.bind("<Enter>",on_Enter)
label_button.bind("<Leave>",on_leave)


#---------Attendance Button---------
def on_Enter1(e):
    attendance_image.configure(file="hov2.png")
def on_leave1(e):
    attendance_image.configure(file="sttendance ico.png")

attendance_image=PhotoImage(file="sttendance ico.png")
attendance_button = Button(main,image=attendance_image,border=0,command=__attendance__)
attendance_button.place(x=50,y=270)
attendance_button.bind("<Enter>",on_Enter1)
attendance_button.bind("<Leave>",on_leave1)



#---------------Transaction ---------
def on_Enter2(e):
    transaction_image.configure(file="hov3.png")
def on_leave2(e):
    transaction_image.configure(file="sransaction ico.png")

transaction_image=PhotoImage(file="sransaction ico.png")
tran_button = Button(main,image=transaction_image,border=0,command=__transaction__)
tran_button.place(x=50,y=375)
tran_button.bind("<Enter>",on_Enter2)
tran_button.bind("<Leave>",on_leave2)


#----------DEV 1----CJ------
user = PhotoImage(file = "kpo.png")
user1 = Button( main, image = user,relief="groove",bd=0,bg="#003b41",command=__user1__)
user1.place(x = 960, y = 70, height=28,width=30)




mainloop()

