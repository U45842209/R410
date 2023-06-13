from fastapi import FastAPI
app = FastAPI()

@app.get("/")
async def root():
	return {"message":"Hello racine"}

@app.get("/world")
async def root():
	return {"message":"Hello World"}
