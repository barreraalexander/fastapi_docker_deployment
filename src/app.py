from fastapi import FastAPI

app = FastAPI(debug=True, reload=True)

@app.get('/')
def home():
    return 'hello world'