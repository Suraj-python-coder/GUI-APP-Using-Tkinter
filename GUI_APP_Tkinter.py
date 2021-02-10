# TKinter: it is a pythons standard module ,library, to use we have to import it
# pronunciation: tee-kinter or tk-inter or kinter

# NOTE: when we import tkinter library we have to write three lines compalsory which is given bellow

#  we can import tkinter in many way are as follows:

# starter code:
# ======================

# import tkinter            # 1st type to import tkinter
# from tkinter import *     # 2nd type to import tkinter ---> not preferd
import tkinter as tk        # 3rd type to import tkinter  ---> preferd to use
from tkinter import ttk     # here we import ttk class for better visual of widgets
from csv import DictWriter
import os
# win = tkinter.Tk() 
win = tk.Tk()               # here in tkinter module we get one class which name is 'Tk', and we call constructor of that classs using () 
                            #  here create object name is 'win', we can use any name like [root,window] etc. these are according to convension 
win.title('GUI')


# create label :
# =================

# widgets --> label , buttons, radio buttons -> all are in 'tk' class but we use 'ttk' class because in ttk class its representation is  better than tk class

# ttk.Label(win, text='Enter your name :').grid(row=0,column=0)   # inside ttk there are Lable class, in side () --> on which window you have to create Lable that window name,
name_label = ttk.Label(win, text='Enter your Name :')
name_label.grid(row=0,column=0, sticky=tk.W) 

email_label = ttk.Label(win, text='Enter your Email :')
email_label.grid(row=1,column=0, sticky=tk.W)

age_label = ttk.Label(win, text='Enter your Age :')
age_label.grid(row=2,column=0, sticky=tk.W) 

gender_label = ttk.Label(win, text='Select your Gender :')
gender_label.grid(row=3,column=0, sticky=tk.W) 


# create entry box:
# =====================

# here we create entry box and we write any thing in it but that written data need to store in a variable
# for this we create a variable for the box are as follows

name_var = tk.StringVar()     # here we create a variable which is in string type for this we use 'StringVar()'
name_enterybox = ttk.Entry(win, width=16, textvariable= name_var)    # here we pass that variable in textvariable 
name_enterybox.grid(row=0, column=1)
name_enterybox.focus()   #focusing corsor on the name entry box

email_var = tk.StringVar()     # here we create a variable which is in string type for this we use 'StringVar()'
email_enterybox = ttk.Entry(win, width=16, textvariable= email_var)    # here we pass that variable in textvariable 
email_enterybox.grid(row=1, column=1)

age_var = tk.StringVar()     # here we create a variable which is in string type for this we use 'StringVar()'
age_enterybox = ttk.Entry(win, width=16, textvariable= age_var)    # here we pass that variable in textvariable 
age_enterybox.grid(row=2, column=1)


# create combobox :
# ===================

# here we create combobox and we write any thing in it but that entered data need to store in a variable
# for this we create a variable for the combobox are as follows

gender_var = tk.StringVar()
gender_combobox = ttk.Combobox(win, width=14, textvariable= gender_var, state='readonly')    # here we pass 'state' using this user not write in the combobox ,he read only and select the options   ,here we create the combobox
gender_combobox['values'] = ('Male','Female','Other')  # here we give the values for combobox
gender_combobox.current(0)           # here set the value in combobox, (0) this zero is for in tuple at zeroth position 'Male' is present, it index position of tuple
gender_combobox.grid(row=3,column=1)


# create Radio button:
# ====================

usertype_var = tk.StringVar()
radiobtn1 = ttk.Radiobutton(win, text='Student',value='Student', variable=usertype_var)
radiobtn1.grid(row=4, column=0)

radiobtn2 = ttk.Radiobutton(win, text='Teacher',value='Teacher', variable=usertype_var)
radiobtn2.grid(row=4, column=1)


# create check button:
# ======================

checkbtn_var = tk.IntVar()
checkbtn = ttk.Checkbutton(win, text='check if you want to subscribe to our newsletter', variable=checkbtn_var)
checkbtn.grid(row=5,columnspan=3)   # this columnspan is used for , it don't disturb the other column ,only extend for self


# create  Button:
# ===============

# if we want that our button perform operation for that we have to create a function for performing some action
# def action():
#     username = name_var.get()
#     useremail = email_var.get()
#     userage = age_var.get()
#     print(f"Name:{username},\nAge:{userage},\nemail_id: {useremail}")
#     usergender = gender_var.get()
#     usertype = usertype_var.get()
#     if checkbtn_var.get()==0:
#         subscribed = 'NO'
#     else:
#         subscribed = 'Yes'
#     print(f'Gender:{usergender},\nTeacher/Student:{usertype},\nSubscribed:{subscribed}')
    

# storeing data in .txt file:
# =============================

#     with open('s199_file.txt','a') as f:
#         f.write(f'{username},{userage},{useremail},{usergender},{usertype},{subscribed}\n')

#     name_enterybox.delete(0,tk.END)   # this is just for,when we enter data in our gui app and click submit button, after that it clears the entry_box
#     age_enterybox.delete(0,tk.END)     # clear entry_box after click of submit button
#     email_enterybox.delete(0,tk.END)

#     # name_label.configure(foreground='Green')  # after above operation it changes the coloure of labels
#     # age_label.configure(foreground='Green')
#     # email_label.configure(foreground='Green')

#     name_label.configure(foreground='#ff9800') # we can pick colour from google also, just go on 'google colour picker' and select 'colour tool' site, after that select colour and copy its # value, and pest it in our code 
#     age_label.configure(foreground='#ff9800')
#     email_label.configure(foreground='#ff9800')

#     submit_button.configure(foreground='#33691e')  # giving submit button foreground coloure

# submit_button = tk.Button(win, text='Submit', command=action) # we use tk function just for button insted of ttk because in ttk there in no 'foreground' function 
# # submit_button = ttk.Button(win, text='Submit', command=action)  # here we pass the function name at last for button 
# submit_button.grid(row=6,column=0)

# write to CSV file:
# ====================
def action():
    username = name_var.get()
    useremail = email_var.get()
    userage = age_var.get()
    usergender = gender_var.get()
    usertype = usertype_var.get()
    if checkbtn_var.get()==0:
        subscribed = 'NO'
    else:
        subscribed = 'Yes'
    
    # write to csv file:

    with open('s199_file.csv','a',newline='') as f:
        dict_writer = DictWriter(f, fieldnames=['UserName', 'UserAge', 'UserEmail', 'UserGender', 'UserType',
         'Subscriber'])
        if os.stat('s199_file.csv').st_size==0:
            dict_writer.writeheader()
        
        dict_writer.writerow({
            'UserName' : username,
            'UserAge' : userage,
            'UserEmail' : useremail,
            'UserGender' : usergender,
            'UserType' : usertype,
            'Subscriber' : subscribed
        })

    

    name_enterybox.delete(0,tk.END)   
    age_enterybox.delete(0,tk.END)     
    email_enterybox.delete(0,tk.END)
    name_label.configure(foreground='#ff9800') 
    age_label.configure(foreground='#ff9800')
    email_label.configure(foreground='#ff9800')

    submit_button.configure(foreground='#33691e')  # giving submit button foreground coloure




submit_button = tk.Button(win, text='Submit', command=action) # we use tk function just for button insted of ttk because in ttk there in no 'foreground' function 
# submit_button = ttk.Button(win, text='Submit', command=action)  # here we pass the function name at last for button 
submit_button.grid(row=6,column=0)

win.mainloop()              # this is use for infinit loop,