from MathSpecMapping import BehavioralAction
from entities import rpc_consumer, node_operator, network_watcher, user_application, ingress_operator, treasury

behavioral_action_space = {}

behavioral_action_space["Submit RPC Request"] = BehavioralAction(label="Submit RPC Request",
                                                                       description="The behavioral action of an RPC consumer submitting a request with the API.",
                                                                       called_by=[
                                                                           rpc_consumer],
                                                                       constraints=[])

behavioral_action_space["Win Dutch Auction"] = BehavioralAction(label="Win Dutch Auction",
                                                                description="The action for putting down stake to get a license after winning a dutch auction for the NFT.",
                                                                called_by=[
                                                                    node_operator],
                                                                constraints=[])

behavioral_action_space["Receive and Process API Request"] = BehavioralAction(label="Receive and Process API Request",
                                                                              description="This is the action of a node operator doing the work for API requests",
                                                                              called_by=[
                                                                                  node_operator],
                                                                              constraints=[])

behavioral_action_space["Delegate to Node Operator"] = BehavioralAction(label="Delegate to Node Operator",
                                                                              description="Token holders may signal their support for specific node operators by delegating their Exfura tokens to them. The delegators receive rewards for supporting the most performant node operators and get slashed otherwise.",
                                                                              called_by=[
                                                                                  network_watcher, rpc_consumer, user_application],
                                                                              constraints=[])

behavioral_action_space["Increase Stake"] = BehavioralAction(label="Increase Stake",
                                                             description="The behavior of adding new stake",
                                                             called_by=[
                                                                 node_operator, network_watcher, rpc_consumer, user_application, ingress_operator],
                                                             constraints=[])

behavioral_action_space["Decrease Stake"] = BehavioralAction(label="Decrease Stake",
                                                             description="The behavior of decreasing stake",
                                                             called_by=[
                                                                 node_operator, network_watcher, rpc_consumer, user_application, ingress_operator],
                                                             constraints=[])


behavioral_action_space["App API Request Via Ingress"] = BehavioralAction(label="App API Request Via Ingress",
                                                                          description="An app makes a request on the API",
                                                                          called_by=[
                                                                              user_application],
                                                                          constraints=[])

behavioral_action_space["Monitor Performance"] = BehavioralAction(label="Monitor Performance",
                                                                  description="Watchers can monitor the performance of node operators",
                                                                  called_by=[
                                                                      network_watcher],
                                                                  constraints=[])

behavioral_action_space["Purchase Compute Credits"] = BehavioralAction(label="Purchase Compute Credits",
                                                                       description="RPC consumers can purchase compute credits to be used within the network",
                                                                       called_by=[
                                                                           rpc_consumer],
                                                                       constraints=[])

behavioral_action_space["Vote for New NFT"] = BehavioralAction(label="Vote for New NFT",
                                                               description="The behavior for starting the dutch auction process",
                                                               called_by=[
                                                                   node_operator, network_watcher, rpc_consumer, user_application, ingress_operator],
                                                               constraints=[])

behavioral_action_space["Buyback for Burn"] = BehavioralAction(label="Buyback for Burn",
                                                               description="The process by which a treasury buys back exfura and burns it to decrease token supply",
                                                               called_by=[
                                                                   treasury],
                                                               constraints=[])

behavioral_action_space["Vote for Slashing"] = BehavioralAction(label="Vote for Slashing",
                                                                description="The process by which network watchers decide who should be slashed",
                                                                called_by=[
                                                                    network_watcher],
                                                                constraints=[])

behavioral_action_space["Earn Staking Rewards"] = BehavioralAction(label="Earn Staking Rewards",
                                                                   description="The process by which an entity calls for earning their rewards from staking",
                                                                   called_by=[
                                                                       node_operator, network_watcher, rpc_consumer, user_application, ingress_operator],
                                                                   constraints=["The user must have stake in the treasury"])
