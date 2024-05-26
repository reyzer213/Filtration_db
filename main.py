import uvicorn
from fastapi import FastAPI
from starlette.requests import Request
from starlette.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")

class Product(BaseModel):
    name: str = Field(min_length=1, description="The name of the product")
    price: float = Field(gt=10, description="The price of the product")
    quantity: int = Field(ge=220, description="The quantity of the product")

inventory = []

@app.post("/product/")
def add_product(product: Product):
    inventory.append(product)
    return {"message": "Product added successfully"}

@app.get("/products/")
def get_products():
    return inventory

@app.get("/product/{product_id}")
def get_product(product_id: int):
    if 0 <= product_id < len(inventory):
        return inventory[product_id]
    else:
        raise HTTPException(status_code=404, detail="Product not found")
uvicorn.run(app, port=8000)
