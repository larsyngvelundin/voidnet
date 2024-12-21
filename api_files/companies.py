from fastapi import FastAPI, HTTPException

from db_setup import get_connection
from db import (
    create_company,
    read_all_companies,
    read_company,
    update_company,
    delete_company,
)

from fastapi import APIRouter

router = APIRouter()


# get companies
@router.get("")
def get_companies():
    con = get_connection()
    result = read_all_companies(con)
    return result


# get companies {id}
@router.get("/{company_id}")
def get_company_by_id(company_id: int):
    con = get_connection()
    result = read_company(con, company_id=company_id)
    return result


# post companies
@router.post("", status_code=201)
def post_companies(company: dict):
    if "company_name" in company:
        try:
            con = get_connection()
            company_id = create_company(con, company)
            return {"message": "Company successfully created", "company_id": company_id}
        except Exception:
            raise HTTPException(
                status_code=400,
                detail=f"Unable to create company '{company["company_name"]}'",
            )
    else:
        raise HTTPException(
            status_code=400,
            detail=f"No valid company included in request. An object with company_name is required. Got: {company}",
        )


# put companies {id}
@router.put("/{company_id}")
def put_company_by_id(company_id: int, updates: dict):
    con = get_connection()
    result = update_company(con, company_id=company_id, updates=updates)
    return {"message": "Update successful", "company": result}


# delete company {id}
@router.delete("/{company_id}")
def delete_company_by_id(company_id: int):
    con = get_connection()
    result = delete_company(con, company_id=company_id)
    return {"message": "Deletion successful"}
