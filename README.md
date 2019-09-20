# pyEasyAdb

A library that makes it easy for python to communicate with ADB.

# Commands

## Base

Let's instantiate the Base class:

```py
from commands import Base

base = Base()
```

Now we can use your methods.

### execute

Execute an adb command(this command will restart your device)

```py
base.execute('reboot')
```

If you prefer to specify a device:

```py
base.execute('shell', device=base.treat_device('<device_id>'))
```

treat_device is required because it treats the string before it can be added to the command. Exemple:

```py
print(base.treat_device('<device_id>'))

```

The return will be: ``` -s 1585c853 ```

### devices

Returns a list of all plugged in devices.

```py

print(base.devices())

```

as an example returns ```['device_id', 'device_id2']```

## BaseCommand

This class is used to execute rotary commands.
Let's instantiate the class BaseCommand:

```py
from commands import BaseCommand

baseCommand = BaseCommand()

```

### input_text

This command types specified text directly into the device:

```py
baseCommand.input_text('Text example')
```

## Final notes

This library is still in beta, I'm working to improve every day.
My goal is to make it as simple and abstract as possible.



