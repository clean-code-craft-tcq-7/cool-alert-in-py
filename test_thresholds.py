import unittest
from thresholds import ThermalManagementType, alert_temperature_for_cooling_type

# ---------- STEP 5 code starts ----------
#class TestThresholds(unittest.TestCase):
#    def test_cooling_dependent_thresholds(self):
#        passive_limit = alert_temperature_for_cooling_type(ThermalManagementType.THERMAL_PASSIVE)
#        hi_active_limit = alert_temperature_for_cooling_type(ThermalManagementType.THERMAL_ACTIVE)
#        med_active_limit = alert_temperature_for_cooling_type(ThermalManagementType.THERMAL_HYBRID)
#
#        self.assertLess(passive_limit, med_active_limit)
#        self.assertLess(med_active_limit, hi_active_limit)
# ---------- STEP 5 code ends ----------