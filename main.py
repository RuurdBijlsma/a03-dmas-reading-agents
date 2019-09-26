import random

import parameters
from agents import RandomAgent
from gossip import CallMeOnceGossipProtocol

secret = random.randint(1, parameters.N_BOOKS)

# Create agents that pick randomly and communicate using a Call Me Once protocol
agents = []

book_reads = {}
for i in range(1, parameters.N_BOOKS + 1):
    book_reads[i] = 0

for i in range(0, parameters.N_AGENTS):
    agent = RandomAgent(i, book_reads)
    agent.gossip_protocol = parameters.GOSSIP_PROTOCOL(agent)
    agents.append(agent)

print("Agents will now start searching books for the secret")
print("Protocol: {}, book count: {}, agent count: {}".format(parameters.GOSSIP_PROTOCOL.__name__,
                                                             parameters.N_BOOKS,
                                                             parameters.N_AGENTS))
print(
    "\nStarting simulation, each iteration every agent will read a random" +
    " book which hasn't already been read in the previous iterations" +
    "\nAt the end of each iteration the agents share which books have been read via gossip")
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

duplicate_reads = 0
duplicate_book_reads = 0
books_read = 0

for key in book_reads:
    if book_reads[key] > 0:
        books_read += 1
    if book_reads[key] > 1:
        duplicate_reads += book_reads[key] - 1
        duplicate_book_reads += 1

print("secret found: {}!".format(secret))
print("\nRead books (synchronized between all agents via gossip): {}".format(agents[0].read_books))

print("Read {} out of {} books".format(books_read, parameters.N_BOOKS))
print("{} books were read more than once".format(duplicate_book_reads))
print("{} redundant reads were performed (book was already read when reading)".format(duplicate_reads))
