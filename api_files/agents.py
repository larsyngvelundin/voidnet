from fastapi import FastAPI, HTTPException

from db_setup import get_connection
from db import (
    create_agent,
    read_all_agents,
    read_all_agents_combined,
    read_agent,
    update_agent,
    delete_agent,
)

from fastapi import APIRouter

router = APIRouter()

# post agents


# get agents
@router.get("")
def get_agents():
    con = get_connection()
    result = read_all_agents(con)
    return result


# get agents {id}


# get agents combined
@router.get("/combined")
def get_agents_combined():
    con = get_connection()
    result = read_all_agents_combined(con)
    return result


# put agents {id}


# delete agents {id}
