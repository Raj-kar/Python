import unittest

from robot import Robot


class RobotTest(unittest.TestCase):
    def setUp(self):
        self.rob1 = Robot("Raj", battery=50)

    def test_charge(self):
        self.assertEqual(self.rob1.battery, 50)
        self.assertEqual(self.rob1.charge(), "battery charged !")
        self.rob1.charge()
        self.assertEqual(self.rob1.battery, 100)

    def test_say_hello(self):
        self.assertEqual(self.rob1.say_name(), "BIP BIP BIP ! MY name is Raj")
        self.rob1.battery -= 100
        self.assertEqual(self.rob1.say_name(), "Oh noo! charge me !")

    def test_learn_skill(self):
        self.assertEqual(self.rob1.learn_skill("dance", 30),
                         "BIP BIP BIP !!.. Now I know how to dance")
        self.assertEqual(self.rob1.learn_skill("sing", 30),
                         "Oh noo! charge me for learn sing")
        self.rob1.charge()		# full charge
        self.assertEqual(self.rob1.learn_skill("sing", 100),
                         "BIP BIP BIP !!.. Now I know how to sing")

    def test_battery_overload(self):
        with self.assertRaises(ValueError):
        	 self.rob1.charge(percentage=200)

if __name__ == "__main__":
    unittest.main()
