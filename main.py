from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
 
app = FastAPI()

# Define our static folder, where will be our svelte build later
app.mount("/assets", StaticFiles(directory="public/assets"), name="static")

# Simply the root will return our Svelte build
@app.get("/", response_class=FileResponse)
async def main():
    return "public/index.html"
