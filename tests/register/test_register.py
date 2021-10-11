import pytest

from fixtures.common_models import MessageResponse
from fixtures.constants import ResponseText
from fixtures.register.model import RegisterUser
from fixtures.register.model import RegisterUserResponse


class TestRegisterUser:

    @pytest.mark.positive
    def test_register_user_with_valid_data(self, app):
        """
        1. Try to register user with valid data
        2. Check that status code is 201
        3. Check response
        """
        data = RegisterUser.random()
        res = app.register.register(data=data, type_response=RegisterUserResponse)
        assert res.status_code == 201, "Check status code"
        assert res.data.message == ResponseText.MESSAGE_REGISTER_USER

    @pytest.mark.negative
    @pytest.mark.parametrize("field", ["username", "password"])
    def test_register_user_with_empty_data(self, app, field):
        """
        1. Try to register user with empty data
        2. Check that status code is 400
        3. Check response
        """
        data = RegisterUser.random()
        setattr(data, field, None)
        res = app.register.register(data=data, type_response=MessageResponse)
        assert res.status_code == 400, "Check status code"
        assert res.data.message == ResponseText.MESSAGE_USER_PASSWORD_REQUIRED

    @pytest.mark.negative
    def test_register_user_with_the_same_data(self, app):
        """
        1. Try to register user with the same valid data
        2. Check that status code is 400
        3. Check response
        """
        data = RegisterUser.random()
        app.register.register(data=data, type_response=RegisterUserResponse)
        res = app.register.register(data=data, type_response=RegisterUserResponse)
        assert res.status_code == 400, "Check status code"
