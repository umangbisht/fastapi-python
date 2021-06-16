from main import home

def test_index():
    data = home()
    assert data == "Hello, World!"
