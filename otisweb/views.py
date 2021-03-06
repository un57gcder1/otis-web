from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist
from django.db.utils import OperationalError
from django_registration.backends.one_step.views import RegistrationView
import core

class OTISRegistrationView(RegistrationView):
	def registration_allowed(self):
		try:
			semester = core.models.Semester.objects.get(active=True)
			return semester.registration_open
		except (MultipleObjectsReturned, ObjectDoesNotExist, OperationalError):
			return False
	def register(self, form):
		user = super(OTISRegistrationView, self).register(form)
		user.first_name = form.data['first_name']
		user.last_name = form.data['last_name']
		user.save()
