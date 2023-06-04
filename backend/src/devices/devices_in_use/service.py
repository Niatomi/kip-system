
from .. import models
from decimal import Decimal


def calc_amortization(device: models.DevicesPool, months_in_use):
    yearly_metric_ammortization = 100 / device.resource_of_useful_usage
    yearly_sum_ammortization = (Decimal(device.price) *
                                Decimal(yearly_metric_ammortization)) / Decimal(100)
    monthly_ammortization = yearly_sum_ammortization / 12

    return monthly_ammortization * months_in_use
