import mysql.connector

class Admin():
    def __init__(self):
        self.mydb = mysql.connector.connect(host="utbweb.its.ltu.se", user="19990730", passwd="19990730", database="db19990730")
        self.mycursor = self.mydb.cursor()

    def remove_asset(self, sellerid:int):
        sql_delete_query = """DELETE FROM Assets WHERE SellerID = {}""".format(sellerid)
        self.mycursor.execute(sql_delete_query)
        self.mydb.commit()

    def remove_customer(self, customerid:int):
        sql_delete_query = """DELETE FROM Customer WHERE CustomerID = {}""".format(customerid)
        id = customerid
        self.mycursor.execute(sql_delete_query)
        self.mydb.commit()

    def remove_seller(self, sellerid:int):
        self.mycursor.execute("DELETE FROM Seller WHERE SellerID = {}".format(sellerid))
        self.mydb.commit()

    def testinsert(self):
        sql = "INSERT INTO Customer (CustomerID, LastName, FirstName, City, Address) VALUES (%s, %s, %s, %s, %s)"
        val = (1, "Norling", "Emil", "Sandviken", "Professors")
        self.mycursor.execute(sql, val)
        self.mydb.commit()


admin = Admin()
admin.remove_customer(2)


  