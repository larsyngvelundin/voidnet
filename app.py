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


# INSPIRATION FOR A POST-ENDPOINT, uses a pydantic model to validate
# @app.post("/validation_items/")
# def create_item_validation(item: ItemCreate):
#     con = get_connection()
#     item_id = add_item_validation(con, item)
#     return {"item_id": item_id}

