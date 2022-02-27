from flask import render_template
from app import app


@app.route('/')
def index():
    """Render the index template"""
    return render_template('index.html', title="News App")


@app.route('/news/top-headlines/source/<str:news_src>')
def news_from_src(news_src):
    # todo make an api request for news with the src in the param
    title = f"News - {news_src}"
    return render_template('news_list.html', title=title, news_array="The array with all the news objs")


@app.route('news/top-headlines/country/<str:country>')
def news_from_country(country):
    # todo make an api request for news with the country in the param
    title = f"News - {country}"
    return render_template('news_list.html', title=title, news_array="The array with all the news with the country")


@app.route('news/top-headlines/category/<str:category>')
def news_from_category(category):
    # todo make an api request for news with the category in the param
    title = f"News - {category}"
    return render_template('news_list.html', title=title, news_array="The array with all the news with the category")


@app.route('news/top-headlines/query/<query>')
def news_from_top_headlines_query(query):
    # todo make an api request for news with the query in the param
    title = f"News - {query}"
    return render_template('news_list.html', title=title, news_array="The array with all the news with the query")

