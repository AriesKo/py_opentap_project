from opentap import *
from System import Double, String, Int32
import OpenTap
import time

@attribute(OpenTap.Display("N9917A", "FieldFox Microwave Annalyzer", "py_opentap_pj"))
class N9917A_Instrument(OpenTap.ScpiInstrument):
    
    def __init__(self):
        super(N9917A_Instrument,self).__init__()
        self.Name = "N9917A_Inst"
        self._sw = None
    
    def Open(self):
        super(N9917A_Instrument,self).Open()

    def Close(self):
        if self._sw != None:
            self._sw.Stop()
        super(N9917A_Instrument,self).Close()

    def FullReset(self):
        self.ScpiCommand("*RST")
        time.sleep(0.5)
        temp = self.ScpiQuery[String]("*OPC?")

        op_mode = self.ScpiQuery[String]("INST:SEL?")
        if op_mode != "SA":
            self.ScpiCommand("INST:SEL 'SA'")
            time.sleep(1)
            temp = self.ScpiQuery[String]("*OPC?")

        self.ScpiCommand("MEAS:AOFF")
        time.sleep(1)
        temp = self.ScpiQuery[String]("*OPC?")

        self.ScpiCommand("INIT:CONT OFF")

    def SA_PeakSearch(self,avgcnt,cent_freq,span_freq,band_res,band_vid,ref_level,offset,attenuation,timeout):
        op_mode = self.ScpiQuery[String]("INST:SEL?")
        if op_mode != "SA":
            self.ScpiCommand("INST:SEL 'SA'")
            time.sleep(1)
            temp = self.ScpiQuery[String]("*OPC?")

        self.ScpiCommand("INIT:CONT OFF")
        temp = self.ScpiQuery[String]("*OPC?")

        self.ScpiCommand("TRAC:TYPE AVG")
        self.ScpiCommand("AVER:COUN "+str(avgcnt))
        
        self.ScpiCommand("FREQ:CENT "+str(cent_freq))
        self.ScpiCommand("FREQ:SPAN "+str(span_freq))
        self.ScpiCommand("BAND:RES "+str(band_res))
        self.ScpiCommand("BAND:VID "+str(band_vid))
        self.ScpiCommand("DISP:WIND:TRAC:Y:SCAL:RLEV "+str(ref_level))
        self.ScpiCommand("POW:RF:EXTG "+str(offset))
        self.ScpiCommand("POW:RF:ATT "+str(attenuation))
        self.ScpiCommand("INIT")

        for k in range(timeout*2):
            temp = self.ScpiQuery[String]("*OPC?")
            if temp == 1:
                break
            else:
                time.sleep(0.5)

        self.ScpiCommand("CALC:MARK1:FUNC:MAX")
        temp = self.ScpiQuery[String]("*OPC?")

        x_string = self.ScpiQuery[String]("CALC:MARK1:X?")
        y_string = self.ScpiQuery[String]("CALC:MARK1:Y?")

        return x_string, y_string