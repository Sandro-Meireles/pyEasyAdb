from os import popen

ADB_LOCATION = 'adb'

class Base:

    def execute(self, command, device=''):
        if device:
            device = ' -s {} '.format(device)

        response = popen('{}{} {}'.format(ADB_LOCATION, device, command)).read()

        return response

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
        self.execute('shell input text {}'.format(value), device=device)
    
    def input_key(self, key, device=''):

        self.execute('shell input keyevent {}'.format(key), device=device)


class Package(Base):

    def install(self, location, device=''):
        self.execute('install {}'.format(location), device=device)

    def uninstall(self, app, device=''):
        self.execute('uninstall {}'.format(app), device=device)