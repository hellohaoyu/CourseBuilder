from utils import BaseHandler
class FaqHandler(BaseHandler):
  """Handler for FAQ page."""
  def get(self):
    """Handler GET requests."""
    if not self.personalize_page_and_get_enrolled():
      return
    self.template_value['navbar'] = {'faq': True}
    self.render('faq.html')
