from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse

from db_setup import get_connection
from db import (
    read_all_user_types,
    create_user,
    read_all_users,
    read_user,
    update_user,
    delete_user,
    create_user_image,
    read_user_image_by_user_id,
)

from fastapi import APIRouter

router = APIRouter()


@router.get("/types")
def get_user_types():
    con = get_connection()
    result = read_all_user_types(con)
    return result


@router.post("", status_code=201)
def post_users(user: dict):
    if (
        "user_type" in user
        and "username" in user
        and "email" in user
        and "display_name" in user
    ):
        try:
            con = get_connection()
            user_id = create_user(con, user)
            return user_id
        except Exception:
            raise HTTPException(
                status_code=400, detail=f"Unable to create user '{user["username"]}'"
            )
    else:
        raise HTTPException(
            status_code=400,
            detail=f"No valid user included in request. An object with user_type, username, email, and display_name is required. Got: {user}",
        )


@router.get("")
def get_users():
    con = get_connection()
    result = read_all_users(con)
    return result


@router.get("/{user_id}")
def get_user_by_id(user_id: int):
    con = get_connection()
    result = read_user(con, user_id=user_id)
    return result


@router.put("/{user_id}")
def put_user_by_id(user_id: int, updates: dict):
    con = get_connection()
    result = update_user(con, user_id=user_id, updates=updates)
    return {"message": "Update successful", "user": result}


@router.delete("/{user_id}")
def delete_user_by_id(user_id: int):
    con = get_connection()
    result = delete_user(con, user_id=user_id)
    return {"message": "Deletion successful"}


# post user image
@router.post("/{user_id}/image", status_code=201)
def post_user_image(user_id: int, image: dict):
    if "image_path" in image:
        try:
            image["user_id"] = user_id
            con = get_connection()
            image_id = create_user_image(con, image)
            return image_id
        except Exception:
            raise HTTPException(status_code=400, detail="Unable to create image")
    else:
        raise HTTPException(
            status_code=400,
            detail=f"No valid image info included in request. An object with image_path is required. Got: {image}",
        )


# get user image {id}
@router.get("/{user_id}/image")
def get_user_image(user_id: int):
    con = get_connection()
    image_info = read_user_image_by_user_id(con, user_id=user_id)
    if image_info:
        return FileResponse(image_info["image_path"])
    else:
        raise HTTPException(status_code=404, detail="Image not found")


# put user image {id}


# delete user image {id}


#


# get favorites {user id}


# get favorites {listing id}


# post favorites {user&listing id}


# delete favorites {id}
