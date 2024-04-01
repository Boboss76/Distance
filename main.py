basic.show_leds("""
    # . # . #
    . # # # .
    # # # # #
    . # # # .
    # . # . #
    """)

def on_forever():
    basic.show_string("D=")
    basic.show_number(sonar.ping(DigitalPin.P0, DigitalPin.P1, PingUnit.CENTIMETERS))
basic.forever(on_forever)
