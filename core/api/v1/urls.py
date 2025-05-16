from ninja import Router

from core.api.v1.products.handlers import router as product_router
from core.api.v1.users.handlers import router as user_router


router = Router(tags=["v1"])
router.add_router("products/", product_router)
router.add_router("users/", user_router)
