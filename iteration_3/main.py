import requests

# Get token manually from webpage
TOKEN = "################################"

# Add items to the cart
url = "https://yzy-prod.swell.store/api/cart/items"
headers = {
    "Authorization": f"Basic {TOKEN}",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:148.0) Gecko/20100101 Firefox/148.0",
}
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
checkout_url = json["checkout_url"]

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
print(r.json())
