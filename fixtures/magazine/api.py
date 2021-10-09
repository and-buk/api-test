from requests import Response

from common.deco import logging as log
from fixtures.validator import Validator


class StoreMagazine(Validator):
    def __init__(self, app):
        self.app = app

    POST_MAGAZINE = "/store/{}"
    GET_MAGAZINE = "/store/{}"

    @log("Add new store")
    def add_new_store(
        self, name_store: str, header=None, type_response=None
    ) -> Response:
        """
        https://app.swaggerhub.com/apis-docs/berpress/flask-rest-api/1.0.0#/storeMagazine/storeAdd
        """
        response = self.app.client.request(
            method="POST",
            url=f"{self.app.url}{self.POST_MAGAZINE.format(name_store)}",
            headers=header,
        )
        return self.structure(response, type_response=type_response)

    @log("Get store")
    def get_store(self, name_store: str, header=None, type_response=None) -> Response:
        """
        https://app.swaggerhub.com/apis-docs/berpress/flask-rest-api/1.0.0#/storeMagazine/storeGet
        """
        response = self.app.client.request(
            method="GET",
            url=f"{self.app.url}{self.GET_MAGAZINE.format(name_store)}",
            headers=header,
        )
        return self.structure(response, type_response=type_response)
