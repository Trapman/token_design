from MathSpecMapping import PolicyAction

policies = {}

policies["Stake for License Policy"] = PolicyAction("Stake for License Policy",
                                                    "The policy which determines if the NFT license should be granted, and if so directs any of the mechanisms for granting it.",
                                                    [])

policies["Increase Stake Policy"] = PolicyAction("Increase Stake Policy",
                                                 "The policy which determines if staking can be increased.",
                                                 [])

policies["Decrease Stake Policy"] = PolicyAction("Decrease Stake Policy",
                                                 "The policy which determines if staking can be decreased.",
                                                 [])


policies["App API Request Via Ingress Policy"] = PolicyAction("App API Request Via Ingress Policy",
                                                              "The policy which takes care of any logic around an app api request.",
                                                              [])


policies["Purchase Compute Credits Policy"] = PolicyAction("Purchase Compute Credits Policy",
                                                           "The policy which takes care of converting funds to compute credits.",
                                                           [])

policies["Purchase Compute Credits Policy"] = PolicyAction("Purchase Compute Credits Policy",
                                                           "The policy which takes care of converting funds to compute credits.",
                                                           [])
policies["Purchase Compute Credits Policy"] = PolicyAction("Purchase Compute Credits Policy",
                                                           "The policy which takes care of converting funds to compute credits.",
                                                           [])


policies["Monitor Performance Send API Request"] = PolicyAction("Monitor Performance Send API Request",
                                                                "The policy which takes care of how a watcher sends a request to check.",
                                                                [])

policies["Monitor Performance Receive API Request"] = PolicyAction("Monitor Performance Receive API Request",
                                                                   "The policy which takes care of how a watcher receives the API request response and then deals with it.",
                                                                   [])

policies["New NFT Creation Policy"] = PolicyAction("New NFT Creation Policy",
                                                   "The policy which decides if votes add up to enough for creating a new NFT.",
                                                   [])

policies["Increase Stake Policy (Node Operator)"] = PolicyAction("Increase Stake Policy (Node Operator)",
                                                                 "The policy which determines how to deal with node operator specific staking increases.",
                                                                 [])


policies["Buyback for Burn Policy"] = PolicyAction("Buyback for Burn Policy",
                                                   "The policy which determines how the buyback for burn takes place.",
                                                   [])

policies["Earn Staking Rewards Policy"] = PolicyAction("Earn Staking Rewards Policy",
                                                       "The policy which determines both where a user can earn a staking reward at the current time and what it should be worth.",
                                                       [])

policies["Slashing Policy"] = PolicyAction("Slashing Policy",
                                           "The policy which takes care of possible stake slashing.",
                                           [])
