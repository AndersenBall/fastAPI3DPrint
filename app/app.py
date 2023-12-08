# -*- coding: utf-8 -*-
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.orderManager import *
from app.stlsManager import *
from app.userManager import *
from typing import Union
import time
import json
import shutil
import os

timestr = time.strftime("%Y%m%d-%H%M%S")
from fastapi import FastAPI, File, UploadFile, Body, HTTPException, Request

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_DIR = "uploads"

# Ensure the UPLOAD_DIR exists
os.makedirs(UPLOAD_DIR, exist_ok=True)

app = FastAPI()

# Front End Files
app.mount("/static", StaticFiles(directory="static"), name="static")
# Configure templates
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    # Render the specified HTML file using Jinja2Templates
    return templates.TemplateResponse("login.html", {"request": request})

@app.get("/shop", response_class=HTMLResponse)
async def read_root(request: Request):
    # Render the specified HTML file using Jinja2Templates
    return templates.TemplateResponse("shop.html", {"request": request})

@app.get("/login", response_class=HTMLResponse)
async def read_root(request: Request):
    # Render the specified HTML file using Jinja2Templates
    return templates.TemplateResponse("login.html", {"request": request})
                                                     
@app.get("/userRegistration", response_class=HTMLResponse)
async def read_root(request: Request):
    # Render the specified HTML file using Jinja2Templates
    return templates.TemplateResponse("userRegistration.html", {"request": request})

@app.get("/checkout", response_class=HTMLResponse)
async def read_root(request: Request):
    # Render the specified HTML file using Jinja2Templates
    return templates.TemplateResponse("checkout.html", {"request": request})

orders = []
users = []


@app.get("/")
def read_root():
    return {"Hello": "Fast"}

@app.post("/userAuthent/newUser")
def new_user(
    fullName: str = Body(...),
    fullAddress: str = Body(...),
    username: str = Body(...),
    password: str = Body(...),
    email: str = Body(...),
    phoneNumber: str = Body(...),
):
    try:
        if User.find_user_by_id(users,username) is not None:
            raise HTTPException(status_code=409, detail='User already exists')
        
        newUser = User(fullName, fullAddress, username, password, email, phoneNumber)
        users.append(newUser)
        return {"Hello": str(users[-1])}
    
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/userAuthent/allUsers")
def read_all_Users():
    return {"users": [str(user) for user in users]}

@app.get("/userAuthent/GetUser/{userid}")
def getUserId(userid:str):
    user = User.find_user_by_id(users,userid)
    if user == None:
        raise HTTPException(status_code=404, detail="user not found")
    return {user}

@app.post("/checkout/newOrder")
def new_order(
    street: str = Body(...),
    town: str = Body(...),
    postal: int = Body(...),
    modelName: str = Body(...),
    userName: str = Body(...),
):
    try:
        #TODO add code to connect this directly to a user and check that a user exists
        neworder = Order(Address(street, town, postal), modelName, userName)
        orders.append(neworder)
        return {"Hello": str(orders[-1])}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/checkout/allorders")
def read_all_orders():
    return {"orders": [str(order) for order in orders]}


@app.get("/checkout/orders/{orderID}")
def read_order(orderID: int):
    try:
        return {"order": str(orders[orderID])}
    except IndexError:
        raise HTTPException(status_code=404, detail="Order not found")


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    try:
        return Upload_File(file)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/calcfileCost/{filename}")
async def calcfileCost(filename: str):
    try:
        return Calc_Cost(filename)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="File not found")
