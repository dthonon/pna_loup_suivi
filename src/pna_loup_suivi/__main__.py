"""Command-line interface."""

import logging
from logging.handlers import TimedRotatingFileHandler
from pathlib import Path

import click
import pandas as pd  # type: ignore

from . import _
from . import __version__
from . import dist_name


logger = logging.getLogger(__name__)


@click.command()
@click.version_option()
def main() -> None:
    """Pna_Loup_Suivi."""
    data_url = "https://raw.githubusercontent.com/dthonon/pna_loup_suivi/main/data/"

    # Create $HOME/tmp directory if it does not exist
    (Path.home() / "tmp").mkdir(exist_ok=True)

    # create file handler which logs even debug messages
    fh = TimedRotatingFileHandler(
        Path.home() / "tmp" / (dist_name + ".log"),
        when="midnight",
        interval=1,
        backupCount=100,
    )
    # create console handler with a higher log level
    ch = logging.StreamHandler()
    # create formatter and add it to the handlers
    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(module)s:%(funcName)s - %(message)s"
    )
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)
    # add the handlers to the logger
    logger.addHandler(fh)
    logger.addHandler(ch)
    logger.setLevel(logging.INFO)

    logger.info(_("Summarize data files, version %s"), __version__)

    dept = pd.read_csv(
        data_url + "departements-region.csv",
        sep=";",
        header=0,
        names=[
            "Num_Département",
            "Département",
            "Région",
        ],
    )
    # print(dept.head(30))

    # Summarize dommages
    # dommages = pd.read_csv("data/" + "dommages.csv", sep=";")
    dommages = pd.read_csv(data_url + "dommages.csv", sep=";")
    dommages = pd.merge(dommages, dept, on="Département")
    # print(dommages)
    dommages_y = dommages.groupby(["Année", "Région"])
    print(dommages_y.sum(numeric_only=True))

    # Summarize interventions
    # interventions = pd.read_csv("data/" + "protocole_intervention.csv", sep=";")
    interventions = pd.read_csv(data_url + "protocole_intervention.csv", sep=";")
    # print(interventions.set_index("Année").loc[2021].sort_values(by="Département"))
    interventions = pd.merge(interventions, dept, on="Département")
    interventions_y = interventions.groupby(["Année"])
    print(interventions_y.sum(numeric_only=True))

    # Summarize wolf population
    # interventions = pd.read_csv("data/" + "nbloupsestime.csv", sep=";")
    population = pd.read_csv(data_url + "nbloupsestime.csv", sep=";")
    print(population)


if __name__ == "__main__":
    main(prog_name="pna_loup_suivi")  # pragma: no cover
