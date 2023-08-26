radio.onReceivedNumber(function (receivedNumber) {
    if (receivedNumber == 1) {
        LightUP()
    } else if (receivedNumber == 2) {
        LightDown()
    }
})
input.onButtonPressed(Button.A, function () {
    LightUP()
})
function LightUP () {
    LightLevel = LightLevel / 1.41421356
    if (LightLevel < 1) {
        LightLevel = 0
    }
    pins.analogWritePin(AnalogPin.P1, LightLevel)
}
function LightDown () {
    LightLevel = LightLevel * 1.41421356
    if (LightLevel > 1023) {
        LightLevel = 1023
    }
    if (LightLevel == 0) {
        LightLevel = 1
    }
    pins.analogWritePin(AnalogPin.P1, LightLevel)
}
function 光適応 () {
    Light = input.lightLevel()
    pins.analogWritePin(AnalogPin.P1, Light * 4 * (LightLevel / 1023))
}
input.onButtonPressed(Button.B, function () {
    LightDown()
})
let Light = 0
let LightLevel = 0
LightLevel = 800
pins.analogWritePin(AnalogPin.P1, LightLevel)
radio.setGroup(123)
basic.pause(1000)
basic.forever(function () {
    光適応()
    basic.pause(500)
})
