from package_name.capitalize import capitalize

def test_capitalize():

    assert capitalize('hello') == 'Hello'
    assert capitalize('') == ''
    print('Все тесты пройдены!')
    