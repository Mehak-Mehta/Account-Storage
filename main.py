from tkinter import *
from tkinter import messagebox


class Window:

# This window is created for generating password

    def __init__(self,master):
        top = self.top = Toplevel(master)
        top.title("PASSWORD")
        top.resizable(width=False,height=False)
        self.password = Label(top,text="PASSWORD",justify=CENTER,font=('Helvetica', 14))
        self.password.grid(row=0)
        self.random = Button(top,text="Generate password",command= main, justify=CENTER,font=('Helvetica', 14))
        self.random.grid(row=3)
        self.final = Label(top,text="You can view your password from the terminal",font=('Helvetica', 14))
        self.final.grid(row=6)
    

class email_add:
    
# This is for writing/ saving the details


    def __init__(self,master,n,p,e):
        self.name = n
        self.passcode = p
        self.email = e
        self.frame = master

        strN = ""
        strP = ""
        strE = ""

        for letter in self.name:
            if letter ==  '':
                strN += ""
            else:
                strN += chr(ord(letter))
        
        for letter in self.passcode:
            if letter == "":
                strP += ""
            else:
                strP += chr(ord(letter))
        
        for letter in self.email:
            if letter ==  '':
                strE += ""
            else:
                strE += chr(ord(letter))
    
        f = open("emails.txt","a")
        f.write(strN + strP + strE)
        f.close()

        self.label_name = Label(root,text=strN)
        self.label_pass = Label(root,text=strP)
        self.label_email = Label(root,text=strE)

        self.label_name.grid(row=6)
        self.label_pass.grid(row=6,column=1)
        self.label_email.grid(row=6,column=2)

        

def onsubmit():
    m = entry1.get()
    p = entry2.get()
    n = entry3.get()
    e = email_add(root, n, p, m)
    entry1.delete(0, 'end')
    entry2.delete(0, 'end')
    entry3.delete(0, 'end')
    messagebox.showinfo('Added Entity', 'Successfully Added, \n' + 'Name: ' + m + '\nEmail: ' + n + '\nPassword: ' + p)
    
    
root = Tk()
root.title("Email storage")

# final details 

m = Window(root)
root.resizable(width=False,height=False)


Name = Label(root,text="Name",font=('Helvetica',14))
password = Label(root,text="Passcode",font=('Helvetica',14))
email = Label(root,text="Email",font=('Helvetica',14))
add = Button(root,text="Add Email",command = onsubmit ,font=('Helvetica',14),justify=CENTER)

Name.grid(row = 0)
password.grid(row = 1)
email.grid(row = 2,)
add.grid(row = 3)

entry1 = Entry(root)
entry1.grid(row = 0,column=1)

entry2 = Entry(root)
entry2.grid(row = 1,column=1)

entry3 = Entry(root)
entry3.grid(row = 2,column=1)


pass_label2= Label(root, text='password: ', font=('Helvetica', 14))
email_label2= Label(root, text='email: ', font=('Helvetica', 14))
name_label2 = Label(root, text='Name: ', font=('Helvetica', 14))

pass_label2.grid(row=5,column=1)
email_label2.grid(row=5)
name_label2.grid(row=5, column=2)



root.mainloop()

