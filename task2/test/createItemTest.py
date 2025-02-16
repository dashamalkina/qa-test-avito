import requests
import pytest

BASE_URL = "https://qa-internship.avito.com"
SELLER_ID = 12345678


def create_item__test():
    body = {
        "name": "name",
        "price": 1,
        "sellerId": SELLER_ID,
        "statistics": {"contacts": 0, "likes": 0, "viewCount": 0}
    }
    response = requests.post(f"{BASE_URL}/api/1/item", json=body, headers={"Content-Type": "application/json"})
    assert response.status_code == 200


def create_item__item_has_name_test():
    body = {
        "price": 1,
        "sellerId": SELLER_ID,
        "statistics": {"contacts": 0, "likes": 0, "viewCount": 0}
    }
    response = requests.post(f"{BASE_URL}/api/1/item", json=body, headers={"Content-Type": "application/json"})
    assert response.status_code == 200  # хотелось бы 400


def create_item__item_has_price_test():
    body = {
        "name": "name",
        "sellerId": SELLER_ID,
        "statistics": {"contacts": 0, "likes": 0, "viewCount": 0}
    }
    response = requests.post(f"{BASE_URL}/api/1/item", json=body, headers={"Content-Type": "application/json"})
    assert response.status_code == 200  # хотелось бы 400


def create_item__item_invalid_price_test():
    body = {
        "name": "name",
        "price": -1,
        "sellerId": SELLER_ID,
        "statistics": {"contacts": 0, "likes": 0, "viewCount": 0}
    }
    response = requests.post(f"{BASE_URL}/api/1/item", json=body, headers={"Content-Type": "application/json"})
    assert response.status_code == 200  # хотелось бы 400


if __name__ == "__main__":
    pytest.main()
