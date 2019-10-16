from agents import Agent
from gossip import GossipProtocol


class SpiderGossipProtocol(GossipProtocol):
    def __init__(self, agent: Agent):
        super().__init__(agent)
        self.token = 1

    def can_gossip(self, other: Agent):
        if self.token == 1:
            if other.token == 1:
                other.token = 0
                return True

        return False

    def next_iteration(self):
        self.token = 1

    @staticmethod
    def __str__(**kwargs):
        return "Spider"
