"""
====================
Redis DB CLI options
====================

Command line options for configuring job/result queue Redis DBs in psimulate runs.

"""
import click

from vivarium_cluster_tools.psimulate.redis_dbs.launcher import (
    DEFAULT_JOBS_PER_REDIS_INSTANCE,
    DEFAULT_NUM_REDIS_DBS,
)

with_redis = click.option(
    "--redis",
    type=int,
    default=DEFAULT_NUM_REDIS_DBS,
    help=(
        f"Number of redis databases to use.  Defaults to a redis instance for every "
        f"{DEFAULT_JOBS_PER_REDIS_INSTANCE} jobs."
    ),
)
