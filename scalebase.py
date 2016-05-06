# just notes, not working code!

import os
import struct
from datetime import datetime, timedelta
from time import sleep, strftime

def getWeightInGrams(self, dev="/dev/usb/hiddev0"):
        """
        This device normally appears on /dev/usb/hiddev0, assume
        device still appears on this file handle.
        """
        # If we cannot find the USB device, return -1

        grams = -1
        try:
            fd = os.open(dev, os.O_RDONLY)

            # Read 4 unsigned integers from USB device
            hiddev_event_fmt = "IIII"
            usb_binary_read = struct.unpack(hiddev_event_fmt, os.read(fd, struct.calcsize(hiddev_event_fmt)))
            grams = usb_binary_read[3]
            os.close(fd)
        except OSError as e:
            print("{0} - Failed to read from USB device".format(datetime.utcnow()))
        return grams
        
        