import pytest

from fixtures.common_models import MessageResponse
from fixtures.constants import ResponseText
from fixtures.userInfo.model import AddUserInfo


class TestUserInfo:

    @pytest.mark.positive
    def test_update_user_info(self, app, user_info_):
        """
        Steps.
        1. Register new user
        2. Access to store
        3. Add user info
        4. Try to update user info
        5. Check that status code is 200
        6. Check response
        """
        data = AddUserInfo.random()
        res = app.user_info.update_user_info(
            user_id=user_info_.user_uuid,
            data=data,
            header=user_info_.header,
            type_response=MessageResponse,
        )
        assert res.status_code == 200
        assert res.data.message == ResponseText.MESSAGE_UPDATE_USER_INFO

    @pytest.mark.negative
    def test_update_info_of_non_existent_user(self, app, user_info_):
        """
        Steps.
        1. Register new user
        2. Access to store
        3. Add user info
        4. Try to update info of non-existent user
        5. Check that status code is 404
        6. Check response
        """
        data = AddUserInfo.random()
        res = app.user_info.update_user_info(
            user_id=1000,
            data=data,
            header=user_info_.header,
            type_response=MessageResponse,
        )
        assert res.status_code == 404
        assert res.data.message == ResponseText.MESSAGE_INFO_NOT_FOUND_DOT
