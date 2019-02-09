import json

import pytest
from txtenna_transaction_segment import TxTennaTransactionSegment


class TestTxTennaTransactionSegment:

    def test_constructor_defaults(self):
        segment = TxTennaTransactionSegment("1000", "w]8f<vRG}fayY4]vRG}fayYm#vRG}fayYnc")
        assert segment.tx_hash is None
        assert segment.payload_id == "1000"
        assert segment.payload == "w]8f<vRG}fayY4]vRG}fayYm#vRG}fayYnc"
        assert segment.sequence_num == 0
        assert not segment.testnet
        assert segment.segment_count is None

    def test_str(self):
        segment = TxTennaTransactionSegment("1000", "w]8f<vRG}fayY4]vRG}fayYm#vRG}fayYnc", \
                                            tx_hash="123abc", testnet=False, segment_count=1, sequence_num=0)
        segment_str = str(segment)
        assert segment_str == "Tx 123abc Part 0"

    def test_repr(self):

        segment = TxTennaTransactionSegment("1000", "w]8f<vRG}fayY4]vRG}fayYm#vRG}fayYnc", \
                                            tx_hash="123abc", testnet=False, segment_count=1, sequence_num=0)

        segment_repr = repr(segment)
        assert segment_repr == '{"i": "1000", "t": "w]8f<vRG}fayY4]vRG}fayYm#vRG}fayYnc", "s": 1, "h": "123abc"}'

    def test_serialize_first_segment(self):
        segment = TxTennaTransactionSegment("1000", "w]8f<vRG}fayY4]vRG}fayYm#vRG}fayYnc", \
                                            tx_hash="123abc", testnet=False, segment_count=1, sequence_num=0)

        json_ser = segment.serialize_to_json()
        assert json_ser == '{"i": "1000", "t": "w]8f<vRG}fayY4]vRG}fayYm#vRG}fayYnc", "s": 1, "h": "123abc"}'

    def test_serialize_non_first_segment(self):
        segment = TxTennaTransactionSegment("1000", "w]8f<vRG}fayY4]vRG}fayYm#vRG}fayYnc", \
                                            tx_hash="123abc", testnet=False, segment_count=2, sequence_num=1)

        json_ser = segment.serialize_to_json()
        assert json_ser == '{"i": "1000", "t": "w]8f<vRG}fayY4]vRG}fayYm#vRG}fayYnc", "c": 1}'

    def test_serialize_testnet_segment(self):
        segment = TxTennaTransactionSegment("1000", "w]8f<vRG}fayY4]vRG}fayYm#vRG}fayYnc", \
                                            tx_hash="123abc", testnet=True, segment_count=2, sequence_num=1)

        json_ser = segment.serialize_to_json()
        assert json_ser == '{"i": "1000", "t": "w]8f<vRG}fayY4]vRG}fayYm#vRG}fayYnc", "c": 1, "n": "t"}'

    def test_deserialize_first_from_json(self):
        json_ser = '{"i": "1000", "t": "w]8f<vRG}fayY4]vRG}fayYm#vRG}fayYnc", "s": 1, "h": "123abc"}'
        segment = TxTennaTransactionSegment.deserialize_from_json(json_ser)
        assert segment.payload_id == "1000"
        assert segment.tx_hash == "123abc"
        assert segment.sequence_num == 0
        assert segment.segment_count == 1
        assert segment.testnet is False
        assert segment.payload == "w]8f<vRG}fayY4]vRG}fayYm#vRG}fayYnc"

    def test_deserialize_non_first_from_json(self):
        json_ser = '{"i": "1000", "t": "w]8f<vRG}fayY4]vRG}fayYm#vRG}fayYnc", "c": 1}'
        segment = TxTennaTransactionSegment.deserialize_from_json(json_ser)
        assert segment.payload_id == "1000"
        assert segment.sequence_num == 1
        assert segment.segment_count is None
        assert segment.testnet is False
        assert segment.payload == "w]8f<vRG}fayY4]vRG}fayYm#vRG}fayYnc"

    def test_segment_json_first_is_invalid_nonzero_sequence(self):
        json_ser = '{"i": "1000", "t": "w]8f<vRG}fayY4]vRG}fayYm#vRG}fayYnc", "s": 1, "h": "123abc", "c": 1}'
        json_obj = json.loads(json_ser)
        assert not TxTennaTransactionSegment.segment_json_is_valid(json_obj)

    def test_segment_json_first_is_valid_explicit_zero_sequence(self):
        json_ser = '{"i": "1000", "t": "w]8f<vRG}fayY4]vRG}fayYm#vRG}fayYnc", "s": 1, "h": "123abc", "c": 0}'
        json_obj = json.loads(json_ser)
        assert TxTennaTransactionSegment.segment_json_is_valid(json_obj)

    def test_segment_json_is_invalid_non_zero_sequence_with_hash(self):
        json_ser = '{"i": "1000", "t": "w]8f<vRG}fayY4]vRG}fayYm#vRG}fayYnc", "h": "123abc", "c": 1}'
        json_obj = json.loads(json_ser)
        assert not TxTennaTransactionSegment.segment_json_is_valid(json_obj)

    def test_segment_json_is_invalid_non_zero_sequence_with_segment_count(self):
        json_ser = '{"i": "1000", "t": "w]8f<vRG}fayY4]vRG}fayYm#vRG}fayYnc", "c": 1, "s": 2}'
        json_obj = json.loads(json_ser)
        assert not TxTennaTransactionSegment.segment_json_is_valid(json_obj)

