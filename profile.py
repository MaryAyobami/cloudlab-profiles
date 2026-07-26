"""KSplit evaluation"""

# Import the Portal object.
import geni.portal as portal
# Import the ProtoGENI library.
import geni.rspec.pg as pg

# Create a portal context.
pc = portal.Context()

node_types = [
    ("c220g2", "c220g2"),
    ("c220g5", "c220g5"),
    ("sm110p", "sm110p"),
    ("sm220u", "sm220u"),
    ("r650", "r650"),
    ("c6620", "c6620"),
    ("d760p", "d760p"),
    ("c6525-25g", "c6525-25g"),
    ("c6525-100g", "c6525-100g"),
    ("r6525", "r6525"),
    ("r6615", "r6615"),
    ("d7615", "d7615"),
]


pc.defineParameter(
    "nodeType",
    "Node type",
    portal.ParameterType.STRING,
    node_types[0][0],
    node_types,
    "",
)




params = pc.bindParameters()

request = pc.makeRequestRSpec()

node_0 = request.RawPC('node-0')
node_0.hardware_type = params.nodeType
node_0.disk_image = 'urn:publicid:IDN+wisc.cloudlab.us+image+redshift-PG0:ksplit-eval-test-nd'

# Install and execute a script that is contained in the repository.
node_0.addService(pg.Execute(shell="sh", command="/local/repository/ksplit-top.sh"))

# Print the generated rspec
pc.printRequestRSpec(request)
