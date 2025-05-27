from supabase import create_client, Client

url = ""
key = ""
supabase: Client = create_client(url, key)

# Example: fetch users
data = supabase.table("users").select("*").execute()
print(data)