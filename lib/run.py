import ipdb

from pet import Pet
from owner import Owner
from cli import Cli

Pet.create_table()
Owner.create_table()

cli = Cli()
cli.start()

# ipdb.set_trace()