from dataclasses import dataclass
from primitives import NodeOperatorAddress, RPCConsumerAddress, UserApplicationAddress, IngressOperatorAddress, NetworkWatcherAddress, ExfuraToken, APIRequestDetails, ComputeCredits, APIRequestResponse, FiatCurrency
from typing import Union


@dataclass
class LicenseStakeMessage:
    node_operator_address: NodeOperatorAddress
    token_amount: ExfuraToken
    color: str = "grey"


@dataclass
class StakeMessage:
    staker_address: Union[NodeOperatorAddress, RPCConsumerAddress,
                          UserApplicationAddress, IngressOperatorAddress,
                          NetworkWatcherAddress]
    token_amount: ExfuraToken
    color: str = "grey"


@dataclass
class AppApiRequestMessage:
    address: UserApplicationAddress
    request_details: APIRequestDetails
    color: str = "blue"


@dataclass
class AppApiResponseMessage:
    address: UserApplicationAddress
    request_details: APIRequestDetails
    response_details: APIRequestResponse
    color: str = "purple"


@dataclass
class PurchaseComputeCreditsMessage:
    address: UserApplicationAddress
    payment: ExfuraToken
    color: str = "red"


@dataclass
class TransferComputeCreditsMessage:
    address: UserApplicationAddress
    credits: ComputeCredits
    color: str = "green"


@dataclass
class PublicBulletinPostMessage:
    operator_address: NodeOperatorAddress
    watcher_address: NetworkWatcherAddress
    details: str
    color: str = "orange"


@dataclass
class NFTVoteMessage:
    vote: str
    color: str = "grey"


@dataclass
class NFTAuctionStartMessage:
    details: str
    color: str = "red"


@dataclass
class BuyBackMessage:
    seller_address: Union[NodeOperatorAddress, RPCConsumerAddress,
                          UserApplicationAddress, IngressOperatorAddress,
                          NetworkWatcherAddress]
    token_amount: ExfuraToken
    fiat_amount: FiatCurrency
    color: str = "yellow"


@dataclass
class InitiateStakingRewardMessage:
    called_by: Union[NodeOperatorAddress, RPCConsumerAddress,
                     UserApplicationAddress, IngressOperatorAddress,
                     NetworkWatcherAddress]
    called_at: int
    color: str = "grey"


@dataclass
class StakingRewardMessage:
    called_by: Union[NodeOperatorAddress, RPCConsumerAddress,
                     UserApplicationAddress, IngressOperatorAddress,
                     NetworkWatcherAddress]
    called_at: int
    reward_amount: ExfuraToken
    color: str = "purple"


@dataclass
class VoteForSlashingMessage:
    called_by: NetworkWatcherAddress
    operator: NodeOperatorAddress
    called_at: int
    details: str
    color: str = "grey"


@dataclass
class SlashingMessage:
    called_by: NetworkWatcherAddress
    operator: NodeOperatorAddress
    called_at: int
    details: str
    slashed_amount: ExfuraToken
    color: str = "pink"
