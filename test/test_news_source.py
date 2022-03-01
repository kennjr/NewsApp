import unittest

from app.models import newsSource


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here


    def setUp(self) -> None:
        """
        Set up method that will run before every Test
        """
        self.new_article = newsSource(source_id="the id", source_img="imageurl", source_url="www.apnews.com",
                                      source_name="AP", source_description="a news agency")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article, newsSource))

if __name__ == '__main__':
    unittest.main()
