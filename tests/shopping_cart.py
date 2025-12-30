from src.shopping_cart import ShoppingCart
import pytest

#(Пример плохого кода)
def test_add_item():
    # --- Начало блока подготовки ---
    cart = ShoppingCart()
    cart.add_item("apple", price=10)
    cart.add_item("banana", price=20)
    # --- Конец блока подготовки ---

    cart.add_item("cherry", price=30)
    assert "cherry" in cart.items


def test_remove_item():
    # --- Начало блока подготовки (ТОЧНАЯ КОПИЯ) ---
    cart = ShoppingCart()
    cart.add_item("apple", price=10)
    cart.add_item("banana", price=20)
    # --- Конец блока подготовки ---

    cart.remove_item("apple")
    assert "apple" not in cart.items

def test_get_total_price():
    # --- Начало блока подготовки (И СНОВА КОПИЯ) ---
    cart = ShoppingCart()
    cart.add_item("apple", price=10)
    cart.add_item("banana", price=20)
    # --- Конец блока подготовки ---

    assert cart.get_total_price() == 30

#(Пример с фикстурами)
@pytest.fixture
def filled_cart():
    """Создает и возвращает корзину с двумя товарами."""
    # 2. Здесь находится наш код ПОДГОТОВКИ (Setup)
    cart = ShoppingCart()
    cart.add_item("apple", price=10)
    cart.add_item("banana", price=20)
    # 3. Возвращаем подготовленный объект
    return cart

# 4. Пишем тест, который ЗАПРАШИВАЕТ фикстуру
def test_add_item(filled_cart):
    # `filled_cart` здесь - это тот самый объект `cart`, 
    # который вернула наша фикстура
    filled_cart.add_item("cherry", price=30)
    assert "cherry" in filled_cart.items

def test_get_total_price(filled_cart):
    # Мы можем использовать ту же самую фикстуру в другом тесте!
    assert filled_cart.get_total_price() == 30