"""Threshold signature primitives."""


class ThresholdSignature:
    def __init__(self, threshold: int, curve: str = "bls12-381"):
        self.threshold = threshold
        self.curve = curve
        self._channel = None

    def bind(self, channel):
        self._channel = channel
        if hasattr(channel, "bind_signer"):
            channel.bind_signer(self)
        return self
