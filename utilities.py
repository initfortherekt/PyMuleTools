import random
import string


def get_message_id(id_length=8):
    # In the java version, the toJSON method has multiple concerns and global side-effects

    # The construction of message_id should be broken out into a utility that follows
    # this recipe:
    #
    # If GoTenna:
    #   Id starts as the GoTenna UID (GID, 15 characters) if present, otherwise, empty string
    #   A pipe character ('|') is appended
    #   A global counter is incremented and appended
    #   The thusfar id string is MD5 hashed and the first 8 bytes are taken?
    #   Depending on preference the id is either z85 or hex encoded
    #
    # Else (SMS case):
    #   Simply increment the global counter and that's your id
    #
    # But for now, you get a random string ¯\_(ツ)_/¯ annnnd yw

    ''.join([random.choice(string.ascii_letters + string.digits) for n in range(0, id_length)])
