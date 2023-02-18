import mysql.connector

class Admin():
    def __init__(self):
        self.mydb = mysql.connector.connect(host="utbweb.its.ltu.se", user="19990730", passwd="19990730", database="db19990730")
        self.mycursor = self.mydb.cursor()

    def remove_asset(self, furtnitureid:int):
        #Maybe furnitureID needs to be a string
        self.mycursor.execute("DELETE FROM Asset WHERE FurnitureID={}".format(furtnitureid))
        self.mydb.commit()

    def remove_customer(self, customerid:int):
        sql = "DELETE FROM Customer WHERE CustomerID = %d"
        id = (customerid)
        self.mycursor.execute(sql, id)
        self.mydb.commit()

    def remove_seller(self, sellerid:int):
        self.mycursor.execute("DELETE FROM Seller WHERE SellerID={}".format(sellerid))
        self.mydb.commit()

    def testinsert(self):
        sql = "INSERT INTO Customer (CustomerID, LastName, FirstName, City, Address) VALUES (%s, %s, %s, %s, %s)"
        val = (1, "Norling", "Klas", "Luleå", "Professors")
        self.mycursor.execute(sql, val)
        self.mydb.commit()


admin = Admin()
admin.remove_customer(1)


  