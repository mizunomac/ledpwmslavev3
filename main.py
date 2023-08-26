def on_received_number(receivedNumber):
    global LightLevel
    if receivedNumber == 1:
        LightLevel = LightLevel * 1.41421356
        if LightLevel > 1023:
            LightLevel = 1023
        pins.analog_write_pin(AnalogPin.P1, LightLevel)
    elif receivedNumber == 2:
        LightLevel = LightLevel / 1.41421356
        if LightLevel < 1:
            LightLevel = 1
        pins.analog_write_pin(AnalogPin.P1, LightLevel)
radio.on_received_number(on_received_number)

LightLevel = 0
LightLevel = 128
pins.analog_write_pin(AnalogPin.P1, LightLevel)
radio.set_group(123)
strip = neopixel.create(DigitalPin.P0, 17, NeoPixelMode.RGB_RGB)
strip.show_rainbow(1, 360)
basic.pause(1000)
range2 = strip.range(0, 1)
range22 = strip.range(1, 1)
range3 = strip.range(2, 1)
range2.show_color(neopixel.colors(NeoPixelColors.RED))
range22.show_color(neopixel.colors(NeoPixelColors.GREEN))
range3.show_color(neopixel.colors(NeoPixelColors.BLUE))
strip.clear()
basic.clear_screen()

def on_forever():
    for index in range(8):
        strip.show_rainbow(90, 270)
        basic.pause(500)
        strip.show_rainbow(45, 360)
        basic.pause(500)
        strip.show_rainbow(135, 360)
        basic.pause(500)
        strip.show_rainbow(180, 360)
        basic.pause(500)
        strip.show_rainbow(225, 400)
        basic.pause(500)
        strip.show_rainbow(270, 400)
        basic.pause(500)
        strip.show_rainbow(315, 444)
        basic.pause(500)
basic.forever(on_forever)

