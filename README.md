# ImitationLearningTutorialEACL2017

## Installation

You need to install RISE following the instructions here: https://github.com/damianavila/RISE

We assume python3, jupyter and the Chrome browser

To run execute `jupyter notebook` and pick the appropriate notebeook. I suggest the creation of a notebook per tutorial section in order to avoid having very large notebooks that would be difficult to edit collaboratively.

## Structure:

Part 1

Section 1.0
- introduction/motivation: where have they seen this before, recent paper, e.g. dynamic oracles, reinforcement learning for anaphora?

Section 1.1
- structure prediiction basics->transition-based
- kinds of supervision: per-action, end reward
- decomposability
- Cost-sensitive classification

Section 1.2
Pos tagging example interleaved with the algorithm
- exact imitation
- DAgger
- with roll outs and non-decomposable loss
- latent variables/sub-optimal experts


Section 1.3
- A bit of the theory from Goodman et al. 2016
- LoLS diagram connecting it to RL
- Connections with RNNs
- Bandit learning
- Adversarial training/best demonstration not necessarily the best teaching material.
- Negative sampling
- Actor-Critic
- Jana Rao Doppa
- Jason Eisner Coaching

Part 2

- Dependency parsing: heuristic expert definition
- NLG
- Semantic parsing
- focused costing, sequence correction, targeted exploration, changeprop, asymmetric losses for trade off accuracy runtim, precision recall
