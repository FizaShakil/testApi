import os
from fastapi import FastAPI
from supabase import create_client
from dotenv import load_dotenv
load_dotenv()

app = FastAPI()

# Initialize Supabase client
url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")
supabase = create_client(url, key)

@app.get("/records")
def get_records():
    # Fetch all data from the 'records' table
    response = supabase.table("records").select("*").execute()
    return response.data
