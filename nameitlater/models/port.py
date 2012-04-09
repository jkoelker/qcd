
from dictshield import document

from nameitlater.models import mixins
from nameitlater.models import fields


class Port(document.Document, mixins.Id, mixins.Tenant,
           mixins.OperationalStatus):
    status = fields.StringField(max_length=8, choices=["ACTIVE", "DOWN"])
    network_id = fields.UUIDField()
    device_id = fields.UUIDField()
    mac_address = fields.MacAddressField()
