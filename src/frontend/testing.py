import mysql.connector


class User:
    def __init__(self):
        self.mydb = mysql.connector.connect(host="utbweb.its.ltu.se", user="19990730", passwd="19990730", database="db19990730")
        self.mycursor = self.mydb.cursor()

    def add_item_shoppingbasket(self, furniture, price, furnitureid:int, customerid:int):
        sql = "INSERT INTO ShoppingBasket (Furniture, Price, CustomerID, FurnitureID) VALUES (%s, %s, %s, %s)"
        val = (furniture, price, customerid, furnitureid)
        self.mycursor.execute(sql, val)
        self.mydb.commit()


    def remove_item_shoppingbasket(self, furnitureid:int, customerid:int):
        sql_delete_query = """DELETE FROM ShoppingBasket WHERE CustomerID={} AND FurnitureID={}""".format(customerid, furnitureid)
        self.mycursor.execute(sql_delete_query)
        self.mydb.commit()


    def place_order(self, customerid:int, furnitureid:int, city:str, address:str, last_name:str, first_name:str):
        sql = "INSERT INTO Orders (CustomerID, Furniture, CustomerID, LastName, FirstName, City) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (customerid, furnitureid, city, address, last_name, first_name)
        self.mycursor.execute(sql, val)
        self.mydb.commit()


    def comment_post(self, text:str):
        pass

    def remove_comment(self, commentid:int):
        pass


    def post_item(self, sellerid, price, furnitureid):
        sql = "INSERT INTO Assets (SellerID, Price, FurnitureID) VALUES (%s, %s, %s)"
        val = (sellerid, price, furnitureid)
        self.mycursor.execute(sql, val)
        self.mydb.commit()

    def remove_item(self, furnitureid:int):
        pass

    def create_user(self, last_name:str, first_name:str, city:str, address:str):
        sql = "INSERT INTO Customer (CustomerID, LastName, FirstName, City, Address) VALUES (%s, %s, %s, %s, %s)"
        val = (1, "Norling", "Emil", "Sandviken", "Professors")
        self.mycursor.execute(sql, val)
        self.mydb.commit()


def handle_click():
    mydb = mysql.connector.connect(host="utbweb.its.ltu.se", user="19990730", passwd="19990730", database="db19990730", auth_plugin="mysql_native_password")
    mycursor = mydb.cursor()
    sql_delete_query = """DELETE FROM ShoppingBasket WHERE CustomerID={} AND FurnitureID={}""".format(1, 1)
    mycursor.execute(sql_delete_query)
    mydb.commit()


    





    


