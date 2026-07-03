import tkinter

FONT=("arial",13,"normal")

# Windows configuration
windows= tkinter.Tk()
windows.title("Miles to Kilometer converter")
windows.config(padx=20,pady=20,)


# Create Input
miles_imput= tkinter.Entry()
miles_imput.config(width=10)
miles_imput.insert(tkinter.END, string="0",)
miles_imput.grid(column=1,row=0)

def calc():
    miles = float(miles_imput.get())
    km= miles * 1.60934
    km_value_lable.config(text=km)

# create button
button= tkinter.Button(text="Calculate",font=FONT,command=calc)
button.grid(column=1,row=2)


# Create Lables
mile_lable= tkinter.Label(text="Miles",font=FONT)
mile_lable.grid(column=2,row=0)

km_lable= tkinter.Label(text= "Km",font=FONT)
km_lable.grid(column=2,row=1)

km_value_lable= tkinter.Label(text= "0",font=FONT)
km_value_lable.grid(column=1,row=1)

text= tkinter.Label(text= "is equal to",font=("arial",10,"normal"))
text.grid(column=0,row=1)


windows.mainloop()

