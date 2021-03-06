from .models import *


class UserAPI:
    @staticmethod
    def get(primary_key):
        try:
            the_user = User.objects.get(pk=primary_key)
        except(KeyError, User.DoesNotExist):
            return None
        else:
            return the_user

    @staticmethod
    def put(username, email, name, password):
        u = User(username=username, email=email, name=name, password=password)
        u.save()
        return u


class SurveyAPI:
    @staticmethod
    def get(primary_key):
        try:
            the_survey = Survey.objects.get(pk=primary_key)
        except(KeyError, Survey.DoesNotExist):
            return None
        else:
            return the_survey

    @staticmethod
    def put(date, questions, answer, sentiment, survey_id, u_username, a_username):
        s = Survey(date=date, questions=questions, answer=answer, sentiment=sentiment, survey_id=survey_id, u_username=(UserAPI.get(u_username)), a_username=(AnalystAPI.get(a_username)))
        s.save()
        return s


class StockAnalysisAPI:
    @staticmethod
    def get(primary_key):
        try:
            sa = Stock_Analysis.objects.get(pk=primary_key)
        except(KeyError, Stock_Analysis.DoesNotExist):
            return None
        else:
            return sa

    @staticmethod
    def put(title, username, ticker):
        s = Survey(title=(AnalysisAPI.get(title)), username=(AnalystAPI.get(username)), ticker=(StockAPI.get(ticker)))
        s.save()
        return s


class AnalysisAPI:
    @staticmethod
    def get(primary_key):
        try:
            a = Analysis.objects.get(pk=primary_key)
        except(KeyError, Analysis.DoesNotExist):
            return None
        else:
            return a

    @staticmethod
    def put(description, date, title, username):
        a = Analysis(description=description, date=date, title=title, username=(AnalystAPI.get(username)))
        a.save()
        return a


class AnalystAPI:
    @staticmethod
    def get(primary_key):
        try:
            a = Analyst.objects.get(pk=primary_key)
        except(KeyError, Analyst.DoesNotExist):
            return None
        else:
            return a

    @staticmethod
    def put(username, email, name, password):
        s = Analyst(username=username, email=email, name=name, password=password)
        s.save()
        return s


class WatchlistEntryAPI:
    @staticmethod
    def get(ticker, user):
        try:
            we = Watchlist_Entry.objects.get(ticker=ticker, username=user)
        except(KeyError, Watchlist_Entry.DoesNotExist):
            return None
        else:
            return we

    @staticmethod
    def put(username, ticker):
        we = Watchlist_Entry(username=(UserAPI.get(username)), ticker=(StockAPI.get(ticker)))
        we.save()
        return we

    @staticmethod
    def get_for_user(user):
        we = Watchlist_Entry.objects.filter(username=user)
        return we


class ViewedHistoryAPI:
    @staticmethod
    def remove(vh):
        vh.delete()

    @staticmethod
    def put(date_viewed, username, ticker):
        vh = Viewed_History(date_viewed=date_viewed, username=(UserAPI.get(username)), ticker=(StockAPI.get(ticker)))
        vh.save()
        return vh

    @staticmethod
    def get_user_history(username):
        try:
            vh = Viewed_History.objects.filter(username=username).order_by('-date_viewed')
        except(KeyError, Viewed_History.DoesNotExist):
            return None
        else:
            return vh


class ExchangeAPI:
    @staticmethod
    def get(exchange_id):
        try:
            e = Exchange.objects.get(exchange_id=exchange_id)
            return e
        except(KeyError, Exchange.DoesNotExist):
            return None

    @staticmethod
    def put(exchange_timezone, exchange_id):
        e = Exchange(exchange_timezone=exchange_timezone, exchange_id=exchange_id)
        e.save()
        return e


class StockAPI:
    @staticmethod
    def get(primary_key):
        try:
            the_stock = Stock.objects.get(pk=primary_key)
        except(KeyError, Stock.DoesNotExist):
            return None
        else:
            return the_stock

    @staticmethod
    def put(name, current_value, ticker, ex_dividend_date, dividend_amount, exchange_id):
        s = Stock(name=name, current_value=current_value, ticker=ticker, ex_dividend_date=ex_dividend_date,
                  dividend_amount=dividend_amount, exchange_id=ExchangeAPI.get(exchange_id))
        s.save()
        return s

    @staticmethod
    def update_price(stock, price):
        stock.current_value = price
        stock.save()
        return stock


class PutAPI:
    @staticmethod
    def get(expiry_date, strike_price, ticker):
        try:
            the_put = Put.objects.get(expiry_date=expiry_date, strike_price=strike_price, ticker=ticker)
        except(KeyError, Put.DoesNotExist):
            return None
        else:
            return the_put

    @staticmethod
    def put(expiry_date, strike_price, bid, ask, premium, ticker):
        p = Put(expiry_date=expiry_date, strike_price=strike_price, bid=bid, ask=ask, premium=premium,
                ticker=StockAPI.get(ticker))
        p.save()
        return p

    @staticmethod
    def get_expiring_on(ticker, date):
        p = Put.objects.filter(ticker=ticker, expiry_date=date)
        if p.count() == 0:
            return None
        else:
            return p

    @staticmethod
    def update_updatable(put, bid, ask, premium):
        put.bid = bid
        put.ask = ask
        put.premium = premium
        put.save()
        return put


class CallAPI:
    @staticmethod
    def get(expiry_date, strike_price, ticker):
        try:
            the_call = Call.objects.get(expiry_date=expiry_date, strike_price=strike_price, ticker=ticker)
        except(KeyError, Call.DoesNotExist):
            return None
        else:
            return the_call

    @staticmethod
    def put(expiry_date, strike_price, bid, ask, premium, ticker):
        c = Call(expiry_date = expiry_date, strike_price = strike_price, bid = bid, ask = ask, premium = premium, ticker= StockAPI.get(ticker))
        c.save()
        return c

    @staticmethod
    def get_expiring_on(ticker, date):
        c = Call.objects.filter(ticker=ticker, expiry_date=date)
        if c.count() == 0:
            return None
        else:
            return c

    @staticmethod
    def update_updatable(call, bid, ask, premium):
        call.bid = bid
        call.ask = ask
        call.premium = premium
        call.save()
        return call


class ValueHistoryAPI:
    @staticmethod
    def get(ticker, date):
        try:
            vh = Value_History.objects.get(ticker=ticker, date=date)
            return vh
        except(KeyError, Value_History.DoesNotExist):
            return None

    @staticmethod
    def put(date, value, ticker):
        vh = Value_History(date=date, value=value, ticker=StockAPI.get(ticker))
        vh.save()
        return vh

    @staticmethod
    def all_for_ticker(ticker):
        vh_list = Value_History.objects.filter(ticker=ticker).order_by('date')
        if vh_list.count == 0:
            return None
        else:
            return vh_list


class Histogram_EntryAPI:
    @staticmethod
    def get(id):
        try:
            he = Histogram_Entry.objects.get(id=id)
            return he
        except(KeyError, Histogram_Entry.DoesNotExist):
            return None

    @staticmethod
    def put(value, the_id):
        h = Histogram_Entry(value=value, id=the_id)
        h.save()
        return h

