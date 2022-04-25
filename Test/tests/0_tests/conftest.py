import pytest
from Account import Account


@pytest.fixture  #тестовая функция
def newaccount():
    account = Account("mr.Bond", 0)
    yield account
    # замерает

    account.close
    del account
#Уровни скоупа фикстур:
"""
@pytest.fixture(scope="class")#уровень класса
@pytest.fixture(scope="module")#дергается на уровне модуля (файла py)какой первый тест в модуле дернул после этого используется фикстуцра как только пройдет по всему файлу - закроется
@pytest.fixture(scope="session")#уровень сессия (авторизация)

"""
