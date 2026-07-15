import typer
from rich.console import Console
from roku_shell.ecp import press_key
from platformdirs import PlatformDirs
from roku_shell.config import get_or_prompt_ip

app = typer.Typer()
console = Console()

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
        # IP is fetched only when this specific command functions runs!
        roku_ip = get_or_prompt_ip()
        press_key(roku_ip, key_name)
        console.print(f"Sent {key_name}")
    command.__doc__ = description
    return command

for cmd_name, key_name, description in KEY_COMMANDS:
    app.command(name=cmd_name)(_make_key_command(key_name, description))

@app.callback(invoke_without_command=True)
def main(ctx: typer.Context):
    """Roku Shell CLI."""
    if ctx.invoked_subcommand is None:
        console.print("[bold cyan]Welcome to Roku-Shell![/bold cyan]")
        
        # Safe display: Show the IP if it exists, otherwise tell them how to set it
        if IP_FILE.exists():
            console.print(f"[dim]Using Roku IP: {IP_FILE.read_text(encoding='utf-8').strip()}[/dim]")
        else:
            console.print("[dim]No Roku IP configured yet. Run any command to set it up.[/dim]")
            
        console.print("Run [green]roku-shell --help[/green] to see available commands.")

