import logging
import os
from fastapi import FastAPI, HTTPException
from supabase import create_client
from dotenv import load_dotenv

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

load_dotenv()

app = FastAPI()

# Initialize Supabase client
url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")
supabase = None
try:
    supabase = create_client(url, key)
    logger.info("Supabase client initialized successfully")
except Exception as e:
    logger.error(f"Failed to initialize Supabase client: {e}")


@app.get("/")
def root():
    return {"status": "ok"}


@app.get("/records")
def get_records():
    if supabase is None:
        raise HTTPException(status_code=503, detail="Supabase client is not available")

    try:
        response = supabase.table("records").select("*").execute()
        return response.data
    except Exception as e:
        logger.error(f"Error fetching records from Supabase: {e}")
        raise HTTPException(status_code=500, detail="Failed to fetch records")