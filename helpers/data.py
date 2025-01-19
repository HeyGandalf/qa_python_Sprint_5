import random


class PersonalData:
    user_name = 'Евгения Харченко'
    login = 'yevgeniya_kharchenko_17_123@gmail.com'
    password = '123qwe'


class ValidData:
    user_name = 'Test test'
    login = f"Test_test{random.randint(10, 999)}@gmail.com"
    password = f"{random.randint(100, 999)}{random.randint(100, 999)}"
