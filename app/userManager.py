from app.orderManager import *
from fastapi.exceptions import HTTPException
class User:
    def __init__(self, fullName:str, fullAddress:str,username:str,password:str,email:str,phoneNumber:str):
        self.name = fullName
        self.address = fullAddress
        self.thingverseUsername = ""
        self.userID = username
        self.password = password
        self.email = email
        self.phoneNumber = phoneNumber
        self.objects = {}
        self.orders = {}

    def __str__(self):
        return f"User ID: {self.userID}, Name: {self.name}, Address: {self.address}, Thingverse Username: {self.thingverseUsername}, Password: {self.password}, Email: {self.email}, Phone Number: {self.phoneNumber}, Objects: {self.objects}, Orders: {self.orders}"

    
    @staticmethod
    def find_user_by_id(cls, target_user_id):
        for index, user in enumerate(cls):
            if user.userID == target_user_id:
                return user
        return None