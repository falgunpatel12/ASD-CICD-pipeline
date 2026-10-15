from app import add, greet, login

def test_add():
       assert add(2, 3) == 5
def test_greet():
       assert "Hello, Asha!" in greet("Asha")
def test_login():
       assert login("a@b.com", "secret1") is True