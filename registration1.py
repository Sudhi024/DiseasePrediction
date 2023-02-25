from tkinter import *
import sqlite3
import re 
from tkinter import messagebox
from login2 import *

class regist:
# root = Tk()
 def __init__(self,root):
  self.root= root
  root.title("Registration Form")
  root.geometry('500x500')
  #Button(root, text='Reset',width=20,bg='brown',fg='white',command=validation).place(x=180,y=430)
  # Centering Root Window on Screen

  w = 500 # width for the Tk root
  h = 500 # height for the Tk root

  # get screen width and height
  ws = root.winfo_screenwidth() # width of the screen
  hs = root.winfo_screenheight() # height of the screen

  # calculate x and y coordinates for the Tk root window
  x = (ws/2) - (w/2)
  y = (hs/2) - (h/2)


  root["bg"] = '#98fb98'
  # set the dimensions of the screen 
  # and where it is placed
  root.geometry('%dx%d+%d+%d' % (w, h, x, y))

  self.Name=StringVar()
  self.Email=StringVar()
  self.Phno =StringVar()
  self.Uid=StringVar()
  self.Pswd=StringVar()

  self.label_0 = Label(self.root, text="Registration Form",width=20,font=("Courier New", 20, "bold"),bg='#98fb98',fg='red')

  self.label_0.place(x=90,y=53)


  self.label_1 = Label(self.root, text="Name",width=15,font=("bold", 10),bg='#98fb98', anchor='w')
  self.label_1.place(x=70,y=130)

  self.entry_1 = Entry(self.root,textvar=self.Name)
  self.entry_1.place(x=180,y=130)

  self.label_2 = Label(self.root, text="Email",width=15,font=("bold", 10),bg='#98fb98', anchor='w')
  self.label_2.place(x=70,y=180)

  self.entry_2 = Entry(self.root,textvar=self.Email)
  self.entry_2.place(x=180,y=180)

  self.label_3 = Label(self.root, text="Phone",width=15,font=("bold", 10),bg='#98fb98', anchor='w')
  self.label_3.place(x=70,y=230)

  c=self.root.register(self.only_numeric_input)
  self.entry_3 = Entry(self.root,textvar=self.Phno,validate="key",validatecommand=(c,'%P'))
  self.entry_3.place(x=180,y=230)


  self.label_4 = Label(self.root, text="User Id",width=15,font=("bold", 10),bg='#98fb98', anchor='w')
  self.label_4.place(x=70,y=280)

  self.entry_4 = Entry(self.root,textvar=self.Uid)
  self.entry_4.place(x=180,y=280)


  self.label_5 = Label(self.root, text="Password",width=15,font=("bold", 10),bg='#98fb98', anchor='w')
  self.label_5.place(x=70,y=330)

  self.entry_5 = Entry(self.root,textvar=self.Pswd,show='*')
  self.entry_5.place(x=180,y=330)

  Button(self.root, text='Submit',width=15,bg='brown',fg='white',command=self.database).place(x=350,y=180)
  Button(self.root, text='Reset',width=15,bg='brown',fg='white',command=self.df1).place(x=350,y=230)
  Button(self.root, text='Exit',width=15,bg='brown',fg='white',command=self.logform).place(x=350,y=280)

 def only_numeric_input(self,e):
  #this is allowing all numeric input
  if e.isdigit():
   return True
  #this will allow backspace to work
  elif e=="":
   return True
  else:
   return False

 def logform(self):
  #Do the work done by the main of Login2.py
  #Destroy current window
  self.root.destroy()
  #Open new window
  newroot = Tk()
  application = User_Login(newroot)
  newroot.mainloop()

 def df1(self):
  exp=''
  self.Name.set(exp)
  self.Email.set(exp)
  self.Phno.set(exp)
  self.Uid.set(exp)
  self.Pswd.set(exp)
   
 def validation(self):
  name1=self.Name.get()
  email=self.Email.get()
  phno1=self.Phno.get()
  uid1=self.Uid.get()
  pswd1=self.Pswd.get()
  valemail=self.checkemail(email)
  ip=len(name1) != 0 and len(email) != 0 and len(phno1) != 0 and len(uid1) != 0 and len(pswd1) != 0 and valemail=="Valid Email"
  return ip

 def checkemail(self,email):  
  regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'

  # pass the regualar expression and the string in search() method 
  if(re.search(regex,email)):  
   return "Valid Email"
       
  else:  
   return "Invalid Email"
      

 def checkuser(self,userdet):
  cu=1
  cu1=0
  conn = sqlite3.connect('DiseasePred.db')
  c = conn.cursor()
  # select only the field "username" from the table
  c.execute("SELECT Username FROM Register where Username=?", (userdet,)) 
  #c.execute("SELECT * FROM tasks WHERE priority=?", (priority,))
  # build a set with all names, from the results given as [('name1',), ('name2',), ('name3',)]
  names = {name[0] for name in c.fetchall()}
  #for n in c.fetchall():
  if userdet in names: 
   return cu
  else:
   return cu1

 def database(self):
  name1=self.Name.get()
  email=self.Email.get()
  phno1=self.Phno.get()
  uid1=self.Uid.get()
  pswd1=self.Pswd.get()
  conn = sqlite3.connect('DiseasePred.db')
  with conn:
   cursor=conn.cursor()
  cursor.execute('CREATE TABLE IF NOT EXISTS Register(Name TEXT,Email TEXT,Phno TEXT,Username TEXT,Password TEXT)')

  ip1=self.validation()   
  if self.checkuser(uid1) == 1:
   messagebox.showinfo("Status", "User Exists")            
  else:
   if ip1==1:
    cursor.execute('INSERT INTO Register VALUES(?,?,?,?,?)',(name1,email,phno1,uid1,pswd1))
    conn.commit()
    messagebox.showinfo("Status", "Registration successful")
    self.df1() 
   else:
    messagebox.showinfo("Status", "All fields are mandatory and Give Correct Values.")

if __name__ == '__main__':

 root = Tk()

 application=regist(root)
 #root.geometry('500x500') 
 root.mainloop()





