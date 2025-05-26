from supabase import create_client, Client

url = "https://lvpeuzvnmldgvmogqfvm.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imx2cGV1enZubWxkZ3Ztb2dxZnZtIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDgxNDk2ODgsImV4cCI6MjA2MzcyNTY4OH0.Lyv8Ag9XchXXzPOv1cbRMqFIQtY8t7QSh7CQzLZCHZE"
supabase: Client = create_client(url, key)

# Example: fetch users
data = supabase.table("users").select("*").execute()
print(data)