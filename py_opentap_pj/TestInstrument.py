# Example code. Do with it what you like.
# no rights reserved.

from opentap import *
from System import Double
import OpenTap
import clr
import math
clr.AddReference("py_opentap_pj.Api")
from py_opentap_pj.Api import PythonInstrumentApi

@attribute(OpenTap.Display("Test Instrument", "This class implements a shared Python API.", "py_opentap_pj"))
class TestInstrument(Instrument, PythonInstrumentApi):
    def __init__(self):
        "Set up the properties, methods and default values of the instrument."
        super(TestInstrument, self).__init__() # The base class initializer must be invoked.
        self.count = 0
        
    #implement the DoMeasurement method required by ITestApi1.
    @method(Double)
    def DoMeasurement(self):
        """Example of a measurement method."""
        self.count = self.count + 1
        return math.sin(self.count * 4.31532 * 1932141)

