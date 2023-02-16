import tkinter as tk

root = tk.Tk()
root.geometry("500x500")

def payment():
    if loan_amount_entry.get() and interest_rate_entry.get() and years_entry.get():
        loan = float(loan_amount_entry.get())
        interest_rate = float(interest_rate_entry.get())
        monthly_rate = interest_rate/1200
        years = int(years_entry.get())
        months = years*12
        payment = loan*monthly_rate/(1-(1+monthly_rate) ** (-months))
        payment= '%.2f' % payment 
        result_label.config(text=f"The monthly payment is:${payment}")
    else:
        result_label.config(text="Not enough information. Plese, provide all data")

root.title("Your mortgage calculator")
label_frame = tk.LabelFrame(root,text="Calculate your mortgage monthly payment")
label_frame.pack(pady=30)

frame = tk.Frame(label_frame)
frame.pack(pady=20,padx=20)

loan_amount_label = tk.Label(frame,text="Loan amount")
loan_amount_entry = tk.Entry(frame,font=("Helvetica", 16)) 

loan_amount_label.grid(row=0, column=0)
loan_amount_entry.grid(row=0, column=1)

interest_rate_label = tk.Label(frame,text="Interest rate")
interest_rate_entry = tk.Entry(frame,font=("Helvetica", 16)) 

interest_rate_label.grid(row=1, column=0)
interest_rate_entry.grid(row=1, column=1,pady=20)


years_label = tk.Label(frame,text="Loan term: ")
years_entry = tk.Entry(frame,font=("Helvetica", 16)) 

years_label.grid(row=2, column=0)
years_entry.grid(row=2, column=1)


button = tk.Button(label_frame,text="Get Payment",font=("Helvetica",16),cursor="arrow",command=payment)
button.pack(pady=20)

result_label = tk.Label(root,text="",font=("Helvetica",16))
result_label.pack(pady=20)

root.mainloop()
