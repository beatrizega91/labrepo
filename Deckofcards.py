import requests

url = "https://deckofcardsapi.com/api/deck/ctg1jt5cw5eg/draw/?count=6"

payload = {}
headers = {
  'Cookie': '__cfduid=d9fa620fc3adcd7f36e96bdd2d346e2511590101213'
}

response = requests.request("GET", url, headers=headers, data = payload)

print(response.text.encode('utf8'))


deck = response.json()
deck_id = deck['deck_id']
print(deck_id)