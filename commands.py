from os import popen
import settings

class Base:

    def execute(self, command, device=''):
        response = popen(f'./{settings.ADB_LOCATION} {command}').read()

        return response

    def treat_device(self, device):
        device = f' -s {device} '

        return device

    def devices(self):

        devices = []

        open_devices = popen("adb devices").read()

        open_devices = open_devices.replace('List of devices attached', '')
        open_devices = open_devices.split('device')
        open_devices.pop(-1)

        for item in open_devices:
            item = item.replace('\n', '')
            item = item.replace('\t', '')
            devices.append(item)

        return devices

class BaseCommand(Base):

    def input_text(self, value, device=''):

        value = value.replace(' ', '%s')
        self.execute(f'{device}shell input text {value}')

baseCommand = BaseCommand()

baseCommand.input_text('Text example')


