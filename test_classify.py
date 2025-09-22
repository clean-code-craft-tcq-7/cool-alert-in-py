import unittest
# ---------- STEP 5 code starts ----------
#from battery_data_model import BatteryDataModel, BatteryState
#from classify import classify_battery_state
#from thresholds import ThermalManagementType

#class TestClassify(unittest.TestCase):
#    def test_battery_ok(self):
#        battery_data = BatteryDataModel(10567, ThermalManagementType.THERMAL_PASSIVE, 25)
#        state = classify_battery_state(battery_data)
#        self.assertEqual(state, BatteryState.BATTERY_OK)
#    
#    def test_battery_alert(self):
#        battery_data = BatteryDataModel(21389, ThermalManagementType.THERMAL_HYBRID, 60)
#        state = classify_battery_state(battery_data)
#        self.assertEqual(state, BatteryState.BATTERY_ALERT)
# ---------- STEP 5 code ends ----------