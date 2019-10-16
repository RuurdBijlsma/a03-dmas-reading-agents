from agents import Agent
from gossip import GossipProtocol


class SpiderGossipProtocol(GossipProtocol):
    def __init__(self, agent: Agent):
        super().__init__(agent)
        self.token = True

    def can_gossip(self, other: Agent):
        if self.token and other.gossip_protocol.token:
            other.gossip_protocol.token = False
            return True

        return False

    def next_iteration(self):
        self.token = True

    @staticmethod
    def __str__(**kwargs):
        return "Spider"
