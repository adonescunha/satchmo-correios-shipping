# -*- coding: utf-8 -*-

from correios_frete.constants import *

CONFIG_KEY = 'satchmo_correios_shipping'
SHIPPING_CHOICES = (
    ((SEDEX, 'SEDEX')),
    ((SEDEX_A_COBRAR, u'SEDEX à Cobrar')),
    ((SEDEX_A_COBRAR_COM_CONTRATO, u'SEDEX à Cobrar com Contrato')),
    ((SEDEX_10, 'SEDEX 10')),
    ((SEDEX_HOJE, 'SEDEX Hoje')),
    ((SEDEX_COM_CONTRATO_1, 'SEDEX com Contrato 1')),
    ((SEDEX_COM_CONTRATO_2, 'SEDEX com Contrato 2')),
    ((SEDEX_COM_CONTRATO_3, 'SEDEX com Contrato 3')),
    ((SEDEX_COM_CONTRATO_4, 'SEDEX com Contrato 4')),
    ((SEDEX_COM_CONTRATO_5, 'SEDEX com Contrato 5')),
    ((SEDEX_COM_CONTRATO, 'SEDEX com Contrato')),
    ((PAC, 'PAC')),
    ((PAC_COM_CONTRATO, 'PAC com Contrato')),
    ((E_SEDEX, 'e-SEDEX')),
    ((E_SEDEX_PRIORITARIO, u'e-SEDEX Prioritário')),
    ((E_SEDEX_EXPRESS, 'e-SEDEX Express')),
    ((GRUPO_1_E_SEDEX, 'Grupo 1 e-SEDEX')),
    ((GRUPO_2_E_SEDEX, 'Grupo 2 e-SEDEX')),
    ((GRUPO_3_E_SEDEX, 'Grupo 3 e-SEDEX')),
)
