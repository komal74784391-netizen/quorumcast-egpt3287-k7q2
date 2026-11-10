# QuorumCast

Reference implementation of **QuorumCast**, a threshold-signature broadcast
layer for edge clusters.

## Repository layout

```
quorumcast/
  transport/
    gossip.py
  consensus/
    threshold.py
  testbed/
    failure_injection.py
scripts/
  run_cluster.sh
tests/
  test_threshold.py
requirements.txt
```

The complete implementation (transport, consensus layer, failure-injection
testbed) is in the tree below; no release tags are published.

## Citation

> A. Evans, T. Lindqvist. QuorumCast: Threshold-Signature Broadcast for Edge
> Clusters. Middleware '26.
