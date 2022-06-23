#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from tkinter import*
from tkinter.ttk import*  #new widgets
from tkinter.filedialog import askopenfile  #for file access
import tkinter.messagebox  #for pop-up box
from tkinter.tix import*  #for tips
import time




#creating the frame
ws=Tk()
ws.title('STUDY-MATERIAL SHARING INTERFACE')
ws.geometry('400x300')

#colour of window
ws.configure(bg='#d9eafa')

#created tooltip
tip=Balloon(ws)

#function to open access any type of files and binding to buttons(choose file)
#def open_file():
    #file=filedialog.askopenfilename()
    #if file is not None:
        #pass
    
my_str1=StringVar()  #making a variable string
my_str2=StringVar()
my_str3=StringVar()

def open_name1():    #dialog box and fetching file name
    file1=filedialog.askopenfilename()
    if(file1):
        my_str1.set(file1)
        
       
def open_name2():    #dialog box and fetching file name
    file2=filedialog.askopenfilename()
    if(file2):
        my_str2.set(file2)
        
        
        
        
def open_name3():    #dialog box and fetching file name
    file3=filedialog.askopenfilename()
    if(file3):
        my_str3.set(file3)
        
        


#function binded to upload button
def upload_files():
    pb=Progressbar(ws, orient=HORIZONTAL, length=300, mode='determinate')  #creating a progressbar
    pb.grid(row=4, columnspan=3, pady=20)
    for i in range(5):  #filling the bar 20% for 5 times
        ws.update_idletasks()
        pb['value']+=20
        time.sleep(1) #giving a delay of one sec
    pb.destroy()  #destroying the progressbar
    tkinter.messagebox.showinfo("File Upload Status", "File Uploaded Successfully!")  #pop-up after progressbar fills up
    #Label(ws, text='File Uploaded Successfully!', foreground='green').grid(row=4, columnspan=3, pady=10)
    
#function binded to close button   
def Exit():
    tkinter.messagebox.showinfo("Program Closed", "THANK YOU!!") #pop-up on clicking the button
    ws.destroy()   #destroys the frame
    

#creating label    
hw=Label(ws, text='Hand-written Notes', bg='#d9eafa')
hw.grid(row=0, column=0, padx=10)  #placing the label

#creating button
hwbtn=Button(ws, text='Choose File', bg='#65a2db', command=lambda:open_name1())
hwbtn.grid(row=0, column=1)  #placing the button

#tip message while hovering over the button
tip.bind_widget(hwbtn, balloonmsg="Click to choose a file")

hwlabel=Label(ws, textvariable=my_str1, foreground='RED')
hwlabel.grid(row=0, column=2)
my_str1.set("NO FILE SELECTED")

#creating label
ppt=Label(ws, text='Class Notes', bg='#d9eafa')
ppt.grid(row=1, column=0, padx=10)  #placing the label

#creating button
pptbtn=Button(ws, text='Choose File', bg='#65a2db', command=lambda:open_name2())
pptbtn.grid(row=1, column=1)  #placing the button

#tip message while hovering over the button
tip.bind_widget(pptbtn, balloonmsg="Click to choose a file")

pptlabel=Label(ws, textvariable=my_str2, foreground='RED')
pptlabel.grid(row=1, column=2)
my_str2.set("NO FILE SELECTED")

#creating label
sn=Label(ws, text='Short Notes', bg='#d9eafa')
sn.grid(row=2, column=0, padx=10)  #placing the label

#creating button
snbtn=Button(ws, text='Choose File', bg='#65a2db', command=lambda:open_name3())
snbtn.grid(row=2, column=1)  #placing the button

#tip message while hovering over the button
tip.bind_widget(snbtn, balloonmsg="Click to choose a file")

snlabel=Label(ws, textvariable=my_str3, foreground='RED')
snlabel.grid(row=2, column=2)
my_str3.set("NO FILE SELECTED")


#creating button
upld=Button(ws, text='Upload Files', command=upload_files)
upld.grid(row=3, column=0, pady=10)  #placing the button

#tip message while hovering over the button
tip.bind_widget(upld, balloonmsg="Click to upload your files")


#creating button
Ext=Button(ws, text='Close', bg='red', activebackground='red', command=Exit)
Ext.grid(row=3, column=1, pady=10)  #placing the button

#tip message while hovering over the button
tip.bind_widget(Ext, balloonmsg="Click to close the program")



mainloop()


# In[ ]:





# In[ ]:





# In[ ]:


#=================database creation=============================
import mysql.connector
stdb = mysql.connector.connect(host = "localhost", user = "root", 
                               password = "Arijeet1!")
mycursor = stdb.cursor()    
mycursor.execute("create database studentdb")


# In[ ]:





# In[ ]:





# In[ ]:


#==============table creation===================================
import mysql.connector 
mydb = mysql.connector.connect(host = "localhost",  
                               user = "root",  
                               password = "Arijeet1!",  
                               database = "studentdb") 
mycursor = mydb.cursor() 
mycursor.execute("CREATE TABLE student0(registration int(15) PRIMARY KEY,name VARCHAR(255), password int(15))")


# In[ ]:





# In[ ]:





# In[ ]:


#=======================row insertion=================================
import mysql.connector 
 
stdb = mysql.connector.connect( host="localhost", user="root", password="Arijeet1!", database="studentdb")  
 
mycursor = stdb.cursor() 
 
sql = "INSERT INTO student0(registration, name, password) VALUES (%s, %s, %s)" 
val = [ 
        (1200,'Anupam',100), 
        (1201,'Arijeet',101), 
        (1202, 'Aniket',102), 
        (1203,'Vishal',103), 
        (1204, 'Aman',104), 
        (1205, 'Rahul',105),
        (1206, 'Vikas',106),
        (1207, 'Harsh',107)]

mycursor.executemany(sql, val) 
 
stdb.commit()  


# In[ ]:





# In[ ]:





# In[ ]:


#======================login page=======================================
from tkinter import*
from tkinter import messagebox
class login:
    def __init__(self,root):
        self.root=root
        self.root.title("Welcome to Login")
        self.root.geometry("1000x600")
        self.root.config(bg="#021e2f")
        
        frm=Frame(self.root,bg="light cyan")
        frm.place(x=250,y=100,width=850,height=500)
        
        #label in the frame
        title=Label(frm,text="Login Here !",font=("times new roman",30,"bold"),bg="light cyan",fg="crimson")
        title.place(x=290,y=20)
        
        #text label and entry box for taking values
        reg=Label(frm,text="Registration Number",font=("arial rounded mt",20),bg="light cyan",fg="olive")
        reg.place(x=20,y=100)
        self.reg_in=Entry(frm,font=("arial",15),bg="powder blue",width=30,border=1)
        self.reg_in.place(x=20,y=140,height=35)
        
        #text label and entry box for taking values
        pas=Label(frm,text="Password",font=("arial rounded mt",20),bg="light cyan",fg="olive")
        pas.place(x=20,y=200)
        self.pas_in=Entry(frm,font=("arial",15),bg="powder blue",width=30,border=1)
        self.pas_in.place(x=20,y=240,height=35)
        
        #button for login
        butn=Button(frm,cursor="hand2",text="Login",font=("arial rounded mt",20,"bold"),bg="lime green",fg="white",width=10,border=2,command=self.display)
        butn.place(x=20, y=320)
        
    def display(self):
           if self.pas_in.get()=="" or self.reg_in.get()=="":
                messagebox.showerror("Error","Please fill all the required fields !",parent=self.root)
                
           else:
                try:
                    stdb=mysql.connector.connect(host = "localhost", user = "root", password = "Arijeet1!",database="studentdb")
                    mycursor=stdb.cursor()
                    mycursor.execute("select * from student0 where registration=%s and password=%s",(self.reg_in.get(),self.pas_in.get()))
                    check=mycursor.fetchone()
                    
                    if check==None:
                        messagebox.showerror("Error","Invalid registration or Password",parent=self.root)
                    else:
                        messagebox.showinfo("Login success","Welcome to our file Sharing platform",parent=self.root)
    
                except:
                    m=Message(root,text="OOPS! something went wrong",width=300,font=('Roman', 20, 'bold'), fg='red')
                    m.pack(padx=250,pady=700)
root=Tk()
obj=login(root)
root.mainloop()


# In[ ]:





# In[ ]:





# In[ ]:


import mysql.connector  
  
stdb = mysql.connector.connect(  
  host="localhost",  
  user="root",  
  password="Arijeet1!",  
  database="studentdb"  
)  
  
mycursor = stdb.cursor()  
mycursor.execute("SELECT * FROM student0")   
for x in mycursor:  
    print(x)


# In[ ]:





# In[ ]:





# In[ ]:


#======================FINAL PROJECT=============================


# In[ ]:


from tkinter import*
from tkinter import messagebox #for pop-ups
from tkinter.ttk import*  #new widgets
from tkinter.filedialog import askopenfile  #for file access
from tkinter.tix import*  #for tips
import time  #for time related methods

class login:
    def __init__(self,root):
        self.root=root
        self.root.title("Welcome to Login")
        self.root.geometry("1000x600")
        self.root.config(bg="#021e2f")
        
        frm=Frame(self.root,bg="light cyan")
        frm.place(x=250,y=100,width=850,height=500)
        
        #label in the frame
        title=Label(frm,text="Login Here !",font=("times new roman",30,"bold"),bg="light cyan",fg="crimson")
        title.place(x=290,y=20)
        
        #text label and entry box for taking values
        reg=Label(frm,text="Registration Number",font=("arial rounded mt",20),bg="light cyan",fg="olive")
        reg.place(x=20,y=100)
        self.reg_in=Entry(frm,font=("arial",15),bg="powder blue",width=30,border=1)
        self.reg_in.place(x=20,y=140,height=35)
        
        #text label and entry box for taking values
        pas=Label(frm,text="Password",font=("arial rounded mt",20),bg="light cyan",fg="olive")
        pas.place(x=20,y=200)
        self.pas_in=Entry(frm,font=("arial",15),bg="powder blue",width=30,border=1)
        self.pas_in.place(x=20,y=240,height=35)
        
        #button for login
        butn=Button(frm,cursor="hand2",text="Login",font=("arial rounded mt",20,"bold"),bg="lime green",fg="white",width=10,border=2,command=self.display)
        butn.place(x=20, y=320)
        
        
        
    def display(self):
           if self.pas_in.get()=="" or self.reg_in.get()=="":
                messagebox.showerror("Error","Please fill all the required fields !",parent=self.root)
                
           else:
                try:
                    stdb=mysql.connector.connect(host = "localhost", user = "root", password = "Arijeet1!",database="studentdb")
                    mycursor=stdb.cursor()
                    mycursor.execute("select * from student0 where registration=%s and password=%s",(self.reg_in.get(),self.pas_in.get()))
                    check=mycursor.fetchone()
                    
                    if check==None:
                        messagebox.showerror("Error","Invalid registration or Password",parent=self.root)
                    else:
                        messagebox.showinfo("Login success","Welcome to our file Sharing platform",parent=self.root)
                        
                        #creating the redirect
                        ws=Toplevel(root)
                
                        ws.title('STUDY-MATERIAL SHARING INTERFACE')
                        ws.geometry('400x300')

                        #colour of window
                        ws.configure(bg='#d9eafa')

                        #created tooltip
                        tip=Balloon(ws)

                        
                        my_str1=StringVar()
                        my_str2=StringVar()
                        my_str3=StringVar()
                        
                        def open_name(hello=None):
                            file=filedialog.askopenfilename()
                            if(file):
                                if hello == 'hwbtn':
                                    my_str1.set(file)
                                elif(hello == 'pptbtn'):
                                    my_str2.set(file)
                                elif(hello == 'snbtn'):
                                    my_str3.set(file)
           
                        #function binded to upload button
                        def upload_files():
                            pb=Progressbar(ws, orient=HORIZONTAL, length=300, mode='determinate')  #creating a progressbar
                            pb.grid(row=4, columnspan=3, pady=20)
                            for i in range(5):  #filling the bar 20% for 5 times
                                ws.update_idletasks()  #to process the progress bar
                                pb['value']+=20
                                time.sleep(1) #giving a delay of one sec
                            pb.destroy()  #destroying the progressbar
                            tkinter.messagebox.showinfo("File Upload Status", "File Uploaded Successfully!")  #pop-up after progressbar fills up
                            #Label(ws, text='File Uploaded Successfully!', foreground='green').grid(row=4, columnspan=3, pady=10)
    
                        #function binded to close button   
                        def Exit():
                            tkinter.messagebox.showinfo("Program Closed", "THANK YOU!!") #pop-up on clicking the button
                            ws.destroy()   #destroys the frame
    

                        #creating label    
                        hw=Label(ws, text='Hand-written Notes', bg='#d9eafa')
                        hw.grid(row=0, column=0, padx=10)  #placing the label

                        #creating button
                        hwbtn=Button(ws, text='Choose File', bg='#65a2db', command=lambda:open_name('hwbtn'))
                        hwbtn.grid(row=0, column=1)  #placing the button

                        #tip message while hovering over the button
                        tip.bind_widget(hwbtn, balloonmsg="Click to choose a file")

                        hwlabel=Label(ws, textvariable=my_str1, foreground='RED')
                        hwlabel.grid(row=0, column=2)
                        my_str1.set("No file selected")


                        #creating label
                        ppt=Label(ws, text='Class Notes', bg='#d9eafa')
                        ppt.grid(row=1, column=0, padx=10)  #placing the label

                        #creating button
                        pptbtn=Button(ws, text='Choose File', bg='#65a2db', command=lambda:open_name('pptbtn'))
                        pptbtn.grid(row=1, column=1)  #placing the button

                        #tip message while hovering over the button
                        tip.bind_widget(pptbtn, balloonmsg="Click to choose a file")

                        pptlabel=Label(ws, textvariable=my_str2, foreground='RED')
                        pptlabel.grid(row=1, column=2)
                        my_str2.set("No file selected")


                        #creating label
                        sn=Label(ws, text='Short Notes', bg='#d9eafa')
                        sn.grid(row=2, column=0, padx=10)  #placing the label

                        #creating button
                        snbtn=Button(ws, text='Choose File', bg='#65a2db', command=lambda:open_name('snbtn'))
                        snbtn.grid(row=2, column=1)  #placing the button

                        #tip message while hovering over the button
                        tip.bind_widget(snbtn, balloonmsg="Click to choose a file")

                        snlabel=Label(ws, textvariable=my_str3, foreground='RED')
                        snlabel.grid(row=2, column=2)
                        my_str3.set("No file selected")



                        #creating button
                        upld=Button(ws, text='Upload Files', command=upload_files)
                        upld.grid(row=3, column=0, pady=10)  #placing the button

                        #tip message while hovering over the button
                        tip.bind_widget(upld, balloonmsg="Click to upload your files")


                        #creating button
                        Ext=Button(ws, text='Close', bg='red', activebackground='red', command=Exit)
                        Ext.grid(row=3, column=1, pady=10)  #placing the button
                

                        #tip message while hovering over the button
                        tip.bind_widget(Ext, balloonmsg="Click to close the program")
                        
                        ws.mainloop()
                except:
                    m=Message(root,text="OOPS! something went wrong",width=300,font=('Roman', 20, 'bold'), fg='red')
                    m.pack(padx=250,pady=700)
root=Tk()
obj=login(root)
root.mainloop()

