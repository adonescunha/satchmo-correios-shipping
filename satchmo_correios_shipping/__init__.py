# -*- coding: utf-8 -*-

from .shipper import Shipper
from .utils import get_shipping_choices
from livesettings import config_choice_values, config_get_group
from correios_frete.client import Client

def get_methods():
    return map(lambda o: shipper.Shipper(service_option=o),
        get_shipping_choices())

def get_client():
    settings = config_get_group('satchmo_correios_shipping')

    return Client(
        settings.CEP_ORIGEM.value,
        codigo_empresa=settings.CODIGO_EMPRESA.value,
        senha=settings.SENHA.value
    )
