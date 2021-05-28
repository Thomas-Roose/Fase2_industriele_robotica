#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from ariac_flexbe_example_behaviors.get_order_sm import get_orderSM
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Thu May 27 2021
@author: Thomas Roose
'''
class pick_part_from_binSM(Behavior):
	'''
	unit1
	'''


	def __init__(self):
		super(pick_part_from_binSM, self).__init__()
		self.name = 'pick_part_from_bin'

		# parameters of this behavior

		# references to used behaviors
		self.add_behavior(get_orderSM, 'get_order')

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:30 y:365, x:405 y:232
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])
		_state_machine.userdata.OrderId = ' '
		_state_machine.userdata.Shipments = []
		_state_machine.userdata.NumberOfShipments = []
		_state_machine.userdata.ShipmentType = ' '
		_state_machine.userdata.AgvId = ' '
		_state_machine.userdata.Products = []
		_state_machine.userdata.NumberOfProducts = []
		_state_machine.userdata.ShipmentIterator = []
		_state_machine.userdata.ProductIterator = 0
		_state_machine.userdata.ProductType = []
		_state_machine.userdata.ProductPose = []
		_state_machine.userdata.MaterialsLocationList = []

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:108 y:31
			OperatableStateMachine.add('get_order',
										self.use_behavior(get_orderSM, 'get_order'),
										transitions={'finished': 'finished', 'fail': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'fail': Autonomy.Inherit})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
