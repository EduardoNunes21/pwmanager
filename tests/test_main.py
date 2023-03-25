from main import User, db, app, sign_up


class TestClass:


    def test_home_page_access(self):
        with app.test_client() as test_client:
            response = test_client.get("/")
            assert response.status_code == 302


    def test_novo_usuario(self):
        """
        GIVEN um modelo de usuario
        WHEN quando um novo usuario for criado
        THEN verifica se os campos do usuario foram definidos corretamente
        """
        user = User('teste@gmail.com', '123456')

        assert user.username == 'teste@gmail.com'
        assert user.password == '123456'