'''
*******************************************************************************
*    BUGBaseControl.py is free software: you can redistribute it and/or modify
*    it under the terms of the GNU General Public License as published by
*    the Free Software Foundation, either version 3 of the License, or
*    (at your option) any later version.
*
*    BUGBaseControl.py is distributed in the hope that it will be useful,
*    but WITHOUT ANY WARRANTY; without even the implied warranty of
*    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
*    GNU General Public License for more details.
*
*    You should have received a copy of the GNU General Public License
*    along with BUGBaseControl.py.  If not, see <http://www.gnu.org/licenses/>.
********************************************************************************

Created on Dec 29, 2009

@author: iocanto
'''


from ioctl_wrapper import ioctl_iow_int
import operator  

DEVICE_NODE = "/dev/bugnavcntl"   # Bug Base device node 
GRPOCTL    = 'b'                  # the group that the ioctl
CMDOCTLON  = 0x1                  #
CMDOCTLOFF = 0x2                  #

HOTKEY_LED_1   = 0x0;
HOTKEY_LED_2   = 0x1;
HOTKEY_LED_3   = 0x2;
HOTKEY_LED_4   = 0x3;

class BUGBaseControl:
    

    def __init__(self):
        try:
            self.device = open(DEVICE_NODE,'r')
        except IOError: 
            print "Unable to open input device: " + DEVICE_NODE  

    def close(self):
        self.device.close()

    def clearLED(self, index):
        index = operator.and_(index, 0xF)
        index = operator.lshift(1, index)
        return  ioctl_iow_int(self.device, GRPOCTL, CMDOCTLOFF, index)

    def clearLEDs(self, index):
        index = operator.and_(index, 0xF)        
        return  ioctl_iow_int(self.device, GRPOCTL, CMDOCTLOFF, index)


    def setLED(self, index):
        index = operator.and_(index, 0xF)
        index = operator.lshift(1, index)
        return  ioctl_iow_int(self.device, GRPOCTL, CMDOCTLON, index)

    def setLEDs(self,index):
        index = operator.and_(index, 0xF)
        return  ioctl_iow_int(self.device, GRPOCTL, CMDOCTLON, index)
    
    

def Test():
    from time import sleep
    base = BUGBaseControl()
    
    for i in range(4):
        print "Turning LED %i On" %(i+1)
        base.setLED(i)
        sleep (1)
        
    for i in range(4):
        sleep (1)
        print "Turning LED %i Off" %(i+1)
        base.clearLED(i)   

    base.close()            