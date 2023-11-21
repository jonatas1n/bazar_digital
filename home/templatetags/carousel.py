from django import template
from product.models import Product

register = template.Library()

@register.inclusion_tag('carousel.html')
def carousel():
    products = Product.objects.all()[:5]
    return {'products': products}