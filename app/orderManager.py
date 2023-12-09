from app.stlsManager import Calc_Cost, FindStlFilePath
from app.stlsManager import *

class Address:
    def __init__(self,streetAddress:str,city:str,state:str,postal:int):
        self.streetAddress = streetAddress
        self.city = city
        self.state = state
        self.postalcode = postal
    
    def __str__(self):
        return str({"streetAddress":self.streetAddress,"town": self.city ,"postal":self.postalcode})


class Payment:

    def __init__(self,firstname:str,lastname:str, address:str,payment:float):
        self.address = address
        self.firstName = firstname
        self.lastname = lastname
        self.paymentSent = payment

    

class Order:

    def __init__(self, address:str,stlObj:STLObject,user:str):
        self.address = address
        self.stlObj = stlObj
        self.stlFilePath = FindStlFilePath(self.stlObj.filename)
        self.userID = user
        self.status = "pending"
        self.price = Calc_Cost(self.stlObj)["content"]

    def __str__(self):
        return f"Order Details:Address: {self.address} Object: {self.stlObj} User ID: {self.userID} Status: {self.status} Price: {self.price}"
    
    def makePayment(self,payment:Payment):
        if payment.paymentSent>=self.price:
            self.status = "paid"
            return True
        else:
            return False

    def confirmShipment(self):
        self.status = "shipped"

    def calculateCost(self):
        Calc_Cost(self.stlFile)["content"]









