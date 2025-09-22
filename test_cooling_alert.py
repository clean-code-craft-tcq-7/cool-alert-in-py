import unittest
from cooling_alert import CoolingType, ActionType, battery_temperature_to_action

class TestCoolingAlert(unittest.TestCase):
    def test_passive_cooling_alert_to_email(self):
        action = battery_temperature_to_action(CoolingType.PASSIVE_COOLING, 45.0)
        self.assertEqual(action.action_type, ActionType.ALERT_EMAIL)
        self.assertEqual(action.action_body, "Temperature alert: 45.0")
    
    def test_no_alert(self):
        action = battery_temperature_to_action(CoolingType.PASSIVE_COOLING, 32)
        self.assertEqual(action.action_type, ActionType.NO_ALERT)

    def test_hi_active_cooling_alert_to_email(self):
        action = battery_temperature_to_action(CoolingType.HI_ACTIVE_COOLING, 60.0)
        self.assertEqual(action.action_type, ActionType.ALERT_EMAIL)
        self.assertEqual(action.action_body, "Temperature alert: 60.0")