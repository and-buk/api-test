import pytest

from fixtures.auth.model import Auth
from fixtures.common_models import AuthInvalidResponse
from fixtures.constants import ResponseText


class TestAuthUser:

    @pytest.mark.positive
    def test_auth_user_with_valid_data(self, app, register_user):
        """
        Steps.
        1. Register new user
        2. Try to access to store with valid data
        3. Check that status code is 200
        4. Check response
        """
        res = app.auth.login(data=register_user.user)
        assert res.status_code == 200, "Check status code"

    @pytest.mark.negative
    def test_auth_user_with_random_data(self, app):
        """
        1. Try to auth user (access to store) with random invalid data
        2. Check that status code is 401
        3. Check response
        """
        data = Auth.random()
        res = app.auth.login(data=data, type_response=AuthInvalidResponse)
        assert res.status_code == 401, "Check status code"
        assert res.data.description == ResponseText.DESCRIPTION_AUTH
        assert res.data.error == ResponseText.ERROR_AUTH
