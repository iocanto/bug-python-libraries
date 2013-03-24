'''
*******************************************************************************
*    ButtonEvent.py is free software: you can redistribute it and/or modify
*    it under the terms of the GNU General Public License as published by
*    the Free Software Foundation, either version 3 of the License, or
*    (at your option) any later version.
*
*    ButtonEvent.py is distributed in the hope that it will be useful,
*    but WITHOUT ANY WARRANTY; without even the implied warranty of
*    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
*    GNU General Public License for more details.
*
*    You should have received a copy of the GNU General Public License
*    along with ButtonEvent.py.  If not, see <http://www.gnu.org/licenses/>.
********************************************************************************

Created on Jan 5, 2010

@author: iocanto
'''

BUTTON_SELECT = 257

BUTTON_HOTKEY_1 = 258;

BUTTON_HOTKEY_2 = 259;

BUTTON_HOTKEY_3 = 260;

BUTTON_HOTKEY_4 = 261;

BUTTON_RIGHT = 262;

BUTTON_LEFT = 263;

BUTTON_UP = 264;

BUTTON_DOWN = 265;

KEY_UP   = 0

KEY_DOWN = 1

class ButtonEvent():  
        
    # Constructor
    def __init__(self, button = BUTTON_HOTKEY_1, action = KEY_UP ):
        self.__button = button
        self.__action = action
            
        
    def __str__ (self):
        return "ButtonEvent [__button %i]" % self.__button
    
    def getAction(self):
        return self.__action
    
    def getButton(self):
        return self.__button
    
    def getButtonName(self):
        return  {  257  : "BUTTON_SELECT"  ,
                   258  : "BUTTON_HOTKEY_1",
                   259  : "BUTTON_HOTKEY_2",
                   260  : "BUTTON_HOTKEY_3",
                   261  : "BUTTON_HOTKEY_4",
                   262  : "BUTTON_RIGHT"   ,
                   263  : "BUTTON_LEFT"    ,
                   264  : "BUTTON_UP"      ,
                   265  : "BUTTON_DOWN"    ,                  
        }[self.__button]
    
    def setAction(self, action):
        self.__action = action
    
    def setButton(self, button):
        self.__button = button            
    

    
        
    

               
            
        
    
        
        
        

        