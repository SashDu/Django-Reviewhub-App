from datetime import datetime
from typing import List, Optional

from core.apps.products.entities.products import Product as ProductEntity
from pydantic import BaseModel


class ProductSchema(BaseModel):
    id: int
    title: str
    description: str
    created_at: datetime
    updated_at: Optional[datetime] = None
    
    @staticmethod
    def from_entity(entity: ProductEntity) -> 'ProductSchema':
        return ProductSchema(
            id=entity.id,
            title=entity.title,
            description=entity.description,
            created_at=entity.created_at,
            updated_at=entity.updated_at,
        )


ProductListSchema = List[ProductSchema]
