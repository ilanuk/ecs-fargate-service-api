from fastapi import FastAPI

app = FastAPI(
    title='My API',
    description='A minimal API to use as a starting point')


@app.get('/health-check')
def healthcheck():
    return {'healthy': 'true'}


@app.get('/valuation')
def valuation():
    return {'price': 100.0}
