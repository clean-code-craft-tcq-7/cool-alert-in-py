import unittest
from unittest.mock import MagicMock, ANY
from actions import Actuators
from battery_data_model import BatteryDataModel
from chain import battery_data_to_action
from thresholds import ThermalManagementType

#----------- STEP 6 code starts ----------
#class TestChain(unittest.TestCase):
#    def test_battery_data_to_action(self):
#        battery_data = BatteryDataModel(10342, ThermalManagementType.THERMAL_HYBRID, 60)
#        mock_actuators = Actuators()
#        mock_actuators.email_sender = MagicMock()
#
#        battery_data_to_action(battery_data, mock_actuators)
#        mock_actuators.email_sender.assert_called_once_with("manager@battery.com", ANY, ANY, ANY)
#----------- STEP 6 code ends ----------