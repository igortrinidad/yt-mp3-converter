# download_mp3.py
from flask import Blueprint, request, send_file
from pytube import YouTube
from moviepy.editor import VideoFileClip
import time
import os
import logging
from utils.sanitize_filename import sanitize_filename

download_mp3_bp = Blueprint('download_mp3', __name__)

@download_mp3_bp.route('/download', methods=['POST'])
def download_mp3():
  try:

    video_url = request.form['video_url']

    yt = YouTube(video_url)

    video_title = yt.title

    stream = yt.streams.filter(only_audio=True).first()

    timestamp = int(time.time())

    filename_with_timestamp = sanitize_filename(f'{ video_title }_{ timestamp }.mp3')
    
    mp3_path = os.path.join('tmp/mp3', filename_with_timestamp)

    stream.download(output_path='tmp/mp3', filename = filename_with_timestamp)

    file_name_to_download = sanitize_filename(f'{ video_title }.mp3')

    response = send_file(mp3_path, as_attachment=True, download_name = file_name_to_download)

    os.remove(mp3_path)

    return response

  except Exception as e:
      return str(e)