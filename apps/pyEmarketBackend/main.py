from fastapi import FastAPI
from supabaseclient import supabase  # ✔️ import the client

app = FastAPI()

@app.get("/products")
def list_products():
    try:
        response = supabase.table("products").select("*").execute()
        # Return the data part of the response directly
        return response.data
    except Exception as e:
        return {"error": str(e)}
