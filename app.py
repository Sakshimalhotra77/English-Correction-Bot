from flask import Flask, request
from pymessenger  import Bot
from utils import fetch_reply
from capi import eng
from papi import aud
from about import tellmeabout
import traceback

app = Flask("My news bot")
FB_ACCESS_TOKEN="EAAOjuI30HEcBAI56rY4fqLlvMiD29TTlZA7RMgLkZCyPsFkH5NDFdbPnWZChNLTvgZBbZAWngd2D1YiHUFQf9AHTWPFeUvZBqZBXdXlW685JaQxnhKgKPhMC7HZCqmF9NZA8HyzQzDlKvPEX9Q1KX6aQyS8mRcDEuDgHuznfGkqzKovA317k9y9se"
bot = Bot(FB_ACCESS_TOKEN)

VERIFICATION_TOKEN = "hello"


@app.route('/', methods=['GET'])
def verify():
	if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
		if not request.args.get("hub.verify_token") == VERIFICATION_TOKEN:
			return "Verification token mismatch", 403
		return request.args["hub.challenge"], 200
	return "Hello world", 200


@app.route('/', methods=['POST'])
def webhook():
	print(request.data)
	data = request.get_json()

	if data['object'] == "page":
		entries = data['entry']

		for entry in entries:
			messaging = entry['messaging']

			for messaging_event in messaging:

				sender_id = messaging_event['sender']['id']
				recipient_id = messaging_event['recipient']['id']

				if messaging_event.get('message'):
					# HANDLE NORMAL MESSAGES HERE

					if messaging_event['message'].get('text'):
						# HANDLE TEXT MESSAGES

						query = messaging_event['message']['text']
						if query[0:7]=="Correct":
							reply=eng(query)
							bot.send_text_message(sender_id,reply)
						elif query[0:9]=="Pronounce":
							try:
								reply=aud(query)
								attachment_type="audio"
								a=bot.send_audio(recipient_id=sender_id,audio_path="welcome.mp3")
								print(a)
							except Exception as e:
								print(traceback.format_exc())
						elif query[0:13]=="Tell me about":
							reply=tellmeabout(query)
							bot.send_text_message(sender_id,reply)
						else:
							reply = fetch_reply(query, sender_id)
							bot.send_text_message(sender_id, reply)
	return "ok", 200


if __name__ == "__main__":
	app.run(port=8000, use_reloader = True)