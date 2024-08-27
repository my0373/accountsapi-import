
import random
from fastapi import FastAPI
from typing import List
from random import randint
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
import json
from datetime import datetime, timedelta


app = FastAPI()

def get_random_first_name():
    first_names = ['John', 'Jane', 'Michael', 'Emily', 'David', 'Olivia']
    return random.choice(first_names)

def get_random_family_name():
    family_names = ['Smith', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis']
    return random.choice(family_names)

def get_random_dob():
    current_date = datetime.now()
    days = random.randint(0, 20000)

    random_date = current_date - timedelta(days)
    return random_date.strftime("%Y-%m-%d")

def get_random_account_balance():
    return random.randint(-3000, 120000)

def get_random_classifier():
    return random.randint(1, 14)

def get_random_date():
    current_date = datetime.now()
    start_date = current_date - timedelta(days=3650)  # 10 years ago
    end_date = current_date - timedelta(days=1)  # Yesterday
    random_date = random_date = current_date - timedelta(days=random.randint(1, 3650))
    return random_date.strftime("%Y-%m-%d")

def get_random_account():
    return {
        'first_name': get_random_first_name(),
        'family_name': get_random_family_name(),
        'dob': get_random_dob(),
        'account_balance': get_random_account_balance(),
        'account_type': get_random_classifier(),
        'account_opened': get_random_date(),
    }

@app.get("/accounts")
def get_accounts():
    customers = [get_random_account() for i in range(1,200)]  
    customer_accounts = JSONResponse(content=jsonable_encoder(customers))
    return customer_accounts
    
 