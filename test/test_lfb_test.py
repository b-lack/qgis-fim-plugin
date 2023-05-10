import os.path as path
import unittest


from lfb import fib
#from qgisplugin.interfaces import import_image

#DATA_FOLDER = path.join(path.dirname(__file__), "data")

class TestCore(unittest.TestCase):

    def test_core(self):
        # input
        #image, _ = import_image(path.join(DATA_FOLDER, 'image.tif'))

        # run code
        erere = fib(5)

        #result = MyCode(image=image, normalize=True, quotient=255).execute(constant=0.01, threshold=0.2)

        # evaluate
        #self.assertEqual(len(result), len(image))
        # todo it makes more sense to compare the actual content of the array, we leave this up to you