#!/usr/bin/env python3
"""
Simple CLI tool developed with Grok
"""

import click

@click.command()
@click.option('--name', default='World', help='Name to greet')
def hello(name):
    """Simple greeting command."""
    click.echo(f'Hello, {name}! 👋')
    click.echo('This project was created together with Grok 🚀')

if __name__ == '__main__':
    hello()
