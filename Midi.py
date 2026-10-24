# Kudi keyboard code
import board
import touchio

from kmk.extensions.media_keys import MediaKeys
from kmk.extensions.rgb import RGB, AnimationModes
from kmk.keys import KC
from kmk.kmk_keyboard import KMKKeyboard
from kmk.modules.encoder import EncoderHandler
from kmk.modules.midi import MidiKeys
from kmk.scanners import Scanner
from kmk.scanners.keypad import KeysScanner


# Capacitive touch scanner
class TouchScanner(Scanner):

    def __init__(self, pins):
        self.pads = [touchio.TouchIn(p) for p in pins]
        self.pressed = [False] * len(pins)

    @property
    def key_count(self):
        return len(self.pads)

    def scan_for_changes(self):
        for i, pad in enumerate(self.pads):
            touched = pad.value
            if touched != self.pressed[i]:
                self.pressed[i] = touched
                return i + self.offset if touched else None


keyboard = KMKKeyboard()
midi = MidiKeys()
media_keys = MediaKeys()

# Conects hardware to the keyboard pins
keyboard.matrix = [
    # 9 Touch pads mapped to GP1-GP9 (Keys 1-9)
    TouchScanner([
        board.GP1,  # TOUCH1
        board.GP2,  # TOUCH2
        board.GP3,  # TOUCH3
        board.GP4,  # TOUCH4
        board.GP5,  # TOUCH5
        board.GP6,  # TOUCH6
        board.GP7,  # TOUCH7
        board.GP8,  # TOUCH8
        board.GP9,  # TOUCH9
    ]),
    # 2 Physical switches mapped to RX and TX (Keys 9 and 10)
    KeysScanner(
        pins=[board.RX, board.TX], value_when_pressed=False, pull=True
    ),
]

# Midi note mapping for the touch pads and switches
keyboard.keymap = [[
    # Touch Pads (9 notes: C major scale progression from MIDI C4 onwards)
    KC.MIDI_NOTE(60),  # TOUCH1
    KC.MIDI_NOTE(62),  # TOUCH2
    KC.MIDI_NOTE(64),  # TOUCH3
    KC.MIDI_NOTE(65),  # TOUCH4
    KC.MIDI_NOTE(67),  # TOUCH5
    KC.MIDI_NOTE(69),  # TOUCH6
    KC.MIDI_NOTE(71),  # TOUCH7
    KC.MIDI_NOTE(72),  # TOUCH8
    KC.MIDI_NOTE(74),  # TOUCH9
    # Switches (2 drum triggers: Kick and Snare)
    KC.MIDI_NOTE(36),  # SWITCH1
    KC.MIDI_NOTE(38),  # SWITCH2
]]

# Rotary encoder configuration matching GP11 and GP12 (A/B), and GP10 for the button click
encoder = EncoderHandler()
encoder.pins = ((board.GP11, board.GP12, board.GP10),)
encoder.map = [
    ((KC.VOLD, KC.VOLU, KC.MPLY),)
]  # Clockwise = Vol+, Counter = Vol-, Click = Play/Pause

keyboard.modules = [midi, encoder]

# 3-pixel SK6812MINI-E rainbow strip configured on GP13
keyboard.extensions = [
    media_keys,
    RGB(
        pixel_pin=board.GP13,
        num_pixels=3,
        val_default=80,
        animation_mode=AnimationModes.RAINBOW,
    ),
]

if __name__ == '__main__':
    keyboard.go()
