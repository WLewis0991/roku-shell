import typer
from rich.console import Console
from roku_shell.ecp import press_key

app = typer.Typer()
console = Console()
ROKU_IP= XXX.XXX.X.XXX

KEY_COMMANDS = [
    ("home", "Home", "Send the Roku to the home screen."),
    ("power", "Power", "Turn the Roku on/off."),
    ("up", "Up", "Press Up."),
    ("down", "Down", "Press Down."),
    ("left", "Left", "Press Left"),
    ("right", "Right", "Press Right"),
    ("back", "Back", "Press Back"),
    ("select", "Select", "Press Select/OK."),
    ("volume-up", "VolumeUp", "Turn Up Volume"),
    ("mute", "VolumeMute", "Mute Volume"),
    ("volume-down", "VolumeDown", "Turn Down Volume"),
    ("play", "Play", "Play Media"),
    ("pause", "Pause", "Pause Media"),
    ("rev", "Rev", "Reverse Media"),
    ("fwd", "Fwd", "Fast Forward Media")

]

def _make_key_command(key_name: str, description: str):
    def command():
        press_key(ROKU_IP, key_name)
        console.print(f"Sent {key_name}")
    command.__doc__ = description
    return command

for cmd_name, key_name, description in KEY_COMMANDS:
    app.command(name=cmd_name)(_make_key_command(key_name, description))
