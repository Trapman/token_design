from MathSpecMapping import MechanismAction
mechanisms = {}
mechanisms["Treasury Stake Inflow"] = MechanismAction("Treasury Stake Inflow",
                                                      "The mechanism which directs new stake into the treasury",
                                                      [], logic="")
mechanisms["Treasury Stake Outflow"] = MechanismAction("Treasury Stake Outflow",
                                                       "The mechanism which directs new stake out of the treasury",
                                                       [], logic="")
mechanisms["Decrease Token Holder Funds"] = MechanismAction("Decrease Token Holder Funds",
                                                            "The mechanism which decreases the funds that a token holder has",
                                                            [], logic="")
mechanisms["Increase Token Holder Funds"] = MechanismAction("Increase Token Holder Funds",
                                                            "The mechanism which increases the funds that a token holder has",
                                                            [], logic="Increase the funds at the staker_address (from input message) by the amount (also from input message) ")
mechanisms["Ingress Gateway Add Request"] = MechanismAction("Ingress Gateway Add Request",
                                                            "The mechanism which takes care of adding a request to the ingress gateway",
                                                            [], logic="")
mechanisms["Decrease User Tokens"] = MechanismAction("Decrease User Tokens",
                                                     "The mechanism which decreases the user tokens for payment",
                                                     [],
                                                     logic="")
mechanisms["Increase User Compute Credits"] = MechanismAction("Increase User Compute Credits",
                                                              "The mechanism which increases the user compute credits",
                                                              [],
                                                              logic="")
mechanisms["Post Watcher Details"] = MechanismAction("Post Watcher Details",
                                                     "The mechanism which takes a given watcher report of performance and posts it to the public bulletin",
                                                     [],
                                                     logic="")
mechanisms["Initiate Dutch Auction"] = MechanismAction("Initiate Dutch Auction",
                                                       "The mechanism which starts a dutch auction for NFT sale",
                                                       [],
                                                       logic="")
mechanisms["Decrease Token Holder Funds (Node Operator)"] = MechanismAction("Decrease Token Holder Funds (Node Operator)",
                                                                            "The mechanism which decreases the funds that a node operator has",
                                                                            [], logic="")
mechanisms["Allocate NFT License"] = MechanismAction("Allocate NFT License",
                                                     "The mechanism which allocates a new NFT license",
                                                     [], logic="")
mechanisms["Increase User Fiat Currency"] = MechanismAction("Increase User Fiat Currency",
                                                            "The mechanism which increases the amount of fiat currency a user has",
                                                            [], logic="")
mechanisms["Decrease Treasury Fiat Currency"] = MechanismAction("Decrease Treasury Fiat Currency",
                                                                "The mechanism which decreases the amount of fiat currency the treasury has",
                                                                [], logic="")

mechanisms["Decrease Treasury Funds"] = MechanismAction("Decrease Treasury Funds",
                                                        "The mechanism which decreases the amount of funds the treasury has",
                                                        [], logic="")
                                                        [], logic="Decrease the funds attribute for the treasury entity by Input[0].reward_amount")

mechanisms["Decrease Treasury Stake"] = MechanismAction("Decrease Treasury Stake",
                                                        "The mechanism which decreases the stake a user has in the treasury",
                                                        [], logic="Decrease the funds attribute for the treasury entity by Input[0].reward_amount")
                                                        [], logic="Decrease Treasury.stake at Input[0].operator by Input[0].slashed_amount")
