import pytest
from vehicle import Car, Motorcycle, Vehicle


@pytest.fixture
def car():
    return Car()


@pytest.fixture
def motorcycle():
    return Motorcycle()


def test_car_instance(car):
    assert isinstance(car, Car)
    assert isinstance(car, Vehicle)


def test_car_num_wheels(car):
    assert car.numWheels == 4


def test_motorcycle_num_wheels(motorcycle):
    assert motorcycle.numWheels == 2


def test_car_test_drive(car):
    car.testDrive()
    assert car.speed == 60


def test_motorcycle_test_drive(motorcycle):
    motorcycle.testDrive()
    assert motorcycle.speed == 75


def test_car_park(car):
    car.testDrive()
    car.park()
    assert car.speed == 0


def test_motorcycle_park(motorcycle):
    motorcycle.testDrive()
    motorcycle.park()
    assert motorcycle.speed == 0
