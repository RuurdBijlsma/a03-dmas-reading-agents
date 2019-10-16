from gossip.gossip_protocol import GossipProtocol
from gossip.call_me_once_gossip_protocol import CallMeOnceGossipProtocol
from gossip.learn_new_secrets_gossip_protocol import LearnNewSecretsGossipProtocol
from gossip.spider_gossip_protocol import SpiderGossipProtocol
from gossip.token_gossip_protocol import TokenGossipProtocol


def name_to_class(name):
    # print("name to class " + name)
    return {
        'Call me once': CallMeOnceGossipProtocol,
        'Spider': SpiderGossipProtocol,
        'Token': TokenGossipProtocol,
        'Learn new secret': LearnNewSecretsGossipProtocol,
    }[name]


def class_to_name(class_object):
    # print("class to name " + str(class_object))
    return {
        CallMeOnceGossipProtocol: 'Call me once',
        SpiderGossipProtocol: 'Spider',
        TokenGossipProtocol: 'Token',
        LearnNewSecretsGossipProtocol: 'Learn new secret',
    }[class_object]
