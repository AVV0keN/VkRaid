import requests
import time
apiurl = 'https://api.vk.com/method/'
token = 'Пиши свой токен сюда!'
chatid = 123 #Сюда пиши айди конфы,как узнать? Смотри репозиторий!
text = 'Напиши сюда текст который хочешь видеть при рэйде' 

while True:
	one = requests.get(apiurl + 'messages.send', {'v': 5.67, 'access_token': token, 'chat_id': 
			chatid, 'message': 'a'})
	two = requests.get(apiurl + 'messages.edit', {'v': 5.67, 'access_token': token, 'peer_id': 
			2000000000 + chatid, 'message_id': one.json()['response'], 'message': text})
	print(two.json())
	time.sleep(7)
