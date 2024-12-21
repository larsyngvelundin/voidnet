from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse

from db_setup import get_connection
from db import (
    create_listing,
    create_listing_with_names,
    read_all_listings,
    read_all_listings_combined,
    read_listing,
    read_listing_combined,
    read_listing_image_by_listing,
    read_listing_image,
)

from fastapi import APIRouter

router = APIRouter()


# post listings
@router.post("", status_code=201)
def post_listing(listing: dict):
    if (
        "agent_username" in listing
        and "location" in listing
        and "price" in listing
        and "name" in listing
        and "description" in listing
        and "category_name" in listing
        and "status_name" in listing
    ):
        try:
            con = get_connection()
            listing_id = create_listing_with_names(con, listing)
            return {"message": "Listing successfully created", "listing_id": listing_id}
        except Exception:
            raise HTTPException(
                status_code=400,
                detail=f"Unable to create listing '{listing["name"]}'",
            )
    else:
        raise HTTPException(
            status_code=400,
            detail=f"No valid listing included in request. An object with agent_username, location, price,name,description,category_name,and status_name is required. Got: {listing}",
        )


# get listings
@router.get("")
def get_listings(limit: int = 5, offset: int = 0):
    con = get_connection()
    result = read_all_listings(con, limit=limit, offset=offset)
    return result


@router.get("/combined")
def get_listings_combined(limit: int = 5, offset: int = 0):
    con = get_connection()
    result = read_all_listings_combined(con, limit=limit, offset=offset)
    return result


# get listings {id}
@router.get("/{listing_id}")
def get_listing(listing_id: int):
    con = get_connection()
    result = read_listing(con, listing_id=listing_id)
    return result


@router.get("/{listing_id}/combined")
def get_listing_combined(listing_id: int):
    con = get_connection()
    result = read_listing_combined(con, listing_id=listing_id)
    return result


# get listings {filter}


#


# put listings {id}


#


# delete listings {id}


#


# get categories

# get categories {id}


#


# get statuses

# get statuses {id}


#


# get views

# get views {listing id}

# post add_view {listing id}


#


# get entities {id}

# post entities

# put entities {id}

# delete entities {id}


#


# get listing images


# get listing images {id}
@router.get("/images/{image_id}")
def get_listing_images_by_image_id(image_id: int):
    con = get_connection()
    image_info = read_listing_image(con, image_id=image_id)
    if image_info:
        return FileResponse(image_info["image_path"])
    else:
        raise HTTPException(status_code=404, detail="Image not found")


# get listing images {listing id}
@router.get("/{listing_id}/images")
def get_listing_images_by_lsting_id(listing_id: int):
    con = get_connection()
    result = read_listing_image_by_listing(con, listing_id=listing_id)
    return result


# post listing images

# delete listing images
