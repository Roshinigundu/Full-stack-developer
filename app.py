from flask import Flask, request, render_template
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# ... your existing imports ...

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files or 'subtitles' not in request.files:
        return "Both video and subtitles files are required"
    
    video_file = request.files['file']
    subtitles_file = request.files['subtitles']
    font_size = request.form.get('font_size', type=int, default=16)
    font_color = request.form.get('font_color', default='#ffffff')
    
    if video_file.filename == '' or subtitles_file.filename == '':
        return "Please select both video and subtitles files"
    
    video_path = os.path.join(app.config['UPLOAD_FOLDER'], 'video.mp4')
    video_file.save(video_path)
    
    subtitles_path = os.path.join(app.config['UPLOAD_FOLDER'], 'subtitles.vtt')
    subtitles_file.save(subtitles_path)
    
    # Save custom subtitle appearance settings
    with open(subtitles_path, 'a') as f:
        f.write('\n\nSTYLE\n::cue { font-size: ' + str(font_size) + 'px; color: ' + font_color + '; }\n')
    
    return "Files uploaded successfully"

# ... your existing code ...

if __name__ == '__main__':
    app.run(debug=True)

