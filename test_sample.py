def test_addition():
    assert 5 == 5

def test_login():
    expected_url = "https://www.saucedemo.com/inventory.html"
    actual_url = "https://www.google.com"

    assert expected_url == actual_url, "login fail"