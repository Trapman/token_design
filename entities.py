from MathSpecMapping import Entity
from states import (NodeOperatorState, NetworkWatcherState,
                    IngressOperatorState, RPCConsumerState,
                    UserApplicationState, TreasuryState,
                    IngressGatewayState, PublicBulletinBoardState,
                    TargetBlockChainState, NodeRegistryState)

node_operator = Entity("Node Operator", NodeOperatorState)
network_watcher = Entity("Network Watcher", NetworkWatcherState)
ingress_operator = Entity("Ingress Operator", IngressOperatorState)
rpc_consumer = Entity("RPC Consumer", RPCConsumerState)
user_application = Entity("User Application", UserApplicationState)
treasury = Entity("Treasury", TreasuryState)
ingress_gateway = Entity("Ingress Gateway", IngressGatewayState)
public_bulletin_board = Entity(
    "Public Bulletin Board", PublicBulletinBoardState)
target_blockchain = Entity(
    "Target Block Chain", TargetBlockChainState)
node_registry = Entity(
    "Node Registry", NodeRegistryState)
