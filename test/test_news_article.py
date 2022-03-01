import unittest

from app.models import newsArticle


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here


    def setUp(self) -> None:
        """
        Set up method that will run before every Test
        """
        self.new_article = newsArticle(description="description", source="source", author="author", title="title",
                                     url="www.url.com", url_to_image="url_to_img", published_at="news_publish_date",
                                     content="format_content", custom_url="custom_url")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article, newsArticle))

if __name__ == '__main__':
    unittest.main()
