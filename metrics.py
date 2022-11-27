from MathSpecMapping import DerivedMetric, MetricSet


average_qos = DerivedMetric(name="Average Quality of Service",
                            description="The average quality of service in the system",
                            value="",
                            domain="$\mathbb{Z}$",)


class GlobalMetrics(MetricSet):
    average_qos: average_qos


number_of_operators = DerivedMetric(name="Number of Operators",
                                    description="The number of operators in the system at a given time",
                                    value="",
                                    domain="$\mathbb{Z}^∗$",)


class LocalMetrics(MetricSet):
    number_of_operators: number_of_operators
