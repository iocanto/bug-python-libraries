'''
*******************************************************************************
*    sample.py is free software: you can redistribute it and/or modify
*    it under the terms of the GNU General Public License as published by
*    the Free Software Foundation, either version 3 of the License, or
*    (at your option) any later version.
*
*    sample.py is distributed in the hope that it will be useful,
*    but WITHOUT ANY WARRANTY; without even the implied warranty of
*    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
*    GNU General Public License for more details.
*
*    You should have received a copy of the GNU General Public License
*    along with sample.py.  If not, see <http://www.gnu.org/licenses/>.
********************************************************************************

Created on Jan 13, 2010

@author: iocanto
'''

import BUGBaseControl
import InputEventProvider

if __name__ == "__main__":
    print "STARTING BugBaseControl TEST"
    BUGBaseControl.Test()
    
    
    print "\nSTARTING InputEventProvider TEST"
    print "The test will run for 60 sec, Press any key"    
    InputEventProvider.Test()
