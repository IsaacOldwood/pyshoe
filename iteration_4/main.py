from httpx import AsyncClient
from typing import Mapping
import asyncio


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


async def _add_to_cart(headers: dict[str, str], client: AsyncClient) -> str:
    """Add items to a cart.

    Args:
        headers (dict[str, str]): Request headers, including auth.
        client (AsyncClient): Async request client.

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
    r = await client.put(url=url, headers=headers, json=payload)
    json = r.json()
    # Get checkout URL
    return json["checkout_url"]


async def _checkout(
    headers: dict[str, str],
    checkout_url: str,
    payment_info: Mapping[str, str | Mapping],
    client: AsyncClient,
) -> dict:
    """Checkout a given cart.

    Args:
        headers (dict[str, str]): Request headers, including auth.
        checkout_url (str): The checkout URl for a given cart
        payment_info (Mapping[str, str | Mapping]): User payment info.
        client (AsyncClient): Async request client.

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

    r = await client.post(url=checkout_url, headers=headers, json=payload)
    return r.json()


async def main(
    token: str, payment_info: Mapping[str, str | Mapping], client: AsyncClient
) -> dict:
    """Main script to buy stuff.

    Args:
        token (str): User token for a given cart.
        payment_info (Mapping[str, str  |  Mapping]): Payment info.
        client (AsyncClient): Async request client.

    Returns:
        dict: Results of checkout.
    """
    headers = _build_headers(token)
    checkout_url = await _add_to_cart(headers, client)
    return await _checkout(headers, checkout_url, payment_info, client)


async def run(inputs: list[tuple[str, dict]]):
    async with AsyncClient() as client:
        tasks = []
        for token, user_info in inputs:
            tasks.append(main(token, user_info, client))
        return await asyncio.gather(*tasks)


if __name__ == "__main__":
    # User info setup
    TOKEN1 = "################################"
    user_info1 = {
        "email": "email1@example.com",
        # ...
    }
    TOKEN2 = "################################"
    user_info2 = {
        "email": "email2@example.com",
        # ...
    }

    # Run script
    inputs = [(TOKEN1, user_info1), (TOKEN2, user_info2)]
    asyncio.run(run(inputs))
