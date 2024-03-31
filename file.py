from flask import Flask, render_template, request
from pytube import YouTube

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    video_url = request.form['video_url']
    try:
        yt = YouTube(video_url)
        stream = yt.streams.get_highest_resolution()
        stream.download()
        message = 'Video downloaded successfully!'
    except Exception as e:
        message = f'Error: {str(e)}'
    return render_template('index.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)
  
