import pytest
from txtenna_segment import TxSegment
from payload_factory import PayloadFactory, IncompletePayloadSegmentsError


class TestPayloadFactory:

    @pytest.fixture()
    def raw_hex_transaction(self):
        return "010000000104f98a8dcd4ebc881603fe81e85b46f2e55dce862bf6a8489f46be56956997fb010000006b4830450221008b5d109df78db7e9be30ddf59cf6b37826f495c35ec800f531f394db2ef036d8022021c0a0db1bae17a406f7f10017bfdc9c816febb60b8e5e3697ef3c7d57c87156012102c31ca8111f8adaf3cff9facd1ca30fba8e0acebebc7b51ad484ca615eaef6da1feffffff0240420f00000000001976a914e5bbd998864b9cf9ae76e5c0c779d9cc06e5457088ac8fa5a200000000001976a91441e85563ae76eccb3f2955906523b63c6394209a88ac00000000"

    @pytest.fixture()
    def z85_gotenna_segments(self):

        # 010000000104f98a8dcd4ebc881603fe81e85b46f2e55dce862bf6a8489f46be56956997fb010000006b4830450221008b5d109df78db7e9be30ddf59cf6b37826f495c35ec800f531f394db2ef036d8022021c0a0db1bae17a406f7f10017bfdc9c816febb60b8e5e3697ef3c7d57c87156012102c31ca8111f8adaf3cff9facd1ca30fba8e0acebebc7b51ad484ca615eaef6da1feffffff0240420f00000000001976a914e5bbd998864b9cf9ae76e5c0c779d9cc06e5457088ac8fa5a200000000001976a91441e85563ae76eccb3f2955906523b63c6394209a88ac00000000
        # 0rr910r&jQJM>khH.Z9(F-{rc]5Tf5Haz$@ns@w=r*vx=}VcV%0bCaVmfjRjI^l)+{L(VDZa!yoOC6plcIiOvuDrctg4QT:f7p^K0W5V4PXyA*7O?of[C<xu*)&}l(:vgYun!esjBHqLAAi8-0(D1R5G=[:]uWme+]AF?X@EcyZpX!&TW(c.73+m8Q5L8(@@LCL4/=Of000)WStaEa/{EH!OCxsh<?O]Z/#%VZmr16:KenMJ000008fR$[lfIrUU6ffPkpGP]wH1SCw0wa8H]ZNR000

        # 350f6de5d2b86c4f1618c6dfe06e86541094f39b6db4e11b9869aece24a89883
        # h4KM=^ZT9?78U6G&bjoG5r#^Qzm5mvM$-.Gb=E8.

        payload_segment_0 = TxSegment("30", "0rr910r&jQJM>khH.Z9(F-{rc]5Tf5Haz$@ns@w=r*vx=}VcV%0bCaVmfjRjI^l)+{L(VDZa!yoOC6plcIiOvuDrctg4QT:f7p^K0W5V4PXyA*7O?of[C<xu*)&}",
                                      tx_hash="h4KM=^ZT9?78U6G&bjoG5r#^Qzm5mvM$-.Gb=E8.",
                                      sequence_num=0, segment_count=2, testnet=True)

        payload_segment_1 = TxSegment("30", "l(:vgYun!esjBHqLAAi8-0(D1R5G=[:]uWme+]AF?X@EcyZpX!&TW(c.73+m8Q5L8(@@LCL4/=Of000)WStaEa/{EH!OCxsh<?O]Z/#%VZmr16:KenMJ000008fR$[lfIrUU6ffPkpGP]wH1SCw0wa8H]ZNR000",
                                      sequence_num=1)

        return [payload_segment_0, payload_segment_1]
        # 0rr910099?BH{)mCfen5Qmo<?G*.8{pqa2YWg7WztdsyFxcu*E0000n7624Wwh)}]4]@+D.]z!8sa@W<+GzQt%nS92f<Gn}000007Pwapa.v!NI%<&{zRotVY}net9Y?P40f\/u+000007Pw9vOAa>sv23If5M([.93h2h[v4ng0.j}j0W8+z}Mxm3hzK7p?]+pAhUQM6Zra^h<lT-?V+[8G@jSjPf\/:o[:UUK=P?Hn%6E4KQ=9mO:mYRQdX*34nNu$Y<0u?Kdk6l?@1FhE]^BHSJ!FQy>-*Y=0I1tEqp85]MTn}O!0000

    @pytest.fixture()
    def z85_segments(self):

        # 010000000104f98a8dcd4ebc881603fe81e85b46f2e55dce862bf6a8489f46be56956997fb010000006b4830450221008b5d109df78db7e9be30ddf59cf6b37826f495c35ec800f531f394db2ef036d8022021c0a0db1bae17a406f7f10017bfdc9c816febb60b8e5e3697ef3c7d57c87156012102c31ca8111f8adaf3cff9facd1ca30fba8e0acebebc7b51ad484ca615eaef6da1feffffff0240420f00000000001976a914e5bbd998864b9cf9ae76e5c0c779d9cc06e5457088ac8fa5a200000000001976a91441e85563ae76eccb3f2955906523b63c6394209a88ac00000000
        # 0rr910r&jQJM>khH.Z9(F-{rc]5Tf5Haz$@ns@w=r*vx=}VcV%0bCaVmfjRjI^l)+{L(VDZa!yoOC6plcIiOvuDrctg4QT:f7p^K0W5V4PXyA*7O?of[C<xu*)&}l(:vgYun!esjBHqLAAi8-0(D1R5G=[:]uWme+]AF?X@EcyZpX!&TW(c.73+m8Q5L8(@@LCL4/=Of000)WStaEa/{EH!OCxsh<?O]Z/#%VZmr16:KenMJ000008fR$[lfIrUU6ffPkpGP]wH1SCw0wa8H]ZNR000

        # 350f6de5d2b86c4f1618c6dfe06e86541094f39b6db4e11b9869aece24a89883
        # h4KM=^ZT9?78U6G&bjoG5r#^Qzm5mvM$-.Gb=E8.

        # 0rr910r&jQJM>khH.Z9(F-{rc]5Tf5Haz$@ns@w=r*vx=}VcV%0bCaVmfjRjI^l)
        # +{L(VDZa!yoOC6plcIiOvuDrctg4QT:f7p^K0W5V4PXyA*7O?of[C<xu*)&}l(:vgYun!esjBHqLAAi8-0(D1R5G=[:]uWme+]AF?X@EcyZpX!&TW(c.73+m
        # 8Q5L8(@@LCL4/=Of000)WStaEa/{EH!OCxsh<?O]Z/#%VZmr16:KenMJ000008fR$[lfIrUU6ffPkpGP]wH1SCw0wa8H]ZNR000

        payload_segment_0 = TxSegment("30", "0rr910r&jQJM>khH.Z9(F-{rc]5Tf5Haz$@ns@w=r*vx=}VcV%0bCaVmfjRjI^l)",
                                      tx_hash="h4KM=^ZT9?78U6G&bjoG5r#^Qzm5mvM$-.Gb=E8.",
                                      sequence_num=0, segment_count=3, testnet=True)

        payload_segment_1 = TxSegment("30", "+{L(VDZa!yoOC6plcIiOvuDrctg4QT:f7p^K0W5V4PXyA*7O?of[C<xu*)&}l(:vgYun!esjBHqLAAi8-0(D1R5G=[:]uWme+]AF?X@EcyZpX!&TW(c.73+m",
                                      sequence_num=1)

        payload_segment_2 = TxSegment("30", "8Q5L8(@@LCL4/=Of000)WStaEa/{EH!OCxsh<?O]Z/#%VZmr16:KenMJ000008fR$[lfIrUU6ffPkpGP]wH1SCw0wa8H]ZNR000",
                                      sequence_num=2)

        return [payload_segment_0, payload_segment_1, payload_segment_2]
        # 0rr910099?BH{)mCfen5Qmo<?G*.8{pqa2YWg7WztdsyFxcu*E0000n7624Wwh)}]4]@+D.]z!8sa@W<+GzQt%nS92f<Gn}000007Pwapa.v!NI%<&{zRotVY}net9Y?P40f\/u+000007Pw9vOAa>sv23If5M([.93h2h[v4ng0.j}j0W8+z}Mxm3hzK7p?]+pAhUQM6Zra^h<lT-?V+[8G@jSjPf\/:o[:UUK=P?Hn%6E4KQ=9mO:mYRQdX*34nNu$Y<0u?Kdk6l?@1FhE]^BHSJ!FQy>-*Y=0I1tEqp85]MTn}O!0000

    @pytest.fixture()
    def hex_gotenna_segments(self):

        payload_segment_0 = TxSegment("1000", "010000000104f98a8dcd4ebc881603fe81e85b46f2e55dce862bf6a8489f46be56956997fb010000006b4830450221008b5d",
                                      tx_hash="350f6de5d2b86c4f1618c6dfe06e86541094f39b6db4e11b9869aece24a89883",
                                      sequence_num=0, segment_count=3)
        payload_segment_1 = TxSegment("1000", "109df78db7e9be30ddf59cf6b37826f495c35ec800f531f394db2ef036d8022021c0a0db1bae17a406f7f10017bfdc9c816febb60b8e5e3697ef3c7d57c87156012102c31ca8111f8adaf3cff9facd1ca30fba8e0acebebc7b51",
                                      sequence_num=1)
        payload_segment_2 = TxSegment("1000", "ad484ca615eaef6da1feffffff0240420f00000000001976a914e5bbd998864b9cf9ae76e5c0c779d9cc06e5457088ac8fa5a200000000001976a91441e85563ae76eccb3f2955906523b63c6394209a88ac00000000",
                                      sequence_num=2)

        return [payload_segment_0, payload_segment_1, payload_segment_2]

    def test_from_segments_z85_gotenna_segments(self, z85_gotenna_segments):
        raw_tx = PayloadFactory.from_segments(z85_gotenna_segments)
        assert raw_tx == bytes.fromhex("010000000104f98a8dcd4ebc881603fe81e85b46f2e55dce862bf6a8489f46be56956997fb010000006b4830450221008b5d109df78db7e9be30ddf59cf6b37826f495c35ec800f531f394db2ef036d8022021c0a0db1bae17a406f7f10017bfdc9c816febb60b8e5e3697ef3c7d57c87156012102c31ca8111f8adaf3cff9facd1ca30fba8e0acebebc7b51ad484ca615eaef6da1feffffff0240420f00000000001976a914e5bbd998864b9cf9ae76e5c0c779d9cc06e5457088ac8fa5a200000000001976a91441e85563ae76eccb3f2955906523b63c6394209a88ac00000000")

    def test_from_segments_hex_gotenna_segments(self, hex_gotenna_segments):
        raw_tx = PayloadFactory.from_segments(hex_gotenna_segments)
        assert raw_tx == bytes.fromhex("010000000104f98a8dcd4ebc881603fe81e85b46f2e55dce862bf6a8489f46be56956997fb010000006b4830450221008b5d109df78db7e9be30ddf59cf6b37826f495c35ec800f531f394db2ef036d8022021c0a0db1bae17a406f7f10017bfdc9c816febb60b8e5e3697ef3c7d57c87156012102c31ca8111f8adaf3cff9facd1ca30fba8e0acebebc7b51ad484ca615eaef6da1feffffff0240420f00000000001976a914e5bbd998864b9cf9ae76e5c0c779d9cc06e5457088ac8fa5a200000000001976a91441e85563ae76eccb3f2955906523b63c6394209a88ac00000000")

    def test_from_segments_missing_segments_from_length_inspection(self, hex_gotenna_segments):
        incompete_segments = hex_gotenna_segments[0:1]
        with pytest.raises(IncompletePayloadSegmentsError) as err:
            PayloadFactory.from_segments(incompete_segments)
        assert err.value.args[0] == "Segments length does not match anticipated count in head at index 0"
        assert err.value.missing_index == 0

    def test_from_segments_missing_segments_from_bad_sequence(self, hex_gotenna_segments):
        incomplete_segments = hex_gotenna_segments[-2:]
        with pytest.raises(IncompletePayloadSegmentsError) as err:
            PayloadFactory.from_segments(incomplete_segments)
        assert err.value.args[0] == "Missing segment at index 0"
        assert err.value.missing_index == 0

    def test_from_segments_hash_mismatch(self, hex_gotenna_segments):

        payload_segment_0 = TxSegment("1000", "010000000104f98a8dcd4ebc881603fe81e85b46f2e55dce862bf6a8489f46be56956997fb010000006b4830450221008b5d",
                                      tx_hash="450f6de5d2b86c4f1618c6dfe06e86541094f39b6db4e11b9869aece24a89883",
                                      sequence_num=0, segment_count=3)
        bad_hash_segments = hex_gotenna_segments[1:]
        bad_hash_segments.insert(0, payload_segment_0)
        with pytest.raises(ValueError) as err:
            PayloadFactory.from_segments(bad_hash_segments)
        assert err.value.args[0] == "Transaction payload does not validate against transaction hash"

    def test_from_json(self, z85_gotenna_segments, raw_hex_transaction):
        tx = PayloadFactory.from_json([segment.serialize_to_json() for segment in z85_gotenna_segments])
        assert tx == bytes.fromhex(raw_hex_transaction)

    def test_to_segments_gotenna_z85(self, z85_gotenna_segments, raw_hex_transaction):
        segments = PayloadFactory.to_segments(bytes.fromhex(raw_hex_transaction), "30", is_gotenna=True, use_z85=True,
                                              is_testnet=True)

        assert len(segments) == 2
        assert segments[0].serialize_to_json() == z85_gotenna_segments[0].serialize_to_json()
        assert segments[1].serialize_to_json() == z85_gotenna_segments[1].serialize_to_json()

    def test_to_segments_gotenna_hex(self, hex_gotenna_segments, raw_hex_transaction):

        segments = PayloadFactory.to_segments(bytes.fromhex(raw_hex_transaction), "1000", is_gotenna=True,
                                              use_z85=False, is_testnet=False)

        assert len(segments) == 3
        assert segments[0].serialize_to_json() == hex_gotenna_segments[0].serialize_to_json()
        assert segments[1].serialize_to_json() == hex_gotenna_segments[1].serialize_to_json()
        assert segments[2].serialize_to_json() == hex_gotenna_segments[2].serialize_to_json()

    def test_to_segments_z85(self, z85_segments, raw_hex_transaction):
        segments = PayloadFactory.to_segments(bytes.fromhex(raw_hex_transaction), "30", is_gotenna=False, use_z85=True,
                                              is_testnet=True)

        assert len(segments) == 3
        assert segments[0].serialize_to_json() == z85_segments[0].serialize_to_json()
        assert segments[1].serialize_to_json() == z85_segments[1].serialize_to_json()
        assert segments[2].serialize_to_json() == z85_segments[2].serialize_to_json()

    def test_to_segments_single_segment(self):
        segments = PayloadFactory.to_segments(b'The Times 03 Jan 2009 Chancellor on Brink of Second Bailout for Banks.',
                                              "30", is_gotenna=True, use_z85=True, is_testnet=True)
        assert len(segments) == 1
        assert segments[0].tx_data == 'ra]?=rb3hXB09d)awc6WatLS8iuQX5vqYN^y&13gaA8culul^TyANLcax8&Yz/f8dlsBOAz/{dAw]zYjlsB+EB1N'

    def test_to_json(self, raw_hex_transaction, z85_gotenna_segments):
        json_segments = PayloadFactory.to_json(bytes.fromhex(raw_hex_transaction), "30", is_gotenna=True, use_z85=True,
                                               is_testnet=True)
        expected_json_segments = [segment.serialize_to_json() for segment in z85_gotenna_segments]
        assert json_segments[0] == expected_json_segments[0]
        assert json_segments[1] == expected_json_segments[1]

