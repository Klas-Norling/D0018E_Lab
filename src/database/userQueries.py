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


    def post_item(self, sellerid, price, furnitureid):
        sql = "INSERT INTO Assets (SellerID, Price, FurnitureID) VALUES (%s, %s, %s)"
        val = (sellerid, price, furnitureid)
        self.mycursor.execute(sql, val)
        self.mydb.commit()

    def remove_item(self, furnitureid):
        sql_delete_query = """DELETE FROM Assets WHERE FurnitureID={}""".format(furnitureid)
        self.mycursor.execute(sql_delete_query)
        self.mydb.commit()


    def create_user(self, last_name:str, first_name:str, city:str, address:str):
        sql = "INSERT INTO Customer (CustomerID, LastName, FirstName, City, Address) VALUES (%s, %s, %s, %s, %s)"
        val = (3, "Jakobsson", "Robin", "Linköping", "Gränslevägen 23")
        self.mycursor.execute(sql, val)
        self.mydb.commit()

    def remove_user(self, customerid):
        sql_delete_query = """DELETE FROM Customer WHERE CustomerID={}""".format(customerid)
        self.mycursor.execute(sql_delete_query)
        self.mydb.commit()


    
    def create_seller(self, sellerid, last_name, first_name, city):
        sql = "INSERT INTO Seller (SellerID, LastName, FirstName, City) VALUES (%s, %s, %s, %s)"
        val = (sellerid, last_name, first_name, city)
        self.mycursor.execute(sql, val)
        self.mydb.commit()
    
    def remove_seller(self, sellerid):
        sql_delete_query = """DELETE FROM Seller WHERE SellerID={}""".format(sellerid)
        self.mycursor.execute(sql_delete_query)
        self.mydb.commit()

    
    def add_comment(self, commentid, furnitureid, customerid, comment, grading):
        sql = "INSERT INTO Comments (CommentID, FurnitureID, CustomerID, Comments, Grading) VALUES (%s, %s, %s, %s, %s)"
        val = (commentid, furnitureid, customerid, comment, grading)
        self.mycursor.execute(sql, val)
        self.mydb.commit()



    def calc_average_grading(self, furnitureid):
        sql = "SELECT Grading FROM Comments WHERE FurnitureID={}".format(furnitureid)
        self.mycursor.execute(sql)
        myresult = self.mycursor.fetchall()
        avg = 0
        i = 0
        for grading in myresult:
            avg = avg + grading[0]
            i = i + 1
        avg = avg/i

        sql2 = "UPDATE Assets SET avg_grading={} WHERE FurnitureID={}".format(avg, furnitureid)
        self.mycursor.execute(sql2)
        self.mydb.commit()
       
        



#user = User()
#user.create_user("klas", "hej", "då", "lala")
#user.add_item_shoppingbasket("chair", 200, 2, 2)
#user.remove_item_shoppingbasket(1, 1)
#user.post_item(2, 200, 2)


def test_cases_add():
    user = User()
    user.create_user("Jakobsson", "Robin", "Linköping", "Gränslevägen 23")
    user.create_seller(2, "Andersson", "Anton", "Stockholm")
    user.post_item(2, 200, 2)
    user.add_item_shoppingbasket("chair", 200, 2, 2)

def test_cases_del():
    user = User()
    user.remove_user(3)
    user.remove_item_shoppingbasket(2, 2)
    user.remove_item(2)
    user.remove_seller(2)

user = User()
#user.add_comment(1, 1, 1, "Nice post", 5)
#user.add_comment(2, 1, 2, "Pretty nice post", 4)
#user.calc_average_grading(1)
    

#test_cases_del()
test_cases_add()
