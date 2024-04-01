basic.showLeds(`
    # . # . #
    . # # # .
    # # # # #
    . # # # .
    # . # . #
    `)
basic.forever(function on_forever() {
    basic.showString("D=")
    basic.showNumber(sonar.ping(DigitalPin.P0, DigitalPin.P1, PingUnit.Centimeters))
})
