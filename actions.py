
import os
import time
from abc import abstractmethod
from pynput.keyboard import Key, Controller


class ActionBuilder():

    ACTION_RUN_APP = 1
    ACTION_SLEEP = 2
    ACTION_KEYSTROKE = 3

    # def __init__(self, action: dict):
    #     ActionBuilder.build_action(action)

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
        print(f"Running action: {self.name}...")


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
        print(f"Waiting for {self.value} seconds...")
        time.sleep(self.value)


class KeystrokeAction(Action):

    def __init__(self, name, sequence: list):
        super().__init__(name)     
        self.sequence = sequence    

    def run_action(self):
        super().run_action()
        print(f"Pressing given key sequence [{','.join(self.sequence)}]...")
