from agents import Agent
from gossip import GossipProtocol


class CallMeOnceGossipProtocol(GossipProtocol):
    def can_gossip(self, agent_a, agent_b):
        if agent_b not in agent_a.called:
            agent_a.append(agent_b)
            agent_b.called.append(self)
            return True

        return False

    def next_iteration(self, agent):
        agent.called = []

    @staticmethod
    def __str__(**kwargs):
        return "Call me once"
