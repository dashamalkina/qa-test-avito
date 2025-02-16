import requests
import pytest

BASE_URL = "https://qa-internship.avito.com"
SELLER_ID = 12345678


def get_item_by_id__test():
    body = {
        "name": "name",
        "price": 1,
        "sellerId": SELLER_ID,
        "statistics": {"contacts": 0, "likes": 0, "viewCount": 0}
    }
    response = requests.post(f"{BASE_URL}/api/1/item", json=body, headers={"Content-Type": "application/json"})
    item_id = response.json().get("status", "").split(" - ")[-1]

    response = requests.get(f"{BASE_URL}/api/1/item/{item_id}", headers={"Accept": "application/json"})
    assert response.status_code == 200
    assert response.json()[0]["id"] == item_id


def get_item_by_id__correct_info_test():
    name = "name"
    price = 1
    body = {
        "name": name,
        "price": price,
        "sellerId": SELLER_ID,
        "statistics": {"contacts": 0, "likes": 0, "viewCount": 0}
    }
    response = requests.post(f"{BASE_URL}/api/1/item", json=body, headers={"Content-Type": "application/json"})
    item_id = response.json().get("status", "").split(" - ")[-1]

    response = requests.get(f"{BASE_URL}/api/1/item/{item_id}", headers={"Accept": "application/json"})
    assert response.status_code == 200
    print(response.json())
    assert response.json()[0]["id"] == item_id
    assert response.json()[0]["price"] == price
    assert response.json()[0]["sellerId"] == SELLER_ID
    assert response.json()[0]["name"] == "dsdsd"  # а должно быть name


def get_item_by_id__correct_info_test():
    response = requests.get(f"{BASE_URL}/api/1/item/{-1}", headers={"Accept": "application/json"})
    assert response.status_code == 400


if __name__ == "__main__":
    pytest.main()
