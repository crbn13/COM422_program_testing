import pytest
import table_booking

@pytest.fixture
def table():
    return table_booking.Table(4, 4)

@pytest.fixture
def restaurant():
    return table_booking.Restaurant()

def test_add_table(restaurant, table):
    restaurant.add_table(table)
    assert table.table_number in restaurant.tables

def test_remove_table(restaurant, table):
    restaurant.add_table(table)
    assert table.table_number in restaurant.tables

    restaurant.remove_table(4)
    assert table.table_number not in restaurant.tables