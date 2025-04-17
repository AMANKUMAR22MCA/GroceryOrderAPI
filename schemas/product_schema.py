from pydantic import BaseModel, validator

class ProductBase(BaseModel):
    name: str
    price_per_unit: float
    unit: str

    @validator("price_per_unit")
    def price_positive(cls, v):
        if v <= 0:
            raise ValueError("Price must be positive")
        return v

class ProductCreate(ProductBase):
    pass

class ProductResponse(ProductBase):
    id: int
    class Config:
        orm_mode = True
