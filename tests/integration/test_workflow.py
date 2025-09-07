iimport pytest

from src.app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_user_registration_flow(client):
    """Test complete user registration workflow"""
    # Test registration page loads
    rv = client.get('/register')
    assert rv.status_code == 200

    # Test registration form submission
    rv = client.post(
        '/register',
        data={
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'testpassword',
        },
    )
    assert rv.status_code in [200, 302]  # 302 if redirect to login
