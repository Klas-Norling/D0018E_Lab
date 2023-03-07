import mysql.connector

mydb = mysql.connector.connect(host="utbweb.its.ltu.se",
                                user="19990730", 
                                passwd="19990730", 
                                database="db19990730")

mycursor = mydb.cursor()

def main(a,b):
    if a=="select":
        x=a+" * from " +b
        mycursor.execute(x)
        for i in mycursor:
            print(i)
            hello=str(print(i))
            
main("select", "Customer")