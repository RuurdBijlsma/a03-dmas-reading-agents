from agents import Agent


class GossipProtocol(object):
    def __init__(self, agent: Agent):
        self.agent = Agent

    def can_gossip(self, other: Agent):
        pass

    def next_iteration(self):
        pass