import requests

url = "https://yzy-prod.swell.store/api/cart/items"
headers = {
    "Authorization": "Basic cGtfdkVnQVFUTUVOSng4QmN6RDF4YU5yYTV4eXlxT0x5RnM=",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:148.0) Gecko/20100101 Firefox/148.0",
    "X-Session": "74d32d4c20ab7eb978235515649d1b57:85f69dc17926f406ddfc3e7cc251aacef0f567c71a2ef2e4687f2ba93f59a6c0ea5d8c957d7da73946073607d3d0cfb3ad623dd41f6fcfdd8e352951b78696b388c7d8533bf18260670b6da2c73edaa4c60461b429e9c0a8ce2e623b57482864fa0c45cd29e46b61aadd000eea31dd13a12df56252b65fc9576db15f6a4cecaa399e44e494396513",
}

payload = [
    {
        "product_id": "68fbc9076a2d040012b7f64a",
        "quantity": 6,
        "variant_id": "694d83a3252dbe00127cc4a3",
    }
]

r = requests.put(url=url, headers=headers, json=payload)
print(r.status_code)
print(r.json())
