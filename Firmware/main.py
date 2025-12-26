import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Macros, Press, Release, Tap
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.media_keys import MediaKeys

keyboard.extensions.append(MediaKeys())

keyboard = KMKKeyboard()
macros = Macros()
keyboard.modules.append(macros)

encoders = EncoderHandler()
keyboard.modules.append(encoders)

# Define your button pins here (based on the schematic: SW1 to SW6
KEY_PINS = [
    board.GPIO1,  # SW1
    board.GPIO2,  # SW2
    board.GPIO4,  # SW3
    board.GPIO3,  # SW4
    board.GPIO26,   # SW5
    board.GPIO27,   # SW6
    board.GPIO29,   # SW7 left (rotary)
    board.GPIO28,   # SW7 right (rotary)
]

keyboard.matrix = KeysScanner(
    pins=KEY_PINS,
    value_when_pressed=False,
)

# Define the rotary encoder pins (A, B, and no integrated button pin since push is separate)
encoders.pins = [
    (board.GPIO29, board.GPIO28, None),
]

# Example keymap for the 7 buttons
keyboard.keymap = [
    [
        # Currently, SW1 and SW5: i haven't assigned anything on purpose!
        KC.NO, KC.UP, KC.LEFT, KC.DOWN, KC.NO, KC.RIGHT, KC.VOLD, KC.VOLU, 
    ]
]

# Example encoder map (one layer, one encoder: clockwise, counterclockwise, button - but button is handled separately)
encoders.map = [
    [(KC.VOLU, KC.VOLD, KC.NO)],  # Use KC.NO for button since it's in the keymap
]

if __name__ == '__main__':
    keyboard.go()
