import shutil
from rich.console import Console
from pyfiglet import Figlet

console = Console()

def show_banner():

    width = shutil.get_terminal_size().columns

    if width >= 100:
        font = "slant"
    elif width >= 70:
        font = "standard"
    else:
        console.print("SubPulse", style="bold purple")
        return

    figlet = Figlet(font=font)
    banner = figlet.renderText("SubPulse")

    console.print(banner, style="bold purple")


def show_target_banner(domain: str):
    text = f"Enumerating: {domain} "

    console.print(f"[bold purple]{text}[/bold purple]")
    console.print()