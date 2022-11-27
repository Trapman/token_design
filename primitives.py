from dataclasses import dataclass
from typing import Union
from MathSpecMapping import StateVariable
from typing import TypedDict, Dict, List


class NodeOperatorAddress(StateVariable):
    variable_type = str
    name = "NodeOperatorAddress"


class ExfuraToken(StateVariable):
    variable_type = int
    name = "ExfuraToken"


class RPCConsumerAddress(StateVariable):
    variable_type = str
    name = "RPCConsumerAddress"


class UserApplicationAddress(StateVariable):
    variable_type = str
    name = "UserApplicationAddress"


class IngressOperatorAddress(StateVariable):
    variable_type = str
    name = "IngressOperatorAddress"


class NetworkWatcherAddress(StateVariable):
    variable_type = str
    name = "NetworkWatcherAddress"


class APIRequestDetails(StateVariable):
    variable_type = str
    name = "APIRequestDetails"


class ComputeCredits(StateVariable):
    variable_type = int
    name = "ComputeCredits"


class NFT(StateVariable):
    variable_type = str
    name = "NFT"


class FiatCurrency(StateVariable):
    variable_type = int
    name = "FiatCurrency"


class StakeMap(StateVariable):
    variable_type = Dict[NodeOperatorAddress, ExfuraToken]
    name = "StakeMap"


class APIRequest(StateVariable):
    variable_type = TypedDict('APIRequest', requester_address=Union[RPCConsumerAddress, UserApplicationAddress],
                              request_details=APIRequestDetails)
    name = "APIRequest"


class APIRequestResponse(StateVariable):
    variable_type = TypedDict('APIRequestResponse', data=str)
    name = "APIRequestResponse"


class APIRequestQueue(StateVariable):
    variable_type = List[APIRequest]
    name = "APIRequestQueue"


# Fix to avoid partial load
PublicBulletinPostMessage = str


class PublicBulletinPosts(StateVariable):
    variable_type = List[PublicBulletinPostMessage]
    name = "PublicBulletinPosts"


class NFTCollection(StateVariable):
    variable_type = List[NFT]
    name = "NFTCollection"


class Time(StateVariable):
    variable_type = int
    name = "Time"
