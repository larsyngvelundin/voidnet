import os

import psycopg2
from db_setup import get_connection
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from api_files.agents import router as agent_router
from api_files.companies import router as company_router
from api_files.listings import router as listing_router
from api_files.reviews import router as review_router
from api_files.users import router as user_router

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(agent_router, prefix="/API/agents", tags=["Agents"])
app.include_router(company_router, prefix="/API/companies", tags=["Companies"])
app.include_router(listing_router, prefix="/API/listings", tags=["Listings"])
app.include_router(review_router, prefix="/API/reviews", tags=["Reviews"])
app.include_router(user_router, prefix="/API/users", tags=["Users"])

"""
ADD ENDPOINTS FOR FASTAPI HERE
Make sure to do the following:
- Use the correct HTTP method (e.g get, post, put, delete)
- Use correct STATUS CODES, e.g 200, 400, 401 etc. when returning a result to the user
- Use pydantic models whenever you receive user data and need to validate the structure and data types (VG)
This means you need some error handling that determine what should be returned to the user
Read more: https://www.geeksforgeeks.org/10-most-common-http-status-codes/
- Use correct URL paths the resource, e.g some endpoints should be located at the exact same URL, 
but will have different HTTP-verbs.
"""


# INSPIRATION FOR A LIST-ENDPOINT - Not necessary to use pydantic models, but we could to ascertain that we return the correct values
# @app.get("/items/")
# def read_items():
#     con = get_connection()
#     items = get_items(con)
#     return {"items": items}


# INSPIRATION FOR A POST-ENDPOINT, uses a pydantic model to validate
# @app.post("/validation_items/")
# def create_item_validation(item: ItemCreate):
#     con = get_connection()
#     item_id = add_item_validation(con, item)
#     return {"item_id": item_id}


# IMPLEMENT THE ACTUAL ENDPOINTS! Feel free to remove
