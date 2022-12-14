"""Command-line interface."""
import logging
from logging.handlers import TimedRotatingFileHandler
from pathlib import Path

import click
import pandas as pd

from . import _
from . import __version__


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
        str(Path.home()) + "/tmp/" + __name__ + ".log",
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

    logger.info(_("Summarize data files"))

    reg = pd.read_csv(
        data_url + "reg2016.tab",
        sep="\t",
        header=0,
        names=[
            "Num_Région",
            "Chef_lieu",
            "TNCC",
            "Région_M",
            "Région",
        ],
        usecols=[
            "Num_Région",
            "Région",
        ],
    )
    print(reg)
    dept = pd.read_csv(
        data_url + "depts2016.tab",
        sep="\t",
        header=0,
        names=[
            "Num_Région",
            "Num_dept",
            "Chef_lieu",
            "TNCC",
            "Département_M",
            "Département",
        ],
        usecols=[
            "Num_Région",
            "Num_dept",
            "Département",
        ],
    )
    print(dept)
    dommages = pd.read_csv(data_url + "dommages.csv", sep=";")
    dommages = pd.merge(dommages, dept, on="Département")
    dommages = pd.merge(dommages, reg, on="Num_Région")
    print(dommages)
    interventions = pd.read_csv(data_url + "protocole_intervention.csv", sep=";")
    interventions = pd.merge(interventions, dept, on="Département")
    interventions = pd.merge(interventions, reg, on="Num_Région")
    print(interventions)


if __name__ == "__main__":
    main(prog_name="pna_loup_suivi")  # pragma: no cover
