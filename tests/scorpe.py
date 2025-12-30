import pytest, json
from src.shopping_cart import ShoppingCart, ApiClient, connect_to_database
# Это полностью эквивалентно тому, что мы писали раньше - Фикстура создается для каждой тестовой функции индивидуально: 
# т.к. "function" - это значение по умолчанию.
@pytest.fixture(scope="function")
def filled_cart():
    return ShoppingCart()

class TestUserAPI:
    @pytest.fixture(scope="class")
    def api_client(self):
        # Соединение устанавливается один раз для всего класса
        client = ApiClient(user="test", password="123")
        yield client
        # --- TEARDOWN ---
        # Этот код выполнится один раз в самом конце всего запуска
        client.close()
        
    def test_get_user_profile(self, api_client):
        # Использует общий клиент
        ...
    
    def test_update_user_settings(self, api_client):
        # Использует тот же самый общий клиент
        ...

#Фикстура создается один раз для всего тестового файла (.py модуля). Все тесты в этом файле, которые запрашивают фикстуру, будут использовать один и тот же экземпляр.
@pytest.fixture(scope="module")
def test_data():
    # Файл читается с диска всего один раз
    with open("test_dataset.json") as f:
        data = json.load(f)
    return data

def test_process_part_A(test_data):
    # Использует общие данные
    ...

def test_process_part_B(test_data):
    # Использует те же самые общие данные
    ...

#Фикстура создается всего один раз за весь запуск pytest.
#Все тесты во всех файлах, которые запрашивают эту фикстуру, будут использовать абсолютно один и тот же экземпляр.
@pytest.fixture(scope="session")
def db_connection():
    # Соединение с БД устанавливается один раз в самом начале
    connection = connect_to_database("test.db")
    return connection

# В любом тестовом файле
def test_user_exists(db_connection):
    # Использует глобальное соединение
    ...