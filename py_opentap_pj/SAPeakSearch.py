from opentap import *
from System import Double, String, Int32
import OpenTap

@attribute(OpenTap.Display("SCPI Instrument", "Keysight xSA", "py_opentap_pj"))
class BasicScpiInstrument(OpenTap.ScpiInstrument):
    
    def __init__(self):
        super(BasicScpiInstrument, self).__init__()
        self.log = Trace(self)
        self.Name = "PyInstrument"
    
    def GetIdnString(self):
        self.ScpiQuery[String]("*IDN?")
    
    def SetFrequency(self, frequency):
        self.ScpiCommand("CENT:FREQ {0}", frequency)
        
    def GetFrequency(self):
        self.ScpiQuery[Double]("CENT:FREQ {0}")

@attribute(OpenTap.Display("Peak Search", "Setup & Measure for Peak search Measurement", "py_opentap_pj"))
class PeakSearch(TestStep):
    StepSetting = property(Int32, 10).add_attribute(OpenTap.Display("Step Setting"))

    def __init__(self):
        super().__init__()

    def Run(self):
        self.log.Info("Running Test Step")
        self.UpgradeVerdict(OpenTap.Verdict.Pass)