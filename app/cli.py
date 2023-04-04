from datetime import datetime, timedelta

import rich_click as click


@click.group("app")
def cli():
    pass


@cli.command("run")
@click.option(
    "--start-date",
    type=click.DateTime(),
    help="the start date that which the algorithm runs in",
)
@click.option("--end-date", type=click.DateTime(), help="the end time (exclusive")
def run(start_date: datetime.datetime, end_date: datetime.datetime):
    print("successfully launched")

    # set the default end date to be 2 am the next day
    if not end_date:
        end_date = start_date + timedelta(days=1)
        end_date = end_date.replace(hour=2, minute=0, second=0, microsecond=0)
        
    print(f'Launched from {start_date} to {end_date}')
    