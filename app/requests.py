import urllib.request
import json
import datetime
from datetime import timedelta


# Getting api key
from app import models
from config import Config

api_key = None
# Getting the movie base url
top_headlines_base_url = ""
news_sources_list = {}


def configure_request():
    global api_key, top_headlines_base_url, news_sources_list, everything_base_url
    api_key = Config.API_KEY
    top_headlines_base_url = Config.NEWS_API_TOP_HEADLINES_BASE_URL
    everything_base_url = Config.NEWS_API_EVERYTHING_BASE_URL
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


def process_results(news_results_list, custom_url):
    """
    Function  that processes the movie result and transform them to a list of Objects
    Args:
        news_results_list: A list of dictionaries that contain movie details
    Returns :
        movie_results: A list of movie objects
    """
    news_results = []
    for news_item in news_results_list:
        title = news_item.get('title')
        description = news_item.get("description")
        url = news_item.get("url")
        url_to_img = news_item.get("urlToImage")
        author = news_item.get("author")
        content = news_item.get("content")
        published_at = news_item.get("publishedAt")
        source = news_item['source'].get("name")
        if author is None:
            author = "Anonymous"

        if url:
            publish_date = published_at.split("T")[0]
            date_fields = publish_date.split("-")
            news_publish_date = datetime.date(int(date_fields[0]), int(date_fields[1]), int(date_fields[2]))
            news_publish_date.strftime("%b %d %Y")

            format_content = content
            if content is not None:
                format_content = content.split("[")[0]

            news_obj = models.newsArticle(description=description, source=source, author=author, title=title, url=url,
                                          url_to_image=url_to_img, published_at=news_publish_date,
                                          content=format_content, custom_url=custom_url)
            news_results.append(news_obj)

    return news_results


def get_news_from_src(src_id):
    if top_headlines_base_url != "":
        src = "sources="+src_id
        # the line below will format url and replace the curly braces with the category and the api_key resp.
        custom_src_url = top_headlines_base_url.format(src, api_key)

        # we're using the with as our context manager to send a request using urllib.request.urlopen()
        with urllib.request.urlopen(custom_src_url) as url:
            #  we use the url.read() fun to read the response and store it in the var get_movies_data
            get_news_data = url.read()

            get_news_response = json.loads(get_news_data)

            news_results = None

            if get_news_response["articles"]:
                news_results_list = get_news_response["articles"]
                news_results = process_results(news_results_list, custom_src_url)

    return news_results


def get_news_from_everything(query):
    if everything_base_url != "":

        # the line below will format url and replace the curly braces with the category and the api_key resp.
        custom_src_url = everything_base_url.format(query, api_key)

        # we're using the with as our context manager to send a request using urllib.request.urlopen()
        with urllib.request.urlopen(custom_src_url) as url:
            #  we use the url.read() fun to read the response and store it in the var get_movies_data
            get_news_data = url.read()

            get_news_response = json.loads(get_news_data)

            news_results = None

            if get_news_response["articles"]:
                news_results_list = get_news_response["articles"]
                news_results = process_results(news_results_list, custom_src_url)

    return news_results
