import requests

def press_key(ip: str, key: str) -> None:
    """Send a keypress command to the Roku device."""
    url = f"http://{ip}:8060/keypress/{key}"
    response = requests.post(url)
    response.raise_for_status()
