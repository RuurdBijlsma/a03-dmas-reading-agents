from agents import Agent


class GossipProtocol(object):
    def __init__(self, agent: Agent):
        self.agent = agent

    def can_gossip(self, other: Agent):
        pass

    def next_iteration(self):
        pass

    @staticmethod
    def __str__(**kwargs):
        return "General gossip"
