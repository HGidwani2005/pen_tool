import click
from scanners import nmap_scan, nikto_scan, nessus_scan

@click.group()
def cli():
    pass

@cli.command()
@click.argument('target')
def nmap(target):
    result = nmap_scan(target)
    click.echo(result)

@cli.command()
@click.argument('target')
def nikto(target):
    result = nikto_scan(target)
    click.echo(result)

@cli.command()
@click.argument('target')
@click.option('--access-key', required=True)
@click.option('--secret-key', required=True)
@click.option('--policy-id', default=1, type=int)
def nessus(target, access_key, secret_key, policy_id):
    result = nessus_scan(target, access_key, secret_key, policy_id)
    click.echo(result)

if __name__ == '__main__':
    cli()