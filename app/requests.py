import app


# Getting api key
from app import models
from config import Config

api_key = None
# Getting the movie base url
base_url = None
news_sources_list = {}


def configure_request():
    global api_key, base_url, news_sources_list
    api_key = Config.API_KEY
    base_url = Config.NEWS_API_BASE_URL
    news_sources_list = Config.NEWS_SOURCES_ARRAY


def get_news_sources_list():
    the_list = []
    if news_sources_list is not None:
        for agency in news_sources_list:
            src_id = agency.get('source_id')
            src_name = agency.get('source_name')
            src_description = agency.get("source_description")
            src_url = agency.get("source_url")
            src_img = agency.get("source_img")

            new_agency = models.newsSource(src_id, src_name, src_img, src_description, src_url)
            the_list.append(new_agency)
        return the_list
    else:
        return None
