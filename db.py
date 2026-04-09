# import psycopg2
# from psycopg2.extras import RealDictCursor


def read_all_user_types(con):
    # with con:
    #     with con.cursor(cursor_factory=RealDictCursor) as cursor:
    #         cursor.execute("SELECT * FROM user_types")
    #         result = cursor.fetchall()
    # return result
    pass


def read_all_users(con):
    # with con:
    #     with con.cursor(cursor_factory=RealDictCursor) as cursor:
    #         cursor.execute("SELECT * FROM users")
    #         result = cursor.fetchall()
    # return result
    pass


def read_user(con, user_id: int):
    # with con:
    #     with con.cursor(cursor_factory=RealDictCursor) as cursor:
    #         query = "SELECT * FROM users WHERE user_id = %s"
    #         cursor.execute(query, (user_id,))
    #         result = cursor.fetchone()
    # return result
    pass


def create_user(con, user: dict):
    # with con:
    #     with con.cursor(cursor_factory=RealDictCursor) as cursor:
    #         query = """
    #             INSERT INTO users(user_type, username, email, display_name)
    #             VALUES (%s,%s,%s,%s)
    #             RETURNING user_id;
    #         """
    #         cursor.execute(
    #             query,
    #             (
    #                 user["user_type"],
    #                 user["username"],
    #                 user["email"],
    #                 user["display_name"],
    #             ),
    #         )
    #         user_id = cursor.fetchone()["user_id"]
    # return user_id
    pass


def update_user(con, user_id: int, updates: dict):
    # with con:
    #     with con.cursor(cursor_factory=RealDictCursor) as cursor:
    #         allowed_columns = {"user_type", "username", "email", "display_name"}
    #         set_query_list = []
    #         value_list = []
    #         for index, (key, value) in enumerate(updates.items()):
    #             if key in allowed_columns:
    #                 value_list.append(value)
    #                 set_query_list.append(f"{key} = %s")
    #         set_query_str = ", ".join(set_query_list)
    #         len(updates.keys())
    #         query = f"""
    #             UPDATE users
    #             SET {set_query_str}
    #             WHERE user_id = %s;
    #             """
    #         print(query)
    #         str_values = value_list + [user_id]
    #         cursor.execute(query, str_values)
    # return read_user(con, user_id=user_id)
    pass


def delete_user(con, user_id: int):
    # with con:
    #     with con.cursor(cursor_factory=RealDictCursor) as cursor:
    #         query = "DELETE FROM users WHERE user_id = %s"
    #         cursor.execute(query, (user_id,))
    #         return True
    pass


# Realtor Companies


def create_company(con, company: dict):
    # with con:
    #     with con.cursor(cursor_factory=RealDictCursor) as cursor:
    #         query = """
    #             INSERT INTO realtor_companies(company_name)
    #             VALUES (%s)
    #             RETURNING company_id;
    #         """
    #         cursor.execute(
    #             query,
    #             (company["company_name"],),
    #         )
    #         company_id = cursor.fetchone()["company_id"]
    # return company_id
    pass


def read_all_companies(con):
    # with con:
    #     with con.cursor(cursor_factory=RealDictCursor) as cursor:
    #         cursor.execute("SELECT * FROM realtor_companies")
    #         result = cursor.fetchall()
    # return result
    pass


def read_company(con, company_id: int):
    # with con:
    #     with con.cursor(cursor_factory=RealDictCursor) as cursor:
    #         query = "SELECT * FROM realtor_companies WHERE company_id = %s"
    #         cursor.execute(query, (company_id,))
    #         result = cursor.fetchone()
    # return result
    pass


def update_company(con, company_id: int, updates: dict):
    # with con:
    #     with con.cursor(cursor_factory=RealDictCursor) as cursor:
    #         allowed_columns = {"company_name"}
    #         set_query_list = []
    #         value_list = []
    #         for index, (key, value) in enumerate(updates.items()):
    #             if key in allowed_columns:
    #                 value_list.append(value)
    #                 set_query_list.append(f"{key} = %s")
    #         set_query_str = ", ".join(set_query_list)
    #         len(updates.keys())
    #         query = f"""
    #             UPDATE realtor_companies
    #             SET {set_query_str}
    #             WHERE company_id = %s;
    #             """
    #         print(query)
    #         str_values = value_list + [company_id]
    #         cursor.execute(query, str_values)
    # return read_company(con, company_id=company_id)
    pass


def delete_company(con, company_id: int):
    # with con:
    #     with con.cursor(cursor_factory=RealDictCursor) as cursor:
    #         query = "DELETE FROM realtor_companies WHERE company_id = %s"
    #         cursor.execute(query, (company_id,))
    #         return True

    pass


# Agents


def read_all_agents(con):
    # with con:
    #     with con.cursor(cursor_factory=RealDictCursor) as cursor:
    #         cursor.execute("SELECT * FROM realtor_agents")
    #         result = cursor.fetchall()
    # return result
    pass


def read_all_agents_combined(con):
    # with con:
    #     with con.cursor(cursor_factory=RealDictCursor) as cursor:
    #         cursor.execute("""
    #                     SELECT
    #                         users.user_id,
    #                         user_types.type_name,
    #                         users.display_name,
    #                         users.email,
    #                         realtor_companies.company_name,
    #                         user_images.user_id as image_user_id
    #                     FROM realtor_agents
    #                         LEFT JOIN users
    #                             ON realtor_agents.user_id = users.user_id
    #                         LEFT JOIN realtor_companies
    #                             on realtor_agents.company_id = realtor_companies.company_id
    #                         LEFT JOIN user_Types
    #                             on users.user_type = user_types.type_id
    #                         LEFT JOIN user_images
    #                             on users.user_id = user_images.user_id
    #                             ;
    #                        """)
    #         result = cursor.fetchall()
    # return result
    pass


def read_agent(con, agent_id: int):
    # with con:
    #     with con.cursor(cursor_factory=RealDictCursor) as cursor:
    #         query = "SELECT * FROM realtor_agents WHERE agent_id = %s"
    #         cursor.execute(query, (agent_id,))
    #         result = cursor.fetchone()
    # return result
    pass


def create_agent(con, agent: dict):
    #     with con:
    #         with con.cursor(cursor_factory=RealDictCursor) as cursor:
    #             query = """
    #                 INSERT INTO realtor_agents(user_id, company_id)
    #                 VALUES (%s,%s)
    #                 RETURNING agent_id;
    #             """
    #             cursor.execute(
    #                 query,
    #                 (
    #                     agent["user_id"],
    #                     agent["company_id"],
    #                 ),
    #             )
    #             agent_id = cursor.fetchone()["agent_id"]
    #     return agent_id
    pass


def create_agent_with_names(con, agent: dict):
    #     with con:
    #         with con.cursor(cursor_factory=RealDictCursor) as cursor:
    #             query = """
    #                 INSERT INTO realtor_agents(user_id, company_id)
    #                 VALUES (
    #                 (SELECT user_id FROM users WHERE username = %s),
    #                 (SELECT company_id FROM realtor_companies WHERE company_name = %s)
    #                 )
    #                 RETURNING agent_id;
    #             """
    #             cursor.execute(
    #                 query,
    #                 (
    #                     agent["username"],
    #                     agent["company_name"],
    #                 ),
    #             )
    #             agent_id = cursor.fetchone()["agent_id"]
    #     return agent_id
    pass


# def update_agent(con, agent_id: int, updates: dict):
#     with con:
#         with con.cursor(cursor_factory=RealDictCursor) as cursor:
#             allowed_columns = {"user_id", "company_id"}
#             set_query_list = []
#             value_list = []
#             for index, (key, value) in enumerate(updates.items()):
#                 if key in allowed_columns:
#                     value_list.append(value)
#                     set_query_list.append(f"{key} = %s")
#             set_query_str = ", ".join(set_query_list)
#             len(updates.keys())
#             query = f"""
#                 UPDATE realtor_agents
#                 SET {set_query_str}
#                 WHERE agent_id = %s;
#                 """
#             print(query)
#             str_values = value_list + [agent_id]
#             cursor.execute(query, str_values)
#     return read_agent(con, agent_id=agent_id)


# def delete_agent(con, agent_id: int):
#     with con:
#         with con.cursor(cursor_factory=RealDictCursor) as cursor:
#             query = "DELETE FROM realtor_agents WHERE agent_id = %s"
#             cursor.execute(query, (agent_id,))
#             return True


# ## Listing Categories


# def read_all_listing_categories(con):
#     with con:
#         with con.cursor(cursor_factory=RealDictCursor) as cursor:
#             cursor.execute("SELECT * FROM listing_categories")
#             result = cursor.fetchall()
#     return result


# ## Listing Statuses


# def read_all_listing_statuses(con):
#     with con:
#         with con.cursor(cursor_factory=RealDictCursor) as cursor:
#             cursor.execute("SELECT * FROM listing_statuses")
#             result = cursor.fetchall()
#     return result


# ## Listings


# def read_all_listings(con, limit: int = 5, offset: int = 0):
#     with con:
#         with con.cursor(cursor_factory=RealDictCursor) as cursor:
#             query = """
#                 SELECT * FROM listings
#                 LIMIT %s OFFSET %s;
#             """
#             cursor.execute(query, (limit, offset))
#             result = cursor.fetchall()
#     return result


# def read_all_listings_combined(con, limit: int = 5, offset: int = 0):
#     with con:
#         with con.cursor(cursor_factory=RealDictCursor) as cursor:
#             query = """
#                 SELECT
#                     listings.name,
#                     listings.description,
#                     listings.location,
#                     listings.price,
#                     listing_categories.category_name as category,
#                     listing_statuses.status_name as status,
#                     users.display_name AS agent,
#                     users.email,
#                     realtor_companies.company_name AS company
#                 FROM listings
#                     LEFT JOIN listing_categories
#                         ON listings.category_id = listing_categories.category_id
#                     LEFT JOIN listing_statuses
#                         on listings.status_id = listing_statuses.status_id
#                     LEFT JOIN realtor_agents
#                         on listings.agent_id = realtor_agents.agent_id
#                     LEFT JOIN users
#                         on realtor_agents.user_id = users.user_id
#                     LEFT JOIN realtor_companies
#                         on realtor_agents.company_id = realtor_companies.company_id
#                 LIMIT %s OFFSET %s;
#                 """
#             cursor.execute(query, (limit, offset))
#             result = cursor.fetchall()
#     return result


# def read_listing(con, listing_id: int):
#     with con:
#         with con.cursor(cursor_factory=RealDictCursor) as cursor:
#             query = "SELECT * FROM listings WHERE listing_id = %s"
#             cursor.execute(query, (listing_id,))
#             result = cursor.fetchone()
#     return result


# def read_listing_combined(con, listing_id: int):
#     with con:
#         with con.cursor(cursor_factory=RealDictCursor) as cursor:
#             query = """
#                 SELECT
#                     listings.name,
#                     listings.description,
#                     listings.location,
#                     listings.price,
#                     listing_categories.category_name as category,
#                     listing_statuses.status_name as status,
#                     users.display_name AS agent,
#                     users.email,
#                     realtor_companies.company_name AS company,
#                     user_images.user_id as image_user_id
#                 FROM listings
#                     LEFT JOIN listing_categories
#                         ON listings.category_id = listing_categories.category_id
#                     LEFT JOIN listing_statuses
#                         on listings.status_id = listing_statuses.status_id
#                     LEFT JOIN realtor_agents
#                         on listings.agent_id = realtor_agents.agent_id
#                     LEFT JOIN users
#                         on realtor_agents.user_id = users.user_id
#                     LEFT JOIN realtor_companies
#                         on realtor_agents.company_id = realtor_companies.company_id
#                     LEFT JOIN user_images
#                         on realtor_agents.user_id = user_images.user_id
#                 WHERE listing_id = %s;
#                 """
#             cursor.execute(query, (listing_id,))
#             result = cursor.fetchone()
#     return result


def create_listing(con, listing: dict):
    #     with con:
    #         with con.cursor(cursor_factory=RealDictCursor) as cursor:
    #             query = """
    #                 INSERT INTO listings(agent_id, location, price,name,description,category_id,status_id)
    #                 VALUES (%s,%s,%s,%s)
    #                 RETURNING listing_id;
    #             """
    #             cursor.execute(
    #                 query,
    #                 (
    #                     listing["agent_id"],
    #                     listing["location"],
    #                     listing["price"],
    #                     listing["name"],
    #                     listing["description"],
    #                     listing["category_id"],
    #                     listing["status_id"],
    #                 ),
    #             )
    #             listing_id = cursor.fetchone()["listing_id"]
    #     return listing_id
    pass


def create_listing_with_names(con, listing: dict):
    #     with con:
    #         with con.cursor(cursor_factory=RealDictCursor) as cursor:
    #             query = """
    #                 INSERT INTO listings(agent_id, location, price,name,description,category_id,status_id)
    #                 VALUES (
    #                     (SELECT agent_id FROM realtor_agents WHERE user_id =
    #                         (SELECT user_id FROM users WHERE username = %s)
    #                     ),
    #                     %s,
    #                     %s,
    #                     %s,
    #                     %s,
    #                     (SELECT category_id FROM listing_categories WHERE category_name = %s),
    #                     (SELECT status_id FROM listing_statuses WHERE status_name = %s)
    #                 )
    #                 RETURNING listing_id;
    #             """
    #             cursor.execute(
    #                 query,
    #                 (
    #                     listing["agent_username"],
    #                     listing["location"],
    #                     listing["price"],
    #                     listing["name"],
    #                     listing["description"],
    #                     listing["category_name"],
    #                     listing["status_name"],
    #                 ),
    #             )
    #             listing_id = cursor.fetchone()["listing_id"]
    #     return listing_id
    pass


# def update_listing(con, listing_id: int, updates: dict):
#     with con:
#         with con.cursor(cursor_factory=RealDictCursor) as cursor:
#             allowed_columns = {
#                 "agent_id",
#                 "location",
#                 "price",
#                 "name",
#                 "description",
#                 "category_id",
#                 "status_id",
#             }
#             set_query_list = []
#             value_list = []
#             for index, (key, value) in enumerate(updates.items()):
#                 if key in allowed_columns:
#                     value_list.append(value)
#                     set_query_list.append(f"{key} = %s")
#             set_query_str = ", ".join(set_query_list)
#             len(updates.keys())
#             query = f"""
#                 UPDATE listings
#                 SET {set_query_str}
#                 WHERE listing_id = %s;
#                 """
#             print(query)
#             str_values = value_list + [listing_id]
#             cursor.execute(query, str_values)
#     return read_user(con, listing_id=listing_id)


# def delete_listing(con, listing_id: int):
#     with con:
#         with con.cursor(cursor_factory=RealDictCursor) as cursor:
#             query = "DELETE FROM listings WHERE listing_id = %s"
#             cursor.execute(query, (listing_id,))
#             return True


# # Reviews


# def read_all_realtor_agent_reviews(con):
#     with con:
#         with con.cursor(cursor_factory=RealDictCursor) as cursor:
#             cursor.execute("SELECT * FROM realtor_agent_reviews")
#             result = cursor.fetchall()
#     return result


# def read_realtor_agent_review(con, review_id: int):
#     with con:
#         with con.cursor(cursor_factory=RealDictCursor) as cursor:
#             query = "SELECT * FROM realtor_agent_reviews WHERE review_id = %s"
#             cursor.execute(query, (review_id,))
#             result = cursor.fetchone()
#     return result


def create_realtor_agent_review(con, review: dict):
    #     with con:
    #         with con.cursor(cursor_factory=RealDictCursor) as cursor:
    #             query = """
    #                 INSERT INTO realtor_agent_reviews(user_id, agent_id, review_rating, review_text)
    #                 VALUES (%s,%s,%s,%s)
    #                 RETURNING review_id;
    #             """
    #             cursor.execute(
    #                 query,
    #                 (
    #                     review["user_id"],
    #                     review["agent_id"],
    #                     review["review_rating"],
    #                     review["review_text"],
    #                 ),
    #             )
    #             review_id = cursor.fetchone()["review_id"]
    return review_id


# def update_realtor_agent_review(con, review_id: int, updates: dict):
#     with con:
#         with con.cursor(cursor_factory=RealDictCursor) as cursor:
#             allowed_columns = {"user_id", "agent_id", "review_rating", "review_text"}
#             set_query_list = []
#             value_list = []
#             for index, (key, value) in enumerate(updates.items()):
#                 if key in allowed_columns:
#                     value_list.append(value)
#                     set_query_list.append(f"{key} = %s")
#             set_query_str = ", ".join(set_query_list)
#             len(updates.keys())
#             query = f"""
#                 UPDATE realtor_agent_reviews
#                 SET {set_query_str}
#                 WHERE review_id = %s;
#                 """
#             print(query)
#             str_values = value_list + [review_id]
#             cursor.execute(query, str_values)
#     return read_user(con, review_id=review_id)


# def delete_realtor_agent_review(con, review_id: int):
#     with con:
#         with con.cursor(cursor_factory=RealDictCursor) as cursor:
#             query = "DELETE FROM realtor_agent_reviews WHERE review_id = %s"
#             cursor.execute(query, (review_id,))
#             return True


# ## view counter


# def read_all_listing_view_counters(con):
#     with con:
#         with con.cursor(cursor_factory=RealDictCursor) as cursor:
#             cursor.execute("SELECT * FROM listing_view_counters")
#             result = cursor.fetchall()
#     return result


# def read_listing_view_counter(con, listing_id: int):
#     with con:
#         with con.cursor(cursor_factory=RealDictCursor) as cursor:
#             query = "SELECT * FROM listing_view_counters WHERE view_counter_id = %s"
#             cursor.execute(query, (listing_id,))
#             result = cursor.fetchone()
#     return result


# def update_listing_view_counter(con, view_counter_id: int, updates: dict):
#     with con:
#         with con.cursor(cursor_factory=RealDictCursor) as cursor:
#             allowed_columns = {"views"}
#             set_query_list = []
#             value_list = []
#             for index, (key, value) in enumerate(updates.items()):
#                 if key in allowed_columns:
#                     value_list.append(value)
#                     set_query_list.append(f"{key} = %s")
#             set_query_str = ", ".join(set_query_list)
#             len(updates.keys())
#             query = f"""
#                 UPDATE listing_view_counters
#                 SET {set_query_str}
#                 WHERE view_counter_id = %s;
#                 """
#             print(query)
#             str_values = value_list + [view_counter_id]
#             cursor.execute(query, str_values)
#     return read_user(con, review_id=view_counter_id)


# ## Favorites


# def read_all_favorites(con):
#     with con:
#         with con.cursor(cursor_factory=RealDictCursor) as cursor:
#             cursor.execute("SELECT * FROM favorites")
#             result = cursor.fetchall()
#     return result


# def read_favorite(con, favorite_id: int):
#     with con:
#         with con.cursor(cursor_factory=RealDictCursor) as cursor:
#             query = "SELECT * FROM favorites WHERE favorite_id = %s"
#             cursor.execute(query, (favorite_id,))
#             result = cursor.fetchone()
#     return result


# def read_favorites_from_user(con, user_id: int):
#     with con:
#         with con.cursor(cursor_factory=RealDictCursor) as cursor:
#             query = "SELECT * FROM favorites WHERE user_id = %s"
#             cursor.execute(query, (user_id,))
#             result = cursor.fetchall()
#     return result


def create_favorite(con, review: dict):
    #     with con:
    #         with con.cursor(cursor_factory=RealDictCursor) as cursor:
    #             query = """
    #                 INSERT INTO favorites(listing_id, user_id)
    #                 VALUES (%s,%s)
    #                 RETURNING favorite_id;
    #             """
    #             cursor.execute(
    #                 query,
    #                 (
    #                     review["listing_id"],
    #                     review["user_id"],
    #                 ),
    #             )
    #             favorite_id = cursor.fetchone()["favorite_id"]
    #     return favorite_id
    pass


# def delete_favorite(con, favorite_id: int):
#     with con:
#         with con.cursor(cursor_factory=RealDictCursor) as cursor:
#             query = "DELETE FROM favorites WHERE favorite_id = %s"
#             cursor.execute(query, (favorite_id,))
#             return True


# # Entities


# def read_all_entities(con):
#     with con:
#         with con.cursor(cursor_factory=RealDictCursor) as cursor:
#             cursor.execute("SELECT * FROM listing_entities")
#             result = cursor.fetchall()
#     return result


# def read_entity(con, entity_id: int):
#     with con:
#         with con.cursor(cursor_factory=RealDictCursor) as cursor:
#             query = "SELECT * FROM listing_entities WHERE entity_id = %s"
#             cursor.execute(query, (entity_id,))
#             result = cursor.fetchone()
#     return result


# def read_entities_from_listing(con, entity_id: int):
#     with con:
#         with con.cursor(cursor_factory=RealDictCursor) as cursor:
#             query = "SELECT * FROM listing_entities WHERE listing_id = %s"
#             cursor.execute(query, (entity_id,))
#             result = cursor.fetchall()
#     return result


def create_entity(con, review: dict):
    #     with con:
    #         with con.cursor(cursor_factory=RealDictCursor) as cursor:
    #             query = """
    #                 INSERT INTO listing_entities(listing_id, entity_name, entity_description)
    #                 VALUES (%s,%s)
    #                 RETURNING entity_id;
    #             """
    #             cursor.execute(
    #                 query,
    #                 (
    #                     review["listing_id"],
    #                     review["entity_name"],
    #                     review["entity_description"],
    #                 ),
    #             )
    #             entity_id = cursor.fetchone()["entity_id"]
    #     return entity_id
    pass


# def delete_entity(con, entity_id: int):
#     with con:
#         with con.cursor(cursor_factory=RealDictCursor) as cursor:
#             query = "DELETE FROM listing_entities WHERE entity_id = %s"
#             cursor.execute(query, (entity_id,))
#             return True


# # Listing Photos


# def read_all_listing_images(con):
#     with con:
#         with con.cursor(cursor_factory=RealDictCursor) as cursor:
#             cursor.execute("SELECT * FROM listing_images")
#             result = cursor.fetchall()
#     return result


# def read_listing_image(con, image_id: int):
#     with con:
#         with con.cursor(cursor_factory=RealDictCursor) as cursor:
#             query = "SELECT * FROM listing_images WHERE image_id = %s"
#             cursor.execute(query, (image_id,))
#             result = cursor.fetchone()
#     return result


# def read_listing_image_by_listing(con, listing_id: int):
#     with con:
#         with con.cursor(cursor_factory=RealDictCursor) as cursor:
#             query = "SELECT * FROM listing_images WHERE listing_id = %s"
#             cursor.execute(query, (listing_id,))
#             result = cursor.fetchall()
#     return result


def create_listing_image(con, image: dict):
    #     with con:
    #         with con.cursor(cursor_factory=RealDictCursor) as cursor:
    #             query = """
    #                 INSERT INTO listing_images(listing_id, image_path)
    #                 VALUES (%s,%s)
    #                 RETURNING image_id;
    #             """
    #             cursor.execute(
    #                 query,
    #                 (
    #                     image["listing_id"],
    #                     image["image_path"],
    #                 ),
    #             )
    #             image_id = cursor.fetchone()["image_id"]
    #     return image_id
    pass


# def delete_listing_image(con, image_id: int):
#     with con:
#         with con.cursor(cursor_factory=RealDictCursor) as cursor:
#             query = "DELETE FROM listing_images WHERE image_id = %s"
#             cursor.execute(query, (image_id,))
#             return True


# # User Photos


def create_user_image(con, image: dict):
    # with con:
    #     with con.cursor(cursor_factory=RealDictCursor) as cursor:
    #         query = """
    #             INSERT INTO user_images(user_id, image_path)
    #             VALUES (%s,%s)
    #             RETURNING image_id;
    #         """
    #         cursor.execute(
    #             query,
    #             (
    #                 image["user_id"],
    #                 image["image_path"],
    #             ),
    #         )
    #         image_id = cursor.fetchone()["image_id"]
    # return image_id
    pass


# def read_all_user_images(con):
#     with con:
#         with con.cursor(cursor_factory=RealDictCursor) as cursor:
#             cursor.execute("SELECT * FROM user_images")
#             result = cursor.fetchall()
#     return result


# def read_user_image(con, image_id: int):
#     with con:
#         with con.cursor(cursor_factory=RealDictCursor) as cursor:
#             query = "SELECT * FROM user_images WHERE image_id = %s"
#             cursor.execute(query, (image_id,))
#             result = cursor.fetchone()
#     return result


# def read_user_image_by_user_id(con, user_id: int):
#     with con:
#         with con.cursor(cursor_factory=RealDictCursor) as cursor:
#             query = "SELECT * FROM user_images WHERE user_id = %s"
#             cursor.execute(query, (user_id,))
#             result = cursor.fetchone()
#     return result


# def delete_user_image(con, image_id: int):
#     with con:
#         with con.cursor(cursor_factory=RealDictCursor) as cursor:
#             query = "DELETE FROM user_images WHERE image_id = %s"
#             cursor.execute(query, (image_id,))
#             return True


# # Entity Photos


# def read_all_entity_images(con):
#     with con:
#         with con.cursor(cursor_factory=RealDictCursor) as cursor:
#             cursor.execute("SELECT * FROM entity_images")
#             result = cursor.fetchall()
#     return result


# def read_entity_image(con, image_id: int):
#     with con:
#         with con.cursor(cursor_factory=RealDictCursor) as cursor:
#             query = "SELECT * FROM entity_images WHERE image_id = %s"
#             cursor.execute(query, (image_id,))
#             result = cursor.fetchone()
#     return result


# def read_entity_image_by_entity(con, entity_id: int):
#     with con:
#         with con.cursor(cursor_factory=RealDictCursor) as cursor:
#             query = "SELECT * FROM entity_images WHERE entity_id = %s"
#             cursor.execute(query, (entity_id,))
#             result = cursor.fetchall()
#     return result


def create_entity_image(con, image: dict):
    #     with con:
    #         with con.cursor(cursor_factory=RealDictCursor) as cursor:
    #             query = """
    #                 INSERT INTO entity_images(entity_id, image_path)
    #                 VALUES (%s,%s)
    #                 RETURNING image_id;
    #             """
    #             cursor.execute(
    #                 query,
    #                 (
    #                     image["entity_id"],
    #                     image["image_path"],
    #                 ),
    #             )
    #             image_id = cursor.fetchone()["image_id"]
    #     return image_id
    pass


# def delete_entity_image(con, image_id: int):
#     with con:
#         with con.cursor(cursor_factory=RealDictCursor) as cursor:
#             query = "DELETE FROM entity_images WHERE image_id = %s"
#             cursor.execute(query, (image_id,))
#             return True
