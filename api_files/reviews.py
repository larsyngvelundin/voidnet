from fastapi import FastAPI, HTTPException

from db_setup import get_connection
from db import (
    create_realtor_agent_review,
    read_all_realtor_agent_reviews,
    read_realtor_agent_review,
    update_realtor_agent_review,
    delete_realtor_agent_review,
)

from fastapi import APIRouter

router = APIRouter()

# get reviews

# get reviews {review id}

# get reviews {agent id}

# get review_score {agent id}

# post reviews

# put reviews {id}

# delete reviews {id}
