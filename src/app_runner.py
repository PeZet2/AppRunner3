import yaml
from lib.actions import ActionBuilder


class AppRunner():

    def __init__(self, configuration: str):
        self.configuration = self.read_config(configuration)
        self.actions = list()

    def read_config(self, filename: str) -> dict:
        with open(filename, 'r') as config:
            return yaml.safe_load(config)

    def build_action_list_sequence(self) -> list:
        for i in self.configuration.keys():
            self.actions.append(ActionBuilder.build_action(self.configuration[i]))

    def run(self):
        self.build_action_list_sequence()
        for action in self.actions:
            action.run_action()


if __name__ == "__main__":
    apprunner = AppRunner('config.yml')
    apprunner.run()
