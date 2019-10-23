from agents import Agent


class GossipProtocol(object):
    def can_gossip(self, agent_a, agent_b):
        pass

    def next_iteration(self, agent):
        pass

    @staticmethod
    def __str__(**kwargs):
        return "General gossip"
