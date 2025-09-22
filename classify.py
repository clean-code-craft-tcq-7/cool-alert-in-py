from battery_data_model import BatteryDataModel, BatteryState
from thresholds import alert_temperature_for_cooling_type

def classify_battery_state(battery_data: BatteryDataModel) -> BatteryState:
    """Classify the battery state based on its temperature and thermal management type.
    """
    state = BatteryState.BATTERY_OK
    alert_threshold = alert_temperature_for_cooling_type(battery_data.thermal_management_type)
    if battery_data.temperature > alert_threshold:
        state = BatteryState.BATTERY_ALERT
    
    return state
    