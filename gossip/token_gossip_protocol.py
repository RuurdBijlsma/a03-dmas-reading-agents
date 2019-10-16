from agents import Agent
from gossip import GossipProtocol


class TokenGossipProtocol(GossipProtocol):
    def __init__(self, agent: Agent):
        super().__init__(agent)
        self.token = True

    def can_gossip(self, other: Agent):
        if other.gossip_protocol.token and self.token:
            self.token = False
            return True

        return False

    def next_iteration(self):
        self.token = True

    @staticmethod
    def __str__(**kwargs):
        return "Token"
