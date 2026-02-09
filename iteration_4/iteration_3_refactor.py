import requests


def add_to_cart(headers: dict[str, str]) -> str:
    """Add items to a cart.

    Args:
        headers (dict[str, str]): Request headers, including auth.

    Returns:
        str: Checkout URL
    """
    url = "https://yzy-prod.swell.store/api/cart/items"
    payload = [
        {
            "product_id": "68fbc9076a2d040012b7f64a",
            "quantity": 6,
            "variant_id": "694d83a3252dbe00127cc4a3",
        }
    ]
    r = requests.put(url=url, headers=headers, json=payload)
    json = r.json()
    # Get checkout URL
    return json["checkout_url"]


def checkout(headers: dict[str, str], checkout_url: str) -> dict:
    """Checkout a given cart.

    Args:
        headers (dict[str, str]): Request headers, including auth.
        checkout_url (str): The checkout URl for a given cart

    Returns:
        dict: The checkout JSON response.
    """
    # Checkout cart and pay
    payload = {
        "email": "me@example.com",
        "shipping": {
            "first_name": "Python",
            "last_name": "Person",
            "address": {
                "line_1": "1 Main Street",
                "line_2": "",
                "city": "New York",
                "state": "New York",
                # ...
            },
        },
        "payment": {"cc": "5555555555554444", "cvv": "123"},
        "billing": {"same_as_shipping": True},
        # ..
    }

    r = requests.post(url=checkout_url, headers=headers, json=payload)
    return r.json()


if __name__ == "__main__":
    # Get token manually from webpage
    TOKEN = "################################"

    # Add items to the cart
    headers = {
        "Authorization": f"Basic {TOKEN}",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:148.0) Gecko/20100101 Firefox/148.0",
    }

    checkout_url = add_to_cart(headers=headers)
    result = checkout(headers, checkout_url)
