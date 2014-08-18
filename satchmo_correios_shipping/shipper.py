# -*- coding: utf-8 -*-

from shipping.modules.base import BaseShipper
from decimal import Decimal
from .utils import get_shipping_delay, build_package_from_cart,\
    build_free_shipping_package_from_cart, get_shipping_choices

class Shipper(BaseShipper):

    def __init__(self, cart=None, contact=None, service_option=None):
        self._valid = False
        self._calculated = False
        self._free_shipping = None
        self._charged_shipping = None
        self.cart = cart
        self.contact = contact

        if service_option:
            self.service_code = service_option[0]
            self.service_description = service_option[1]

        self.id = u'correios-%s' % (self.service_code)

    def __unicode__(self):
        return 'Entrega dos Correios'

    def description(self):
        return self._charged_shipping and self._charged_shipping['description'] or self._free_shipping['description']

    def method(self):
        result = {}

        if self._charged_shipping:
            result['charged_shipping'] = self._charged_shipping

        if self._free_shipping:
            result['free_shipping'] = self._free_shipping

        return result

    def valid(self, order=None):
        return self._valid

    def cost(self):
        print self._calculated
        print self._charged_shipping
        if self._calculated:
            return self._charged_shipping and self._charged_shipping['cost'] or 0

    def expectedDelivery(self):
        if self._charged_shipping:
            delivery_days = self._charged_shipping['delivery_days']
        else:
            delivery_days = self._free_shipping['delivery_days']

        return u'%d dias úteis' % delivery_days

    def calculate(self, cart, contact):
        self._valid = False
        self.calculate_charged_shipping(cart, contact)
        self.calculate_free_shipping(cart, contact)

        if self._free_shipping or self._charged_shipping:
            self._valid = True
            self._calculated = True

    def calculate_charged_shipping(self, cart, contact):
        package = build_package_from_cart(cart)
        self._charged_shipping = self.calculate_shipping(cart, contact, package,
            self.service_code, self.service_description)

    def calculate_free_shipping(self, cart, contact):
        package = build_free_shipping_package_from_cart(cart)
        free_shipping_choice = get_shipping_choices(True)[0]
        self._free_shipping = self.calculate_shipping(cart, contact, package,
            free_shipping_choice[0], free_shipping_choice[1])
        self._free_shipping['cost'] = 0

    def calculate_shipping(self, cart, contact, package, shipping_code,
            service_description):
        from satchmo_correios_shipping import get_client

        services = get_client().calc_preco_prazo(package,
            contact.shipping_address.postal_code, shipping_code)

        if len(services) > 0:
            service = services[0]
            delivery_days = service.prazo_entrega + get_shipping_delay()
            return {
                'description': u'Correios - %s (%s dias úteis)' % (service_description,
                    delivery_days),
                'cost': Decimal(service.valor),
                'delivery_days': delivery_days,
                'method': 'Correios'
            }
