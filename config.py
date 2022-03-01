class Config:
    """The key that we'll pass in our get requests"""
    API_KEY = "a3121d3568944bf782807ac90b13b1f7"
    """This is for the base url that we'll use to make requests to the news api"""
    ADD_API_KEY = "https://newsapi.org/v2/top-headlines?country=us&apiKey=a3121d3568944bf782807ac90b13b1f7"
    NEWS_API_TOP_HEADLINES_BASE_URL = "https://newsapi.org/v2/top-headlines?{}&apiKey={}"
    NEWS_API_EVERYTHING_BASE_URL = "https://newsapi.org/v2/everything?q={}&apiKey={}"
    NEWS_SOURCES_ARRAY = [
        {
            "source_name": "Associated Press",
            "source_img": "https://2.bp.blogspot.com/-sJ8mGd6LmkU/T0ajVykwreI/AAAAAAAAESA/WNOI4QF4lIw/s1600/AP+logo+2012.png",
            "source_id": "associated-press",
            "source_url": "https://apnews.com",
            "source_description": "The Associated Press (AP) is an American non-profit news agency headquartered in New York City. Founded in 1846, it operates as a cooperative, unincorporated association. Its members are U.S. newspapers and broadcasters."
        },
        {
            "source_name": "Reuters",
            "source_img": "https://logodownload.org/wp-content/uploads/2014/05/reuters-logo-0-599x599.png",
            "source_id": "reuters",
            "source_url": "https://www.reuters.com",
            "source_description": "Reuters journalists use the Standards and Values as a guide for fair presentation and disclosure of relevant interests, to maintain the values of integrity and freedom upon which their reputation for reliability, accuracy, speed and exclusivity relies"
        },
        {
            "source_name": "CNN",
            "source_img": "https://download.logo.wine/logo/CNN/CNN-Logo.wine.png",
            "source_id": "cnn",
            "source_url": "https://www.cnn.com",
            "source_description": "The Cable News Network (CNN) is a multinational news-based pay television channel headquartered in Atlanta, United States. The network is known for its dramatic live coverage of breaking news, some of which has drawn criticism as overly sensationalistic."
        },
        {
            "source_name": "Fox News",
            "source_img": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/67/Fox_News_Channel_logo.svg/1200px-Fox_News_Channel_logo.svg.png",
            "source_id": "fox-news",
            "source_url": "https://www.foxnews.com",
            "source_description": "Fox News, and stylized in all caps, is an American multinational conservative cable news television channel based in New York City. The channel broadcasts primarily from studios at 1211 Avenue of the Americas in Midtown Manhattan. Fox News provides service to 86 countries and overseas territories worldwide, with international broadcasts featuring Fox Extra segments during ad breaks."
        },
        {
            "source_name": "BBC News",
            "source_img": "https://download.logo.wine/logo/BBC_News/BBC_News-Logo.wine.png",
            "source_id": "bbc-news",
            "source_url": "https://www.bbc.com/news",
            "source_description": "BBC News is an operational business division of the British Broadcasting Corporation (BBC) responsible for the gathering and broadcasting of news and current affairs. The department is the world's largest broadcast news organisation and generates about 120 hours of radio and television output each day, as well as online news coverage."
        },
        {
            "source_name": "MSNBC",
            "source_img": "https://www.petergeorgescu.com/wp-content/uploads/2019/10/msnbc-logo-png-1920.png",
            "source_id": "msnbc",
            "source_url": "https://www.msnbc.com",
            "source_description": "MSNBC and its website were founded in 1996 under a partnership between Microsoft and General Electric's NBC unit, hence the network's naming. It provides NBC News coverage as well as its own reporting and political commentary on current events."
        },
        {
            "source_name": "ABC News",
            "source_img": "https://i.ya-webdesign.com/images/abc-logo-png-2.png",
            "source_id": "abc-news",
            "source_url": "https://www.abcnews.go.com",
            "source_description": "ABC News is the news division of Walt Disney Television's ABC broadcast network. Its flagship program is the daily evening newscast ABC World News Tonight with David Muir. In addition to the division's television programs, ABC News also has radio and digital outlets, including ABC News Radio and ABC News Live, plus various podcasts hosted by ABC News personalities."
        },
        {
            "source_name": "Politico",
            "source_img": "https://static.politico.com/0e/5b/3cf3e0f04ca58370112ab667c255/politico-logo.png",
            "source_id": "politico",
            "source_url": "https://www.politico.com",
            "source_description": "The Politico, is a political journalism company based in Arlington County, Virginia, that covers politics and policy in the United States and internationally. It primarily distributes content online but also with printed newspapers, radio, and podcasts. Its coverage in Washington, D.C., includes the U.S. Congress, lobbying, the media, and the presidency."
        },
        {
            "source_name": "TechCrunch",
            "source_img": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b9/TechCrunch_logo.svg/1200px-TechCrunch_logo.svg.png",
            "source_id": "techcrunch",
            "source_url": "https://www.techcrunch.com",
            "source_description": "TechCrunch is an American online newspaper focusing on high tech and startup companies. It was founded in June 2005 by Archimedes Ventures, led by partners Michael Arrington and Keith Teare. In addition to its news reporting, TechCrunch is also known for its Disrupt conference, an annual technology event hosted in several cities across United States, Europe, and China."
        },
        {
            "source_name": "VICE News",
            "source_img": "https://i1.wp.com/www.broadbandtvnews.com/wp-content/uploads/2015/07/Vice_Logo.png",
            "source_id": "vice-news",
            "source_url": "https://www.vice.com/en/section/news",
            "source_description": "Vice News is Vice Media's current affairs channel, producing daily documentary essays and video through its website and YouTube channel. It promotes itself on its coverage of under-reported stories Vice News was created in December 2013 and is based in New York City, though it has bureaus worldwide."
        },
        {
            "source_name": "Bloomberg",
            "source_img": "https://logos-download.com/wp-content/uploads/2016/03/Bloomberg_logo_logotype_emblem.png",
            "source_id": "bloomberg",
            "source_url": "https://www.bloomberg.com",
            "source_description": "Bloomberg News (originally Bloomberg Business News) is an international news agency headquartered in New York City and a division of Bloomberg L.P.. Content produced by Bloomberg News is disseminated through Bloomberg Terminals, Bloomberg Television, Bloomberg Radio, Bloomberg Businessweek, Bloomberg Markets, Bloomberg.com, and Bloomberg's mobile platforms."
        },
        {
            "source_name": "The Wall Street Journal",
            "source_img": "https://yt3.ggpht.com/-sH3JAVQUyJw/AAAAAAAAAAI/AAAAAAAAAAA/8s1D-T2B0XI/s900-c-k-no-mo-rj-c0xffffff/photo.jpg",
            "source_id": "the-wall-street-journal",
            "source_url": "https://www.wsj.com",
            "source_description": "The Wall Street Journal, also known as The Journal or WSJ, is an American business-focused, English-language international daily newspaper based in New York City, with international editions also available in Chinese and Japanese. The Journal, along with its Asian editions, is published six days a week by Dow Jones & Company, a division of News Corp. The newspaper is published in the broadsheet format and online. "
        },
        {
            "source_name": "The Washington Post",
            "source_img": "https://logos-download.com/wp-content/uploads/2016/05/The_Washington_Post_logo_newspaper.png",
            "source_id": "the-washington-post",
            "source_url": "https://www.washingtonpost.com",
            "source_description": "The Washington Post (also known as the Post and, informally, WaPo) is an American daily newspaper published in Washington, D.C. It is the most-widely circulated newspaper within the Washington metropolitan area and has a large national audience. Daily broadsheet editions are printed for D.C., Maryland, and Virginia. The paper is well known for its political reporting and is one of the few remaining American newspapers to operate foreign bureaus."
        }
    ]
    pass


class DevConfig:
    """The development configurations will be in this class"""
    DEBUG = True
    pass


class ProdConfig:
    """The production configurations will be in this class"""
    pass
