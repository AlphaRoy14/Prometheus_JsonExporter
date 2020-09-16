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

## output
The exporter should run at [http://localhost:8003/](http://localhost:8003/)

## data
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
