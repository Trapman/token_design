from MathSpecMapping import SystemState
from dataclasses import dataclass
from primitives import (NodeOperatorAddress, ExfuraToken, RPCConsumerAddress, UserApplicationAddress, IngressOperatorAddress,
                        NetworkWatcherAddress, ComputeCredits, FiatCurrency, StakeMap, APIRequestQueue,
                        PublicBulletinPosts, NFTCollection, Time)


@dataclass
class NodeOperatorState(SystemState):
    node_operator_address: NodeOperatorAddress(
        description="The address of the node operator",
        symbol="$A^N$",
        domain="{0,1}^140")
    funds: ExfuraToken(
        description="Funds in native exfura the node operator has in their account",
        symbol="$EXF^N$",
        domain="$\mathbb{Z}^∗$")
    fiat_currency: FiatCurrency(description="Fiat funds a node operator has",
                                domain="$\mathbb{Z}^∗$",
                                symbol="$FIAT^N$")


@dataclass
class NetworkWatcherState(SystemState):
    network_watcher_address: NetworkWatcherAddress(description="The address of the network watcher",
                                                   symbol="$A^W$",
                                                   domain="{0,1}^140")
    funds: ExfuraToken(
        description="Funds in native exfura the network watcher has in their account",
        symbol="$EXF^W$",
        domain="$\mathbb{Z}^∗$")
    fiat_currency: FiatCurrency(
        description="Fiat funds a network watcher has", domain="$\mathbb{Z}^∗$",
        symbol="$FIAT^W$")


@dataclass
class IngressOperatorState(SystemState):
    ingress_operator_address: IngressOperatorAddress(description="The address of the ingress operator",
                                                     symbol="$A^I$",
                                                     domain="{0,1}^140")
    funds: ExfuraToken(
        description="Funds in native exfura the ingress operator has in their account",
        symbol="$EXF^I$",
        domain="$\mathbb{Z}^∗$")
    fiat_currency: FiatCurrency(
        description="Fiat funds an ingress operator has",  domain="$\mathbb{Z}^∗$",
        symbol="$FIAT^I$")


@dataclass
class RPCConsumerState(SystemState):
    rpc_consumer_address: RPCConsumerAddress(description="The address of the rpc consumer",
                                             symbol="$A^R$",
                                             domain="{0,1}^140")
    funds: ExfuraToken(
        description="Funds in native exfura the rpc consumer has in their account",
        symbol="$EXF^R$",
        domain="$\mathbb{Z}^∗$")
    compute_credits: ComputeCredits(
        description="The amount of compute credits that a RPC consumer has attributed to their account",  domain="$\mathbb{Z}^∗$",
        symbol="$CC^R$")
    fiat_currency: FiatCurrency(
        description="Fiat funds a rpc consumer has",  domain="$\mathbb{Z}^∗$",
        symbol="$FIAT^R$")


@dataclass
class UserApplicationState(SystemState):
    user_application_address: UserApplicationAddress(description="The address of the user application",
                                                     symbol="$A^U$",
                                                     domain="{0,1}^140")
    funds: ExfuraToken(
        description="Funds in native exfura the user application has in their account",
        symbol="$EXF^U$",
        domain="$\mathbb{Z}^∗$")
    fiat_currency: FiatCurrency(
        description="Fiat funds a user application has",  domain="$\mathbb{Z}^∗$",
        symbol="$FIAT^U$")


@dataclass
class TreasuryState(SystemState):
    funds: ExfuraToken(description="The funds which the treasury holds on hand",
                       symbol="$EXF^T$",
                       domain="$\mathbb{Z}^∗$")
    stake: StakeMap(description="A dictionary which maps a user address to the amount of stake that address has in the system",
                    symbol="$S^T$",
                    domain="$\mathbb{Z}^∗$")
    fiat_funds: FiatCurrency(description="The amount of fiat currency within the treasury",
                             symbol="$FIAT^T$",
                             domain="$\mathbb{Z}^∗$")


@dataclass
class IngressGatewayState(SystemState):
    request_queue: APIRequestQueue(description="The queue of requests in the ingress gateway which have not yet been taken care of",
                                   symbol="$Q$")


@dataclass
class PublicBulletinBoardState(SystemState):
    watcher_posts: PublicBulletinPosts(description="The posts sent to the public bulletin board",
                                       symbol="$M$")


@dataclass
class TargetBlockChainState(SystemState):
    pass


@dataclass
class NodeRegistryState(SystemState):
    licenses: NFTCollection(
        description="The licenses that have been allocated in the system for operators to be using",
        symbol="$C$")


@dataclass
class FullSystemState(SystemState):
    time: Time(description="The current time in the system",
               symbol="T",
               domain="$\mathbb{Z}^∗$")
