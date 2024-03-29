from gossip import GossipProtocol


class LearnNewSecretsGossipProtocol(GossipProtocol):
    def can_gossip(self, agent_a, agent_b):
        difference = agent_a.read_books.difference(agent_b.read_books)
        return len(difference) > 0

    def next_iteration(self, agent):
        pass

    def __str__(self):
        return "Learn new secret"
