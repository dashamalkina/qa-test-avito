import requests
import pytest

BASE_URL = "https://qa-internship.avito.com/"
SELLER_ID = 12345678


def get_items_by_sellerID__test():
    response = requests.get(f"{BASE_URL}/{SELLER_ID}/item", headers={"Accept": "application/json"})
    assert response.status_code == 200


def get_items_by_sellerID__invalid_sellerID_test():
    response = requests.get(f"{BASE_URL}/{234242}/item", headers={"Accept": "application/json"})
    assert response.status_code == 200  # хотелось бы 400, так как такого селлера нет

def get_items_by_sellerID__create_new_item_test():
    body = {
        "name": "name2",
        "price": 1,
        "sellerId": SELLER_ID,
        "statistics": {"contacts": 0, "likes": 0, "viewCount": 0}
    }
    response = requests.post(f"{BASE_URL}/api/1/item", json=body, headers={"Content-Type": "application/json"})
    item_id = response.json().get("status", "").split(" - ")[-1]

    response = requests.get(f"{BASE_URL}/api/1/{SELLER_ID}/item", headers={"Accept": "application/json"})
    assert response.json()[-1]["name"] == item_id # должны сравнивать не "name" а "id"


if __name__ == "__main__":
    pytest.main()
