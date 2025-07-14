#!/usr/bin/env python3
import typer
import time
from rich.console import Console
from rich.progress import track

app = typer.Typer()
console = Console()

@app.command()
def pomodoro(timer: int):

    with Progress(
        BarColumn(),
        TimeRemainingColumn(),
        console=console
    ) as progress:
       console.print(f"Time Remaining {timer}")

if __name__ == "__main__":
    typer.run(pomodoro)
