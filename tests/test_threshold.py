from quorumcast.consensus import ThresholdSignature


def test_threshold():
    assert ThresholdSignature(threshold=3).threshold == 3
