"""Bounded-fanout gossip transport."""


class GossipChannel:
    def __init__(self, peers: int, fanout: int):
        self.peers = peers
        self.fanout = fanout
        self._signer = None

    def bind_signer(self, signer):
        self._signer = signer
        return self

    def broadcast(self, payload, ttl_hops: int = 3):
        return {"payload": payload, "ttl_hops": ttl_hops, "fanout": self.fanout}
