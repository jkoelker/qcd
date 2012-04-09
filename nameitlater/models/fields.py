
from dictshield.fields import *  # noqa
import netaddr


class _mac_custom(netaddr.mac_unix):
    word_fmt = '%.2x'


class IpAddressField(BaseField):

    def __set__(self, instance, value):
        if value and not isinstance(value, netaddr.IPAddress):
            value = netaddr.IPAddress(value)
        instance_date[self.field_name] = value

    def _jsonschema_type(self):
        return 'string'

    def validate(self, value):
        if not isinstance(value, netaddr.IPAddress):
            try:
                value = netaddr.IPAddress(value)
            except netaddr.AddrFormatError:
                raise ShieldException('Not a valid IPAddress value',
                                      self.field_name, value)
        return value

    def for_json(self, value):
        return str(value)


class MacAddressField(BaseField):

    def __set__(self, instance, value):
        if value and not isinstance(value, netaddr.EUI):
            value = netaddr.EUI(value)
        instance_date[self.field_name] = value

    def _jsonschema_type(self):
        return 'string'

    def validate(self, value):
        if not isinstance(value, netaddr.EUI):
            try:
                value = netaddr.EUI(value)
            except netaddr.AddrFormatError:
                raise ShieldException('Not a valid MacAddress value',
                                      self.field_name, value)
        return value

    def for_json(self, value):
        value.dialect = _mac_custom
        return str(value)


class IpNetworkField(BaseField):

    def __set__(self, instance, value):
        if value and not isinstance(value, netaddr.IPNetwork):
            value = netaddr.IPNetwork(value)
        instance_date[self.field_name] = value

    def _jsonschema_type(self):
        return 'string'

    def validate(self, value):
        if not isinstance(value, netaddr.IPNetwork):
            try:
                value = netaddr.IPNetwork(value)
            except netaddr.AddrFormatError:
                raise ShieldException('Not a valid IPNetwork value',
                                      self.field_name, value)
        return value

    def for_json(self, value):
        return str(value)
