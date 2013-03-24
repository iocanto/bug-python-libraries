#ioctl_wrapper.py - a wrapper for python ioctl calls that replicates the functionality of _IOW, _IOR, and _IO.
#
#See the python development entry on the buglabs community wiki for more information about how these methods were generated.
#The short answer is that they are largely replicating the _IOR(), _IOW(), and _IO() macros in c.
#


from fcntl import ioctl
import struct
from sys import exc_info
from math import ceil

#ioctl_iow will execute an ioctl call, generating the necessary data for a write command.
#
#device - an open file object to the device in question
#iden - the group that the ioctl type belongs to (first argument to _IOW()) can be a char (Buglabs modules)
#cmd - the ioctl type within the group (second argument to _IOW()).  Often like a command.
#size - the number of bytes to transfer (third argument to _IOW())
#data - the data to transmit using the ioctl call.  Should be packed using struct.pack()
#
#You will need to investigate the kernel module source code to get the ioctl group, type, and size info.
#
def ioctl_iow(device, iden, cmd, size, data):
    if device.closed:
        print "Error, device is not open!"
        return
    if isinstance(iden,basestring) and len(iden) != 1:
        print "Error, iden must be a single character or an integer < 0xFF"
        return        
    elif isinstance(iden,basestring): 
        iden = ord(iden)
    if iden > 0xFF:
        print "Error, iden is too large.  Please limit value to 8 bits"
        return
    if cmd > 0xFF:
        print "Error, cmd is too large.  Please limit value to 8 bits."
        return
    if size > 0xFFF:
        print "Error, size is too large.  please limit value to 12 bits."
        return
    val = 0x4 << (4*7) | size << (4*4) | iden << (4*2) | cmd
    try:
        return ioctl(device, val, data)
    except IOError:
        print "Error preforming ioctl write "+str(iden)+" "+str(cmd)+" "+str(size)
        print exc_info()

#ioctl_iow_int will execute an ioctl call, generating the necessary data for a write command.
#
#int_data - the data to transmit using hte ioctl call.  Should be an unpacked python integer.
#other arguments are the same as above.
#
def ioctl_iow_int(device, iden, cmd, int_data):
    size = 4
    if device.closed:
        print "Error, device is not open!"
        return
    if isinstance(iden,basestring) and len(iden) != 1:
        print "Error, iden must be a single character or an integer < 0xFF"
        return        
    elif isinstance(iden,basestring): 
        iden = ord(iden)
    if iden > 0xFF:
        print "Error, iden is too large.  Please limit value to 8 bits"
        return
    if cmd > 0xFF:
        print "Error, cmd is too large.  Please limit value to 8 bits."
        return
    if size > 0xFFF:
        print "Error, size is too large.  please limit value to 12 bits."
        return
    val = 0x4 << (4*7) | size << (4*4) | iden << (4*2) | cmd
    try:    
        return ioctl(device, val, int_data)
    except IOError:
        print "Error preforming ioctl write "+str(iden)+" "+str(cmd)+" "+str(size)
        print exc_info()

#ioctl_ior will execute an ioctl call, generating the necessary data for a read command.
#arguments are the same as above.
#
def ioctl_ior(device, iden, cmd, size):
    if device.closed:
        print "Error, device is not open!"
        return
    if isinstance(iden,basestring) and len(iden) != 1:
        print "Error, iden must be a single character or an integer < 0xFF"
        return        
    elif isinstance(iden,basestring): 
        iden = ord(iden)
    if iden > 0xFF:
        print "Error, iden is too large.  Please limit value to 8 bits"
        return
    if cmd > 0xFF:
        print "Error, cmd is too large.  Please limit value to 8 bits."
        return
    if size > 0xFFF:
        print "Error, size is too large.  please limit value to 12 bits."
        return
    pack = struct.pack(str(size)+'x')
    val = 0x8 << (4*7) | 4 << (4*4) | iden << (4*2) | cmd
    try:
        return ioctl(device, val, pack)
    except IOError:
        print "Error preforming ioctl read "+str(iden)+" "+str(cmd)+" "+str(size)
        print exc_info()

#ioctl_ior will execute an ioctl call, generating the necessary data for a dataless control command.
#arguments are the same as above. 
#
def ioctl_io(device, iden, cmd):
    if device.closed:
        print "Error, device is not open!"
        return
    if isinstance(iden,basestring) and len(iden) != 1:
        print "Error, iden must be a single character or an integer < 0xFF"
        return        
    elif isinstance(iden,basestring): 
        iden = ord(iden)
    if iden > 0xFF:
        print "Error, iden is too large.  Please limit value to 8 bits"
        return
    if cmd > 0xFF:
        print "Error, cmd is too large.  Please limit value to 8 bits."
        return
    pack = struct.pack('4x')
    val = iden << (4*2) | cmd
    try:
        return ioctl(device, val, pack)
    except IOError:
        print "Error preforming ioctl command "+str(iden)+" "+str(cmd)
        print exc_info()
