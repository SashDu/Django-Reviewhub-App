from functools import lru_cache

import punq

from core.apps.products.services.products import (
    BaseProductService,
    ORMProductService,
)
from core.apps.users.services.auth import (
    AuthService,
    BaseAuthSevice,
)
from core.apps.users.services.codes import (
    BaseCodeService,
    DjangoCacheCodeService,
)
from core.apps.users.services.customer import (
    BaseCustomerService,
    ORMCustomerService,
)
from core.apps.users.services.senders import (
    BaseSenderService,
    DummySenderService,
)


@lru_cache(1)
def get_container() -> punq.Container:
    return _initialize_container()


def _initialize_container() -> punq.Container:
    container = punq.Container()

    # initialize products
    container.register(BaseProductService, ORMProductService)

    # initialize users
    container.register(BaseCustomerService, ORMCustomerService)
    container.register(BaseCodeService, DjangoCacheCodeService)
    container.register(BaseSenderService, DummySenderService)
    container.register(BaseAuthSevice, AuthService)

    return container
