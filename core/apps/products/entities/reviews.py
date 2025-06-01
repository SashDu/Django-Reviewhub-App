from dataclasses import (
    dataclass,
    field,
)

from core.apps.common.enums import EntityStatus
from core.apps.products.entities.products import Product
from core.apps.users.entities import CustomerEntity


@dataclass
class Review:
    customer: CustomerEntity | EntityStatus = field(default=EntityStatus.NOT_LOADED)
    product: Product | EntityStatus = field(default=EntityStatus.NOT_LOADED)
    text: str = field(default="")
    raiting: int = field(default=1)
