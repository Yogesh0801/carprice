from tkinter import *
import joblib
import pandas as pd


def show_entry_fields():
    p1 = float(e1.get())
    p2 = float(e2.get())
    p3 = float(e3.get())
    p4 = float(e4.get())
    p5 = float(e5.get())
    p6 = float(e6.get())
    p7 = float(e7.get())
    
    model = joblib.load('model/car_price_predictor')
    
    data_new = pd.DataFrame({
        'Present_Price': p1,
        'Kms_Driven': p2,
        'Fuel_Type': p3,
        'Seller_Type': p4,
        'Transmission': p5,
        'Owner': p6,
        'Age': p7
    }, index=[0])
    result = model.predict(data_new)
    Label(master, text="Car Purchase Amount", font=("Helvetica", 30)).place(x=200, y=600)
    Label(master, text=str(result[0]), font=("Helvetica", 30)).place(x=700, y=600)
    print("Car Purchase amount", result[0])

master = Tk()
master.title("Car Price Prediction Using Machine Learning")
master.config(bg="Green")
label = Label(master, text="Car Price Prediction Using Machine Learning", bg="black", fg="white", font=("Helvetica", 30))
label.place(x=200, y=50)

Label(master, text="Present_Price", font=("Helvetica", 18)).place(x=200, y=200)
Label(master, text="Kms_Driven", font=("Helvetica", 18)).place(x=200, y=250)
Label(master, text="Fuel_Type", font=("Helvetica", 18)).place(x=200, y=300)
Label(master, text="Seller_Type", font=("Helvetica", 18)).place(x=200, y=350)
Label(master, text="Transmission", font=("Helvetica", 18)).place(x=200, y=400)
Label(master, text="Owner", font=("Helvetica", 18)).place(x=200, y=450)
Label(master, text="Age", font=("Helvetica", 18)).place(x=200, y=500)

e1 = Entry(master, font=("Helvetica", 18))
e2 = Entry(master, font=("Helvetica", 18))
e3 = Entry(master, font=("Helvetica", 18))
e4 = Entry(master, font=("Helvetica", 18))
e5 = Entry(master, font=("Helvetica", 18))
e6 = Entry(master, font=("Helvetica", 18))
e7 = Entry(master, font=("Helvetica", 18))

e1.place(x=400, y=200)
e2.place(x=400, y=250)
e3.place(x=400, y=300)
e4.place(x=400, y=350)
e5.place(x=400, y=400)
e6.place(x=400, y=450)
e7.place(x=400, y=500)

Button(master, text='Predict', command=show_entry_fields, font=("Helvetica", 25)).place(x=300, y=700)
Button(master, text='Exit', command=exit, font=("Helvetica", 25)).place(x=500, y=700)

master.geometry("1200x1500")
mainloop()
