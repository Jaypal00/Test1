from fastapi import APIRouter, HTTPException
from dataclasses import request_data, response_data
from app1 import addition
from loggers import logger

router = APIRouter()

@router.post("/add", response_model=response_data)
async def add_numbers(data : request_data):
    try:
        result = await addition(data)
        return response_data(result=result)
    except ValueError as e:
        logger.error(f"Error during addition: {e}")
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")