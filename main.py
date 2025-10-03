#!/usr/bin/env python3
"""
Sora 2 Video Prompt Loader
Loads and displays video generation prompts from sample files in /src
"""

from pathlib import Path
from rich.console import Console
from rich.panel import Panel
from rich.syntax import Syntax
import sys

def load_prompt_file(filepath):
    """Load a prompt file and return its contents."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return None
    except Exception as e:
        return f"Error reading file: {e}"

def display_prompt(filename, content, console):
    """Display a prompt with rich formatting."""
    if content is None:
        console.print(f"[red]File not found: {filename}[/red]")
        return
    
    console.print(Panel(
        content,
        title=f"[bold blue]{filename}[/bold blue]",
        border_style="blue",
        expand=False
    ))

def main():
    """Main function to load and display video prompts."""
    console = Console()
    
    console.print("[bold green]Sora 2 Video Prompt Loader[/bold green]\n")
    
    # Define source directory
    src_dir = Path(__file__).parent / "src"
    
    # Check if src directory exists
    if not src_dir.exists():
        console.print(f"[yellow]Warning: {src_dir} directory not found.[/yellow]")
        console.print("[yellow]Creating example prompt...[/yellow]\n")
        
        # Display example prompt
        example_prompt = (
            "A serene mountain landscape at sunset, with golden light\n"
            "reflecting off snow-capped peaks. Camera slowly pans across\n"
            "the valley, revealing a crystal-clear lake below. 4K quality,\n"
            "cinematic composition, natural lighting."
        )
        display_prompt("example_prompt.txt", example_prompt, console)
        return
    
    # Get all text files in src directory
    prompt_files = list(src_dir.glob("*.txt")) + list(src_dir.glob("*.md"))
    
    if not prompt_files:
        console.print(f"[yellow]No prompt files found in {src_dir}[/yellow]")
        return
    
    # Display all prompts
    console.print(f"Found {len(prompt_files)} prompt file(s):\n")
    
    for prompt_file in prompt_files:
        content = load_prompt_file(prompt_file)
        display_prompt(prompt_file.name, content, console)
        console.print()  # Add spacing between prompts

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nExiting...")
        sys.exit(0)
