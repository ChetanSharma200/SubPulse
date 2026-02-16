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
    text = f" SubPulse | Enumerating: {domain} "

    # get terminal width
    width = shutil.get_terminal_size().columns

    # ensure minimum width so it doesn't break
    width = max(len(text) + 4, width)

    line = "═" * width

    console.print(f"[bold purple]{line}[/bold purple]")
    console.print(f"[bold purple]{text.center(width)}[/bold purple]")
    console.print(f"[bold purple]{line}[/bold purple]\n")