from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt

console = Console()

def preview_tour(tour_data: dict):
    """Preview the tour in CLI"""
    tour = tour_data.get("tour", {})
    steps = tour.get("steps", [])
    
    console.print(f"\n[bold cyan]Tour:[/bold cyan] {tour.get('name', 'Unnamed Tour')}")
    console.print(f"[dim]Total steps: {len(steps)}[/dim]\n")
    
    for i, step in enumerate(steps, 1):
        panel_content = f"[bold]{step.get('title', 'Untitled')}[/bold]\n\n"
        panel_content += f"{step.get('content', 'No content')}\n\n"
        panel_content += f"[dim]Target: {step.get('target', 'N/A')}[/dim]\n"
        panel_content += f"[dim]Position: {step.get('position', 'bottom')}[/dim]"
        
        console.print(Panel(
            panel_content,
            title=f"Step {i}/{len(steps)}",
            border_style="cyan"
        ))
        
        if i < len(steps):
            Prompt.ask("\n[yellow]Press Enter for next step[/yellow]", default="")
        else:
            console.print("\n[green]✓ Tour preview completed![/green]")
