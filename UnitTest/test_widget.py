import ttk
import unittest

class SimpleWidgetTestCase(unittest):
    def setup(self):
        self.widget = ttk.Widget('The widget')

    def tearDown(self):
        self.widget.dispose()
        self.widget = None



class DeafaultWidgetSizeTestCase(SimpleWidgetTestCase):
    def runTest(self):
        self.assertEqual(self.widget.size(), (50,50), 'incorrect default size')


class WidgetResizeTestCase(SimpleWidgetTestCase):
    def runTest(self):
        self.widget.resize(100,150)
        self.assertEqual(self.widget.size(), (100,150), 'wrong size after resize')


class WidgetTestCase(unittest.TestCase):
    def setUp(self):
        self.widget = ttk.Widget('The widget')

    def tearDown(self):
        self.widget.dispose()
        self.widget = None

    def test_default_size(self):
        self.assertEqual(self.widget.size(), (50, 50), 'incorrect default size')

    def test_resize(self):
        self.widget.resize(100,150)
        self.assertEqual(self.widget.size(), (100,150), 'wrong size after resize')