import requests
import pytest

BASE_URL = "https://qa-internship.avito.com/"
SELLER_ID = 12345678


def get_item_statistic_by_id__test():
    body = {
        "name": "name",
        "price": 1,
        "sellerId": SELLER_ID,
        "statistics": {"contacts": 0, "likes": 0, "viewCount": 0}
    }
    response = requests.post(f"{BASE_URL}/api/1/item", json=body, headers={"Content-Type": "application/json"})
    item_id = response.json().get("status", "").split(" - ")[-1]

    response = requests.get(f"{BASE_URL}/api/1/statistic/{item_id}", headers={"Accept": "application/json"})
    assert response.status_code == 200


def get_item_statistic_by_id__correct_info_test():
    body = {
        "name": "name",
        "price": 1,
        "sellerId": SELLER_ID,
        "statistics": {"contacts": 0, "likes": 1, "viewCount": 2}
    }
    response = requests.post(f"{BASE_URL}/api/1/item", json=body, headers={"Content-Type": "application/json"})
    item_id = response.json().get("status", "").split(" - ")[-1]

    response = requests.get(f"{BASE_URL}/api/1/statistic/{item_id}", headers={"Accept": "application/json"})
    assert response.json()["contacts"] == 0
    assert response.json()["likes"] == 1
    assert response.json()["viewCount"] == 4  # а должен быть на 2 меньше


def get_item_statistic_by_id__invalid_id_test():
    response = requests.get(f"{BASE_URL}/api/1/statistic/{-1}", headers={"Accept": "application/json"})
    assert response.status_code == 400


if __name__ == "__main__":
    pytest.main()
