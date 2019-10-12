from gossip.gossip_protocol import GossipProtocol
from gossip.call_me_once_gossip_protocol import CallMeOnceGossipProtocol
from gossip.learn_new_secrets_gossip_protocol import LearnNewSecretsGossipProtocol


def name_to_class(name):
    # print("name to class " + name)
    return {
        'Call me once': CallMeOnceGossipProtocol,
        'Learn new secret': LearnNewSecretsGossipProtocol,
    }[name]


def class_to_name(class_object):
    # print("class to name " + str(class_object))
    return {
        CallMeOnceGossipProtocol: 'Call me once',
        LearnNewSecretsGossipProtocol: 'Learn new secret',
    }[class_object]
