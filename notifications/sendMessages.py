import requests

ONE_SIGNAL_APP_ID = "df7ccfd1-161d-4323-b24f-8a670194e092"
ONE_SIGNAL_API_KEY = "os_v2_app_356m7uiwdvbshmsprjtqdfhasjakgc4cwf6uxruyu3ubyd47iraj35dvw63vkwmeuxpghqy43st7dagvdbafbyvns2w5mrtytfnuely"

def send_global_notification(titulo, contenido, image):
    url = "https://api.onesignal.com/notifications?c=push"
    image = f"https://adminrosarioscore.pythonanywhere.com/{image}"
    payload = {
        "app_id": "df7ccfd1-161d-4323-b24f-8a670194e092",
        "contents": {
            "es": titulo,
            "en": "title"
        },
        "headings": {
            "es": contenido,
            "en": "content"
            },
        "included_segments": ["Total Subscriptions"],
        "big_picture": image
    }
    headers = {
        "accept": "application/json",
        "Authorization": "Key os_v2_app_356m7uiwdvbshmsprjtqdfhasjakgc4cwf6uxruyu3ubyd47iraj35dvw63vkwmeuxpghqy43st7dagvdbafbyvns2w5mrtytfnuely",
        "content-type": "application/json"
    }


    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}
