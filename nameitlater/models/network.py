
from dictshield import document

from nameitlater.models import mixins
from nameitlater.models import fields


class Network(document.Document, mixins.Id, mixins.Tenant,
              mixins.OperationalStatus):
    name = fields.StringField(max_length=255, required=True)
    priority = fields.IntField()
