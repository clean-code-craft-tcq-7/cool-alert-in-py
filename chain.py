from actions import Actuators
from battery_data_model import BatteryDataModel, BatteryState
from classify import classify_battery_state
# ---------- STEP 6 code starts ----------

#def battery_data_to_action(battery_data: BatteryDataModel, actuators: Actuators):
#    state = classify_battery_state(battery_data)
#    if state == BatteryState.BATTERY_ALERT:
#        actuators.email_sender("manager@battery.com", "Battery Alert", "Battery temperature is too high", 
#                               "noreply@battery.com")
#            
#
# ---------- STEP 6 code ends ----------
