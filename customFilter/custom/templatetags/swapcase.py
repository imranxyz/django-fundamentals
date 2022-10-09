from django import template
register = template.Library()

@register.filter(name='swapcase')
def swap(string):
	return string.swapcase()

@register.filter(name='stringCat')
def stringCat(string, number):
	return string[0: number]