from django import template
from django.core.urlresolvers import reverse

register = template.Library()

from hashlib import sha256
def sha(value):
	return sha256(value).hexdigest()

@register.simple_tag
def view_problems(unit):
	return reverse("view_problems", args=(unit.id, sha(unit.prob_url),))

@register.simple_tag
def view_solutions(unit):
	return reverse("view_solutions", args=(unit.id, sha(unit.soln_url),))

@register.filter(name='display_initial_choice')
def display_initial_choice(field):
	return ' '.join([ucode for (uid, ucode) in field.field._choices\
			if uid in field.initial])