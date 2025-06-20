import tkinter as tk
from random import randint
win = tk.Tk()
win.title("PASSWORD GENERATOR")
win.minsize(300,300)


# Generate random strong password
def rand_num():
    #Clear Your Entry Box 
    entn.delete(0,tk.END)
    # Get Password Lenght and convert to integer
    pw_lenght = int(enyf.get())
    #Create a Variable to hold your password
    my_password  = ""
    #Loop through password Length
    for x  in range(pw_lenght):
        my_password+=chr(randint(33 ,126))
    #lets put  password output on the screen 
    entn.insert(0 ,my_password)


#copy Clickbored
def Copy_idk():
    
    # Clear the click bored 
    win.clipboard_clear()
    #copy to clipBored
    win.clipboard_append(entn.get())
    


#LabelFrame 
lblf = tk.LabelFrame(win ,text  ="HOW MANY CHARACTERS?")
lblf.grid(row = 0 , column= 0 , pady = 20  , padx = 20)

#Entry Frame
enyf = tk.Entry(lblf , font=("Helvetica" , 24))
enyf.pack(pady=20)

# Normal Entry 
entn= tk.Entry(win ,  font=("Helvetica" , 24),bd =0 ,bg = "systembuttonface")
entn.grid(row = 1 , column = 0)

# the buttons 
btnpassword  = tk.Button(win , text = 'Generate Strong Paaword ', command=rand_num)
btnpassword.grid(row = 2 , column=0, padx =20)
btnCopytoClip = tk.Button(win , text  = " Copy To Clipboad", command=Copy_idk)
btnCopytoClip.grid( row  = 3 , column=0, padx = 20, pady= 20)

win.mainloop()