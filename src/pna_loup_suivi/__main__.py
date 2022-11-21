"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """Pna_Loup_Suivi."""


if __name__ == "__main__":
    main(prog_name="pna_loup_suivi")  # pragma: no cover
