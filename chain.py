from actions import Actuators
from battery_data_model import BatteryDataModel
from thresholds import alert_temperature_for_cooling_type
# ---------- STEP 6 code starts ----------

def battery_data_to_action(battery_data: BatteryDataModel, actuators: Actuators):
    if battery_data.temperature > alert_temperature_for_cooling_type(battery_data.thermal_management_type):
        actuators.email_sender("manager@battery.com", "Battery Alert", "Battery temperature is too high", 
                               "noreply@battery.com")
            


# ---------- STEP 6 code ends ----------