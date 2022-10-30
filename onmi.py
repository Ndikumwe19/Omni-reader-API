from fastapi import FastAPI, Request, File, UploadFile
import requests


app = FastAPI(title="Omni-reader")


#Optical Character Recognition Endpoint
@app.get("/ocr")
def ocr(request: Request):
    return True

#Speech to Text Endpoint
@app.get("/stt")
def stt(request: Request):
    return True

#Text to Speech Endpoint
@app.get("/tts")
def tts(request: Request):
    return True

#Voice Message Endpoint
@app.get("voice-message")
def voice_msg(request: Request):
    return True