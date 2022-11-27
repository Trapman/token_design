from MathSpecMapping import ParameterVariable, ParameterSet


minimum_qos = ParameterVariable(int, "Minimum Quality of Service",
                                description="The minimum quality of service that is accepted within the system",
                                symbol="$\\underline q$")

minimum_treasury_funds = ParameterVariable(int, "Minimum Treasury Funds",
                                           description="The minimum amount of funds that need to be held in the treasury")

minimum_query_refresh_time = ParameterVariable(int, "Minimum Query Refresh Time",
                                               description="The minimum amount of epochs which must be waited before querying the same node operator again")


class GlobalParametersSystem(ParameterSet):
    minimum_qos: minimum_qos


class TreasuryParameters(ParameterSet):
    minimum_treasury_funds: minimum_treasury_funds


class NetworkWatcherParameters(ParameterSet):
    minimum_query_refresh_time: minimum_query_refresh_time
