from ._anvil_designer import HomepageTemplate
from anvil import *
import anvil.server


class Homepage(HomepageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    anvil.server.call('CallSampleXml')
    # Any code you write here will run before the form opens.
