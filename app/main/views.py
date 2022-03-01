from flask import render_template, url_for
from app import app
from app.requests import get_news_sources_list, get_news_from_src, get_news_from_everything
from flask import request as req
from werkzeug.utils import redirect


@app.route('/')
def index():
    """Render the index template"""
    search_movie = req.args.get('search_str')
    if search_movie:
        return redirect(url_for('news_from_everything', query=search_movie))
    else:
        agencies_list = get_news_sources_list()
        return render_template('index.html', title="News App", agencies_list=agencies_list)



@app.route('/news/top-headlines/source/<news_src>')
def news_from_src(news_src):

    title = f"News - {news_src}"
    news_results = get_news_from_src(news_src)
    return render_template('news_list.html', title=title, news_array=news_results)


@app.route('/news/top-headlines/country/<country>')
def news_from_country(country):
    # todo make an api request for news with the country in the param
    title = f"News - {country}"
    return render_template('news_list.html', title=title, news_array="The array with all the news with the country")


@app.route('/news/top-headlines/category/<category>')
def news_from_category(category):
    # todo make an api request for news with the category in the param
    title = f"News - {category}"
    return render_template('news_list.html', title=title, news_array="The array with all the news with the category")


@app.route('/news/top-headlines/query/<query>')
def news_from_top_headlines_query(query):
    # todo make an api request for news with the query in the param
    title = f"News - {query}"
    return render_template('news_list.html', title=title, news_array="The array with all the news with the query")


@app.route('/news/everything/<query>')
def news_from_everything(query):
    news_results = get_news_from_everything(query)
    return render_template('news_list.html', news_array=news_results)
