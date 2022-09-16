
from msilib import sequence
import os
import time
from pynput.keyboard import Controller
from signs import sign_dict


class ActionBuilder():

    @staticmethod
    def build_action(action: dict):
        if action.get("type") == "app":
            return AppAction(action.get("name"), action.get("path"))
        elif action.get("type") == "sleep":
            return SleepAction(action.get("name"), action.get("value"))
        elif action.get("type") == "keystroke":
            return KeystrokeAction(action.get("name"), action.get("sequence"))
        

class Action:

    def __init__(self, name: str):
        self.name = name

    def run_action(self):
        pass


class AppAction(Action):

    def __init__(self, name: str, path: str):
        super().__init__(name)
        self.path = path
    
    def run_action(self):
        super().run_action()
        os.system(f"start {self.path}")


class SleepAction(Action):

    def __init__(self, name, value: int):
        super().__init__(name)
        self.value = value
    
    def run_action(self):
        super().run_action()
        time.sleep(self.value)


class KeystrokeAction(Action):

    def __init__(self, name, sequence: list):
        super().__init__(name)     
        self.sequence = sequence
        self.keyboard = Controller()    

    def check_sign(self, value: str) -> str:
        return sign_dict.get(value, value)

    def press_in_sequence(self, series: list):
        for element in series:
            self.write_element(element)

    def press_in_parallel(self, series: list):
        print(series[0])
        if len(series) > 1:
            with self.keyboard.pressed(sign_dict.get(series[0])):
                self.press_in_parallel(series[1:])
        else:
            self.keyboard.press(sign_dict.get(series[0], series[0]))
            self.keyboard.release(sign_dict.get(series[0], series[0]))

    def write_element(self, element: str):
        if element in sign_dict:
            self.keyboard.press(sign_dict.get(element))
            self.keyboard.release(sign_dict.get(element))
        else:
            self.keyboard.type(element)

    def run_action(self):
        super().run_action()
        for seq in self.sequence:
            _type = seq.get('type')
            _value = seq.get('value')
            if _type == "series":
                self.press_in_sequence(_value)
            elif _type == "parallel":
                self.press_in_parallel(_value)
