import os

import psycopg2
from db_setup import get_connection
from fastapi import FastAPI, HTTPException
from db import (
    create_agent_with_names,
    create_company,
    create_listing_image,
    create_listing_with_names,
    create_user,
    create_user_image,
)

app = FastAPI()


def add_placeholders():
    """
    A function to generate placeholder data for testing purposes.
    """
    con = get_connection()

    # USERS
    users = [
        {
            "user_type": 2,
            "username": "dralrizen",
            "email": "dralrizen@void.net",
            "display_name": "dralrizen",
        },
        {
            "user_type": 2,
            "username": "saran",
            "email": "saran@void.net",
            "display_name": "saran",
        },
        {
            "user_type": 2,
            "username": "vegozath",
            "email": "vegozath@void.net",
            "display_name": "vegozath",
        },
        {
            "user_type": 2,
            "username": "gellmezun",
            "email": "gellmezun@void.net",
            "display_name": "gellmezun",
        },
        {
            "user_type": 2,
            "username": "xelramuth",
            "email": "xelramuth@void.net",
            "display_name": "xelramuth",
        },
        {
            "user_type": 1,
            "username": "okosok",
            "email": "okosok@void.net",
            "display_name": "okosok",
        },
        {
            "user_type": 2,
            "username": "ozokach",
            "email": "ozokach@void.net",
            "display_name": "ozokach",
        },
        {
            "user_type": 2,
            "username": "tostranoch",
            "email": "tostranoch@void.net",
            "display_name": "tostranoch",
        },
        {
            "user_type": 2,
            "username": "masked_woman",
            "email": "masked_woman@void.net",
            "display_name": "masked_woman",
        },
        {
            "user_type": 2,
            "username": "oggok",
            "email": "oggok@void.net",
            "display_name": "oggok",
        },
        {
            "user_type": 2,
            "username": "sorthrunoth",
            "email": "sorthrunoth@void.net",
            "display_name": "sorthrunoth",
        },
        {
            "user_type": 2,
            "username": "tekniaku",
            "email": "tekniaku@void.net",
            "display_name": "tekniaku",
        },
        {
            "user_type": 2,
            "username": "venel",
            "email": "venel@void.net",
            "display_name": "venel",
        },
        {
            "user_type": 2,
            "username": "zorzoxoth",
            "email": "zorzoxoth@void.net",
            "display_name": "zorzoxoth",
        },
        {
            "user_type": 2,
            "username": "mr_zaqol",
            "email": "mr_zaqol@void.net",
            "display_name": "mr_zaqol",
        },
        {
            "user_type": 2,
            "username": "jason",
            "email": "jason@void.net",
            "display_name": "jason",
        },
        {
            "user_type": 2,
            "username": "tulvag",
            "email": "tulvag@void.net",
            "display_name": "tulvag",
        },
        {
            "user_type": 2,
            "username": "arkaroth",
            "email": "arkaroth@void.net",
            "display_name": "arkaroth",
        },
        {
            "user_type": 2,
            "username": "erelith",
            "email": "erelith@void.net",
            "display_name": "erelith",
        },
        {
            "user_type": 2,
            "username": "tara",
            "email": "tara@void.net",
            "display_name": "tara",
        },
        {
            "user_type": 2,
            "username": "drog",
            "email": "drog@void.net",
            "display_name": "drog",
        },
        {
            "user_type": 2,
            "username": "kollmonnoth",
            "email": "kollmonnoth@void.net",
            "display_name": "kollmonnoth",
        },
        {
            "user_type": 2,
            "username": "the_adjuster",
            "email": "the_adjuster@void.net",
            "display_name": "the_adjuster",
        },
        {
            "user_type": 2,
            "username": "dalvollath",
            "email": "dalvollath@void.net",
            "display_name": "dalvollath",
        },
        {
            "user_type": 2,
            "username": "agotiza",
            "email": "agotiza@void.net",
            "display_name": "agotiza",
        },
        {
            "user_type": 2,
            "username": "detneth",
            "email": "detneth@void.net",
            "display_name": "detneth",
        },
        {
            "user_type": 2,
            "username": "ur'guth",
            "email": "ur'guth@void.net",
            "display_name": "ur'guth",
        },
        {
            "user_type": 2,
            "username": "danger",
            "email": "danger@void.net",
            "display_name": "danger",
        },
        {
            "user_type": 2,
            "username": "maulgum",
            "email": "maulgum@void.net",
            "display_name": "maulgum",
        },
        {
            "user_type": 2,
            "username": "daedon",
            "email": "daedon@void.net",
            "display_name": "daedon",
        },
        {
            "user_type": 2,
            "username": "igthadoth",
            "email": "igthadoth@void.net",
            "display_name": "igthadoth",
        },
        {
            "user_type": 2,
            "username": "rag'drezos",
            "email": "rag'drezos@void.net",
            "display_name": "rag'drezos",
        },
        {
            "user_type": 2,
            "username": "jaglas",
            "email": "jaglas@void.net",
            "display_name": "jaglas",
        },
        {
            "user_type": 2,
            "username": "vigdrozod",
            "email": "vigdrozod@void.net",
            "display_name": "vigdrozod",
        },
        {
            "user_type": 2,
            "username": "ogmiman",
            "email": "ogmiman@void.net",
            "display_name": "ogmiman",
        },
        {
            "user_type": 2,
            "username": "sargokog",
            "email": "sargokog@void.net",
            "display_name": "sargokog",
        },
        {
            "user_type": 2,
            "username": "bralran",
            "email": "bralran@void.net",
            "display_name": "bralran",
        },
    ]
    for user in users:
        create_user(con, user)

    user_images = [
        {
            "user_id": 1,
            "image_path": "img/users/dralrizen.jpg",
        },
        {
            "user_id": 2,
            "image_path": "img/users/saran.jpg",
        },
        {
            "user_id": 3,
            "image_path": "img/users/vegozath.jpg",
        },
        {
            "user_id": 4,
            "image_path": "img/users/gellmezun.jpg",
        },
        {
            "user_id": 5,
            "image_path": "img/users/xelramuth.jpg",
        },
        {
            "user_id": 6,
            "image_path": "img/users/okosok.jpg",
        },
        {
            "user_id": 7,
            "image_path": "img/users/ozokach.jpg",
        },
        {
            "user_id": 8,
            "image_path": "img/users/tostranoch.jpg",
        },
        {
            "user_id": 9,
            "image_path": "img/users/masked_woman.jpg",
        },
        {
            "user_id": 10,
            "image_path": "img/users/oggok.jpg",
        },
        {
            "user_id": 11,
            "image_path": "img/users/sorthrunoth.jpg",
        },
        {
            "user_id": 12,
            "image_path": "img/users/tekniaku.jpg",
        },
        {
            "user_id": 13,
            "image_path": "img/users/venel.jpg",
        },
        {
            "user_id": 14,
            "image_path": "img/users/zorzoxoth.jpg",
        },
        {
            "user_id": 15,
            "image_path": "img/users/mr_zaqol.jpg",
        },
        {
            "user_id": 16,
            "image_path": "img/users/jason.jpg",
        },
        {
            "user_id": 17,
            "image_path": "img/users/tulvag.jpg",
        },
        {
            "user_id": 18,
            "image_path": "img/users/arkaroth.jpg",
        },
        {
            "user_id": 19,
            "image_path": "img/users/erelith.jpg",
        },
        {
            "user_id": 20,
            "image_path": "img/users/tara.jpg",
        },
        {
            "user_id": 21,
            "image_path": "img/users/drog.jpg",
        },
        {
            "user_id": 22,
            "image_path": "img/users/kollmonnoth.jpg",
        },
        {
            "user_id": 23,
            "image_path": "img/users/the_adjuster.jpg",
        },
        {
            "user_id": 24,
            "image_path": "img/users/dalvollath.gif",
        },
        {
            "user_id": 25,
            "image_path": "img/users/agotiza.jpg",
        },
        {
            "user_id": 26,
            "image_path": "img/users/detneth.jpg",
        },
        {
            "user_id": 27,
            "image_path": "img/users/ur'guth.jpg",
        },
        {
            "user_id": 28,
            "image_path": "img/users/danger.jpg",
        },
        {
            "user_id": 29,
            "image_path": "img/users/maulgum.jpg",
        },
        {
            "user_id": 30,
            "image_path": "img/users/daedon.jpg",
        },
        {
            "user_id": 31,
            "image_path": "img/users/igthadoth.jpg",
        },
        {
            "user_id": 32,
            "image_path": "img/users/rag'drezos.jpg",
        },
        {
            "user_id": 33,
            "image_path": "img/users/jaglas.jpg",
        },
        {
            "user_id": 34,
            "image_path": "img/users/vigdrozod.jpg",
        },
        {
            "user_id": 35,
            "image_path": "img/users/ogmiman.jpg",
        },
        {
            "user_id": 36,
            "image_path": "img/users/sargokog.jpg",
        },
        {
            "user_id": 37,
            "image_path": "img/users/bralran.jpg",
        },
    ]

    for image in user_images:
        create_user_image(con, image=image)

    companies = [
        {"company_name": "Gnome Inc."},
        {"company_name": "Zanoth"},
        {"company_name": "AE Realty"},
        {"company_name": "SKINAMARINK"},
        {"company_name": "Dorcelessness"},
        {"company_name": "друг компания"},
        {"company_name": "Boo"},
    ]
    for company in companies:
        create_company(con, company)

    agents = [
        {"username": "the_adjuster", "company_name": "Gnome Inc."},
        {"username": "gellmezun", "company_name": "Gnome Inc."},
        {"username": "danger", "company_name": "Zanoth"},
        {"username": "mr_zaqol", "company_name": "AE Realty"},
        {"username": "maulgum", "company_name": "SKINAMARINK"},
        {"username": "rag'drezos", "company_name": "Dorcelessness"},
        {"username": "drog", "company_name": "друг компания"},
        {"username": "saran", "company_name": "Boo"},
    ]
    for agent in agents:
        create_agent_with_names(con, agent)

    listings = [
        {  # Backrooms D
            "agent_username": "maulgum",
            "location": "void",
            "price": 20000,
            "name": "Spacious living space",
            "description": "Very open concept. Hard to enter, even harder to leave.",
            "category_name": "plot",
            "status_name": "listed",
        },
        {  # Subway A
            "agent_username": "gellmezun",
            "location": "Somewhere in Russia",
            "price": 20000,
            "name": "Subway station with a rich history",
            "description": "The history is a genocide that occured in the 1990s. The spirits from this event still roam the area.",
            "category_name": "unknown",
            "status_name": "listed",
        },
        {  # Church A
            "agent_username": "the_adjuster",
            "location": "New Mexico",
            "price": 20000,
            "name": "The Sanctuary",
            "description": "Nestled in the tranquil heart of a picturesque village, The Sanctuary offers a unique living experience for those seeking a residence steeped in history and mystique. Originally constructed in the early 19th century, this charming structure retains much of its original architecture, with a beautifully preserved facade and intricately crafted wooden pews. The Sanctuary boasts an expansive interior that radiates an ethereal aura, featuring vaulted ceilings and stunning stained-glass windows that create a kaleidoscope of color as light filters through. The antique benches within The Sanctuary seem perpetually occupied by silent, ephemeral entities, described by visitors as a tranquil congregation of spirits that appear to be in a state of peaceful repose. These luminous inhabitants seem rooted to the church benches, adding an element of serene constancy to this historic abode. Sightings are most common during twilight hours, although these otherworldly residents pose no known threat to corporeal beings and appear entirely disinterested in the affairs of the living.",
            "category_name": "building",
            "status_name": "listed",
        },
    ]
    for listing in listings:
        create_listing_with_names(con, listing=listing)

    listing_images = [
        {"listing_id": 1, "image_path": "img/locations/backroomsd1.jpg"},
        # {"listing_id": 2, "image_path": "img/locations/subwaya1.jpg"},
        # {"listing_id": 2, "image_path": "img/locations/subwaya2.jpg"},
        {"listing_id": 2, "image_path": "img/locations/subwaya3.jpg"},
        {"listing_id": 3, "image_path": "img/locations/churcha1.jpg"},
    ]

    for image in listing_images:
        create_listing_image(con, image=image)


if __name__ == "__main__":
    add_placeholders()
    print("Placeholders added successfully.")
