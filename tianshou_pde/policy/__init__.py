"""Policy package."""
# isort:skip_file

from tianshou_pde.policy.base import BasePolicy
from tianshou_pde.policy.random import RandomPolicy
from tianshou_pde.policy.modelfree.dqn import DQNPolicy
from tianshou_pde.policy.modelfree.bdq import BranchingDQNPolicy
from tianshou_pde.policy.modelfree.c51 import C51Policy
from tianshou_pde.policy.modelfree.rainbow import RainbowPolicy
from tianshou_pde.policy.modelfree.qrdqn import QRDQNPolicy
from tianshou_pde.policy.modelfree.iqn import IQNPolicy
from tianshou_pde.policy.modelfree.fqf import FQFPolicy
from tianshou_pde.policy.modelfree.pg import PGPolicy
from tianshou_pde.policy.modelfree.a2c import A2CPolicy
from tianshou_pde.policy.modelfree.npg import NPGPolicy
from tianshou_pde.policy.modelfree.ddpg import DDPGPolicy
from tianshou_pde.policy.modelfree.ppo import PPOPolicy
from tianshou_pde.policy.modelfree.trpo import TRPOPolicy
from tianshou_pde.policy.modelfree.td3 import TD3Policy
from tianshou_pde.policy.modelfree.sac import SACPolicy
from tianshou_pde.policy.modelfree.redq import REDQPolicy
from tianshou_pde.policy.modelfree.discrete_sac import DiscreteSACPolicy
from tianshou_pde.policy.imitation.base import ImitationPolicy
from tianshou_pde.policy.imitation.bcq import BCQPolicy
from tianshou_pde.policy.imitation.cql import CQLPolicy
from tianshou_pde.policy.imitation.td3_bc import TD3BCPolicy
from tianshou_pde.policy.imitation.discrete_bcq import DiscreteBCQPolicy
from tianshou_pde.policy.imitation.discrete_cql import DiscreteCQLPolicy
from tianshou_pde.policy.imitation.discrete_crr import DiscreteCRRPolicy
from tianshou_pde.policy.imitation.gail import GAILPolicy
from tianshou_pde.policy.modelbased.psrl import PSRLPolicy
from tianshou_pde.policy.modelbased.icm import ICMPolicy
from tianshou_pde.policy.multiagent.mapolicy import MultiAgentPolicyManager

__all__ = [
    "BasePolicy",
    "RandomPolicy",
    "DQNPolicy",
    "BranchingDQNPolicy",
    "C51Policy",
    "RainbowPolicy",
    "QRDQNPolicy",
    "IQNPolicy",
    "FQFPolicy",
    "PGPolicy",
    "A2CPolicy",
    "NPGPolicy",
    "DDPGPolicy",
    "PPOPolicy",
    "TRPOPolicy",
    "TD3Policy",
    "SACPolicy",
    "REDQPolicy",
    "DiscreteSACPolicy",
    "ImitationPolicy",
    "BCQPolicy",
    "CQLPolicy",
    "TD3BCPolicy",
    "DiscreteBCQPolicy",
    "DiscreteCQLPolicy",
    "DiscreteCRRPolicy",
    "GAILPolicy",
    "PSRLPolicy",
    "ICMPolicy",
    "MultiAgentPolicyManager",
]
