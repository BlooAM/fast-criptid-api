from fastapi import FastAPI


app = FastAPI()


@app.get('/')
def top():
    return 'Top here'


@app.get('/echo/{thing}')
def echo(thing):
    return f'printing: {thing}'


if __name__ == '__main__':
    import uvicorn

    uvicorn.run('main:app', reload=True)
