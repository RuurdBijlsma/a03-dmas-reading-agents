from agents import Agent
from gossip import GossipProtocol


class SpiderGossipProtocol(GossipProtocol):
    def can_gossip(self, agent_a, agent_b):
        if agent_a.token and agent_b.token:
            agent_b.token = False
            return True

        return False

    def next_iteration(self, agent):
        agent.token = True

    @staticmethod
    def __str__(**kwargs):
        return "Spider"
