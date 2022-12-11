def Preparewhen_done_show_text(text: str):
    basic.show_string("Preparing")
    basic.show_leds("""
        . . . . .
                . . . . .
                # . . . .
                . . . . .
                . . . . .
    """)
    basic.pause(100)
    basic.show_leds("""
        . . . . .
                . . . . .
                # . # . .
                . . . . .
                . . . . .
    """)
    basic.pause(100)
    basic.show_leds("""
        . . . . .
                . . . . .
                # . # . #
                . . . . .
                . . . . .
    """)
    basic.clear_screen()
    basic.show_string(text)
    basic.show_leds("""
    # . # . #
    # . # . #
    # . # . #
    # . . . #
    # # # # #
    """)
def on_button_pressed_ab():
    led.stop_animation()
    basic.clear_screen()
    basic.show_string("Terminated goodbye")
    basic.show_string("Err")
    control.reset()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

Preparewhen_done_show_text("Power on")