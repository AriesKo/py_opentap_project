from opentap import *
import OpenTap

from satellite.esgs.can import ACM1
from ITS.moduletester.moduletester import ModuleTester
import time

@attribute(OpenTap.Display("Test Can Echo Example", "A simple python can echo test step", "py_opentap_pj"))
class TestCanEcho (TestStep):
    def __init__(self):
        super(TestCanEcho, self).__init__()
    
    def Run(self):
        tester = ModuleTester(project='esgs')
        tester.connect()
 
        # NMT Echo One time
        # msg = ACM1.EchoRequest()
        # msg.echo_count = 0xFF
        # rpy = tester.send_message(msg)

        # NMT Echo every second
        tester.start_nmt_echo('ACM1')
        # NMT Echo Stop to sending every second
        time.sleep(10)
        tester.stop_nmt_echo('ACM1')