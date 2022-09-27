from tkinter import*
mywin=Tk()
mywin['bg']="white"
mywin.title("CURRENCY CONVERTER")
mywin.geometry('840x450')


def dollarTOr():
            a= int(input_value.get())
            s=81.50
            c= a*s
            ans.delete(0,END)
            ans.insert(0,str(c))
            
def rTOdollar():
            a= int(input_value.get())
            s=81.50
            c= a/s
            ans.delete(0,END)
            ans.insert(0,str(c))

def yenTOr():
            a= int(input_value.get())
            s=0.57
            c= a*s
            ans.delete(0,END)
            ans.insert(0,str(c))

def rTOyen():
            a= int(input_value.get())
            s=0.57
            c= a/s
            ans.delete(0,END)
            ans.insert(0,str(c))

def euroTOr():
            a= int(input_value.get())
            s=78.73
            c= a*s
            ans.delete(0,END)
            ans.insert(0,str(c))

def rTOeuro():
            a= int(input_value.get())
            s=78.73
            c= a/s
            ans.delete(0,END)
            ans.insert(0,str(c))
def poundTOr():
            a= int(input_value.get())
            s=88.47
            c= a*s
            ans.delete(0,END)
            ans.insert(0,str(c))

def rTOpound():
            a= int(input_value.get())
            s=88.47
            c= a/s
            ans.delete(0,END)
            ans.insert(0,str(c))

def swiss_francTOr():
            a= int(input_value.get())
            s=82.41
            c= a*s
            ans.delete(0,END)
            ans.insert(0,str(c))

def rTOswiss_franc():
            a= int(input_value.get())
            s=82.41
            c= a/s
            ans.delete(0,END)
            ans.insert(0,str(c))

def singapore_dollarTOr():
            a= int(input_value.get())
            s=56.72
            c= a*s
            ans.delete(0,END)
            ans.insert(0,str(c))
def rTOsingapore_dollar():
            a= int(input_value.get())
            s=56.72
            c= a/s
            ans.delete(0,END)
            ans.insert(0,str(c))


                           

Label(mywin,text="~~~WIDGET TO CONVERT THE CURRENCY~~~", padx=100, pady=25, bg='white', fg='Blue', bd=7, font='system').grid(row=0,column=1)
Label(mywin,text="Input the Currency you want to convert:", padx=50, pady=15, fg='blue', bg='white').grid(row=1,column=1)
input_value=Entry(mywin,width=15)
input_value.grid(row=1,column=2) 

ans=Entry(mywin,width=15)

ans.grid(row=3,column=2)

Label(mywin,text="Required Currency:", padx=50, pady=15, fg='blue', bg='white').grid(row=3,column=1)
Entry(mywin,width=15)

Button(mywin,text="Convert from Rupee to U.S Dollar ",padx=34,pady=10, command=rTOdollar, bg='yellow').grid(row=4,column=1)
        
Button(mywin,text="Convert from U.S Dollar to Rupee ",padx=34,pady=10, command=dollarTOr, bg='yellow').grid(row=4,column=2)
        
Button(mywin,text="Convert from Rupee to Japanese Yen ",padx=25,pady=10, command=rTOyen, bg='yellow').grid(row=5,column=1)
        
Button(mywin,text="Convert from Japanese Yen to Rupee ",padx=25,pady=10, command=yenTOr, bg='yellow').grid(row=5,column=2)
        
Button(mywin,text="Convert from Rupee to Euro ",padx=48,pady=10, command=rTOeuro, bg='yellow').grid(row=6,column=1)
        
Button(mywin,text="Convert from Euro to Rupee ",padx=48,pady=10, command=euroTOr, bg='yellow').grid(row=6,column=2)
        
Button(mywin,text="Convert from Rupee to British Pound ",padx=24,pady=10, command=rTOpound, bg='yellow').grid(row=7,column=1)
        
Button(mywin,text="Convert from British Pound to Rupee ",padx=24,pady=10, command=poundTOr, bg='yellow').grid(row=7,column=2)
        
Button(mywin,text="Convert from Rupee to Swiss Franc ",padx=30,pady=10, command=rTOswiss_franc, bg='yellow').grid(row=8,column=1)
        
Button(mywin,text="Convert from Swiss Franc to Rupee ",padx=30,pady=10, command=swiss_francTOr, bg='yellow').grid(row=8,column=2)
        
Button(mywin,text="Convert from Rupee to Singapore Dollar ",padx=16,pady=10, command=rTOsingapore_dollar, bg='yellow').grid(row=9,column=1)
        
Button(mywin,text="Convert from Singapore Dollar to Rupee ",padx=16,pady=10, command=singapore_dollarTOr, bg='yellow').grid(row=9,column=2)
        
