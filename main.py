import random

import parameters
from agents import RandomAgent
from gossip import CallMeOnceGossipProtocol

secret = random.randint(1, parameters.N_BOOKS)

# Create agents that pick randomly and communicate using a Call Me Once protocol
agents = []
for i in range(0, parameters.N_AGENTS):
    agent = RandomAgent(i)
    agent.gossip_protocol = CallMeOnceGossipProtocol(agent)
    agents.append(agent)

iteration = 0
while True:
    print("Iteration {}".format(iteration))

    for agent in agents:
        agent.choose_book()
        agent.read()

    # run gossip protocol
    for agent in agents:
        for other in agents:
            if agent == other:
                continue

            if agent.gossip_protocol.can_gossip(other):
                agent.gossip(other)

    # provided the gossiping works, each agent has the same list of read books
    assert (len(set(map(lambda a: len(a.read_books), agents))) == 1)

    if secret in agents[0].read_books:
        break

    for agent in agents:
        agent.gossip_protocol.next_iteration()

    iteration += 1

print("secret found: {}!".format(secret))
print("Read books: {}".format(agents[0].read_books))
