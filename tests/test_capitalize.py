from package_name.capitalize import capitalize

def test_capitalize():

    if capitalize('hello') != 'Hello':
        raise Exception('Функция работает неверно!')

    if capitalize('') != '':
        raise Exception('Функция работает неверно!')

    print('Все тесты пройдены!')