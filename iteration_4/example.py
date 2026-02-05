import requests
from time import time

start = time()
base_url = "https://pokeapi.co/api/v2/pokemon/"

for i in range(20):
    requests.get(base_url + str(i))

print("Time to run: ", round(time() - start, 2))
print("Time/request: ", round(time() - start, 2) / 20)
