import pytest
from txtenna_segment import TxTennaSegment
from segment_storage import SegmentStorage


@pytest.fixture()
def segments():
    payload1seg1 = TxTennaSegment("1000", "ra]?=rb3hXB09d)awc6WatLS8ir", tx_hash="abc123", sequence_num=0,
                                  segment_count=3, testnet=False)
    payload1seg2 = TxTennaSegment("1000", "lUG[Cv}xE)z/M$szxIn^x(mX", sequence_num=1, testnet=False)
    payload1seg3 = TxTennaSegment("1000", "z!pa<wN/T@wfsiEx(4ZgBrCglAV^XSzFKp", sequence_num=2, testnet=False)

    payload2seg1 = TxTennaSegment("1001", "ra]?=B9z5kz6iLlazts{wmYo]Bz(wiA+6klB-N", tx_hash="def456",
                                  sequence_num=0,
                                  segment_count=2, testnet=False)

    payload3seg2 = TxTennaSegment("1002",
                                  "vS==nBzbkdxLzKfz/QaCz!pb7x<(9av%8*jwO#0(wPF#dB0b7qy?$kjw/$M6wNP7ZwPF#jw/#hevrrSlA=(CB",
                                  sequence_num=1, testnet=False)

    # payload3seg1 = "ra]?=v}xL1A:-=bvQTd&az(mxBrC47aARTDB97#7az#ataARJAwmYjUB7DFoxK@q@B-IIlzEW@y"

    storage = SegmentStorage()

    storage.put(payload1seg1)
    storage.put(payload1seg2)
    storage.put(payload1seg3)
    storage.put(payload2seg1)
    storage.put(payload3seg2)
    return storage


@pytest.mark.usefixtures("segments")
class TestSegmentStorage:

    def test_get_payload_segments_when_id_exists(self, segments):
        payload1 = segments.get("1000")
        assert len(payload1) == 3

    def test_get_payload_segments_when_id_does_not_exist(self, segments):
        no_payload = segments.get("2000")
        assert no_payload is None

    def test_get_payload_by_transaction_id(self, segments):
        payload1 = segments.get_by_transaction_id("abc123")
        assert len(payload1) == 3
