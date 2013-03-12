#!/usr/bin/env python
# -*- coding: utf_8 -*-
"""
 Modbus TestKit: Implementation of Modbus protocol in python

 (C)2009 - Luc Jean - luc.jean@gmail.com
 (C)2009 - Apidev - http://www.apidev.fr

 This is distributed under GNU LGPL license, see license.txt
"""

import sys
import serial

#add logging capability
import logging

import modbus_tk
import modbus_tk.defines as cst
import modbus_tk.modbus_rtu as modbus_rtu
import time

logger = modbus_tk.utils.create_logger("console")

if __name__ == "__main__":
    try:
        #Connect to the slave
        master = modbus_rtu.RtuMaster(serial.Serial(port=6, baudrate=9600, parity='N'))
        master.set_timeout(1.0)
        master.set_verbose(True)
        logger.info("connected")
        #Connect to the slave
        master1 = modbus_rtu.RtuMaster(serial.Serial(port=9, baudrate=9600, parity='N'))
        master1.set_timeout(1.0)
        master1.set_verbose(True)
        logger.info("connected")
        
        while True:
            lectura=master.execute(2, cst.READ_DISCRETE_INPUTS, 0, 10)
            time.sleep (0.01)
            x=0
            while x<10:
                if int (lectura[x])==0:
                    master1.execute(1, cst.WRITE_SINGLE_COIL, x, output_value=0)
                    time.sleep(0.01)
                else:
                    master1.execute(1, cst.WRITE_SINGLE_COIL, x, output_value=1)
                x +=1
                
        
        #logger.info(master.execute(1, cst.READ_HOLDING_REGISTERS, 00001, 3))
        #master.execute(1, cst.WRITE_SINGLE_COIL, 6, output_value=1)
        #logger.info(master.execute(1, cst.READ_COILS, 0, 8))
        #logger.info(master.execute(1, cst.READ_DISCRETE_INPUTS, 0, 8))
        #logger.info(master.execute(1, cst.READ_INPUT_REGISTERS, 100, 3))
        #logger.info(master.execute(1, cst.READ_HOLDING_REGISTERS, 100, 12))
        #logger.info(master.execute(1, cst.WRITE_SINGLE_COIL, 7, output_value=1))
        #logger.info(master.execute(1, cst.WRITE_SINGLE_REGISTER, 100, output_value=54))
        #logger.info(master.execute(1, cst.WRITE_MULTIPLE_COILS, 0, output_value=[1, 1, 0, 1, 1, 0, 1, 1]))
        #logger.info(master.execute(1, cst.WRITE_MULTIPLE_REGISTERS, 100, output_value=xrange(12)))
        
    except modbus_tk.modbus.ModbusError, e:
        logger.error("%s- Code=%d" % (e, e.get_exception_code()))
