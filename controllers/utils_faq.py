from utils import BaseHandler
class FaqHandler(BaseHandler):
  """Handler for FAQ page."""
  def get(self):
    """Handler GET requests."""
    # print "Get current get_user"
    # print self.get_user()
    # if not self.get_user():
    # 	self.transient_student = True
    #This if statement will let the non-student unaccessable to the FAQ
	#self.personalize_page_and_get_user():
    # if not self.personalize_page_and_get_enrolled():
    # return
    self.template_value['navbar'] = {'faq': True}
    if not self.get_user():
	    self.template_value['transient_student'] = True
	    self.template_value['loginUrl'] =  True
    self.render('faq.html')
    
