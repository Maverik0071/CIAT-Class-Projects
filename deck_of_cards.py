import requests

url = "https://deckofcardsapi.com/api/deck/new/shuffle/"
querystring = {"deck_count": "6"}
headers = {
'Cache-Control': "no-cache",
'Postman-Token': "dd1d8ca5-7000-21b2-2230-39969d585419"
}
response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
deck = response.json()
deck_id = deck['deck_id']
print(deck_id)