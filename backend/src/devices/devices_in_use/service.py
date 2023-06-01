from .. import models


def calc_amortization(device: models.DevicesPool):
    yearly_metric_ammortization = 100 / device.resource_of_useful_usage
    yearly_sum_ammortization = device.price * yearly_metric_ammortization
    monthly_ammortization = yearly_sum_ammortization / 12

    # add logic from clickhouse
    pass
