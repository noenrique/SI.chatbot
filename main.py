from posixpath import split
import re
from tabnanny import check
from urllib import response
import long_responses as long

def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    # Cuenta cuantas palabras hay en cada mensaje predefinido
    for word in user_message:
        if word in recognised_words:
            message_certainty += 1
    
    #Calcula el porcentaje de palabras reconocidas en el mensaje del usuario
    percentage = float(message_certainty)/float(len(recognised_words))

    #Checa las palabras requeridas en las palabras reconocidas por el mensaje del usuario
    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break
    
    if has_required_words or single_response:
        return int(percentage*100)
    else:
        return 0

def check_all_messages(message):
    highest_prob_list = {}

    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)
    
    #Responde -------------------------------------
    response('¿Qué pedo?', ['hola', 'hey', 'holi', 'buenos dias', 'beunas tardes', 'buenas noches', 'que tranza, bot?'], single_response=True)
    response('Aquí andamos, como siempre',['como' 'estas', 'que', 'ha', 'pasado'], required_words=['como'])
    response('Jajaja tonto', ['te', 'amo'], required_words=['amo'])

    best_match = max(highest_prob_list, key =highest_prob_list.get())
    print(highest_prob_list)

    return best_match

def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response

#Probando el sistema de respuesta
while True:
    print('Bot:    ' + get_response(input('You:  ')))