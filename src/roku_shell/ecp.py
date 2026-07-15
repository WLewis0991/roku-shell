import typer
import requests
from requests.exceptions import RequestException
from rich.console import Console

console = Console()

def press_key(ip: str, key: str) -> None:
    """Send a keypress command to the Roku device."""
    url = f"http://{ip}:8060/keypress/{key}"
    try:
        response = requests.post(url, timeout=5)
        response.raise_for_status()
    except RequestException as e:
        console.print(f"[bold red]Failed to send '{key}' to {ip}:[/bold red] {e}")
        raise typer.Exit(code=1) from e
