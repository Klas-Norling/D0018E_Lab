import mysql.connector


class User:
    def __init__(self):
        self.mydb = mysql.connector.connect(host="utbweb.its.ltu.se", user="19990730", passwd="19990730", database="db19990730")
        self.mycursor = self.mydb.cursor()

    def add_item_shoppingbasket(self, furnitureid:int, customerid:int):
        sql = "INSERT INTO ShoppingBasket (FurnitureID, CustomerID) VALUES (%s, %s)"
        val = (furnitureid, customerid)
        self.mycursor.execute(sql, val)
        self.mydb.commimt()


    def remove_item_shoppingbasket(self, furnitureid:int, customerid:int):
        sql = "DELETE FROM ShoppingBasket WHERE = (%d, %d)"
        val = (furnitureid, customerid)
        self.mycursor.execute(sql, val)
        self.mydb.commit()


    def place_order(self, customerid:int, furnitureid:int, city:str, address:str, last_name:str, first_name:str):
        sql = "INSERT INTO Orders (CustomerID, FurnitureID, City, Address, LastName, FirstName) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (customerid, furnitureid, city, address, last_name, first_name)
        self.mycursor.execute(sql, val)
        self.mydb.commit()


    def comment_post(self, text:str):
        pass

    def remove_comment(self, commentid:int):
        pass


    def post_item(self):
        pass

    def remove_item(self, furnitureid:int):
        pass


    def create_user(self, last_name:str, first_name:str, city:str, address:str):
        pass