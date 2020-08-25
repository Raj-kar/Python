import unittest

from activities import eat, nap, walk, is_funny, laugh, even_numbers


class TestActivities(unittest.TestCase):
    def test_eat_healthy(self):
        """Test for healthy Food"""
        self.assertEqual(eat("rice", is_healthy=True),
                         "I eat rice, because life a temple")

    def test_eat_healthy_bool(self):
        with self.assertRaises(ValueError):
            eat("pizza", is_healthy="a string")

    def test_eat_unhealthy(self):
        """Test for unhealthy Food"""
        self.assertEqual(eat("pizza", is_healthy=False),
                         "I eat pizza, because YOLO")

    def test_short_nap(self):
        """Test for short nap"""
        self.assertEqual(nap(1), "sleep for 1 hour, make me free")

    def test_long_nap(self):
        """Test for long nap"""
        self.assertEqual(nap(3), "sleep for 3 hour, make me more lazy")

    def test_short_walk(self):
        """Test for short wlak"""
        self.assertEqual(walk(1), "I just walk 1 km, Ok that's too low")

    def test_long_walk(self):
        """Test for long walk"""
        self.assertEqual(walk(5), "I just walk 5 km, Ok that's too much")

    def test_is_not_funny(self):
        self.assertFalse(is_funny("Rahul"))

    def test_is_funny(self):
        # self.assertEqual(is_funny("Raj"),True)
        self.assertTrue(is_funny("Raj"))
        self.assertTrue(is_funny("Maoni"))
        self.assertTrue(is_funny("Raima"))

    def test_for_choice(self):
        self.assertIn(laugh(), ("haha", "lol", "tehehe"))

    def test_for_even_numbers_t(self):
        self.assertTrue(even_numbers(4))

    def test_for_even_numbers_f(self):
        self.assertFalse(even_numbers(5))


if __name__ == "__main__":
    unittest.main()

# Run with -v [add at last] for receive output with docstrings !



