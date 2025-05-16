from abc import (
    ABC,
    abstractmethod,
)
from dataclasses import dataclass

from core.apps.users.services.codes import BaseCodeService
from core.apps.users.services.customer import BaseCustomerService
from core.apps.users.services.senders import BaseSenderService


@dataclass(eq=False)
class BaseAuthSevice(ABC):
    user_service: BaseCustomerService
    codes_service: BaseCodeService
    sender_service: BaseSenderService

    @abstractmethod
    def authorize(self, phone: str): ...

    @abstractmethod
    def confirm(self, code: str, phone: str): ...


class AuthService(BaseAuthSevice):
    def authorize(self, phone: str):
        customer = self.user_service.get_or_create(phone)
        code = self.codes_service.generate_code(customer)
        self.sender_service.send_code(customer, code)

    def confirm(self, code: str, phone: str):
        customer = self.user_service.get(phone)
        self.codes_service.validate_code(code, customer)
        return self.user_service.generate_token(customer)
