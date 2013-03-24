'''
*******************************************************************************
*    InputEventProvider.py is free software: you can redistribute it and/or modify
*    it under the terms of the GNU General Public License as published by
*    the Free Software Foundation, either version 3 of the License, or
*    (at your option) any later version.
*
*    InputEventProvider.py is distributed in the hope that it will be useful,
*    but WITHOUT ANY WARRANTY; without even the implied warranty of
*    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
*    GNU General Public License for more details.
*
*    You should have received a copy of the GNU General Public License
*    along with InputEventProvider.py.  If not, see <http://www.gnu.org/licenses/>.
********************************************************************************

Created on Dec 30, 2009

@author: iocanto
'''

import threading
import ButtonEvent
from time import sleep


DEVICE_NODE = "/proc/bugnav"

class InputEventProvider(threading.Thread):   
    def __init__(self):
        threading.Thread.__init__(self)
        self.__observers = []
        self.isRunnig = False
        self.__previosValues =['0','0','0','0','0','0','0','0','0']       
        
    def attach(self, observer):        
        if not observer in self.__observers:
            self.__observers.append(observer)           

    def detach(self, observer):
        try:
            self.__observers.remove(observer)
        except ValueError:
            pass        
          
        
    def __notify(self, events ,modifier=None):
        for observer in self.__observers:
            if modifier != observer:
                observer.update(events)          
    
    def run(self):
        self.isRunnig = True
        
        try:
            device = open(DEVICE_NODE,'r')            
        except IOError:
            print IOError ("Unable to open input device: " + DEVICE_NODE)
            return
        
        inputEvents = device.readlines()
                 
        while (self.isRunnig):
            device.seek(0,0)
            inputEvents = device.readlines()
            events = self.__getListEvent(inputEvents)
            if events:           
                self.__notify(events)
            sleep(0.150)            
            
        # Close File    
        device.close()        
            
                  
    def __getListEvent(self, inputEvents):
        result = []         
        for i in range(9):
            if (inputEvents[i][-2:-1] <> self.__previosValues[i]):
                result.append(self.__InputEventToButtonEvent(inputEvents[i]))
                self.__previosValues[i] = inputEvents[i][-2:-1]
                             
        return result            
    
    
    def __InputEventToButtonEvent(self, InputEvent):   
        r = {     'SEL': ButtonEvent.BUTTON_SELECT,
                  'M1 ': ButtonEvent.BUTTON_HOTKEY_1,
                  'M2 ': ButtonEvent.BUTTON_HOTKEY_2,
                  'M3 ': ButtonEvent.BUTTON_HOTKEY_3,
                  'M4 ': ButtonEvent.BUTTON_HOTKEY_4,
                  'XR ': ButtonEvent.BUTTON_RIGHT,
                  'XL ': ButtonEvent.BUTTON_LEFT,
                  'YU ': ButtonEvent.BUTTON_UP,
                  'YD ': ButtonEvent.BUTTON_DOWN,
        }[InputEvent[0:3]]       
        return ButtonEvent.ButtonEvent (r, int (InputEvent[-2:-1]) )

    def close(self):
        self.isRunnig = False   
        

# This class is the Observer
# The observer just need to have a method called update        
class EventViewer:
    def update(self, events):
        if events[0].getAction() == ButtonEvent.KEY_DOWN:         
            print events[0].getButtonName() + " Pressed" 
        else:
            print events[0].getButtonName() + " Released"                 
        
        
def Test():    
    evenProvider = InputEventProvider()
    evenProvider.attach(EventViewer())
    evenProvider.start()  
    sleep(60)
    evenProvider.close()           


    