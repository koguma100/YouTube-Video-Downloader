from flask import Flask, render_template, request
from pytube import Search
import os
# import random
app = Flask(  # Create a flask app
  __name__,
  template_folder='templates',  # Name of html file folder
  static_folder='static'  # Name of directory for static files
)
videos = os.listdir('videos/')

@app.route('/')  # What happens when the user visits the site
def index_page():
  return render_template('index.html', videos=videos)


@app.route('/download', methods=['POST'])
def parse():
  submission = request.get_json()["title"]
  search = Search(submission)
  video = search.results[0].streams.filter(file_extension="mp4").first()
  video.download('videos/')
  if len(videos) >= 3:
    os.remove(videos[0])
    videos.pop(0)
  videos.append(video.title + ".mp4")
  print(videos)
  return videos
  

if __name__ == "__main__":  # Makes sure this is the main process
  app.run(  # Starts the site
    host='0.0.0.0',  # EStablishes the host, required for repl to detect the site
    port=8080)
