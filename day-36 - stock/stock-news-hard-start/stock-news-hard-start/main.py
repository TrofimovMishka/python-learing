from datetime import datetime as dt, timedelta

from twilio.rest import Client

from stock_data import stock_data as stock_demo_data, news_data

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

NEWS_API_KEY = '####'
STOCK_API_KEY = '####'

SMS_VENDOR_SID = '####'
SMS_VENDOR_API_KEY = '####'
SMS_VENDOR_PHONE = '+####'
MY_PHONE = '####'

# STEP 1: Use https://www.alphavantage.co/query
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
# HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two
# prices. e.g. 40 - 20 = -20, but the positive difference is 20.
# HINT 2: Work out the value of 5% of yesterday's closing stock price.
today_ = dt.today().date()
yesterday = today_ - timedelta(days=1)
day_before_yesterday = today_ - timedelta(days=2)


def verify_stock_changes():
    functions = ["TIME_SERIES_INTRADAY", "TIME_SERIES_DAILY", "TIME_SERIES_WEEKLY", "TIME_SERIES_DAILY_ADJUSTED",
                 "TIME_SERIES_WEEKLY_ADJUSTED", "TIME_SERIES_MONTHLY", "TIME_SERIES_MONTHLY_ADJUSTED", "GLOBAL_QUOTE",
                 "SYMBOL_SEARCH", "MARKET_STATUS"]
    stock_params = {
        'function': functions[1],
        'symbol': STOCK,
        'apikey': STOCK_API_KEY,
        'datatype': 'json',
        'interval': '60min',
        'month': '2024-04',
        'outputsize': 'compact'  # full, compact
    }

    # TODO: You can activate request for live data
    # stock_response = requests.get(STOCK_ENDPOINT, stock_params)
    # stock_response.raise_for_status()
    # print(stock_response.json())
    # stock_output = stock_response.json()

    stock_output = stock_demo_data
    DAILY_ = stock_output['Time Series (Daily)']

    close_results = [DAILY_[dat]['4. close'] for dat in DAILY_ if
                     dat.__contains__(str(yesterday)) or dat.__contains__(str(day_before_yesterday))]
    y_close = float(close_results[0])
    dby_close = float(close_results[1])
    percent_of_diff = round((y_close - dby_close) * 100 / y_close, 2)

    if percent_of_diff > 0 and abs(percent_of_diff) >= 2:  # positive grow
        print(f"Grow is positive {percent_of_diff}")
        news = get_news(company=COMPANY_NAME)
        for i in news:
            send_sms(True, STOCK, abs(percent_of_diff), i)

    elif percent_of_diff < 0 and abs(percent_of_diff) >= 2:  # negative
        print(f"Grow is negative {percent_of_diff}")
        news = get_news(company=COMPANY_NAME)
        for i in news:
            send_sms(False, STOCK, abs(percent_of_diff), i)


# STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME. 
# HINT 1: Think about using the Python Slice Operator

def get_news(company: str) -> []:
    news_params = {
        'apiKey': NEWS_API_KEY,
        'q': company,
        'searchIn': 'title,description',  # title, description, content
        'language': 'en',  # ar de en es fr he it nl no pt ru sv ud zh
        'sortBy': 'relevancy',  # relevancy, popularity, publishedAt
        'pageSize': 3,
        'from': day_before_yesterday,
        'to': yesterday
    }
    # TODO: You can activate request for live data
    # news_response = requests.get(NEWS_ENDPOINT, news_params)
    # print(news_response.json())
    # new_output = news_response.json()['articles']
    # if no use pageSize in request, you can limit result by [:3]
    new_output = news_data['articles']

    news_titles = [news['title'] for news in new_output]
    print(news_titles)
    return news_titles


# STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number. 
# HINT 1: Consider using a List Comprehension.

def send_sms(is_grow: bool, stock: str, percent: float, message: str):
    if is_grow:
        msg = f'{stock}:🔺{percent}% \n\nHeadline: {message}'
    else:
        msg = f'{stock}:🔻{percent}% \n\nHeadline: {message}'

    client = Client(SMS_VENDOR_SID, SMS_VENDOR_API_KEY)

    message = client.messages.create(
        from_=SMS_VENDOR_PHONE,
        to=MY_PHONE,
        body=msg
    )

    print(message.sid)


verify_stock_changes()
