from fastapi import FastAPI
from pydantic import BaseModel

# Initialize the FastAPI app instance
app = FastAPI()

# Define a data validation model using Pydantic
class Product(BaseModel):
    name: str
    price: float
    is_available: bool = True
    color: str | None = None  # Optional field with default value None
    description: str | None = None  # Optional field with default value None
    

# 1. A GET endpoint that reads data from the server
@app.get("/")
def read_root():
    return {"message": "Welcome to the Store API!"}

# 2. A POST endpoint that receives and validates incoming data
@app.post("/products/")
def create_product(product: Product):
    # FastAPI automatically checks if the payload matches the Product model
    return {"status": "Product added successfully", "data": product}

@app.post("/products/bulk/")
def create_bulk_products(products: list[Product]):
    # FastAPI automatically checks if the payload matches the list of Product model
    return {"status": "Bulk products added successfully", "data": products}

@app.delete("/products/{product_id}")
def delete_product(product_id: int):
    # Here you would typically delete the product from your database
    return {"status": "Product deleted successfully", "product_id": product_id}
