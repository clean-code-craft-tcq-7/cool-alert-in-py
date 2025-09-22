from dataclasses import dataclass
from enum import Enum

class CoolingType(Enum):
    PASSIVE_COOLING = 1
    HI_ACTIVE_COOLING = 2
    MED_ACTIVE_COOLING = 3

class ActionType(Enum):
    NO_ALERT = 1
    ALERT_EMAIL = 2

@dataclass
class Action:
    action_type: int
    action_body: str

PASSIVE_COOLING_LIMIT = 40.0;
HI_ACTIVE_COOLING_LIMIT = 55.0;

def battery_temperature_to_action(cooling_type: CoolingType, temperature: float) -> Action:
    action = Action(action_type=0, action_body="")
    if cooling_type == CoolingType.PASSIVE_COOLING and temperature > PASSIVE_COOLING_LIMIT:
        action.action_type = ActionType.ALERT_EMAIL
        action.action_body = f"Temperature alert: {temperature:.1f}"
    elif cooling_type == CoolingType.HI_ACTIVE_COOLING and temperature > HI_ACTIVE_COOLING_LIMIT:
        action.action_type = ActionType.ALERT_EMAIL
        action.action_body = f"Temperature alert: {temperature:.1f}"
    else:
        action.action_type = ActionType.NO_ALERT
        action.action_body = ""
    
    return action