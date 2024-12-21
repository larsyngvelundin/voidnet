import os

import psycopg2
from dotenv import load_dotenv

load_dotenv(override=True)

SERVER = os.getenv("SERVER")
DATABASE_NAME = os.getenv("DATABASE_NAME")
USER = os.getenv("USER")
PASSWORD = os.getenv("PASSWORD")
PORT = os.getenv("PORT")


def get_connection():
    """
    Function that returns a single connection
    In reality, we might use a connection pool, since
    this way we'll start a new connection each time
    someone hits one of our endpoints, which isn't great for performance
    """
    return psycopg2.connect(
        dbname=DATABASE_NAME,
        user=USER,
        password=PASSWORD,
        host=SERVER,
        port=PORT,
    )


def create_tables():
    """
    A function to create the necessary tables for the project.
    """
    con = get_connection()

    drop_tables = """
        DROP TABLE IF EXISTS listing_entities;
        DROP TABLE IF EXISTS listing_images;
        DROP TABLE IF EXISTS listing_view_counters;
        DROP TABLE IF EXISTS user_favorites;
        DROP TABLE IF EXISTS listings;
        DROP TABLE IF EXISTS listing_categories;
        DROP TABLE IF EXISTS listing_statuses;
        DROP TABLE IF EXISTS user_images;
        DROP TABLE IF EXISTS realtor_agent_reviews;
        DROP TABLE IF EXISTS realtor_agents;
        DROP TABLE IF EXISTS realtor_companies;
        DROP TABLE IF EXISTS users;
        DROP TABLE IF EXISTS user_types;
    """

    # Implement
    create_user_types_table = """
        CREATE TABLE IF NOT EXISTS user_types(
            type_id SERIAL PRIMARY KEY,
            type_name VARCHAR(10)
        );
        INSERT INTO user_types(type_name) VALUES  ('admin'),('basic');
    """

    create_users_table = """
        CREATE TABLE IF NOT EXISTS users(
            user_id SERIAL PRIMARY KEY,
            user_type INT REFERENCES user_types(type_id) NOT NULL,
            username VARCHAR(50),
            email VARCHAR(255),
            display_name VARCHAR(50)
        );
    """

    create_user_images_table = """
        CREATE TABLE IF NOT EXISTS user_images(
            image_id SERIAL PRIMARY KEY,
            user_id INT REFERENCES users(user_id) UNIQUE NOT NULL,
            image_path VARCHAR(255)
        );
    """

    create_realtor_companies_table = """
        CREATE TABLE IF NOT EXISTS realtor_companies(
            company_id SERIAL PRIMARY KEY,
            company_name VARCHAR(50) UNIQUE
        );
    """

    # Maybe add company images

    create_realtor_agents_table = """
        CREATE TABLE IF NOT EXISTS realtor_agents(
            agent_id SERIAL PRIMARY KEY,
            user_id INT REFERENCES users(user_id) UNIQUE NOT NULL,
            company_id INT REFERENCES realtor_companies(company_id)
        );
    """

    create_realtor_agent_reviews_table = """
        CREATE TABLE IF NOT EXISTS realtor_agent_reviews(
            review_id SERIAL PRIMARY KEY,
            user_id INT REFERENCES users(user_id) NOT NULL,
            agent_id INT REFERENCES realtor_agents(agent_id) NOT NULL,
            review_rating INT NOT NULL,
            review_text TEXT
        );
    """

    create_listing_categories_table = """
        CREATE TABLE IF NOT EXISTS listing_categories(
            category_id SERIAL PRIMARY KEY,
            category_name VARCHAR(50)
        );
        INSERT INTO listing_categories(category_name)
        VALUES ('house'),('apartment'),('plot'),('building'),('unknown');
    """

    create_listing_statuses_table = """
        CREATE TABLE IF NOT EXISTS listing_statuses(
            status_id SERIAL PRIMARY KEY,
            status_name VARCHAR(50)
        );
        INSERT INTO listing_statuses(status_name) VALUES  ('listed'),('offer'),('sold'),('consumed');
    """

    create_listings_table = """
        CREATE TABLE IF NOT EXISTS listings(
            listing_id SERIAL PRIMARY KEY,
            agent_id INT REFERENCES realtor_agents(agent_id) NOT NULL,
            location VARCHAR(255) NOT NULL,
            price INT NOT NULL,
            name VARCHAR(50),
            description TEXT,
            category_id INT REFERENCES listing_categories(category_id) NOT NULL,
            status_id INT REFERENCES listing_statuses(status_id) NOT NULL,
            rooms INT,
            area_sqr_ft INT,
            floors INT,
            energy_class VARCHAR(5),
            upkeep_cost INT,
            year INT
        );
    """

    create_listing_view_counters_table = """
        CREATE TABLE IF NOT EXISTS listing_view_counters(
            view_counter_id SERIAL PRIMARY KEY,
            listing_id INT REFERENCES listings(listing_id) NOT NULL,
            views INT DEFAULT 0
        );
    """

    create_user_favorites_table = """
        CREATE TABLE IF NOT EXISTS user_favorites(
            favorite_id SERIAL PRIMARY KEY,
            listing_id INT REFERENCES listings(listing_id) NOT NULL,
            user_id INT REFERENCES users(user_id) NOT NULL,
            UNIQUE(listing_id, user_id)
        );
    """

    create_listing_entities_table = """
        CREATE TABLE IF NOT EXISTS listing_entities(
            entity_id SERIAL PRIMARY KEY,
            listing_id INT REFERENCES listings(listing_id) NOT NULL,
            entity_name VARCHAR(50),
            entity_description TEXT
        );
    """

    create_listing_images_table = """
        CREATE TABLE IF NOT EXISTS listing_images(
            image_id SERIAL PRIMARY KEY,
            listing_id INT REFERENCES listings(listing_id) NOT NULL,
            image_path VARCHAR(255)
        );
    """

    with con:
        with con.cursor() as cursor:
            cursor.execute(drop_tables)
            cursor.execute(create_user_types_table)
            cursor.execute(create_users_table)
            cursor.execute(create_user_images_table)
            cursor.execute(create_realtor_companies_table)
            cursor.execute(create_realtor_agents_table)
            cursor.execute
            (create_realtor_agent_reviews_table)
            cursor.execute(create_listing_categories_table)
            cursor.execute(create_listing_statuses_table)
            cursor.execute(create_listings_table)
            cursor.execute(create_listing_view_counters_table)
            cursor.execute(create_user_favorites_table)
            cursor.execute(create_listing_entities_table)
            cursor.execute(create_listing_images_table)


if __name__ == "__main__":
    # Only reason to execute this file would be to create new tables, meaning it serves a migration file
    create_tables()
    print("Tables created successfully.")
