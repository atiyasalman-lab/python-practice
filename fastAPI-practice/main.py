from fastapi import FastAPI
from pydantic import BaseModel
from mockdata import products

# Initialize the FastAPI app instance
app = FastAPI()

# # Define a data validation model using Pydantic
# class Product(BaseModel):
#     name: str
#     price: float
#     is_available: bool = True
#     color: str | None = None  # Optional field with default value None
#     description: str | None = None  # Optional field with default value None
    

# # 1. A GET endpoint that reads data from the server
# @app.get("/")
# def read_root():
#     return {"message": "Welcome to the Store API!"}

# # 2. A POST endpoint that receives and validates incoming data
# @app.post("/products/")
# def create_product(product: Product):
#     # FastAPI automatically checks if the payload matches the Product model
#     return {"status": "Product added successfully", "data": product}

# @app.post("/products/bulk/")
# def create_bulk_products(products: list[Product]):
#     # FastAPI automatically checks if the payload matches the list of Product model
#     return {"status": "Bulk products added successfully", "data": products}

# @app.delete("/products/{product_id}")
# def delete_product(product_id: int):
#     # Here you would typically delete the product from your database
#     return {"status": "Product deleted successfully", "product_id": product_id}

# from typing import Optional
# from fastapi import FastAPI, HTTPException, status
# from pydantic import BaseModel

# # Initialize the FastAPI application
# app = FastAPI(title="Product Management API")

# # Define a Pydantic model for data validation
# class Product(BaseModel):
#     id: int
#     name: str
#     price: float
#     description: Optional[str] = None
#     in_stock: bool = True

# # In-memory database mock
# db_products = {
#     1: Product(id=1, name="Wireless Mouse", price=29.99, description="Ergonomic 2.4GHz mouse"),
#     2: Product(id=2, name="Mechanical Keyboard", price=89.99, in_stock=False)
# }

# # --- ENDPOINTS ---

# # GET (Root): Simple hello world
# @app.get("/")
# def read_root():
#     return {"message": "Welcome to the Product API!"}

# # GET: Retrieve all products with an optional query parameter for filtering
# @app.get("/products")
# def get_products(in_stock: Optional[bool] = None):
#     if in_stock is not None:
#         return [p for p in db_products.values() if p.in_stock == in_stock]
#     return list(db_products.values())

# # GET: Retrieve a specific product using a path parameter
# @app.get("/products/{product_id}")
# def get_product(product_id: int):
#     if product_id not in db_products:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND, 
#             detail=f"Product with ID {product_id} not found"
#         )
#     return db_products[product_id]

# # POST: Create a new product using data validation from the Pydantic model
# @app.post("/products", status_code=status.HTTP_201_CREATED)
# def create_product(product: Product):
#     if product.id in db_products:
#         raise HTTPException(
#             status_code=status.HTTP_400_BAD_REQUEST, 
#             detail=f"Product with ID {product.id} already exists"
#         )
#     db_products[product.id] = product
#     return {"message": "Product created successfully", "product": product}

# DELETE: Remove a product from the database
# @app.delete("/products/{product_id}")
# def delete_product(product_id: int):
#     if product_id not in db_products:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND, 
#             detail="Product not found"
#         )
#     del db_products[product_id]
#     return {"message": f"Product {product_id} deleted successfully"}

@app.get("/")
def home():
    return {"message": "Welcome to the Product API!"}

# @app.get("/contact")
# def contact():
#     return {"message": "Contact us anytime at zoom"}

@app.get("/products")
def get_products():
    return products


# http://127.0.0.1:8000/products/100                                -path params
# http://127.0.0.1:8000/products?id=1&title=Mouse&price=29.99       - query params

# path params
@app.get("/products/{product_id}")
def get_one_product(product_id: int):
# if product is available with the id , return the product details, else return error message.
    for oneProduct in products:
        if oneProduct.get("id") == product_id:
            return oneProduct


    return {
        "error": "Product not found for this ID"
    }


#  query params