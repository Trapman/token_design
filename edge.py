from MathSpecMapping import Edge, StateModificationEdge
from behavioral import behavioral_action_space
from policy import policies
from messages import (LicenseStakeMessage, StakeMessage, AppApiRequestMessage, PurchaseComputeCreditsMessage, TransferComputeCreditsMessage, AppApiResponseMessage,
                      PublicBulletinPostMessage, NFTVoteMessage, NFTAuctionStartMessage, BuyBackMessage, InitiateStakingRewardMessage, VoteForSlashingMessage, StakingRewardMessage,
                      SlashingMessage)
from mechanisms import mechanisms
from entities import treasury, node_operator, network_watcher, rpc_consumer, user_application, ingress_operator, ingress_gateway, public_bulletin_board, node_registry

all_edges = {}

all_edges["Submit RPC Request"] = []

all_edges["Win Dutch Auction"] = [Edge(behavioral_action_space["Win Dutch Auction"],
                                       policies["Stake for License Policy"],
                                       LicenseStakeMessage)]


all_edges["Stake for License Policy"] = [Edge(policies["Stake for License Policy"],
                                              policies["Increase Stake Policy (Node Operator)"],
                                              StakeMessage),
                                         Edge(policies["Stake for License Policy"],
                                              mechanisms["Allocate NFT License"],
                                              StakeMessage)]


all_edges["Allocate NFT License"] = [StateModificationEdge(origin=mechanisms["Allocate NFT License"],
                                                           entity=node_registry,
                                                           variable="licenses")]


all_edges["Receive and Process API Request"] = []

all_edges["Delegate to Node Operator"] = []

all_edges["Increase Stake"] = [Edge(behavioral_action_space["Increase Stake"],
                                    policies["Increase Stake Policy"],
                                    StakeMessage)]

all_edges["Decrease Stake"] = [Edge(behavioral_action_space["Decrease Stake"],
                                    policies["Decrease Stake Policy"],
                                    StakeMessage)]

all_edges["Increase Stake Policy"] = [Edge(policies["Increase Stake Policy"],
                                           mechanisms["Treasury Stake Inflow"],
                                           StakeMessage),
                                      Edge(policies["Increase Stake Policy"],
                                           mechanisms["Decrease Token Holder Funds"],
                                           StakeMessage)]

all_edges["Increase Stake Policy (Node Operator)"] = [Edge(policies["Increase Stake Policy (Node Operator)"],
                                                           mechanisms["Treasury Stake Inflow"],
                                                           StakeMessage),
                                                      Edge(policies["Increase Stake Policy (Node Operator)"],
                                                           mechanisms["Decrease Token Holder Funds (Node Operator)"],
                                                           StakeMessage)]

all_edges["Decrease Stake Policy"] = [Edge(policies["Decrease Stake Policy"],
                                           mechanisms["Treasury Stake Outflow"],
                                           StakeMessage),
                                      Edge(policies["Decrease Stake Policy"],
                                           mechanisms["Increase Token Holder Funds"],
                                           StakeMessage)]

all_edges["Treasury Stake Inflow"] = [StateModificationEdge(origin=mechanisms["Treasury Stake Inflow"],
                                                            entity=treasury,
                                                            variable="funds"),
                                      StateModificationEdge(origin=mechanisms["Treasury Stake Inflow"],
                                                            entity=treasury,
                                                            variable="stake")]
all_edges["Treasury Stake Outflow"] = [StateModificationEdge(origin=mechanisms["Treasury Stake Outflow"],
                                                             entity=treasury,
                                                             variable="funds"),
                                       StateModificationEdge(origin=mechanisms["Treasury Stake Outflow"],
                                                             entity=treasury,
                                                             variable="stake")]
all_edges["Decrease Token Holder Funds"] = [StateModificationEdge(origin=mechanisms["Decrease Token Holder Funds"],
                                                                  entity=node_operator,
                                                                  variable="funds"),
                                            StateModificationEdge(origin=mechanisms["Decrease Token Holder Funds"],
                                                                  entity=network_watcher,
                                                                  variable="funds"),
                                            StateModificationEdge(origin=mechanisms["Decrease Token Holder Funds"],
                                                                  entity=rpc_consumer,
                                                                  variable="funds"),
                                            StateModificationEdge(origin=mechanisms["Decrease Token Holder Funds"],
                                                                  entity=user_application,
                                                                  variable="funds"),
                                            StateModificationEdge(origin=mechanisms["Decrease Token Holder Funds"],
                                                                  entity=ingress_operator,
                                                                  variable="funds")]

all_edges["Decrease Token Holder Funds (Node Operator)"] = [StateModificationEdge(origin=mechanisms["Decrease Token Holder Funds (Node Operator)"],
                                                                                  entity=node_operator,
                                                                                  variable="funds"), ]

all_edges["Increase Token Holder Funds"] = [StateModificationEdge(origin=mechanisms["Increase Token Holder Funds"],
                                                                  entity=node_operator,
                                                                  variable="funds"),
                                            StateModificationEdge(origin=mechanisms["Increase Token Holder Funds"],
                                                                  entity=network_watcher,
                                                                  variable="funds"),
                                            StateModificationEdge(origin=mechanisms["Increase Token Holder Funds"],
                                                                  entity=rpc_consumer,
                                                                  variable="funds"),
                                            StateModificationEdge(origin=mechanisms["Increase Token Holder Funds"],
                                                                  entity=user_application,
                                                                  variable="funds"),
                                            StateModificationEdge(origin=mechanisms["Increase Token Holder Funds"],
                                                                  entity=ingress_operator,
                                                                  variable="funds")]


all_edges["App API Request Via Ingress"] = [Edge(behavioral_action_space["App API Request Via Ingress"],
                                                 policies["App API Request Via Ingress Policy"],
                                                 AppApiRequestMessage)]

all_edges["App API Request Via Ingress Policy"] = [Edge(policies["App API Request Via Ingress Policy"],
                                                        mechanisms["Ingress Gateway Add Request"],
                                                        AppApiRequestMessage,
                                                        optional=True)]

all_edges["Ingress Gateway Add Request"] = [StateModificationEdge(origin=mechanisms["Ingress Gateway Add Request"],
                                                                  entity=ingress_gateway,
                                                                  variable="request_queue")]

all_edges["Monitor Performance"] = [Edge(behavioral_action_space["Monitor Performance"],
                                         policies["Monitor Performance Send API Request"],
                                         AppApiRequestMessage)]

all_edges["Monitor Performance Send API Request"] = [Edge(policies["Monitor Performance Send API Request"],
                                                          policies["Monitor Performance Receive API Request"],
                                                          AppApiResponseMessage)]
all_edges["Monitor Performance Receive API Request"] = [Edge(policies["Monitor Performance Receive API Request"],
                                                             mechanisms["Post Watcher Details"],
                                                             PublicBulletinPostMessage)]

all_edges["Post Watcher Details"] = [StateModificationEdge(origin=mechanisms["Post Watcher Details"],
                                                           entity=public_bulletin_board,
                                                           variable="watcher_posts")]

all_edges["Purchase Compute Credits"] = [Edge(behavioral_action_space["Purchase Compute Credits"],
                                              policies["Purchase Compute Credits Policy"],
                                              PurchaseComputeCreditsMessage)]

all_edges["Purchase Compute Credits Policy"] = [Edge(policies["Purchase Compute Credits Policy"],
                                                     mechanisms["Decrease User Tokens"],
                                                     PurchaseComputeCreditsMessage),
                                                Edge(policies["Purchase Compute Credits Policy"],
                                                     mechanisms["Increase User Compute Credits"],
                                                     TransferComputeCreditsMessage)]

all_edges["Decrease User Tokens"] = [StateModificationEdge(origin=mechanisms["Decrease User Tokens"],
                                                           entity=rpc_consumer,
                                                           variable="funds")]
all_edges["Increase User Compute Credits"] = [StateModificationEdge(origin=mechanisms["Increase User Compute Credits"],
                                                                    entity=rpc_consumer,
                                                                    variable="compute_credits")]

all_edges["Vote for New NFT"] = [Edge(behavioral_action_space["Vote for New NFT"],
                                      policies["New NFT Creation Policy"],
                                      NFTVoteMessage)]

all_edges["New NFT Creation Policy"] = [Edge(policies["New NFT Creation Policy"],
                                             mechanisms["Initiate Dutch Auction"],
                                             NFTAuctionStartMessage,
                                             optional=True)]

all_edges["Initiate Dutch Auction"] = []

all_edges["Buyback for Burn"] = [Edge(behavioral_action_space["Buyback for Burn"],
                                      policies["Buyback for Burn Policy"],
                                      BuyBackMessage,)]
all_edges["Buyback for Burn Policy"] = [Edge(policies["Buyback for Burn Policy"],
                                             mechanisms["Decrease Token Holder Funds"],
                                             BuyBackMessage,),
                                        Edge(policies["Buyback for Burn Policy"],
                                             mechanisms["Increase User Fiat Currency"],
                                             BuyBackMessage,),
                                        Edge(policies["Buyback for Burn Policy"],
                                             mechanisms["Decrease Treasury Fiat Currency"],
                                             BuyBackMessage,)]


all_edges["Increase User Fiat Currency"] = [StateModificationEdge(origin=mechanisms["Increase User Fiat Currency"],
                                                                  entity=node_operator,
                                                                  variable="fiat_currency"),
                                            StateModificationEdge(origin=mechanisms["Increase User Fiat Currency"],
                                                                  entity=network_watcher,
                                                                  variable="fiat_currency"),
                                            StateModificationEdge(origin=mechanisms["Increase User Fiat Currency"],
                                                                  entity=rpc_consumer,
                                                                  variable="fiat_currency"),
                                            StateModificationEdge(origin=mechanisms["Increase User Fiat Currency"],
                                                                  entity=user_application,
                                                                  variable="fiat_currency"),
                                            StateModificationEdge(origin=mechanisms["Increase User Fiat Currency"],
                                                                  entity=ingress_operator,
                                                                  variable="fiat_currency")]

all_edges["Decrease Treasury Fiat Currency"] = [StateModificationEdge(origin=mechanisms["Decrease Treasury Fiat Currency"],
                                                                      entity=treasury,
                                                                      variable="fiat_currency")]

all_edges["Vote for Slashing"] = [Edge(behavioral_action_space["Vote for Slashing"],
                                       policies["Slashing Policy"],
                                       VoteForSlashingMessage,)]

all_edges["Earn Staking Rewards"] = [Edge(behavioral_action_space["Earn Staking Rewards"],
                                          policies["Earn Staking Rewards Policy"],
                                          InitiateStakingRewardMessage,)]


all_edges["Earn Staking Rewards Policy"] = [Edge(policies["Earn Staking Rewards Policy"],
                                                 mechanisms["Increase Token Holder Funds"],
                                                 StakingRewardMessage,
                                                 optional=True),
                                            Edge(policies["Earn Staking Rewards Policy"],
                                                 mechanisms["Decrease Treasury Funds"],
                                                 StakingRewardMessage,
                                                 optional=True)]

all_edges["Decrease Treasury Funds"] = [StateModificationEdge(origin=mechanisms["Decrease Treasury Funds"],
                                                              entity=treasury,
                                                              variable="funds")]

all_edges["Slashing Policy"] = [Edge(policies["Slashing Policy"],
                                     mechanisms["Decrease Treasury Stake"],
                                     SlashingMessage,
                                     optional=True)]

all_edges["Decrease Treasury Stake"] = [StateModificationEdge(origin=mechanisms["Decrease Treasury Stake"],
                                                              entity=treasury,
                                                              variable="stake")]
