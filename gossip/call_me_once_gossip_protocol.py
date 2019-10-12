from agents import Agent
from gossip import GossipProtocol


class CallMeOnceGossipProtocol(GossipProtocol):
    def __init__(self, agent: Agent):
        super().__init__(agent)
        self.called = []

    def can_gossip(self, other: Agent):
        if other not in self.called:
            self.called.append(other)
            other.gossip_protocol.called.append(self)
            return True

        return False

    def next_iteration(self):
        self.called = []

    @staticmethod
    def __str__(**kwargs):
        return "Call me once"
