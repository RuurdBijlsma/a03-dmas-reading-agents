from agents import Agent
from gossip import GossipProtocol


class TokenGossipProtocol(GossipProtocol):
    def __init__(self):
        super().__init__()
        self.token = True

    def can_gossip(self, agent_a, agent_b):
        if agent_b.token and agent_a.token:
            agent_a.token = False
            return True

        return False

    def next_iteration(self, agent):
        agent.token = True

    def __str__(self):
        return "Token"
