import os
import yaml
import time
import argparse
# import webbrowser
from selenium import webdriver
from pynput.keyboard import Key, Controller


def build_action_list_sequence(config: dict) -> list:
    actions = []
    for i in config.keys():
        actions.append(config[i])
    return actions


def authorize_by_form():
    pass
    # driver = webdriver.Chrome(executable_path="C:\\Users\\PeZet2\\IdeaProjects\\lib\\chromedriver.exe")
    # driver.get('http://192.168.1.18:8829/login')
    # time.sleep(2)
    # print(driver.find_elements_by_tag_name("form").text)


def authorize_by_kerberos():
    pass


def run_app(action: dict):
    print(f"Running app: {action['name']}...")
    os.system(f"start {action['path']}")
    if "authorization" in action.keys():
        if action['authorization']['mode'] == AUTH_MODE_FORM:
            print("Authorizing by form...")
            authorize_by_form()
        elif action['authorization']['mode'] == AUTH_MODE_KERBEROS:
            print("Authorizing using kerberos...")
            authorize_by_kerberos()


def run_sleep(value):
    print(f"Waiting for {value} seconds...")
    time.sleep(value)


def run_keystrokes(sequence, flow):
    print("Pressing given key sequence...")


def run_action(action: dict):
    if action['type'] == ACTION_RUN_APP:
        if 'authorization' in action.keys():
            run_app(action)
        else:
            run_app(action)
    elif action['type'] == ACTION_SLEEP:
        run_sleep(action['value'])
    elif action['type'] == ACTION_KEYSTROKE:
        run_keystrokes(action['sequence'], action['flow'])
    else:
        print(f"Action {action['type']} undefined.")


def run_actions(config: dict):
    action_sequence = build_action_list_sequence(config)
    for action in action_sequence:
        run_action(action)


def read_config(filename: str) -> dict:
    with open(filename, 'r') as config:
        return yaml.safe_load(config)


def parse_args():
    parser = argparse.ArgumentParser(description='Parameters for app_runner.')
    parser.add_argument('--config_file',
                        required=True,
                        help='Configuration file')
    return parser.parse_args()


def main():
    # Wczytaj parametry
    args = parse_args()

    # Wczytaj konfigurację z pliku
    config = read_config(args.config_file)
    print(config)

    run_actions(config)


if __name__ == "__main__":
    ACTION_RUN_APP = "app"
    ACTION_SLEEP = "sleep"
    ACTION_KEYSTROKE = "keystroke"

    AUTH_MODE_FORM = "form"
    AUTH_MODE_KERBEROS = "kerberos"

    main()
