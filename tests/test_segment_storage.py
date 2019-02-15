import pytest
from txtenna_segment import TxSegment
from segment_storage import SegmentStorage


@pytest.fixture()
def segments():
    payload1seg1 = TxSegment("1000", "ra]?=rb3hXB09d)awc6WatLS8ir", tx_hash="abc123", sequence_num=0,
                             segment_count=3, testnet=False)
    payload1seg2 = TxSegment("1000", "lUG[Cv}xE)z/M$szxIn^x(mX", sequence_num=1, testnet=False)
    payload1seg3 = TxSegment("1000", "z!pa<wN/T@wfsiEx(4ZgBrCglAV^XSzFKp", sequence_num=2, testnet=False)

    payload2seg1 = TxSegment("1001", "ra]?=B9z5kz6iLlazts{wmYo]Bz(wiA+6klB-N", tx_hash="def456",
                             sequence_num=0,
                             segment_count=2, testnet=False)

    payload3seg2 = TxSegment("1002",
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

    def test_remove_payload_with_seg0(self, segments):
        segments.remove("1000")
        assert segments.get("1000") is None
        assert segments.get_by_transaction_id("abc123") is None

    def test_remove_payload_with_no_seg0(self, segments):
        segments.remove("1002")
        assert segments.get("1002") is None

    def test_remove_payload_when_id_does_not_exist(self, segments):
        segments.remove("9999")

    def test_put_new_payload(self, segments):
        sg = TxSegment("1004", "the payload data for segment 0", tx_hash="789fff", sequence_num=0, segment_count=3)
        segments.put(sg)
        gsg = segments.get("1004")
        assert gsg is not None
        assert gsg[0].tx_hash == "789fff"

    def test_put_new_payload_out_of_order(self, segments):
        sg0 = TxSegment("1005", "the payload data for segment 0", tx_hash="eeeeee", sequence_num=0, segment_count=3)
        sg1 = TxSegment("1005", "the payload data for segment 1", sequence_num=1)
        segments.put(sg1)
        segments.put(sg0)
        gsg = segments.get("1005")
        gsg2 = segments.get_by_transaction_id("eeeeee")
        assert gsg2[0].payload_id == gsg[0].payload_id
        assert len(gsg) == 2
        assert gsg[0].sequence_num == 0
        assert gsg[1].sequence_num == 1

    def test_is_complete_when_no_segments(self, segments):
        assert not segments.is_complete("2000")

    def test_is_complete_when_incomplete(self, segments):
        assert not segments.is_complete("1001")

    def test_is_complete_when_no_first_segment(self, segments):
        assert not segments.is_complete("1002")

    def test_is_complete_when_complete(self, segments):
        assert segments.is_complete("1000")

