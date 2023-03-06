import os
import json
from channel import Channel
from video import Video, PLVideo
from googleapiclient.discovery import build


video1 = Video('9lO06Zxhu88')
print(video1)

video2 = PLVideo('BBotskuyw_M', 'PL7Ntiz7eTKwrqmApjln9u4ItzhDLRtPuD')
print(video2)
