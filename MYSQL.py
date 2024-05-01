import mysql.connector
from tkinter import messagebox

#B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R
def Save_Data_MySql():
    try:
        mydb = mysql.connector.connect(host='localhost', user='root', password="77492652Rt@")
        # conn = mysql.connector.connect(host = 'localhost', password = '77492652Rt@', user = 'root') 
        mycursor = mydb.cursor()
        print("Connection established!")
    except:
        messagebox.showerror("Connection", "Database connection not stablished!!")
       
        
    try:
        command = "create database Heart Data"
        mycursor.execute(command)
        
        command = "use Heart Data"
        mycursor.execute(command)


        command = "create table data(user int auto_increment key not null, Name varchar(50), Date varchar(100), DOB varchar(100), age varchar(100), sex varchar(100), Cp varchar(100), trestbps varchar(100), chol varchar(100), fbs varchar(100), restecg varchar(100), thalach varchar(100), exang varchar(100), oldpeak varchar(100), slope varchar(100), ca varchar(100), thal varchar(100), resultvarchar(100))"
        mycursor.execute(command)
        
        command = "insert into data(Name, Date, DOB, age, sex, Cp, tresbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal, Result) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        mycursor.execute(command,(B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R))
        mydb.commit() 
        mydb.close() 
        messagebox.showinfo("Register", "New User added sucessfully!!!!")
        
    except:
        mycursor.execute("use Heart Data")
        mydb = mysql.connector.connect(host='localhost', user='root', password="77492652Rt@", database = "heart_data")
        mycursor = mydb.cursor()
        
        command = "insert into data(Name, Date, DOB, age, sex, Cp, tresbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal, Result) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        mycursor.execute(command,(B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R))
        mydb.commit() 
        mydb.close() 
        messagebox.showinfo("Register", "New User added sucessfully!!!!")
        
        

        
        
        
    
    
    
    
    
    
    
    
        
        
        
Save_Data_MySql()