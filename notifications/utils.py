import requests

def enviar_notificaciones(tokens, titulo, mensaje):
    url = "https://onesignal.com/api/v1/notifications"
    headers = {
        "Authorization": "Basic TU_REST_API_KEY",
        "Content-Type": "application/json",
    }
    payload = {
        "app_id": "TU_APP_ID",
        "include_player_ids": tokens,  # Lista de tokens
        "headings": {"en": titulo},
        "contents": {"en": mensaje},
    }

    response = requests.post(url, headers=headers, json=payload)
    return response.json()


def obtener_player_ids(app_id, api_key):
    url = f"https://onesignal.com/api/v1/players?app_id={app_id}&limit=50"
    headers = {
        "Authorization": f"Basic {api_key}",
        "Content-Type": "application/json",
    }
    response = requests.get(url, headers=headers)
    return response.json()
