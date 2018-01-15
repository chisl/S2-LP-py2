#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""S2-LP: Ultra-low power, high performance, sub-1GHz transceiver"""

__author__     = "ChISL"
__copyright__  = "TBD"
__credits__    = ["ST Microelectronics"]
__license__    = "TBD"
__version__    = "Version 0.1"
__maintainer__ = "https://chisl.io"
__email__      = "info@chisl.io"
__status__     = "Test"

#
#   THIS FILE IS AUTOMATICALLY CREATED
#    D O     N O T     M O D I F Y  !
#

from S2_LP_constants import *

# name:        S2-LP
# description: Ultra-low power, high performance, sub-1GHz transceiver
# manuf:       ST Microelectronics
# version:     Version 0.1
# url:         http://www.st.com/resource/en/datasheet/s2-lp.pdf
# date:        2018-01-15


# Derive from this class and implement read and write
class S2_LP_Base:
	"""Ultra-low power, high performance, sub-1GHz transceiver"""
	# Register GPIO0_CONF
	
	
	def setGPIO0_CONF(self, val):
		"""Set register GPIO0_CONF"""
		self.write(REG.GPIO0_CONF, val, 8)
	
	def getGPIO0_CONF(self):
		"""Get register GPIO0_CONF"""
		return self.read(REG.GPIO0_CONF, 8)
	
	# Bits GPIO_SELECT
	# Specify the GPIO0 I/O signal, default setting POR (see Table 57). 
	# Bits reserved_0
	# Bits GPIO_MODE
	# Register GPIO1_CONF
	
	
	def setGPIO1_CONF(self, val):
		"""Set register GPIO1_CONF"""
		self.write(REG.GPIO1_CONF, val, 8)
	
	def getGPIO1_CONF(self):
		"""Get register GPIO1_CONF"""
		return self.read(REG.GPIO1_CONF, 8)
	
	# Bits GPIO_SELECT
	# Specify the GPIO1 I/O signal, default setting digital GND (see Table 57). 
	# Bits reserved_0
	# Bits GPIO1_MODE
	# Register GPIO2_CONF
	
	
	def setGPIO2_CONF(self, val):
		"""Set register GPIO2_CONF"""
		self.write(REG.GPIO2_CONF, val, 8)
	
	def getGPIO2_CONF(self):
		"""Get register GPIO2_CONF"""
		return self.read(REG.GPIO2_CONF, 8)
	
	# Bits GPIO_SELECT
	# Specify the GPIO2 I/O signal, default setting digital GND (see Table 57). 
	# Bits reserved_0
	# Bits GPIO2_MODE
	# Register GPIO3_CONF
	
	
	def setGPIO3_CONF(self, val):
		"""Set register GPIO3_CONF"""
		self.write(REG.GPIO3_CONF, val, 8)
	
	def getGPIO3_CONF(self):
		"""Get register GPIO3_CONF"""
		return self.read(REG.GPIO3_CONF, 8)
	
	# Bits GPIO_SELECT
	# Specify the GPIO3 I/O signal, default setting digital GND (see Table 57). 
	# Bits reserved_0
	# Bits GPIO_MODE
	# Register SYNT3
	
	
	def setSYNT3(self, val):
		"""Set register SYNT3"""
		self.write(REG.SYNT3, val, 8)
	
	def getSYNT3(self):
		"""Get register SYNT3"""
		return self.read(REG.SYNT3, 8)
	
	# Bits PLL_CP_ISEL
	# Set the charge pump current according to the XTAL frequency (see Table 34). 
	# Bits BS
	# Synthesizer band select. This parameter selects the out-of loop divide factor of 
	#           the synthesizer (see Section 5.3.1): 
	
	# Bits SYNT
	# MSB bits of the PLL programmable divider (see Section 5.3.1). 
	# Register SYNT2
	# Intermediate bits of the PLL programmable divider (see Section 5.3.1). 
	
	def setSYNT2(self, val):
		"""Set register SYNT2"""
		self.write(REG.SYNT2, val, 8)
	
	def getSYNT2(self):
		"""Get register SYNT2"""
		return self.read(REG.SYNT2, 8)
	
	# Bits SYNT2
	# Register SYNT1
	# Intermediate bits of the PLL programmable divider (see Section 5.3.1). 
	
	def setSYNT1(self, val):
		"""Set register SYNT1"""
		self.write(REG.SYNT1, val, 8)
	
	def getSYNT1(self):
		"""Get register SYNT1"""
		return self.read(REG.SYNT1, 8)
	
	# Bits SYNT1
	# Register SYNT0
	# LSB bits of the PLL programmable divider (see Section 5.3.1). 
	
	def setSYNT0(self, val):
		"""Set register SYNT0"""
		self.write(REG.SYNT0, val, 8)
	
	def getSYNT0(self):
		"""Get register SYNT0"""
		return self.read(REG.SYNT0, 8)
	
	# Bits SYNT0
	# Register IF_OFFSET_ANA
	# Intermediate frequency setting for the analog RF synthesizer, default: 300 kHz (see Equation 11). 
	
	def setIF_OFFSET_ANA(self, val):
		"""Set register IF_OFFSET_ANA"""
		self.write(REG.IF_OFFSET_ANA, val, 8)
	
	def getIF_OFFSET_ANA(self):
		"""Get register IF_OFFSET_ANA"""
		return self.read(REG.IF_OFFSET_ANA, 8)
	
	# Bits IF_OFFSET_ANA
	# Register IF_OFFSET_DIG
	
	
	def setIF_OFFSET_DIG(self, val):
		"""Set register IF_OFFSET_DIG"""
		self.write(REG.IF_OFFSET_DIG, val, 8)
	
	def getIF_OFFSET_DIG(self):
		"""Get register IF_OFFSET_DIG"""
		return self.read(REG.IF_OFFSET_DIG, 8)
	
	# Bits IF_OFFSET_DIG
	# Intermediate frequency setting for the digital shift-to-baseband circuits, default: 300 kHz (see Equation 11). 
	# Register CHSPACE
	
	
	def setCHSPACE(self, val):
		"""Set register CHSPACE"""
		self.write(REG.CHSPACE, val, 8)
	
	def getCHSPACE(self):
		"""Get register CHSPACE"""
		return self.read(REG.CHSPACE, 8)
	
	# Bits CH_SPACE
	# Channel spacing setting (see Equation 3). 
	# Register CHNUM
	
	
	def setCHNUM(self, val):
		"""Set register CHNUM"""
		self.write(REG.CHNUM, val, 8)
	
	def getCHNUM(self):
		"""Get register CHNUM"""
		return self.read(REG.CHNUM, 8)
	
	# Bits CH_NUM
	# Channel number. This value is multiplied by the channel spacing and added to the synthesizer base
	#           frequency to generate the actual RF carrier frequency (see Equation 3). 
	
	# Register MOD4
	
	
	def setMOD4(self, val):
		"""Set register MOD4"""
		self.write(REG.MOD4, val, 8)
	
	def getMOD4(self):
		"""Get register MOD4"""
		return self.read(REG.MOD4, 8)
	
	# Bits DATARATE_M
	# The MSB of the mantissa value of the data rate equation (see Equation 10). 
	# Register MOD3
	
	
	def setMOD3(self, val):
		"""Set register MOD3"""
		self.write(REG.MOD3, val, 8)
	
	def getMOD3(self):
		"""Get register MOD3"""
		return self.read(REG.MOD3, 8)
	
	# Bits DATARATE_M
	# The LSB of the mantissa value of the data rate equation (see Equation 10). 
	# Register MOD2
	
	
	def setMOD2(self, val):
		"""Set register MOD2"""
		self.write(REG.MOD2, val, 8)
	
	def getMOD2(self):
		"""Get register MOD2"""
		return self.read(REG.MOD2, 8)
	
	# Bits MOD_TYPE
	# Modulation type: 
	# Bits DATARATE_E
	# The exponent value of the data rate equation (see Equation 10). 
	# Register MOD1
	
	
	def setMOD1(self, val):
		"""Set register MOD1"""
		self.write(REG.MOD1, val, 8)
	
	def getMOD1(self):
		"""Get register MOD1"""
		return self.read(REG.MOD1, 8)
	
	# Bits PA_INTERP_EN
	# 1: enable the PA power interpolator (see Section 5.6.1). 
	# Bits MOD_INTERP_EN
	# 1: enable frequency interpolator for the GFSK shaping (see Section 5.4.1.1). 
	# Bits CONST_MAP
	# Select the constellation map for 4-(G)FSK or 2-(G)FSK modulations (see Table 38 and Table 39). 
	# Bits FDEV_E
	# The exponent value of the frequency deviation equation (see Equation 7). 
	# Register MOD0
	
	
	def setMOD0(self, val):
		"""Set register MOD0"""
		self.write(REG.MOD0, val, 8)
	
	def getMOD0(self):
		"""Get register MOD0"""
		return self.read(REG.MOD0, 8)
	
	# Bits FDEV_M
	# The mantissa value of the frequency deviation equation (see Equation 7). 
	# Register CHFLT
	
	
	def setCHFLT(self, val):
		"""Set register CHFLT"""
		self.write(REG.CHFLT, val, 8)
	
	def getCHFLT(self):
		"""Get register CHFLT"""
		return self.read(REG.CHFLT, 8)
	
	# Bits CHFLT_M
	# The mantissa value of the receiver channel filter (see Table 41). 
	# Bits CHFLT_E
	# The exponent value of the receiver channel filter (see Table 41). 
	# Register AFC2
	
	
	def setAFC2(self, val):
		"""Set register AFC2"""
		self.write(REG.AFC2, val, 8)
	
	def getAFC2(self):
		"""Get register AFC2"""
		return self.read(REG.AFC2, 8)
	
	# Bits AFC_FREEZE_ON_SYNC
	# Bits AFC_ENABLED
	# Bits AFC_MODE
	# Select AFC mode: 
	# Bits reserved_0
	# Register AFC1
	
	
	def setAFC1(self, val):
		"""Set register AFC1"""
		self.write(REG.AFC1, val, 8)
	
	def getAFC1(self):
		"""Get register AFC1"""
		return self.read(REG.AFC1, 8)
	
	# Bits AFC_FAST_PERIOD
	# The length of the AFC fast period. 
	# Register AFC0
	
	
	def setAFC0(self, val):
		"""Set register AFC0"""
		self.write(REG.AFC0, val, 8)
	
	def getAFC0(self):
		"""Get register AFC0"""
		return self.read(REG.AFC0, 8)
	
	# Bits AFC_FAST_GAIN
	# The AFC loop gain in fast mode (2's log). 
	# Bits AFC_SLOW_GAIN
	# The AFC loop gain in slow mode (2's log). 
	# Register RSSI_FLT
	
	
	def setRSSI_FLT(self, val):
		"""Set register RSSI_FLT"""
		self.write(REG.RSSI_FLT, val, 8)
	
	def getRSSI_FLT(self):
		"""Get register RSSI_FLT"""
		return self.read(REG.RSSI_FLT, 8)
	
	# Bits RSSI_FLT
	# Gain of the RSSI filter. 
	# Bits CS_MODE
	# Carrier sense mode (see Section 5.5.8.2): 
	# Bits reserved_0
	# Register RSSI_TH
	
	
	def setRSSI_TH(self, val):
		"""Set register RSSI_TH"""
		self.write(REG.RSSI_TH, val, 8)
	
	def getRSSI_TH(self):
		"""Get register RSSI_TH"""
		return self.read(REG.RSSI_TH, 8)
	
	# Bits RSSI_TH
	# Signal detect threshold in 1 dB steps. The RSSI_TH can be converted in dBm using the 
	#           formula RSSI_TH-146. 
	
	# Register AGCCTRL4
	
	
	def setAGCCTRL4(self, val):
		"""Set register AGCCTRL4"""
		self.write(REG.AGCCTRL4, val, 8)
	
	def getAGCCTRL4(self):
		"""Get register AGCCTRL4"""
		return self.read(REG.AGCCTRL4, 8)
	
	# Bits LOW_THRESHOLD_0
	# Low threshold 0 for the AGC 
	# Bits LOW_THRESHOLD_1
	# Low threshold 0 for the AGC 
	# Register AGCCTRL3
	
	
	def setAGCCTRL3(self, val):
		"""Set register AGCCTRL3"""
		self.write(REG.AGCCTRL3, val, 8)
	
	def getAGCCTRL3(self):
		"""Get register AGCCTRL3"""
		return self.read(REG.AGCCTRL3, 8)
	
	# Bits LOW_THRESHOLD_SEL
	# Low threshold selection (defined in the AGCCTRL4). Bitmask for each attenuation step. 
	# Register AGCCTRL2
	
	
	def setAGCCTRL2(self, val):
		"""Set register AGCCTRL2"""
		self.write(REG.AGCCTRL2, val, 8)
	
	def getAGCCTRL2(self):
		"""Get register AGCCTRL2"""
		return self.read(REG.AGCCTRL2, 8)
	
	# Bits reserved_0
	# Bits FREEZE_ON_SYNC
	# Enable the AGC algorithm to be frozen on SYNC 
	# Bits reserved_1
	# Bits MEAS_TIME
	# AGC measurement time 
	# Register AGCCTRL1
	
	
	def setAGCCTRL1(self, val):
		"""Set register AGCCTRL1"""
		self.write(REG.AGCCTRL1, val, 8)
	
	def getAGCCTRL1(self):
		"""Get register AGCCTRL1"""
		return self.read(REG.AGCCTRL1, 8)
	
	# Bits HIGH_THRESHOLD
	# High threshold for the AGC 
	# Bits reserved_0
	# Register AGCCTRL0
	
	
	def setAGCCTRL0(self, val):
		"""Set register AGCCTRL0"""
		self.write(REG.AGCCTRL0, val, 8)
	
	def getAGCCTRL0(self):
		"""Get register AGCCTRL0"""
		return self.read(REG.AGCCTRL0, 8)
	
	# Bits AGC_ENABLE
	# Bits reserved_0
	# Bits HOLD_TIME
	# Hold time for after gain adjustment for the AGC. 
	# Register ANT_SELECT_CONF
	
	
	def setANT_SELECT_CONF(self, val):
		"""Set register ANT_SELECT_CONF"""
		self.write(REG.ANT_SELECT_CONF, val, 8)
	
	def getANT_SELECT_CONF(self):
		"""Get register ANT_SELECT_CONF"""
		return self.read(REG.ANT_SELECT_CONF, 8)
	
	# Bits reserved_0
	# Bits EQU_CTRL
	# ISI cancellation equalizer (see Section 5.4.1.2): 
	# Bits CS_BLANKING
	# Do not fill the RX FIFO with data if the CS is above threshold (see Section 5.5.9). 
	# Bits AS_ENABLE
	# 1: enable the antenna switching (see Section 5.5.10). 
	# Bits AS_MEAS_TIME
	# Set the measurement time. 
	# Register CLOCKREC2
	
	
	def setCLOCKREC2(self, val):
		"""Set register CLOCKREC2"""
		self.write(REG.CLOCKREC2, val, 8)
	
	def getCLOCKREC2(self):
		"""Get register CLOCKREC2"""
		return self.read(REG.CLOCKREC2, 8)
	
	# Bits CLK_REC_P_GAIN_SLOW
	# Clock recovery slow loop gain (log2). 
	# Bits CLK_REC_ALGO_SEL
	# Select the symbol timing recovery algorithm: 
	# Bits CLK_REC_I_GAIN_SLOW
	# Set the integral slow gain for symbol timing recovery (PLL mode only). 
	# Register CLOCKREC1
	
	
	def setCLOCKREC1(self, val):
		"""Set register CLOCKREC1"""
		self.write(REG.CLOCKREC1, val, 8)
	
	def getCLOCKREC1(self):
		"""Get register CLOCKREC1"""
		return self.read(REG.CLOCKREC1, 8)
	
	# Bits CLK_REC_P_GAIN_FAST
	# Clock recovery fast loop gain (log2). 
	# Bits PSTFLT_LEN
	# Select the post filter length: 
	# Bits CLK_REC_I_GAIN_FAST
	# Set the integral fast gain for symbol timing recovery (PLL mode only). 
	# Register PCKTCTRL6
	
	
	def setPCKTCTRL6(self, val):
		"""Set register PCKTCTRL6"""
		self.write(REG.PCKTCTRL6, val, 8)
	
	def getPCKTCTRL6(self):
		"""Get register PCKTCTRL6"""
		return self.read(REG.PCKTCTRL6, 8)
	
	# Bits SYNC_LEN
	# The number of bits used for the SYNC field in the packet. 
	# Bits PREAMBLE_LEN
	# The MSB of the number of '01 or '10' of the preamble of the packet. 
	# Register PCKTCTRL5
	
	
	def setPCKTCTRL5(self, val):
		"""Set register PCKTCTRL5"""
		self.write(REG.PCKTCTRL5, val, 8)
	
	def getPCKTCTRL5(self):
		"""Get register PCKTCTRL5"""
		return self.read(REG.PCKTCTRL5, 8)
	
	# Bits PREAMBLE_LEN
	# The LSB of the number of '01 or '10' of the preamble of the packet. 
	# Register PCKTCTRL4
	
	
	def setPCKTCTRL4(self, val):
		"""Set register PCKTCTRL4"""
		self.write(REG.PCKTCTRL4, val, 8)
	
	def getPCKTCTRL4(self):
		"""Get register PCKTCTRL4"""
		return self.read(REG.PCKTCTRL4, 8)
	
	# Bits LEN_WID
	# The number of bytes used for the length field: 
	#         - 0: 1 byte
	#         - 1: 2 bytes. 
	
	# Bits reserved_0
	# Bits ADDRESS_LEN
	# 1: include the ADDRESS field in the packet. 
	# Bits reserved_1
	# Register PCKTCTRL3
	
	
	def setPCKTCTRL3(self, val):
		"""Set register PCKTCTRL3"""
		self.write(REG.PCKTCTRL3, val, 8)
	
	def getPCKTCTRL3(self):
		"""Get register PCKTCTRL3"""
		return self.read(REG.PCKTCTRL3, 8)
	
	# Bits PCKT_FRMT
	# Format of packet: 
	#         - 0: Basic
	#         - 1: 802.15.4g
	#         - 2: UART OTA
	#         - 3: Stack
	#         (see section 6 ) 
	
	# Bits RX_MODE
	# RX mode: 
	#         - 0: normal mode
	#         - 1: direct through FIFO
	#         - 2: direct through GPIO 
	
	# Bits FSK4_SYM_SWAP
	# Select the symbol mapping for 4(G)FSK. 
	# Bits BYTE_SWAP
	# Select the transmission order between MSB and LSB. 
	# Bits PREAMBLE_SEL
	# Select the preamble pattern. 
	# Register PCKTCTRL2
	
	
	def setPCKTCTRL2(self, val):
		"""Set register PCKTCTRL2"""
		self.write(REG.PCKTCTRL2, val, 8)
	
	def getPCKTCTRL2(self):
		"""Get register PCKTCTRL2"""
		return self.read(REG.PCKTCTRL2, 8)
	
	# Bits reserved_0
	# Bits FCS_TYPE_4G
	# This is the FCS type in header field of 802.15.4g packet. 
	# Bits FEC_TYPE_4G_STOP_BIT
	# - If the 802.15.4 mode is enabled, this is the FCS type in header field of 802.15.4g
	#             packet. Select the FEC type of 802.15.4g packet: 
	
	# Bits INT_EN_4G_START_BIT
	# - If the 802.15.4 mode is enabled, 1: enable the
	#             interleaving of 802.15.4g packet. 
	#             If the UART packet is enabled, this is the value
	#             of the START_BIT.
	
	# Bits MBUS_3OF6_EN
	# Bits MANCHESTER_EN
	# Bits FIX_VAR_LEN
	# Packet length mode: 
	# Register PCKTCTRL1
	
	
	def setPCKTCTRL1(self, val):
		"""Set register PCKTCTRL1"""
		self.write(REG.PCKTCTRL1, val, 8)
	
	def getPCKTCTRL1(self):
		"""Get register PCKTCTRL1"""
		return self.read(REG.PCKTCTRL1, 8)
	
	# Bits CRC_MODE
	# CRC field: 
	# Bits WHIT_EN
	# Bits TXSOURCE
	# Tx source data: 
	# Bits SECOND_SYNC_SEL
	# In TX mode: 
	#           1'b0 = PRIMARY    -select the primary SYNC word
	#           1'b0 = SECONDARY  -select the secondary SYNC word.
	#           In RX mode, if 1 enable the dual SYNC word detection mode. 
	
	# Bits FEC_EN
	# Register PCKTLEN1
	
	
	def setPCKTLEN1(self, val):
		"""Set register PCKTLEN1"""
		self.write(REG.PCKTLEN1, val, 8)
	
	def getPCKTLEN1(self):
		"""Get register PCKTLEN1"""
		return self.read(REG.PCKTLEN1, 8)
	
	# Bits PCKTLEN1
	# MSB of length of packet in bytes. 
	# Register PCKTLEN0
	
	
	def setPCKTLEN0(self, val):
		"""Set register PCKTLEN0"""
		self.write(REG.PCKTLEN0, val, 8)
	
	def getPCKTLEN0(self):
		"""Get register PCKTLEN0"""
		return self.read(REG.PCKTLEN0, 8)
	
	# Bits PCKTLEN0
	# LSB of length of packet in bytes. 
	# Register SYNC3
	
	
	def setSYNC3(self, val):
		"""Set register SYNC3"""
		self.write(REG.SYNC3, val, 8)
	
	def getSYNC3(self):
		"""Get register SYNC3"""
		return self.read(REG.SYNC3, 8)
	
	# Bits SYNC3
	# SYNC word byte 3. 
	# Register SYNC2
	
	
	def setSYNC2(self, val):
		"""Set register SYNC2"""
		self.write(REG.SYNC2, val, 8)
	
	def getSYNC2(self):
		"""Get register SYNC2"""
		return self.read(REG.SYNC2, 8)
	
	# Bits SYNC2
	# SYNC word byte 2. 
	# Register SYNC1
	
	
	def setSYNC1(self, val):
		"""Set register SYNC1"""
		self.write(REG.SYNC1, val, 8)
	
	def getSYNC1(self):
		"""Get register SYNC1"""
		return self.read(REG.SYNC1, 8)
	
	# Bits SYNC1
	# SYNC word byte 1. 
	# Register SYNC0
	
	
	def setSYNC0(self, val):
		"""Set register SYNC0"""
		self.write(REG.SYNC0, val, 8)
	
	def getSYNC0(self):
		"""Get register SYNC0"""
		return self.read(REG.SYNC0, 8)
	
	# Bits SYNC0
	# SYNC word byte 0. 
	# Register QI
	
	
	def setQI(self, val):
		"""Set register QI"""
		self.write(REG.QI, val, 8)
	
	def getQI(self):
		"""Get register QI"""
		return self.read(REG.QI, 8)
	
	# Bits SQI_TH
	# SQI threshold. 
	# Bits PQI_TH
	# PQI threshold. 
	# Bits SQI_EN
	# Register PCKT_PSTMBL
	
	
	def setPCKT_PSTMBL(self, val):
		"""Set register PCKT_PSTMBL"""
		self.write(REG.PCKT_PSTMBL, val, 8)
	
	def getPCKT_PSTMBL(self):
		"""Get register PCKT_PSTMBL"""
		return self.read(REG.PCKT_PSTMBL, 8)
	
	# Bits PCKT_PSTMBL
	# Set the packet postamble length. 
	# Register PROTOCOL2
	
	
	def setPROTOCOL2(self, val):
		"""Set register PROTOCOL2"""
		self.write(REG.PROTOCOL2, val, 8)
	
	def getPROTOCOL2(self):
		"""Get register PROTOCOL2"""
		return self.read(REG.PROTOCOL2, 8)
	
	# Bits CS_TIMEOUT_MASK
	# Bits SQI_TIMEOUT_MASK
	# Bits PQI_TIMEOUT_MASK
	# Bits TX_SEQ_NUM_RELOAD
	# TX sequence number to be used when counting reset is required using the related command. 
	# Bits FIFO_GPIO_OUT_MUX_SEL
	# Bits LDC_TIMER_MULT
	# Set the LDC timer multiplier factor: 
	# Register PROTOCOL1
	
	
	def setPROTOCOL1(self, val):
		"""Set register PROTOCOL1"""
		self.write(REG.PROTOCOL1, val, 8)
	
	def getPROTOCOL1(self):
		"""Get register PROTOCOL1"""
		return self.read(REG.PROTOCOL1, 8)
	
	# Bits LDC_MODE
	# Bits LDC_RELOAD_ON_SYNC
	# Bits PIGGYBACKING
	# Bits FAST_CS_TERM_EN
	# Bits SEED_RELOAD
	# Bits CSMA_ON
	# Bits CSMA_PERS_ON
	# Bits AUTO_PCKT_FLT
	# Register PROTOCOL0
	
	
	def setPROTOCOL0(self, val):
		"""Set register PROTOCOL0"""
		self.write(REG.PROTOCOL0, val, 8)
	
	def getPROTOCOL0(self):
		"""Get register PROTOCOL0"""
		return self.read(REG.PROTOCOL0, 8)
	
	# Bits NMAX_RETX
	# Max. number of re-TX (from 0 to 15)(0: re-transmission is not performed). 
	# Bits NACK_TX
	# 1: field NO_ACK=1 on transmitted packet. 
	# Bits AUTO_ACK
	# Bits PERS_RX
	# Bits reserved_0
	# Register FIFO_CONFIG3
	
	
	def setFIFO_CONFIG3(self, val):
		"""Set register FIFO_CONFIG3"""
		self.write(REG.FIFO_CONFIG3, val, 8)
	
	def getFIFO_CONFIG3(self):
		"""Get register FIFO_CONFIG3"""
		return self.read(REG.FIFO_CONFIG3, 8)
	
	# Bits reserved_0
	# Bits RX_AFTHR
	# Set the RX FIFO almost full threshold. 
	# Register FIFO_CONFIG2
	
	
	def setFIFO_CONFIG2(self, val):
		"""Set register FIFO_CONFIG2"""
		self.write(REG.FIFO_CONFIG2, val, 8)
	
	def getFIFO_CONFIG2(self):
		"""Get register FIFO_CONFIG2"""
		return self.read(REG.FIFO_CONFIG2, 8)
	
	# Bits reserved_0
	# Bits RX_AETHR
	# Set the RX FIFO almost empty threshold. 
	# Register FIFO_CONFIG1
	
	
	def setFIFO_CONFIG1(self, val):
		"""Set register FIFO_CONFIG1"""
		self.write(REG.FIFO_CONFIG1, val, 8)
	
	def getFIFO_CONFIG1(self):
		"""Get register FIFO_CONFIG1"""
		return self.read(REG.FIFO_CONFIG1, 8)
	
	# Bits reserved_0
	# Bits TX_AFTHR
	# Set the TX FIFO almost full threshold. 
	# Register FIFO_CONFIG0
	
	
	def setFIFO_CONFIG0(self, val):
		"""Set register FIFO_CONFIG0"""
		self.write(REG.FIFO_CONFIG0, val, 8)
	
	def getFIFO_CONFIG0(self):
		"""Get register FIFO_CONFIG0"""
		return self.read(REG.FIFO_CONFIG0, 8)
	
	# Bits reserved_0
	# Bits TX_AETHR
	# Set the TX FIFO almost empty threshold. 
	# Register PCKT_FLT_OPTIONS
	
	
	def setPCKT_FLT_OPTIONS(self, val):
		"""Set register PCKT_FLT_OPTIONS"""
		self.write(REG.PCKT_FLT_OPTIONS, val, 8)
	
	def getPCKT_FLT_OPTIONS(self):
		"""Get register PCKT_FLT_OPTIONS"""
		return self.read(REG.PCKT_FLT_OPTIONS, 8)
	
	# Bits reserved_0
	# Bits RX_TIMEOUT_AND_OR_SEL
	# Logical Boolean function applied to CS/SQI/PQI values: 1: OR, 0: AND. 
	# Bits reserved_1
	# Bits SOURCE_ADDR_FLT
	# 1: RX packet accepted if its source field matches with RX_SOURCE_ADDR register 
	# Bits DEST_VS_BROADCAST_ADDR
	# 1: RX packet accepted if its source field matches with BROADCAST_ADDR register. 
	# Bits DEST_VS_MULTICAST_ADDR
	# 1: RX packet accepted if its destination address matches with MULTICAST_ADDR register. 
	# Bits DEST_VS_SOURCE_ADDR
	# 1: RX packet accepted if its destination address matches with RX_SOURCE_ADDR register. 
	# Bits CRC_FLT
	# 1: packet discarded if CRC is not valid. 
	# Register PCKT_FLT_GOALS4
	
	
	def setPCKT_FLT_GOALS4(self, val):
		"""Set register PCKT_FLT_GOALS4"""
		self.write(REG.PCKT_FLT_GOALS4, val, 8)
	
	def getPCKT_FLT_GOALS4(self):
		"""Get register PCKT_FLT_GOALS4"""
		return self.read(REG.PCKT_FLT_GOALS4, 8)
	
	# Bits RX_SOURCE_MASK
	# Mask register for source address filtering. 
	# Register PCKT_FLT_GOALS3
	
	
	def setPCKT_FLT_GOALS3(self, val):
		"""Set register PCKT_FLT_GOALS3"""
		self.write(REG.PCKT_FLT_GOALS3, val, 8)
	
	def getPCKT_FLT_GOALS3(self):
		"""Get register PCKT_FLT_GOALS3"""
		return self.read(REG.PCKT_FLT_GOALS3, 8)
	
	# Bits RX_SOURCE_ADDR_DUAL_SYNC3
	# If dual sync mode enabled: dual SYNC word byte 3, Otherwise RX packet source or TX packet destination field. 
	# Register PCKT_FLT_GOALS2
	
	
	def setPCKT_FLT_GOALS2(self, val):
		"""Set register PCKT_FLT_GOALS2"""
		self.write(REG.PCKT_FLT_GOALS2, val, 8)
	
	def getPCKT_FLT_GOALS2(self):
		"""Get register PCKT_FLT_GOALS2"""
		return self.read(REG.PCKT_FLT_GOALS2, 8)
	
	# Bits BROADCAST_ADDR_DUAL_SYNC2
	# If dual sync mode enabled: dual SYNC word byte 2, Broadcast address. 
	# Register PCKT_FLT_GOALS1
	
	
	def setPCKT_FLT_GOALS1(self, val):
		"""Set register PCKT_FLT_GOALS1"""
		self.write(REG.PCKT_FLT_GOALS1, val, 8)
	
	def getPCKT_FLT_GOALS1(self):
		"""Get register PCKT_FLT_GOALS1"""
		return self.read(REG.PCKT_FLT_GOALS1, 8)
	
	# Bits MULTICAST_ADDR_DUAL_SYNC1
	# If dual sync mode enabled: dual SYNC word byte 1, Multicast address. 
	# Register PCKT_FLT_GOALS0
	
	
	def setPCKT_FLT_GOALS0(self, val):
		"""Set register PCKT_FLT_GOALS0"""
		self.write(REG.PCKT_FLT_GOALS0, val, 8)
	
	def getPCKT_FLT_GOALS0(self):
		"""Get register PCKT_FLT_GOALS0"""
		return self.read(REG.PCKT_FLT_GOALS0, 8)
	
	# Bits TX_SOURCE_ADDR_DUAL_SYNC0
	# If dual sync mode enabled: dual SYNC word byte 0, Tx packet source or RX packet destination field. 
	# Register TIMERS5
	
	
	def setTIMERS5(self, val):
		"""Set register TIMERS5"""
		self.write(REG.TIMERS5, val, 8)
	
	def getTIMERS5(self):
		"""Get register TIMERS5"""
		return self.read(REG.TIMERS5, 8)
	
	# Bits RX_TIMER_CNTR
	# Counter for RX timer. 
	# Register TIMERS4
	
	
	def setTIMERS4(self, val):
		"""Set register TIMERS4"""
		self.write(REG.TIMERS4, val, 8)
	
	def getTIMERS4(self):
		"""Get register TIMERS4"""
		return self.read(REG.TIMERS4, 8)
	
	# Bits RX_TIMER_PRESC
	# Prescaler for RX timer. 
	# Register TIMERS3
	
	
	def setTIMERS3(self, val):
		"""Set register TIMERS3"""
		self.write(REG.TIMERS3, val, 8)
	
	def getTIMERS3(self):
		"""Get register TIMERS3"""
		return self.read(REG.TIMERS3, 8)
	
	# Bits LDC_TIMER_PRESC
	# Prescaler for wake up timer. 
	# Register TIMERS2
	
	
	def setTIMERS2(self, val):
		"""Set register TIMERS2"""
		self.write(REG.TIMERS2, val, 8)
	
	def getTIMERS2(self):
		"""Get register TIMERS2"""
		return self.read(REG.TIMERS2, 8)
	
	# Bits LDC_TIMER_CNTR
	# Counter for wake up timer. 
	# Register TIMERS1
	
	
	def setTIMERS1(self, val):
		"""Set register TIMERS1"""
		self.write(REG.TIMERS1, val, 8)
	
	def getTIMERS1(self):
		"""Get register TIMERS1"""
		return self.read(REG.TIMERS1, 8)
	
	# Bits LDC_RELOAD_PRSC
	# Prescaler value for reload operation of wake up timer. 
	# Register TIMERS0
	
	
	def setTIMERS0(self, val):
		"""Set register TIMERS0"""
		self.write(REG.TIMERS0, val, 8)
	
	def getTIMERS0(self):
		"""Get register TIMERS0"""
		return self.read(REG.TIMERS0, 8)
	
	# Bits LDC_RELOAD_CNTR
	# Counter value for reload operation of wake up timer. 
	# Register CSMA_CONF3
	
	
	def setCSMA_CONF3(self, val):
		"""Set register CSMA_CONF3"""
		self.write(REG.CSMA_CONF3, val, 8)
	
	def getCSMA_CONF3(self):
		"""Get register CSMA_CONF3"""
		return self.read(REG.CSMA_CONF3, 8)
	
	# Bits BU_CNTR_SEED
	# MSB part of the seed for the random generator used to apply the CSMA algorithm. 
	# Register CSMA_CONF2
	
	
	def setCSMA_CONF2(self, val):
		"""Set register CSMA_CONF2"""
		self.write(REG.CSMA_CONF2, val, 8)
	
	def getCSMA_CONF2(self):
		"""Get register CSMA_CONF2"""
		return self.read(REG.CSMA_CONF2, 8)
	
	# Bits BU_CNTR_SEED
	# LSB part of the seed for the random generator used to apply the CSMA algorithm. 
	# Register CSMA_CONF1
	
	
	def setCSMA_CONF1(self, val):
		"""Set register CSMA_CONF1"""
		self.write(REG.CSMA_CONF1, val, 8)
	
	def getCSMA_CONF1(self):
		"""Get register CSMA_CONF1"""
		return self.read(REG.CSMA_CONF1, 8)
	
	# Bits BU_PRSC
	# Prescaler value for the back-off unit BU. 
	# Bits CCA_PERIOD
	# Multiplier for the Tcca timer. 
	# Register CSMA_CONF0
	
	
	def setCSMA_CONF0(self, val):
		"""Set register CSMA_CONF0"""
		self.write(REG.CSMA_CONF0, val, 8)
	
	def getCSMA_CONF0(self):
		"""Get register CSMA_CONF0"""
		return self.read(REG.CSMA_CONF0, 8)
	
	# Bits CCA_LEN
	# The number of time in which the listen operation is performed. 
	# Bits reserved_0
	# Bits NBACKOFF_MAX
	# Max number of back-off cycles. 
	# Register IRQ_MASK3
	
	
	def setIRQ_MASK3(self, val):
		"""Set register IRQ_MASK3"""
		self.write(REG.IRQ_MASK3, val, 8)
	
	def getIRQ_MASK3(self):
		"""Get register IRQ_MASK3"""
		return self.read(REG.IRQ_MASK3, 8)
	
	# Bits INT_MASK
	# Enable the routing of the interrupt flag on the configured IRQ GPIO. 
	# Register IRQ_MASK2
	
	
	def setIRQ_MASK2(self, val):
		"""Set register IRQ_MASK2"""
		self.write(REG.IRQ_MASK2, val, 8)
	
	def getIRQ_MASK2(self):
		"""Get register IRQ_MASK2"""
		return self.read(REG.IRQ_MASK2, 8)
	
	# Bits INT_MASK
	# Enable the routing of the interrupt flag on the configured IRQ GPIO. 
	# Register IRQ_MASK1
	
	
	def setIRQ_MASK1(self, val):
		"""Set register IRQ_MASK1"""
		self.write(REG.IRQ_MASK1, val, 8)
	
	def getIRQ_MASK1(self):
		"""Get register IRQ_MASK1"""
		return self.read(REG.IRQ_MASK1, 8)
	
	# Bits INT_MASK
	# Enable the routing of the interrupt flag on the configured IRQ GPIO. 
	# Register IRQ_MASK0
	
	
	def setIRQ_MASK0(self, val):
		"""Set register IRQ_MASK0"""
		self.write(REG.IRQ_MASK0, val, 8)
	
	def getIRQ_MASK0(self):
		"""Get register IRQ_MASK0"""
		return self.read(REG.IRQ_MASK0, 8)
	
	# Bits INT_MASK
	# Enable the routing of the interrupt flag on the configured IRQ GPIO. 
	# Register FAST_RX_TIMER
	
	
	def setFAST_RX_TIMER(self, val):
		"""Set register FAST_RX_TIMER"""
		self.write(REG.FAST_RX_TIMER, val, 8)
	
	def getFAST_RX_TIMER(self):
		"""Get register FAST_RX_TIMER"""
		return self.read(REG.FAST_RX_TIMER, 8)
	
	# Bits RSSI_SETTLING_LIMIT
	# Sniff timer configuration. 
	# Register PA_POWER8
	
	
	def setPA_POWER8(self, val):
		"""Set register PA_POWER8"""
		self.write(REG.PA_POWER8, val, 8)
	
	def getPA_POWER8(self):
		"""Get register PA_POWER8"""
		return self.read(REG.PA_POWER8, 8)
	
	# Bits reserved_0
	# Bits PA_LEVEL8
	# Output power level for 8th slot. 
	# Register PA_POWER7
	
	
	def setPA_POWER7(self, val):
		"""Set register PA_POWER7"""
		self.write(REG.PA_POWER7, val, 8)
	
	def getPA_POWER7(self):
		"""Get register PA_POWER7"""
		return self.read(REG.PA_POWER7, 8)
	
	# Bits reserved_0
	# Bits PA_LEVEL_7
	# Output power level for 7th slot. 
	# Register PA_POWER6
	
	
	def setPA_POWER6(self, val):
		"""Set register PA_POWER6"""
		self.write(REG.PA_POWER6, val, 8)
	
	def getPA_POWER6(self):
		"""Get register PA_POWER6"""
		return self.read(REG.PA_POWER6, 8)
	
	# Bits reserved_0
	# Bits PA_LEVEL_6
	# Output power level for 6th slot. 
	# Register PA_POWER5
	
	
	def setPA_POWER5(self, val):
		"""Set register PA_POWER5"""
		self.write(REG.PA_POWER5, val, 8)
	
	def getPA_POWER5(self):
		"""Get register PA_POWER5"""
		return self.read(REG.PA_POWER5, 8)
	
	# Bits reserved_0
	# Bits PA_LEVEL_5
	# Output power level for 5th slot. 
	# Register PA_POWER4
	
	
	def setPA_POWER4(self, val):
		"""Set register PA_POWER4"""
		self.write(REG.PA_POWER4, val, 8)
	
	def getPA_POWER4(self):
		"""Get register PA_POWER4"""
		return self.read(REG.PA_POWER4, 8)
	
	# Bits reserved_0
	# Bits PA_LEVEL_4
	# Output power level for 4th slot. 
	# Register PA_POWER3
	
	
	def setPA_POWER3(self, val):
		"""Set register PA_POWER3"""
		self.write(REG.PA_POWER3, val, 8)
	
	def getPA_POWER3(self):
		"""Get register PA_POWER3"""
		return self.read(REG.PA_POWER3, 8)
	
	# Bits reserved_0
	# Bits PA_LEVEL_3
	# Output power level for 3rd slot. 
	# Register PA_POWER2
	
	
	def setPA_POWER2(self, val):
		"""Set register PA_POWER2"""
		self.write(REG.PA_POWER2, val, 8)
	
	def getPA_POWER2(self):
		"""Get register PA_POWER2"""
		return self.read(REG.PA_POWER2, 8)
	
	# Bits reserved_0
	# Bits PA_LEVEL_2
	# Output power level for 2nd slot. 
	# Register PA_POWER1
	
	
	def setPA_POWER1(self, val):
		"""Set register PA_POWER1"""
		self.write(REG.PA_POWER1, val, 8)
	
	def getPA_POWER1(self):
		"""Get register PA_POWER1"""
		return self.read(REG.PA_POWER1, 8)
	
	# Bits reserved_0
	# Bits PA_LEVEL_1
	# Output power level for 1st slot. 
	# Register PA_POWER0
	
	
	def setPA_POWER0(self, val):
		"""Set register PA_POWER0"""
		self.write(REG.PA_POWER0, val, 8)
	
	def getPA_POWER0(self):
		"""Get register PA_POWER0"""
		return self.read(REG.PA_POWER0, 8)
	
	# Bits DIG_SMOOTH_EN
	# Bits PA_MAXDBM
	# Bits PA_RAMP_EN
	# Bits PA_RAMP_STEP_LEN
	# Set the step width (unit: 1/8 of bit period). 
	# Bits PA_LEVEL_MAX_IDX
	# Final level for power ramping or selected output power index. 
	# Register PA_CONFIG1
	
	
	def setPA_CONFIG1(self, val):
		"""Set register PA_CONFIG1"""
		self.write(REG.PA_CONFIG1, val, 8)
	
	def getPA_CONFIG1(self):
		"""Get register PA_CONFIG1"""
		return self.read(REG.PA_CONFIG1, 8)
	
	# Bits reserved_0
	# Bits FIR_CFG
	# FIR configuration: 
	# Bits FIR_EN
	# Bits reserved_1
	# Register PA_CONFIG0
	
	
	def setPA_CONFIG0(self, val):
		"""Set register PA_CONFIG0"""
		self.write(REG.PA_CONFIG0, val, 8)
	
	def getPA_CONFIG0(self):
		"""Get register PA_CONFIG0"""
		return self.read(REG.PA_CONFIG0, 8)
	
	# Bits reserved_0
	# Bits PA_FC
	# PA Bessel filter bandwidth: 
	# Register SYNTH_CONFIG2
	
	
	def setSYNTH_CONFIG2(self, val):
		"""Set register SYNTH_CONFIG2"""
		self.write(REG.SYNTH_CONFIG2, val, 8)
	
	def getSYNTH_CONFIG2(self):
		"""Get register SYNTH_CONFIG2"""
		return self.read(REG.SYNTH_CONFIG2, 8)
	
	# Bits reserved_0
	# Bits PLL_PFD_SPLIT_EN
	# Enables increased DN current pulses to improve linearization of CP/PFD (see Table 34). 
	# Bits reserved_1
	# Register VCO_CONFIG
	
	
	def setVCO_CONFIG(self, val):
		"""Set register VCO_CONFIG"""
		self.write(REG.VCO_CONFIG, val, 8)
	
	def getVCO_CONFIG(self):
		"""Get register VCO_CONFIG"""
		return self.read(REG.VCO_CONFIG, 8)
	
	# Bits reserved_0
	# Bits VCO_CALAMP_EXT_SEL
	# Bits VCO_CALFREQ_EXT_SEL
	# Bits reserved_1
	# Register VCO_CALIBR_IN2
	
	
	def setVCO_CALIBR_IN2(self, val):
		"""Set register VCO_CALIBR_IN2"""
		self.write(REG.VCO_CALIBR_IN2, val, 8)
	
	def getVCO_CALIBR_IN2(self):
		"""Get register VCO_CALIBR_IN2"""
		return self.read(REG.VCO_CALIBR_IN2, 8)
	
	# Bits VCO_CALAMP_TX
	# VCO magnitude calibration word (binary coding to be internally converted in thermometric code) used in TX. 
	# Bits VCO_CALAMP_RX
	# VCO magnitude calibration word (binary coding to be internally converted in thermometric code) used in RX. 
	# Register VCO_CALIBR_IN1
	
	
	def setVCO_CALIBR_IN1(self, val):
		"""Set register VCO_CALIBR_IN1"""
		self.write(REG.VCO_CALIBR_IN1, val, 8)
	
	def getVCO_CALIBR_IN1(self):
		"""Get register VCO_CALIBR_IN1"""
		return self.read(REG.VCO_CALIBR_IN1, 8)
	
	# Bits reserved_0
	# Bits VCO_CALFREQ_TX
	# VCO Cbank frequency calibration word to be used in TX. 
	# Register VCO_CALIBR_IN0
	
	
	def setVCO_CALIBR_IN0(self, val):
		"""Set register VCO_CALIBR_IN0"""
		self.write(REG.VCO_CALIBR_IN0, val, 8)
	
	def getVCO_CALIBR_IN0(self):
		"""Get register VCO_CALIBR_IN0"""
		return self.read(REG.VCO_CALIBR_IN0, 8)
	
	# Bits reserved_0
	# Bits VCO_CALFREQ_RX
	# VCO Cbank frequency calibration word to be used in RX. 
	# Register XO_RCO_CONF1
	
	
	def setXO_RCO_CONF1(self, val):
		"""Set register XO_RCO_CONF1"""
		self.write(REG.XO_RCO_CONF1, val, 8)
	
	def getXO_RCO_CONF1(self):
		"""Get register XO_RCO_CONF1"""
		return self.read(REG.XO_RCO_CONF1, 8)
	
	# Bits reserved_0
	# Bits PD_CLKDIV
	# Bits reserved_1
	# Register XO_RCO_CONF0
	
	
	def setXO_RCO_CONF0(self, val):
		"""Set register XO_RCO_CONF0"""
		self.write(REG.XO_RCO_CONF0, val, 8)
	
	def getXO_RCO_CONF0(self):
		"""Get register XO_RCO_CONF0"""
		return self.read(REG.XO_RCO_CONF0, 8)
	
	# Bits EXT_REF
	# Bits GM_CONF
	# Set the driver gm of the XO at start up. 
	# Bits REFDIV
	# Bits reserved_0
	# Bits EXT_RCO_OSC
	# 1: the 34.7 kHz signal must be supplied from any GPIO. 
	# Bits RCO_CALIBRATION
	# Register RCO_CALIBR_CONF3
	
	
	def setRCO_CALIBR_CONF3(self, val):
		"""Set register RCO_CALIBR_CONF3"""
		self.write(REG.RCO_CALIBR_CONF3, val, 8)
	
	def getRCO_CALIBR_CONF3(self):
		"""Get register RCO_CALIBR_CONF3"""
		return self.read(REG.RCO_CALIBR_CONF3, 8)
	
	# Bits RWT_IN
	# RWT word value for the RCO. 
	# Bits RFB_IN
	# MSB part of RFB word value for RCO. 
	# Register RCO_CALIBR_CONF2
	
	
	def setRCO_CALIBR_CONF2(self, val):
		"""Set register RCO_CALIBR_CONF2"""
		self.write(REG.RCO_CALIBR_CONF2, val, 8)
	
	def getRCO_CALIBR_CONF2(self):
		"""Get register RCO_CALIBR_CONF2"""
		return self.read(REG.RCO_CALIBR_CONF2, 8)
	
	# Bits RFB_IN
	# LSB part of RFB word value for RCO. 
	# Bits reserved_0
	# Register PM_CONF4
	
	
	def setPM_CONF4(self, val):
		"""Set register PM_CONF4"""
		self.write(REG.PM_CONF4, val, 8)
	
	def getPM_CONF4(self):
		"""Get register PM_CONF4"""
		return self.read(REG.PM_CONF4, 8)
	
	# Bits reserved_0
	# Bits EXT_SMPS
	# Bits reserved_1
	# Register PM_CONF3
	
	
	def setPM_CONF3(self, val):
		"""Set register PM_CONF3"""
		self.write(REG.PM_CONF3, val, 8)
	
	def getPM_CONF3(self):
		"""Get register PM_CONF3"""
		return self.read(REG.PM_CONF3, 8)
	
	# Bits KRM_EN
	# Bits KRM
	# Sets the divider ratio (MSB) of the rate multiplier (default: Fsw=Fdig/4) 
	# Register PM_CONF2
	
	
	def setPM_CONF2(self, val):
		"""Set register PM_CONF2"""
		self.write(REG.PM_CONF2, val, 8)
	
	def getPM_CONF2(self):
		"""Get register PM_CONF2"""
		return self.read(REG.PM_CONF2, 8)
	
	# Bits KRM
	# Sets the divider ratio (LSB) of the rate multiplier (default: Fsw=Fdig/4) 
	# Register PM_CONF1
	
	
	def setPM_CONF1(self, val):
		"""Set register PM_CONF1"""
		self.write(REG.PM_CONF1, val, 8)
	
	def getPM_CONF1(self):
		"""Get register PM_CONF1"""
		return self.read(REG.PM_CONF1, 8)
	
	# Bits reserved_0
	# Bits BATTERY_LVL_EN
	# Bits SET_BLD_TH
	# Set the BLD threshold: 
	# Bits SMPS_LVL_MODE
	# - 0: SMPS output level will depend upon the value written in the PM_CONFIG0 register (SET_SMPS_LEVEL field) both in RX and TX state.
	#           - 1: SMPS output level will depend upon the value in PM_CONFIG register just in TX state, while in RX state it will be fixed to 1.4 V 
	
	# Bits BYPASS_LDO
	# Set to 0 (default value) 
	# Bits reserved_1
	# Register PM_CONF0
	
	
	def setPM_CONF0(self, val):
		"""Set register PM_CONF0"""
		self.write(REG.PM_CONF0, val, 8)
	
	def getPM_CONF0(self):
		"""Get register PM_CONF0"""
		return self.read(REG.PM_CONF0, 8)
	
	# Bits reserved_0
	# Bits SET_SMPS_LVL
	# SMPS output voltage: 
	# Bits reserved_1
	# Bits SLEEP_MODE_SEL
	# Register MC_STATE1
	
	
	def setMC_STATE1(self, val):
		"""Set register MC_STATE1"""
		self.write(REG.MC_STATE1, val, 8)
	
	def getMC_STATE1(self):
		"""Get register MC_STATE1"""
		return self.read(REG.MC_STATE1, 8)
	
	# Bits reserved_0
	# Bits RCO_CAL_OK
	# RCO calibration successfully terminated. 
	# Bits ANT_SEL
	# Currently selected antenna. 
	# Bits TX_FIFO_FULL
	# Bits RX_FIFO_EMPTY
	# Bits ERROR_LOCK
	# Register MC_STATE0
	
	
	def setMC_STATE0(self, val):
		"""Set register MC_STATE0"""
		self.write(REG.MC_STATE0, val, 8)
	
	def getMC_STATE0(self):
		"""Get register MC_STATE0"""
		return self.read(REG.MC_STATE0, 8)
	
	# Bits STATE
	# Current state. 
	# Bits XO_ON
	# Register TX_FIFO_STATUS
	
	
	def setTX_FIFO_STATUS(self, val):
		"""Set register TX_FIFO_STATUS"""
		self.write(REG.TX_FIFO_STATUS, val, 8)
	
	def getTX_FIFO_STATUS(self):
		"""Get register TX_FIFO_STATUS"""
		return self.read(REG.TX_FIFO_STATUS, 8)
	
	# Bits NELEM_TXFIFO
	# Number of elements in TX FIFO. 
	# Register RX_FIFO_STATUS
	
	
	def setRX_FIFO_STATUS(self, val):
		"""Set register RX_FIFO_STATUS"""
		self.write(REG.RX_FIFO_STATUS, val, 8)
	
	def getRX_FIFO_STATUS(self):
		"""Get register RX_FIFO_STATUS"""
		return self.read(REG.RX_FIFO_STATUS, 8)
	
	# Bits NELEM_RXFIFO
	# Number of elements in RX FIFO. 
	# Register RCO_CALIBR_OUT4
	
	
	def setRCO_CALIBR_OUT4(self, val):
		"""Set register RCO_CALIBR_OUT4"""
		self.write(REG.RCO_CALIBR_OUT4, val, 8)
	
	def getRCO_CALIBR_OUT4(self):
		"""Get register RCO_CALIBR_OUT4"""
		return self.read(REG.RCO_CALIBR_OUT4, 8)
	
	# Bits RWT_OUT
	# RWT word from internal RCO calibrator. 
	# Bits RFB_OUT
	# RFB word (MSB) from internal RCO calibrator. 
	# Register RCO_CALIBR_OUT3
	
	
	def setRCO_CALIBR_OUT3(self, val):
		"""Set register RCO_CALIBR_OUT3"""
		self.write(REG.RCO_CALIBR_OUT3, val, 8)
	
	def getRCO_CALIBR_OUT3(self):
		"""Get register RCO_CALIBR_OUT3"""
		return self.read(REG.RCO_CALIBR_OUT3, 8)
	
	# Bits RFB_OUT
	# RF word (LSB) from internal RCO calibrator. 
	# Bits reserved_0
	# Register VCO_CALIBR_OUT1
	
	
	def setVCO_CALIBR_OUT1(self, val):
		"""Set register VCO_CALIBR_OUT1"""
		self.write(REG.VCO_CALIBR_OUT1, val, 8)
	
	def getVCO_CALIBR_OUT1(self):
		"""Get register VCO_CALIBR_OUT1"""
		return self.read(REG.VCO_CALIBR_OUT1, 8)
	
	# Bits reserved_0
	# Bits VCO_CAL_AMP_OUT
	# VCO magnitude calibration output word (binary coding internally converted from thermometric coding). 
	# Register VCO_CALIBROUT0
	
	
	def setVCO_CALIBROUT0(self, val):
		"""Set register VCO_CALIBROUT0"""
		self.write(REG.VCO_CALIBROUT0, val, 8)
	
	def getVCO_CALIBROUT0(self):
		"""Get register VCO_CALIBROUT0"""
		return self.read(REG.VCO_CALIBROUT0, 8)
	
	# Bits reserved_0
	# Bits VCO_CAL_FREQ_OUT
	# VCO Cbank frequency calibration output word (binary coding internally converted from thermometric coding). 
	# Register TX_PCKT_INFO
	
	
	def setTX_PCKT_INFO(self, val):
		"""Set register TX_PCKT_INFO"""
		self.write(REG.TX_PCKT_INFO, val, 8)
	
	def getTX_PCKT_INFO(self):
		"""Get register TX_PCKT_INFO"""
		return self.read(REG.TX_PCKT_INFO, 8)
	
	# Bits reserved_0
	# Bits TX_SEQ_NUM
	# Current TX packet sequence number. 
	# Bits N_RETX
	# Number of re-transmissions done for the last TX packet. 
	# Register RX_PCKT_INFO
	
	
	def setRX_PCKT_INFO(self, val):
		"""Set register RX_PCKT_INFO"""
		self.write(REG.RX_PCKT_INFO, val, 8)
	
	def getRX_PCKT_INFO(self):
		"""Get register RX_PCKT_INFO"""
		return self.read(REG.RX_PCKT_INFO, 8)
	
	# Bits reserved_0
	# Bits NACK_RX
	# NACK field of the received packet. 
	# Bits RX_SEQ_NUM
	# Sequence number of the received packet. 
	# Register AFC_CORR
	
	
	def setAFC_CORR(self, val):
		"""Set register AFC_CORR"""
		self.write(REG.AFC_CORR, val, 8)
	
	def getAFC_CORR(self):
		"""Get register AFC_CORR"""
		return self.read(REG.AFC_CORR, 8)
	
	# Bits AFC_CORR
	# AFC corrected value. 
	# Register LINK_QUALIF2
	
	
	def setLINK_QUALIF2(self, val):
		"""Set register LINK_QUALIF2"""
		self.write(REG.LINK_QUALIF2, val, 8)
	
	def getLINK_QUALIF2(self):
		"""Get register LINK_QUALIF2"""
		return self.read(REG.LINK_QUALIF2, 8)
	
	# Bits PQI
	# PQI value of the received packet. 
	# Register LINK_QUALIF1
	
	
	def setLINK_QUALIF1(self, val):
		"""Set register LINK_QUALIF1"""
		self.write(REG.LINK_QUALIF1, val, 8)
	
	def getLINK_QUALIF1(self):
		"""Get register LINK_QUALIF1"""
		return self.read(REG.LINK_QUALIF1, 8)
	
	# Bits CS
	# Carrier Sense indication. 
	# Bits SQI
	# SQI value of the received packet. 
	# Register RSSI_LEVEL
	
	
	def setRSSI_LEVEL(self, val):
		"""Set register RSSI_LEVEL"""
		self.write(REG.RSSI_LEVEL, val, 8)
	
	def getRSSI_LEVEL(self):
		"""Get register RSSI_LEVEL"""
		return self.read(REG.RSSI_LEVEL, 8)
	
	# Bits RSSI_LEVEL
	# RSSI level captured at the end of the SYNC word detection of the received packet. 
	# Register RX_PCKT_LEN1
	# Length of the packet received. 
	
	def setRX_PCKT_LEN1(self, val):
		"""Set register RX_PCKT_LEN1"""
		self.write(REG.RX_PCKT_LEN1, val, 16)
	
	def getRX_PCKT_LEN1(self):
		"""Get register RX_PCKT_LEN1"""
		return self.read(REG.RX_PCKT_LEN1, 16)
	
	# Bits RX_PCKT_LEN1
	# Register CRC_FIELD3
	
	
	def setCRC_FIELD3(self, val):
		"""Set register CRC_FIELD3"""
		self.write(REG.CRC_FIELD3, val, 8)
	
	def getCRC_FIELD3(self):
		"""Get register CRC_FIELD3"""
		return self.read(REG.CRC_FIELD3, 8)
	
	# Bits CRC_FIELD3
	# CRC field 3 of the received packet. 
	# Register CRC_FIELD2
	
	
	def setCRC_FIELD2(self, val):
		"""Set register CRC_FIELD2"""
		self.write(REG.CRC_FIELD2, val, 8)
	
	def getCRC_FIELD2(self):
		"""Get register CRC_FIELD2"""
		return self.read(REG.CRC_FIELD2, 8)
	
	# Bits CRC_FIELD2
	# CRC field 2 of the received packet. 
	# Register CRC_FIELD1
	
	
	def setCRC_FIELD1(self, val):
		"""Set register CRC_FIELD1"""
		self.write(REG.CRC_FIELD1, val, 8)
	
	def getCRC_FIELD1(self):
		"""Get register CRC_FIELD1"""
		return self.read(REG.CRC_FIELD1, 8)
	
	# Bits CRC_FIELD1
	# CRC field 1 of the received packet. 
	# Register CRC_FIELD0
	
	
	def setCRC_FIELD0(self, val):
		"""Set register CRC_FIELD0"""
		self.write(REG.CRC_FIELD0, val, 8)
	
	def getCRC_FIELD0(self):
		"""Get register CRC_FIELD0"""
		return self.read(REG.CRC_FIELD0, 8)
	
	# Bits CRC_FIELD0
	# CRC field 0 of the received packet. 
	# Register RX_ADDRE_FIELD1
	
	
	def setRX_ADDRE_FIELD1(self, val):
		"""Set register RX_ADDRE_FIELD1"""
		self.write(REG.RX_ADDRE_FIELD1, val, 8)
	
	def getRX_ADDRE_FIELD1(self):
		"""Get register RX_ADDRE_FIELD1"""
		return self.read(REG.RX_ADDRE_FIELD1, 8)
	
	# Bits RX_ADDRE_FIELD1
	# Source address field of the received packet. 
	# Register RX_ADDRE_FIELD0
	
	
	def setRX_ADDRE_FIELD0(self, val):
		"""Set register RX_ADDRE_FIELD0"""
		self.write(REG.RX_ADDRE_FIELD0, val, 8)
	
	def getRX_ADDRE_FIELD0(self):
		"""Get register RX_ADDRE_FIELD0"""
		return self.read(REG.RX_ADDRE_FIELD0, 8)
	
	# Bits RX_ADDRE_FIELD0
	# Destination address field of the received packet. 
	# Register RSSI_LEVEL_RUN
	# RSSI level of the received packet, which supports continuous fast SPI reading. 
	
	def setRSSI_LEVEL_RUN(self, val):
		"""Set register RSSI_LEVEL_RUN"""
		self.write(REG.RSSI_LEVEL_RUN, val, 8)
	
	def getRSSI_LEVEL_RUN(self):
		"""Get register RSSI_LEVEL_RUN"""
		return self.read(REG.RSSI_LEVEL_RUN, 8)
	
	# Bits RSSI_LEVEL_RUN
	# Register DEVICE_INFO1
	# S2-LP part number 
	
	def setDEVICE_INFO1(self, val):
		"""Set register DEVICE_INFO1"""
		self.write(REG.DEVICE_INFO1, val, 8)
	
	def getDEVICE_INFO1(self):
		"""Get register DEVICE_INFO1"""
		return self.read(REG.DEVICE_INFO1, 8)
	
	# Bits DEVICE_INFO1
	# Register DEVICE_INFO0
	# S2-LP version number 
	
	def setDEVICE_INFO0(self, val):
		"""Set register DEVICE_INFO0"""
		self.write(REG.DEVICE_INFO0, val, 8)
	
	def getDEVICE_INFO0(self):
		"""Get register DEVICE_INFO0"""
		return self.read(REG.DEVICE_INFO0, 8)
	
	# Bits DEVICE_INFO0
	# Register IRQ_STATUS3
	# Interrupt status registers 
	
	def setIRQ_STATUS3(self, val):
		"""Set register IRQ_STATUS3"""
		self.write(REG.IRQ_STATUS3, val, 32)
	
	def getIRQ_STATUS3(self):
		"""Get register IRQ_STATUS3"""
		return self.read(REG.IRQ_STATUS3, 32)
	
	# Bits IRQ_STATUS3
