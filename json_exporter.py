from prometheus_client.core import GaugeMetricFamily, REGISTRY
from prometheus_client import start_http_server
import json
import sys
import requests
import time


class JsonCollector:
    def __init__(self, endpoint):
        self.endpoint = endpoint

    def _get_status(self, status):
        if status == "authenticated":
            return 1
        return 0

    def collect(self):
        response = json.loads(requests.get(self.endpoint).content.decode("UTF-8"))

        for dealer in response:
            g = GaugeMetricFamily(
                "dealer_whatsapp", "status of whatsapp connection of dealers", labels=["dealerName", "info"]
            )
            g.add_metric(labels=[str(dealer["dealer"]), "status"], value=self._get_status(dealer["status"]))
            g.add_metric(
                labels=[str(dealer["dealer"]), "outoundMessages"], value=dealer["totalOutboundMessages"]
            )
            yield g


if __name__ == "__main__":
    start_http_server(int(sys.argv[1]))
    REGISTRY.register(JsonCollector(sys.argv[2]))
    while True:
        time.sleep(1)

"""
Usage: $ python json_exporter.py 8003 https://api.test.com/endpoint
Data looks like
[
    {
        "dealer": "xyz",
        "status": "authenticated",
        "substatus": "normal",
        "totalOutboundMessages": 0
    },
    {
        "dealer": "abc",
        "status": "authenticated",
        "substatus": "normal",
        "totalOutboundMessages": 0
    },
    {
        "dealer": "efg",
        "status": "loading",
        "substatus": "pairing",
        "totalOutboundMessages": 170
    }
]
"""
