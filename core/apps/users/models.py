from uuid import uuid4

from django.db import models

from core.apps.common.models import TimedBaseModel
from core.apps.users.entities import CustomerEntity


class Customer(TimedBaseModel):
    phone = models.CharField(
        verbose_name="Phone Number",
        max_length=12,
        unique=True,
    )
    token = models.CharField(
        verbose_name="User Token",
        max_length=255,
        default=uuid4,
        unique=True,
    )

    def __str__(self) -> str:
        return self.phone

    def to_entity(self) -> CustomerEntity:
        return CustomerEntity(
            phone=self.phone,
            created_at=self.created_at,
        )

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
