import os
from app.orderManager import *
from app.stlsManager import *
from app.userManager import *


print("start unit test:")

adressObj = Address("1726 spring","rochester","mi",48306)

# Example usage:
try:
    filename = "example.stl"
    tech = "FFF-SomeOtherTechnology"
    infil = "10%"
    layerThick = "0.1mm"
    material = "PLA, Opaque, White"

    stl_object = STLObject(filename, tech, infil, layerThick, material)

    order1 = Order(adressObj,stl_object,"ab39")
except Exception as e:
    print(f"pass: no file caught an exception: {e}")

try:
 
    filename = "Flexi_Humpback-Whale-New_Body_v2.stl"
    tech = "FFF-SomeOtherTechnology"
    infil = "10%"
    layerThick = "0.1mm"
    material = "PLA, Opaque, White"

    stl_object = STLObject(filename, tech, infil, layerThick, material)

    order1 = Order(adressObj,stl_object,"ab39")
    print("pass: made order" + str(order1))
except Exception as e:
    print(f"fail: no order made: {e}")

paymentFail = Payment("and","ball","1726 spring creek dr rochester",order1.price-2)
resultofpayment = order1.makePayment(paymentFail)
if resultofpayment==False:
    print("pass: payment failed with not enough paid")
else:
    print("fail: passed with short payment")

paymentFail = Payment("and","ball","1726 spring creek dr rochester",order1.price)
resultofpayment = order1.makePayment(paymentFail)
if resultofpayment==True:
    print("pass: payment passed with just enough")
else:
    print("fail: failed with just enough paid")

paymentFail = Payment("and","ball","1726 spring creek dr rochester",order1.price+2)
resultofpayment = order1.makePayment(paymentFail)
if resultofpayment==True:
    print("pass: payment passed with extra paid")
else:
    print("fail: failed with extra paid")

users = []
try:
    users.append(User("andersen ball","1726 spring creek dr","ab39","zas","andersen@gmail.com","412-023-2133"))
    users.append(User("amanda","1726 spring creek dr","ak00","zas","amand@gmail.com","812-123-2133"))
    users.append(User("mike","1726 spring creek dr","mike","asd","mike@gmail.com","812-021-2133"))


    print("pass: made users succesful ")
except Exception as e:
    print(f"fail: errored while making users{e}")

resultFindUser = User.find_user_by_id(users,'ab39')
if resultFindUser == None:
    print("Fail: user exist but failed")
else:
    print("Pass found user",resultFindUser)

resultFindUser = User.find_user_by_id(users,'a39')
if resultFindUser == None:
    print("Pass: user doesnt exist: a39")
else:
    print("Fail: found user when user shouldnt exist",resultFindUser)


resultFindUser = User.login(users,'ab39','zass')
if resultFindUser == False:
    print("Pass: incorrect password typed in")
else:
    print("Fail: incorrect password typed in still success")
    
resultFindUser = User.login(users,'ab39','zas')
if resultFindUser == True:
    print("Pass: correct password typed in")
else:
    print("Fail: correct password typed in and failed ")

# Example usage:
filename = "example.stl"
tech = "FFF-SomeOtherTechnology"
infil = "20%"
layerThick = "0.1mm"
material = "PLA, Opaque, White"

stl_object = STLObject(filename, tech, infil, layerThick, material)

if stl_object.layerThickness == .1:
    print("pass: layer thickness",stl_object.layerThickness)
else:
    print("fail: layerthickness ")

if stl_object.Infil == 20:
    print("pass: infil",stl_object.Infil)
else:
    print("fail: infil",stl_object.Infil)