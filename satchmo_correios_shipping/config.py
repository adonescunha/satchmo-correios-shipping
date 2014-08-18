# -*- coding: utf-8 -*-

from livesettings import *
from correios_frete.constants import *
from .constants import CONFIG_KEY, SHIPPING_CHOICES

SHIP_MODULES = config_get('SHIPPING', 'MODULES')
SHIP_MODULES.add_choice((CONFIG_KEY, 'Correios'))

SHIPPING_GROUP = ConfigurationGroup(CONFIG_KEY,
    u'Configurações dos Correios',
    requires = SHIP_MODULES,
    requiresvalue=CONFIG_KEY,
    ordering = 101
)

config_register_list(
    StringValue(SHIPPING_GROUP,
        'CEP_ORIGEM',
        description='CEP de origem',
    ),
    StringValue(SHIPPING_GROUP,
        'CODIGO_EMPRESA',
        description=u'Código da empresa',
        help_text=u'Usado apenas para entregas com contrato.'
    ),
    StringValue(SHIPPING_GROUP,
        'SENHA',
        description=u'Senha',
        help_text=u'Usado apenas para entregas com contrato.'
    ),
    MultipleStringValue(SHIPPING_GROUP,
        'SHIPPING_CHOICES',
        description=u'Opções de entrega disponíveis para os clientes.',
        choices=SHIPPING_CHOICES,
        default=(SEDEX, PAC)
    ),
    StringValue(SHIPPING_GROUP,
        'FREE_SHIPPING_CHOICE',
        description=u'Opção de entrega para produtos com frete grátis.',
        choices=SHIPPING_CHOICES,
        default=PAC
    ),
    IntegerValue(SHIPPING_GROUP,
        'SHIPPING_DELAY',
        description='Tempo para o despache',
        help_text=u'Tempo em dias para o pedido ser despachado após a ' +\
            u'confirmação do pagamento.'
    ),
)
