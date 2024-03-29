import gossip
from structures.parameters_structure import Parameters

# Default config that's used when a simulation is run from main.py
parameters = Parameters(
    gossip_cost=1,
    read_cost=5,
    n_agents=100,
    n_books=2000,
    all_agents_must_know=False,
    gossip_protocol=gossip.SpiderGossipProtocol()
)
