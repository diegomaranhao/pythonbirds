from unittest import TestCase

from oo.carro import Motor


class CarroTestCase(TestCase):
    def test_velocidade_inicial(self):
        motor = Motor()
        self.assertEqual(0, motor.velocidade)

    def test_acelerar(self):
        motor = Motor()
        motor.acelerar()
        self.assertEqual(1, motor.velocidade)
        motor.acelerar()
        self.assertEqual(2, motor.velocidade)
        motor.acelerar()
        self.assertEqual(3, motor.velocidade)

    def test_frear(self):
        motor = Motor()
        motor.acelerar()
        motor.acelerar()
        motor.acelerar()
        motor.frear()
        self.assertEqual(1, motor.velocidade)
        motor.frear()
        self.assertEqual(0, motor.velocidade)
        motor.frear()
