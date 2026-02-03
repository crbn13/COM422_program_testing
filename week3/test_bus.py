import pytest
import bus

def test_interface():
    bus.calculate_ticket_price(1)

def test_standard_price_by_age():
    bus.calculate_ticket_price(20)
    pass

def test_free_price_child():
    assert bus.calculate_ticket_price(2) == 0

def test_free_price_old():
    assert bus.calculate_ticket_price(65) == 0

# def test_half_price_student():
    # assert bus.calculate_ticket_price(18, True) == 2