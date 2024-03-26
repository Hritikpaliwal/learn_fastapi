from fastapi import FastAPI

#initializes api
app = FastAPI()

# Creating an end point (can say pages)
@app.get("/")
def home():
    return {"Data": "Testing"}

#creating another endpoint
@app.get("/about")
def about():
    return {"Data":"about"}