from binascii import unhexlify, b2a_base64
from django import template

register = template.Library()

def get_hex_to_base64(hex_string):
    str = b2a_base64(unhexlify(hex_string))
    return str