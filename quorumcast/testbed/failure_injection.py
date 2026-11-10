"""Failure-injection driver used in the paper."""

from quorumcast.transport import GossipChannel
from quorumcast.consensus import ThresholdSignature


def run():
    channel = GossipChannel(peers=5, fanout=2)
    signer = ThresholdSignature(threshold=3, curve="bls12-381")
    signer.bind(channel)
    channel.broadcast({"msg": "heartbeat"}, ttl_hops=4)


if __name__ == "__main__":
    run()
