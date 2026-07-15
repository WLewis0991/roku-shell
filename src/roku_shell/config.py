import typer
from rich.console import Console
from roku_shell.ecp import press_key
from platformdirs import PlatformDirs

app = typer.Typer()
console = Console()

# Setup paths at the top (lightweight, doesn't block execution)
DIRS = PlatformDirs("RokuShell", "MyCompany", ensure_exists=True)
IP_FILE = DIRS.user_config_path / "roku_ip.txt"

def get_or_prompt_ip() -> str:
    """Gets the IP address. Prompts the user ONLY when a command is executed."""
    if IP_FILE.exists():
        return IP_FILE.read_text(encoding="utf-8").strip()
    
    # This block will only run if a real command is executed and no file exists
    console.print("[bold yellow]No Roku IP address found. Initial setup required.[/bold yellow]")
    roku_ip = input("Enter your Roku's IP address (e.g., 192.168.0.135): ").strip()
    
    if roku_ip:
        IP_FILE.write_text(roku_ip, encoding="utf-8")
        console.print(f"[bold green]✅ IP saved successfully to {IP_FILE}[/bold green]\n")
        return roku_ip
    else:
        console.print("[bold red]❌ Error: You must provide an IP address to use Roku Shell.[/bold red]")
      
