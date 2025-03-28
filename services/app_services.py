import requests

def get_data():
    response = requests.get("https://api.stackexchange.com/2.2/search?order=desc&sort=activity&intitle=perl&site=stackoverflow", timeout=4000)

    if (response.status_code == 200):
        return response.json()

    return "Unable to retrieve data!"

def get_answered_responses(json_data):
    """
    Función que cuenta las respuestas contestadas y no contestadas (propiedad: is_answered) en los datos JSON.

    Args:
        json_data (dict): Datos en formato JSON que contienen los ítems a analizar.
    Returns:
        tuple: (answered_responses, no_answered_responses)
    """
    answered_responses = 0
    no_answered_responses = 0

    for item in json_data.get('items', []):
        if item.get('is_answered', False):
            answered_responses += 1
        else:
            no_answered_responses += 1

    return answered_responses, no_answered_responses

def get_answer_highest_reputation(json_data):
    """
    Obtiene la respuesta con mayor reputación (propiedad: reputation) del owner en los datos JSON.

    Args:
        json_data (dict): Datos en formato JSON que contienen los ítems a analizar.

    Returns:
        dict: Diccionario con la respuesta de mayor reputación y su información relevante.
              Retorna None si no hay items o no hay información de reputación.
    """
    max_reputation = -1
    answer_highest_reputation = None

    for item in json_data.get('items', []):
        owner = item.get('owner', {})
        reputacion = owner.get('reputation', -1)

        if reputacion > max_reputation:
            max_reputation = reputacion
            answer_highest_reputation = {
                'question_id': item.get('question_id'),
                'title': item.get('title'),
                'reputation': reputacion,
                'display_name': owner.get('display_name'),
                'is_answered': item.get('is_answered'),
                'link': item.get('link')
            }

    return answer_highest_reputation if max_reputation != -1 else None

def get_answer_fewest_views(json_data):
    """
    Obtiene la respuesta con el menor número de vistas (propiedad: view_count) en los datos JSON.

    Args:
        json_data (dict): Datos en formato JSON que contienen los ítems a analizar.

    Returns:
        dict: Diccionario con la respuesta de menos vistas y su información relevante.
              Retorna None si no hay items o no hay información de view_count.
    """
    min_views = float('inf')
    answer_fewest_views = None

    for item in json_data.get('items', []):
        vistas = item.get('view_count', -1)

        if vistas != -1 and vistas < min_views:
            min_views = vistas
            answer_fewest_views = {
                'question_id': item.get('question_id'),
                'title': item.get('title'),
                'view_count': vistas,
                'display_name': item.get('owner', {}).get('display_name'),
                'is_answered': item.get('is_answered'),
                'link': item.get('link')
            }

    return answer_fewest_views if min_views != float('inf') else None

def get_oldest_and_newest_answer(json_data):
    """
    Obtiene la respuesta más antigua y la más actual basado en la propiedad: creation_date.

    Args:
        json_data (dict): Datos en formato JSON que contienen los ítems a analizar.

    Returns:
        tuple: (oldest_answer, newest_answer)
               Cada una es un diccionario con la información relevante.
               Retorna (None, None) si no hay items válidos.
    """
    oldest_answer = None
    newest_answer = None
    oldest_date = float('inf')
    newest_date = -1

    for item in json_data.get('items', []):
        creation_date = item.get('creation_date', None)

        if creation_date is not None:
            # Respuesta más vieja
            if creation_date < oldest_date:
                oldest_date = creation_date
                oldest_answer = {
                    'question_id': item.get('question_id'),
                    'title': item.get('title'),
                    'creation_date': creation_date,
                    'display_name': item.get('owner', {}).get('display_name'),
                    'link': item.get('link'),
                    'is_answered': item.get('is_answered')
                }

            # Respuesta más actual
            if creation_date > newest_date:
                newest_date = creation_date
                newest_answer = {
                    'question_id': item.get('question_id'),
                    'title': item.get('title'),
                    'creation_date': creation_date,
                    'display_name': item.get('owner', {}).get('display_name'),
                    'link': item.get('link'),
                    'is_answered': item.get('is_answered')
                }

    return (oldest_answer, newest_answer)
