import unittest

from main import win
from sportsman_game import *

class TestGame (unittest.TestCase):
    def test_Projectile_draw_full(self):
        self.assertEqual(Projectile(10,420).draw(40,win), 420)

    def test_Projectile_draw_part(self):
        for s, res in [[30, 415], [31, 410], [32, 405]]:
            with self.subTest(i=s):
                self.assertEqual(Projectile(10,420-(s-30)*5).draw(s,win), res)

    def test_winning(self):
        self.assertEqual(winning(100, win, 50), False)


