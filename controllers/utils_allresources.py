from utils import BaseHandler
class AllResourcesHandler(BaseHandler):
	"""Handler for allresources page."""
	def get(self):
		"""Handler GET requests."""
		if not self.personalize_page_and_get_enrolled():
			return
		self.template_value['navbar'] = {'allresources': True}
		self.render('allresources.html')
