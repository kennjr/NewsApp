class Config:
    """The key that we'll pass in our get requests"""
    API_KEY = "a3121d3568944bf782807ac90b13b1f7"
    """This is for the base url that we'll use to make requests to the news api"""
    NEWS_API_BASE_URL = "https://newsapi.org/v2"
    ADD_API_KEY = "&apiKey=a3121d3568944bf782807ac90b13b1f7"
    TOP_HEADLINES_URL = NEWS_API_BASE_URL + "/top-headlines?country=us" + ADD_API_KEY
    pass


class DevConfig:
    """The development configurations will be in this class"""
    DEBUG = True
    pass


class ProdConfig:
    """The production configurations will be in this class"""
    pass
