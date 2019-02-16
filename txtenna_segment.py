import json


class TxSegment:

    def __init__(self, payload_id, tx_data, sequence_num=0, tx_hash=None, testnet=False, segment_count=None):
        self.segment_count = segment_count
        self.tx_hash = tx_hash
        self.payload_id = payload_id
        self.testnet = testnet
        self.sequence_num = sequence_num
        self.tx_data = tx_data

    def __str__(self):
        return f"Tx {self.tx_hash} Part {self.sequence_num}"

    def __repr__(self):
        return self.serialize_to_json()

    def serialize_to_json(self):
        data = {
            "i": self.payload_id,
            "t": self.tx_data
        }

        if self.sequence_num > 0:
            data["c"] = self.sequence_num

        if self.sequence_num == 0:
            data["s"] = self.segment_count
            data["h"] = self.tx_hash

        if self.testnet:
            data["n"] = "t"
        else:
            data["n"] = "m"

        return json.dumps(data)

    @classmethod
    def deserialize_from_json(cls, json_string):
        data = json.loads(json_string)

        # Validate
        if not cls.segment_json_is_valid(data):
            raise AttributeError(
                f'Segment JSON is valid but not properly constructed. Refer to MuleTools documentation for details.\r\n\
                    {json_string}')

        # Always present
        payload_id = data["i"]
        payload = data["t"]

        # Tail segments
        if "c" in data:
            sequence_num = data["c"]
        else:
            sequence_num = 0

        # Head segments
        if "s" in data:
            segment_count = data["s"]
        else:
            segment_count = None

        if "h" in data:
            tx_hash = data["h"]
        else:
            tx_hash = None

        # Optional network flag
        if "n" in data and data["n"] == "t":
            testnet = True 
        else:
            testnet = False

        return cls(payload_id, payload, tx_hash=tx_hash, sequence_num=sequence_num, testnet=testnet, segment_count=segment_count)

    @classmethod
    def segment_json_is_valid(cls, data):
        return ("i" in data and "t" in data and
                ("n" not in data or ("n" in data and (data["n"] == "m" or data["n"] == "t"))) and
                (
                        ("s" in data and "h" in data and ("c" not in data or ("c" in data and data["c"] == 0)))
                        or
                        ("c" in data and data["c"] > 0 and "s" not in data and "h" not in data)
                ))

