from django.http import HttpRequest
from ninja import Router
from ninja.errors import HttpError

from core.api.schemas import ApiResponse
from core.api.v1.users.schemas import (
    AuthInSchema,
    AuthOutSchema,
    TokenInSchema,
    TokenOutSchema,
)
from core.apps.common.exceptions import ServiceException
from core.apps.users.services.auth import BaseAuthSevice
from core.project.containers import get_container


router = Router(tags=["Users"])


@router.post("auth", response=ApiResponse[AuthOutSchema], operation_id="authorize")
def auth_handler(
    request: HttpRequest,
    schema: AuthInSchema,
) -> ApiResponse[AuthOutSchema]:
    container = get_container()
    service: BaseAuthSevice = container.resolve(BaseAuthSevice)

    service.authorize(schema.phone)
    return ApiResponse(
        data=AuthOutSchema(
            message=f"Code is sent to: {schema.phone}",
        ),
    )


@router.post(
    "confirm", response=ApiResponse[TokenOutSchema], operation_id="confirmCode",
)
def get_token_handler(
    request: HttpRequest,
    schema: TokenInSchema,
) -> ApiResponse[AuthOutSchema]:
    container = get_container()
    service = container.resolve(BaseAuthSevice)
    try:
        token = service.confirm(schema.code, schema.phone)
    except ServiceException as exception:
        raise HttpError(
            status_code=400,
            message=exception.message,
        ) from exception
    return ApiResponse(data=TokenOutSchema(token=token))
