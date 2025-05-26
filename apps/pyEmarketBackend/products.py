from fastapi import APIRouter, HTTPException
from supabaseclient import supabase

router = APIRouter(prefix="/products", tags=["products"])

@router.get("/")
def list_products():
    res = supabase.table("products").select("*").execute()
    if res.error:
        raise HTTPException(status_code=500, detail=res.error.message)
    return res.data

@router.get("/{product_id}")
def get_product(product_id: int):
    res = supabase.table("products").select("*").eq("id", product_id).single().execute()
    if res.error:
        raise HTTPException(status_code=404, detail="Product not found")
    return res.data

@router.post("/")
def add_product(product: dict):
    res = supabase.table("products").insert(product).execute()
    if res.error:
        raise HTTPException(status_code=400, detail=res.error.message)
    return res.data

@router.put("/{product_id}")
def update_product(product_id: int, product: dict):
    res = supabase.table("products").update(product).eq("id", product_id).execute()
    if res.error:
        raise HTTPException(status_code=400, detail=res.error.message)
    return res.data

@router.delete("/{product_id}")
def delete_product(product_id: int):
    res = supabase.table("products").delete().eq("id", product_id).execute()
    if res.error:
        raise HTTPException(status_code=400, detail=res.error.message)
    return {"message": "Product deleted"}
