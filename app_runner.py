import yaml
import argparse
from actions import ActionBuilder


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


def parse_args():
    parser = argparse.ArgumentParser(description='Parameters for app_runner.')
    parser.add_argument('--config_file',
                        required=True,
                        help='Configuration file')
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    apprunner = AppRunner(args.config_file)
    apprunner.run()
