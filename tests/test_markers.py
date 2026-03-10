import  pytest

@pytest.mark.smoke
def test_smoke_case():
    ...

@pytest.mark.regression
def test_regression_case():
    ...


@pytest.mark.smoke
class TestSuit:
    @pytest.mark.some
    def test_case1(self):
        ...
    def test_case2(self):
        ...


class TestUserAuthentication:
    def test_login(self):
        ...

    def test_password_reset(self):
        ...

    def test_logout(self):
        ...