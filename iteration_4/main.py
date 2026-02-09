import requests
from typing import Mapping


def _build_headers(token: str) -> dict[str, str]:
    """Build the request headers from a token.

    Args:
        token (str): Token for a cart.

    Returns:
        dict[str, str]: Request headers.
    """
    return {
        "Authorization": f"Basic {token}",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:148.0) Gecko/20100101 Firefox/148.0",
    }


def _add_to_cart(headers: dict[str, str]) -> str:
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


def _checkout(
    headers: dict[str, str],
    checkout_url: str,
    payment_info: Mapping[str, str | Mapping],
) -> dict:
    """Checkout a given cart.

    Args:
        headers (dict[str, str]): Request headers, including auth.
        checkout_url (str): The checkout URl for a given cart
        payment_info (Mapping[str, str | Mapping]): User payment info.

    Returns:
        dict: The checkout JSON response.
    """
    # Checkout cart and pay
    payload = {
        "email": payment_info["email"],
        "shipping": payment_info["shipping"],
        "payment": payment_info["card_details"],
        "billing": {"same_as_shipping": True},
        # ..
    }

    r = requests.post(url=checkout_url, headers=headers, json=payload)
    return r.json()


def main(token: str, payment_info: Mapping[str, str | Mapping]) -> dict:
    """Main script to buy stuff.

    Args:
        token (str): User token for a given cart.
        payment_info (Mapping[str, str  |  Mapping]): Payment info.

    Returns:
        dict: Results of checkout.
    """
    headers = _build_headers(token)
    checkout_url = _add_to_cart(headers=headers)
    return _checkout(headers, checkout_url, payment_info)


if __name__ == "__main__":
    # User 1
    TOKEN = "################################"
    user_info = {
        "email": "email1@example.com",
        # ...
    }
    main(TOKEN, user_info)

    # User 2
    TOKEN = "################################"
    user_info = {
        "email": "email2@example.com",
        # ...
    }
    main(TOKEN, user_info)
