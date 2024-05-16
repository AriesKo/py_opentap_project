from opentap import *
import OpenTap
import System
from System import Array, Double, Byte, Int32, String, Boolean
from .N9917A import N9917A_Instrument

@attribute(OpenTap.Display("PeakSearch", "A simple python test step", "py_opentap_pj"))
class PeakSearch(TestStep):
    Instrument = property(N9917A_Instrument,None)\
                .add_attribute(OpenTap.Display("Instrument","","Resource"))
    full_reset_en = property(Boolean,False)\
                    .add_attribute(OpenTap.Display('full reset',"","SA Parameter",0))
    cent_freq = property(Double,1e9)\
                .add_attribute(OpenTap.Unit("Hz"))\
                .add_attribute(OpenTap.Display('Frequency',"","SA Parameter",1))

    def __init__(self):
        super(PeakSearch,self).__init__()
    
    def Run(self):
        if self.full_reset_en == True:
            self.Instrument.FullReset()
            self.log.Info("Run the Full Reset")

        avgcnt = 1
        # cent_freq = 3000000000
        span_freq = 100000000
        band_res = 100000
        band_vid = 100000
        ref_level = 0
        offset = 0
        attenuation = 0
        timeout = 3
        x_string,y_string = self.Instrument.SA_PeakSearch(avgcnt,self.cent_freq,span_freq,band_res,band_vid,ref_level,offset,attenuation,timeout)
        self.log.Info("Peak Frequence {0}Hz, Peak Power {0}dBm",x_string,y_string)