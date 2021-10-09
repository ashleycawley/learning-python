import urllib.request, json 
with urllib.request.urlopen("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd") as url:
    data = json.loads(url.read().decode())
    new_data = json.load(data)

    print(type(new_data))