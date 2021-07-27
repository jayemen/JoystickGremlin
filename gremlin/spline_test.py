# -*- coding: utf-8; -*-

import unittest

import spline


def near(a, b):
    print(a, b)
    return abs(a - b) < 10e-12


class TestLinear(unittest.TestCase):
    def test_run(self):
        linear = spline.Linear([
            spline.Point2D(x=0.0, y=0.0),
            spline.Point2D(x=1.0, y=1.0)
        ])

        self.assertTrue(near(linear(0.5), 0.5))
        self.assertTrue(near(linear(0.25), 0.25))
        self.assertTrue(near(linear(0.0), 0.0))
        self.assertTrue(near(linear(1.0), 1.0))

        linear = spline.Linear([
            spline.Point2D(x=0.0, y=0.0),
            spline.Point2D(x=0.25, y=0.5),
            spline.Point2D(x=1.0, y=1.0)
        ])

        self.assertTrue(near(linear(0.5), 0.6666666666666666))
        self.assertTrue(near(linear(0.25), 0.5))
        self.assertTrue(near(linear(0.0), 0.0))
        self.assertTrue(near(linear(1.0), 1.0))

        self.assertTrue(near(linear(0.1), 0.2))

        linear = spline.Linear([
            spline.Point2D(x=-1.0, y=-1.0),
            spline.Point2D(x=1.0, y=1.0)
        ])

        self.assertTrue(near(linear(0), 0))
        self.assertTrue(near(linear(-1.0), -1.0))
        self.assertTrue(near(linear(1.0), 1.0))
        self.assertTrue(near(linear(0.3), 0.3))

