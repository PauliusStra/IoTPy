from time import sleep

from IoTPy.boards.uper import UPER1

with UPER1() as board, board.pwm(27) as redPin:

    redPin.set_frequency(1000)

    while True:
        for i in xrange(0, 100):
            redPin.set_duty_cycle(i)
            sleep(0.01)
        for i in reversed(xrange(0, 100)):
            redPin.set_duty_cycle(i)
            sleep(0.01)