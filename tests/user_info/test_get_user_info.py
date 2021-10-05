from fixtures.userInfo.model import GetUserInfoResponse


class TestGetUserInfo:
    def test_get_user_info(self, app, user_info_):
        """
        1. Try to get user info
        2. Check that status code is 200
        3. Check response
        """
        res = app.user_info.get_user_info(
            user_id=user_info_.user_uuid,
            header=user_info_.header,
            type_response=GetUserInfoResponse,
        )
        assert res.status_code == 200, "Check status code"
        assert res.data.city == user_info_.user_info.address.city, "Check city"
        assert res.data.street == user_info_.user_info.address.street, "Check street"
        assert res.data.email == user_info_.user_info.email, "Check email"
