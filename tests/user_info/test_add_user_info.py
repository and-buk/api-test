from fixtures.common_models import MessageResponse
from fixtures.constants import ResponseText
from fixtures.userInfo.model import AddUserInfo


class TestUserInfo:
    def test_add_user_info(self, app, auth_user):
        """
        Steps.
            1. Try to login user with valid data
            2. Check that status code is 200
            3. Check response
        """
        data = AddUserInfo.random()
        res = app.user_info.add_user_info(
            user_id=auth_user.user_uuid,
            data=data,
            header=auth_user.header,
            type_response=MessageResponse,
        )
        assert res.status_code == 200
        assert res.data.message == ResponseText.MESSAGE_ADD_USER_INFO
