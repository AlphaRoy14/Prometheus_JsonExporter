# Json exporter for prometheus

An exporter to extract json from an API endpoint.

## dependencies
```sh
$ pip install -r requirements.txt
```

## usage

`python json_exporter.py <port_no> <api_endpoint>`
eg:
```sh
$ python3 json_exporter.py 8003 https://api.test.com/endpoint
```
To run it in the background:
```sh
$ python3 json_exporter.py 8003 https://api.test.com/endpoint &amp
```

## data from api endpoint
```json
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
```

## Output
The exporter should run at [http://localhost:8003/](http://localhost:8003/) if 8003 is the specified port

```
# HELP python_gc_objects_collected_total Objects collected during gc
# TYPE python_gc_objects_collected_total counter
python_gc_objects_collected_total{generation="0"} 371.0
python_gc_objects_collected_total{generation="1"} 0.0
python_gc_objects_collected_total{generation="2"} 0.0
# HELP python_gc_objects_uncollectable_total Uncollectable object found during GC
# TYPE python_gc_objects_uncollectable_total counter
python_gc_objects_uncollectable_total{generation="0"} 0.0
python_gc_objects_uncollectable_total{generation="1"} 0.0
python_gc_objects_uncollectable_total{generation="2"} 0.0
# HELP python_gc_collections_total Number of times this generation was collected
# TYPE python_gc_collections_total counter
python_gc_collections_total{generation="0"} 51.0
python_gc_collections_total{generation="1"} 4.0
python_gc_collections_total{generation="2"} 0.0
# HELP python_info Python platform information
# TYPE python_info gauge
python_info{implementation="CPython",major="3",minor="7",patchlevel="7",version="3.7.7"} 1.0
# HELP dealer_whatsapp status of whatsapp connection of dealers
# TYPE dealer_whatsapp gauge
dealer_whatsapp{dealerName="jsphyd",info="status"} 1.0
dealer_whatsapp{dealerName="jsphyd",info="outboundMessages"} 0.0
# HELP dealer_whatsapp status of whatsapp connection of dealers
# TYPE dealer_whatsapp gauge
dealer_whatsapp{dealerName="autofinhonda",info="status"} 1.0
dealer_whatsapp{dealerName="autofinhonda",info="outboundMessages"} 1.0
# HELP dealer_whatsapp status of whatsapp connection of dealers
# TYPE dealer_whatsapp gauge
dealer_whatsapp{dealerName="orangehonda",info="status"} 0.0
dealer_whatsapp{dealerName="orangehonda",info="outboundMessages"} 400.0
```
