import click

from structix.utils.config import load_config
from structix.utils.ops.providers import get_provider_command


@click.command(name="cluster")  # type: ignore
def status_cluster() -> None:
    """Show cluster status across nodes, pods, deployments, etc."""
    config = load_config()
    provider = config.get("cluster", {}).get("provider")

    if not provider:
        click.echo("❌ No cluster provider configured.")
        return

    command = get_provider_command(provider, "status")

    if not command:
        click.echo(f"❌ 'status' is not supported by provider '{provider}'")
        return

    click.echo(f"🔍 Fetching cluster status for provider: {provider}")
    command()
