import requests, json
from django.conf import settings
from typing import Literal


class Logistics:
    def __init__(self) -> None:
        self.url = f"http://{settings.HOST}:{settings.PORT}/api/package/"

    def update_package(self, package_id:int, carrier_id:int|None=None, delivery_status: Literal["Shipped", "Delivered", "Canceled"] | None=None ):
        data = {}
        if carrier_id is not None: data.update({"carrier": carrier_id})
        if delivery_status is not None: data.update({"delivery_status": delivery_status})
        res = requests.patch(f"{self.url}{package_id}/", json=data)
        return json.loads(res.text), res.status_code

logistics = Logistics()