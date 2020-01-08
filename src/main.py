from fastapi import FastAPI
from statsd import StatsClient


app = FastAPI(
    title='My API',
    description='A minimal API to use as a starting point')

statsd = StatsClient()


@app.get('/health-check')
def healthcheck():
    return {'healthy': 'true'}


@app.get('/valuation')
@statsd.timer('valuation.time')
def valuation():
    return {'price': 100.0}
