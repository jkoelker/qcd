
from dictshield import document
from dictshield import fields


class Mixin(document.EmbeddedDocument):
    class Meta:
        mixin = True


class Id(Mixin):
    id = fields.UUIDField(id_field=True, auto_fill=True)


class Tenant(Mixin):
    tenant = fields.StringField(max_length=255, required=True)


class OperationalStatus(Mixin):
    status = fields.StringField(max_length=16, choices=["UNKNOWN",
                                                       "PROVISIONING",
                                                       "UP",
                                                       "DOWN"])
