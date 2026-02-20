import yaml
from pathlib import Path
from rich.console import Console

console = Console()

def create_config(output_path: Path):
    """Create a sample tour configuration"""
    sample_config = {
        "tour": {
            "name": "Product Tour",
            "steps": [
                {
                    "target": "#welcome-button",
                    "title": "Welcome!",
                    "content": "Click here to get started with our product",
                    "position": "bottom"
                },
                {
                    "target": "#dashboard",
                    "title": "Your Dashboard",
                    "content": "This is where you'll see all your important metrics",
                    "position": "right"
                },
                {
                    "target": "#settings",
                    "title": "Settings",
                    "content": "Customize your experience here",
                    "position": "left"
                }
            ]
        }
    }
    
    with open(output_path, 'w') as f:
        yaml.dump(sample_config, f, default_flow_style=False, sort_keys=False)

def load_config(config_path: Path):
    """Load tour configuration from YAML file"""
    if not config_path.exists():
        console.print(f"[red]Error:[/red] Configuration file not found: {config_path}")
        raise typer.Exit(1)
    
    with open(config_path, 'r') as f:
        return yaml.safe_load(f)
