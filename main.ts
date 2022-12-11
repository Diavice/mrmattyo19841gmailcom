input.onButtonPressed(Button.AB, function () {
    led.stopAnimation()
    basic.clearScreen()
    basic.showString("Terminated goodbye")
    basic.showString("Err")
    control.reset()
})
function Preparewhen_done_show_text (text: string) {
    basic.showString("Preparing")
    basic.showLeds(`
        . . . . .
        . . . . .
        # . . . .
        . . . . .
        . . . . .
        `)
    basic.pause(100)
    basic.showLeds(`
        . . . . .
        . . . . .
        # . # . .
        . . . . .
        . . . . .
        `)
    basic.pause(100)
    basic.showLeds(`
        . . . . .
        . . . . .
        # . # . #
        . . . . .
        . . . . .
        `)
    basic.clearScreen()
    basic.showLeds(`
        # . # . #
        # . # . #
        # . # . #
        # . . . #
        # # # # #
        `)
    basic.showString(text)
}
Preparewhen_done_show_text("Power on")
