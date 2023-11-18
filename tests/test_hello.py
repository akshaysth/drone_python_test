from app.hello import hello

def test_hello():
    resp = hello()
    assert resp == "hello world!"
