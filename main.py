import os
import json
from channel import Channel
from video import Video, PLVideo
from playlist import PlayList
from googleapiclient.discovery import build

pl = PlayList('PLguYHBi01DWr4bRWc4uaguASmo7lW4GCb')
print(pl.title)
print(pl.url)

duration = pl.total_duration
print(duration)
print(type(duration))
print(duration.total_seconds())
print(pl.show_best_video())

