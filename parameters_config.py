import gossip
from structures.parameters_structure import Parameters

parameters = Parameters(
    gossip_cost=1,
    read_cost=5,
    n_agents=100,
    n_books=2000,
    gossip_protocol=gossip.SpiderGossipProtocol
)
