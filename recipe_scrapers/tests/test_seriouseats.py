import os
import unittest

from recipe_scrapers.seriouseats import SeriousEats


class TestSeriousEats(unittest.TestCase):
    def setUp(self):
        # tests are run from tests.py
        with open(os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            'test_data',
            'seriouseats.testhtml'
        )) as file_opened:
            self.harvester_class = SeriousEats(file_opened, test=True)

    def test_host(self):
        self.assertEqual(
            'seriouseats.com',
            self.harvester_class.host()
        )

    def test_title(self):
        self.assertEqual(
            self.harvester_class.title(),
            'Homemade Preserved Horseradish Recipe'
        )

    def test_total_time(self):
        self.assertEqual(
            10,
            self.harvester_class.total_time()
        )

    def test_yields(self):
        self.assertEqual(
            "1 item(s)",
            self.harvester_class.yields()
        )

    def test_image(self):
        self.assertEqual(
            'https://www.seriouseats.com/recipes/images/2015/07/20150727-horseradish-vicky-wasik-14.jpg',
            self.harvester_class.image()
        )

    def test_ingredients(self):
        self.assertCountEqual(
            [
                '1 horseradish root, ends trimmed, peeled, cut into 1-inch chunks (see note)',
                'Distilled white vinegar, for soaking',
                'Kosher salt'
            ],
            self.harvester_class.ingredients()
        )

    def test_instructions(self):
        self.assertEqual(
            '1. In a food processor or blender, process horseradish to fine shreds. Add enough vinegar to cover, then season with salt. If it tastes too pungent, add water, 1 tablespoon at a time, until the flavor is a little less harsh (though it should still be very strong and pungent). Keep refrigerated in an airtight container, up to 3 weeks.',
            self.harvester_class.instructions()
        )
