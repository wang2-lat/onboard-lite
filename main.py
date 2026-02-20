import typer
from pathlib import Path
from rich.console import Console
from config import create_config, load_config
from preview import preview_tour
from generator import generate_code

app = typer.Typer(help="Lightweight user onboarding tool for startups")
console = Console()

@app.command()
def create(
    output: Path = typer.Option("tour.yaml", "--output", "-o", help="Output YAML file path")
):
    """Create a new onboarding tour configuration"""
    create_config(output)
    console.print(f"[green]✓[/green] Created tour configuration: {output}")

@app.command()
def preview(
    config_file: Path = typer.Argument("tour.yaml", help="Tour configuration file")
):
    """Preview the onboarding tour in CLI"""
    tour_data = load_config(config_file)
    preview_tour(tour_data)

@app.command()
def generate(
    config_file: Path = typer.Argument("tour.yaml", help="Tour configuration file"),
    output: Path = typer.Option("tour.html", "--output", "-o", help="Output HTML file")
):
    """Generate embeddable HTML/JS code snippet"""
    tour_data = load_config(config_file)
    code = generate_code(tour_data)
    output.write_text(code)
    console.print(f"[green]✓[/green] Generated code snippet: {output}")
    console.print("\n[yellow]Copy the content and paste into your webpage before </body> tag[/yellow]")

if __name__ == "__main__":
    app()
