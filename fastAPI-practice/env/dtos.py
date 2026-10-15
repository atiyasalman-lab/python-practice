from pydantic import BaseModel

# there r 2 types of bodies request body and response body. Request body is the data that the client sends to the server, and response body is the data that the server sends back to the client.
# pydantic model ki help se body me aane wale data ko pehle hi declare kr skte h


# DTO - DATA TRANSFER OBJECT or DATA VALIDATION.
class ProductDTO(BaseModel):
    id: int
    title: str
    # price:int = 0   by default price is 0 if not provided
    price: int = 0
    count: int = 0