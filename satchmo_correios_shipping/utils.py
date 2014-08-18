# -*- coding: utf-8 -*-

from livesettings import config_value, config_choice_values
from correios_frete import Package
from .constants import CONFIG_KEY

def _build_package_from_cart(cart, checking_function):
    package = Package()

    for cart_item in cart.cartitem_set.all():
        product = cart_item.product

        if product.is_shippable and checking_function(product):
            if 'ProductVariation' in product.get_subtypes():
                product = product.productvariation.parent.product

            for i in range(cart_item.quantity):
                package.add_item(
                    weight=float(product.weight),
                    height=float(product.height),
                    width=float(product.width),
                    length=float(product.length)
                )

    return package

def build_package_from_cart(cart, include_free_shipping=False):
    def check(product):
        free_shipping = product.free_shipping

        return not free_shipping or (free_shipping and include_free_shipping)

    return _build_package_from_cart(cart, check)

def build_free_shipping_package_from_cart(cart):
    def check(product):
        return product.free_shipping

    return _build_package_from_cart(cart, check)

def get_shipping_delay():
    return config_value(CONFIG_KEY, 'SHIPPING_DELAY')

def get_shipping_choices(free_shipping=False):
    if free_shipping:
        return config_choice_values(CONFIG_KEY, 'FREE_SHIPPING_CHOICE')

    return config_choice_values(CONFIG_KEY, 'SHIPPING_CHOICES')
