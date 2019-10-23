import gossip


class Parameters(object):
    def __init__(self, gossip_cost=0, read_cost=0, n_agents: int = 0, n_books: int = 0, all_agents_must_know=False,
                 gossip_protocol: gossip.gossip_protocol.GossipProtocol = gossip.CallMeOnceGossipProtocol()):
        self.gossip_cost = gossip_cost
        self.read_cost = read_cost
        self.n_agents = n_agents
        self.n_books = n_books
        self.all_agents_must_know = all_agents_must_know
        self.gossip_protocol = gossip_protocol

    @staticmethod
    def to_csv_names():
        return ['gossip_cost', 'read_cost', 'n_agents', 'n_books', 'all_agents_must_know', 'gossip_protocol']

    def to_csv_row(self):
        return [self.gossip_cost, self.read_cost, self.n_agents, self.n_books, self.all_agents_must_know,
                gossip.class_to_name(self.gossip_protocol)]
