from app.stlsManager import CalculateCost, FindStlFilePath

class Address:
    def __init__(self,streetAddress:str,city:str,state:str,postal:int):
        self.streetAddress = streetAddress
        self.city = city
        self.state = state
        self.postalcode = postal
    
    def __str__(self):
        return str({"streetAddress":self.streetAddress,"town": self.town ,"postal":self.postalcode})


class Payment:

    def __init__(self,firstname:str,lastname:str, address:Address,payment:float):
        self.address = address
        self.firstName = firstname
        self.lastname = lastname
        self.paymentSent = payment

    def makePayment(self, payment:float):
        self.paymentSent = payment


class Order:

    def __init__(self, address:Address,objectName:str,user:str):
        self.address = address
        self.stlFilePath = FindStlFilePath(objectName)
        self.userID = user
        self.status = "pending"
        self.price = CalculateCost(self.stlFilePath)

    def __str__(self):
        return f"Order Details:Address: {self.address} Object Name: {self.stlFilePath} User ID: {self.userID} Status: {self.status} Price: {self.price}"
    
    def makePayment(self,payment:Payment):
        if payment.paymentSent>=self.price:
            self.status = "paid"
            return True
        else:
            return False

    def confirmShipment(self):
        self.status = "shipped"

    def calculateCost(self):
        CalculateCost(self.stlFilePath)









