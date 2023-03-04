import os
import json
import badger2040
from utils import warning

states: list[str] = []
current_state: str = ''

display = badger2040.Badger2040()
display.led(128)
display.update_speed(badger2040.UPDATE_NORMAL)


def initialize() -> None:
    global states, current_state
    cur_dir = os.listdir()
    states = list(sorted(x for x in cur_dir if x.startswith('app_') and x.endswith(".py")))
    if not states:
        warning("SilentOS: no states found", display, timeout=5)
        return

    try:
        os.stat('/silentos')
    except OSError:
        os.mkdir('/silentos')

    try:
        with open('/silentos/state', 'rt') as f:
            data: dict = json.loads(f.read())
            current_state = data.get('current_state', '')
    except OSError:
        pass

    if current_state not in states:
        current_state = states[0]

    return


def shift_state(forward: bool = True) -> None:
    global current_state
    current_state_index = states.index(current_state)
    current_state_index += 1 if forward else -1
    while current_state_index >= len(states):
        current_state_index -= len(states)
    while current_state_index < 0:
        current_state_index += len(states)

    set_state(current_state_index)
    return


def set_state(index: int) -> None:
    global current_state

    if not states:
        warning("SilentOS: states are empty", display, timeout=5)
        return

    if index < 0 or index >= len(states):
        warning(f"SilentOS: incorrect index {index}, setting state[0]", display, timeout=5)
        index = 0
    current_state = states[index]

    # save state
    with open('/silentos/state', 'wt') as f:
        data = {'current_state': current_state}
        f.write(json.dumps(data))

    # load module and call 'enter'
    try:
        __import__(current_state[:-3]).enter(display)
    except ImportError:
        warning(f"SilentOS: {current_state} couldn't be imported", display, timeout=5)
    except Exception as e:
        warning(f"SilentOS: {e}", display, timeout=5)


def load_and_call(method_name: str) -> None:
    try:
        module = __import__(current_state[:-3])
        fun = getattr(module, method_name)
        fun(display)
    except ImportError:
        warning(f"SilentOS: {current_state} couldn't be imported", display, timeout=5)
    except AttributeError:
        warning(f"SilentOS: function {method_name} is not implemented in {current_state}")
        pass
    except Exception as e:
        warning(f"SilentOS: {e}", display, timeout=5)


if __name__ == '__main__':
    initialize()

    while True:
        if display.pressed(badger2040.BUTTON_A):
            load_and_call('process_a')
        if display.pressed(badger2040.BUTTON_B):
            load_and_call('process_b')
        if display.pressed(badger2040.BUTTON_C):
            load_and_call('process_c')
        if display.pressed(badger2040.BUTTON_UP):
            shift_state(True)
        if display.pressed(badger2040.BUTTON_DOWN):
            shift_state(False)

        display.halt()
