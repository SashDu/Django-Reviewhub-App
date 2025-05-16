from dataclasses import dataclass

from core.apps.common.exceptions import ServiceException


@dataclass(eq=False)
class CodeExceptions(ServiceException):
    @property
    def message(self):
        return "Auth code exception occured"


@dataclass(eq=False)
class CodeNotFoundException(CodeExceptions):
    code: str

    @property
    def message(self):
        return "Code not found"


@dataclass(eq=False)
class CodeNotEqualException(CodeExceptions):
    code: str
    cached_code: str
    customer_phone: str

    @property
    def message(self):
        return "Codes are not equal"
