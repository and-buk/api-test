from fixtures.magazine.model import StoreResponse, Store


class TestStore:
    def test_add_store(self, app, auth_user):
        """
        Steps.
            1. Try to login user with valid data
            2. Check that status code is 200
            3. Check response
        """
        name_store = Store.random()
        res = app.operations_with_store.add_new_store(
            name_store=name_store,
            header=auth_user.header,
            type_response=StoreResponse,
        )
        assert res.status_code == 201
