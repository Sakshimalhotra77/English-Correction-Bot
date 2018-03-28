import apiai
import json

# api.ai client
APIAI_ACCESS_TOKEN = "f7ff2fdec6a14b88a1b28bccd7850e2f"
ai = apiai.ApiAI(APIAI_ACCESS_TOKEN)


def apiai_response(query, session_id):
    """
    function to fetch api.ai response
    """
    request = ai.text_request()
    request.lang = 'en'
    request.session_id = session_id
    request.query = query
    response = request.getresponse()
    return json.loads(response.read().decode('utf8'))


def parse_response(response):
    """
    function to parse response and
    return intent and its parameters
    """
    result = response['result']
    params = result.get('parameters')
    intent = result['metadata'].get('intentName')
    return intent, params


def fetch_reply(query, session_id):
    """
    main function to fetch reply for chatbot and
    return a reply
    """
    response = apiai_response(query, session_id)
    print(response)
    intent, params = parse_response(response)

    if response['result']['action'].startswith('smalltalk'):
        reply = response['result']['fulfillment']['speech']
    elif response['result']['action'] == "smalltalk.agent.boss":
        reply=  response['result']['fulfillment']['speech']
    elif response['result']['action'] == "sakshi":
        reply = response['result']['fulfillment']['speech']

    else:
       reply = "Sorry but this is very difficult. I am just your helping hand while you are learning, Try me to correct your grammer(Correct, Followed by error prone sentence), to learn Pronounce sentences(Pronounce, followed by the senetnce) or Know about anything to everything( Tell me about, followed by what your want to know)"


    return reply
