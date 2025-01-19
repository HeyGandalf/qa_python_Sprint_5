import random

class PersonalData:
    USER_NAME = 'Евгения Харченко'
    LOGIN = 'yevgeniya_kharchenko_17_123@gmail.com'
    PASSWORD = '123qwe'

class ValidData:
    USER_NAME = 'Test test'
    LOGIN = f"Test_test{random.randint(10, 999)}@gmail.com"
    PASSWORD = f"{random.randint(100, 999)}{random.randint(100, 999)}"
