from needle.cases import NeedleTestCase
from needle.driver import NeedlePhantomJS


class SomeTest(NeedleTestCase):
	engine_class = 'needle.engines.perceptualdiff_engine.Engine'

	@classmethod
	def get_web_driver(cls):
		return NeedlePhantomJS()

	def test_image(self):
		self.set_viewport_size(width=2000, height=768)
		self.driver.get('http://ncyl-dev.rootid.in/')
		self.assertScreenshot('.home-content', 'google-logo')