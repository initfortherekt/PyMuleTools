
class TxTennaAdapter:
    pass


class TxTennaHexAdapter:
    pass


class TxTennaZ85Adapter:
    pass


# Driver will receive a payload, deserialize and provide adapter with json. Json should be converted to segment

# The driver will simply relay the message to the adapter layer.

# Assume segments can come out of order

# As segments come in, they will be sent to the adapter layer

# Adapter layer will have dictionary storage keyed on payload id
#   what happens if segments come out of order

# Upon completion of validation and receipt of all the segments, what to do?

#   I could signal an event

#   I could manually do a check on every add:

#   SegmentCollection.add(segment)
#   if SegmentCollection.isComplete:
#       tx = SegmentCollection.serialize()


