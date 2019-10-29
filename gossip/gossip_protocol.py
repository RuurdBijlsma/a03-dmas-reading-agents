from agents import Agent


class GossipProtocol(object):
    def can_gossip(self, agent_a, agent_b):
        pass

    def next_iteration(self, agent):
        pass

    def __str__(self):
        return "General gossip"
