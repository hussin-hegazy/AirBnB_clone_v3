#!/usr/bin/python3
import unittest
from your_module import YourClass

class TestYourClass(unittest.TestCase):
    def setUp(self):
        """إعدادات قبل كل اختبار"""
        self.instance = YourClass()

    def test_feature(self):
        """اختبار ميزة جديدة"""
        result = self.instance.some_method()
        self.assertEqual(result, expected_value)

    def test_edge_case(self):
        """اختبار حالة شاذة"""
        result = self.instance.some_method_with_input('invalid')
        self.assertRaises(ExpectedException, result)

    def tearDown(self):
        """تنظيف بعد كل اختبار"""
        pass

if __name__ == '__main__':
    unittest.main()

