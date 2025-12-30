from src.calculator import add, divide
import pytest

@pytest.mark.smoke #Кастомные маркеры. Название задаётся в pytest.ini
def test_add():
    assert add(2,3) == 5

@pytest.mark.regression #Кастомные маркеры. Название задаётся в pytest.ini
def test_add_type_error():
    with pytest.raises(TypeError): # with: Мы открываем менеджер контекста/ pytest.raises "ловит" исключение. Так как это именно тот тип, который мы ожидали (TypeError), pytest.raises завершает свою работу успешно.
        add(5,'')

@pytest.mark.regression #Кастомные маркеры. Название задаётся в pytest.ini
def test_divide_by_zero():
    with pytest.raises(ValueError) as excinfo: #Мы говорим Pytest: "Поймай ZeroDivisionError и положи всю информацию о нем в переменную excinfo".
        divide(10,0)
    assert "Нельзя делить на ноль" in str(excinfo.value) #excinfo.value — здесь лежит сам объект ZeroDivisionError.

@pytest.mark.regression #Кастомные маркеры. Название задаётся в pytest.ini
def test_divide():
        divide(10,2)

@pytest.mark.slow #Кастомные маркеры. Название задаётся в pytest.ini
def test_pop_from_empty_list():
    with pytest.raises(IndexError):
        [].pop()

@pytest.mark.skip(reason="Эта функциональность будет реализована в версии 2.0") #Просто пропускает тест
def test_subtraction():
    """Тест для будущей функции вычитания."""
    # assert subtract(10, 5) == 5
    pass

#@pytest.mark.skipif(Маркер принимает два аргумента: condition (условие) и reason (причина).) 

@pytest.mark.xfail(reason="Известный баг с точностью float, будет исправлен в #TICKET-123") #Проходит тест, но ожидаем в нём ошибку. Вдруг починят
def test_add_floats_bug():
    # Этот тест будет падать из-за особенностей представления float в Python
    assert add(0.1, 0.2) == 0.3