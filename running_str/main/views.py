from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from django.http import FileResponse
from tempfile import NamedTemporaryFile
from .forms import RunningStrForm
import ffmpeg
import os
import uuid



def index(request):
    if request.method == "POST":
    
        form = RunningStrForm(request.POST)
        
        if form.is_valid():

            text = form.cleaned_data['text']
            background_color = form.cleaned_data['background_color']
            fontcolor=form.cleaned_data['text_color']

            video_file_path = generate_video_stream(text, background_color, fontcolor)

            user_request = form.save(commit=False)
            user_request.video_file = video_file_path
            user_request.save()

            return render(request, "index.html", {'form': form, 'filename': f'media/{video_file_path}'})
    else:
        form = RunningStrForm()
    return render(request, 'index.html', {'form': form})

def generate_video_stream(text, background_color, fontcolor):
    width = 100
    height = 100
    duration = 3
    try:
        filename = str(uuid.uuid4()) + '.mp4'
        file_path = os.path.join('C:\\Users\\pletn\\VSCodeProjects\\running_str\\running_str\\main\\static\\media', filename)
        input = ffmpeg.input(f'color=c={background_color}:s={width}x{height}:d={duration}', f='lavfi')
        input_with_text = input.drawtext(text=text, fontcolor=fontcolor, y=(height-10)/2, x=f"-1*(tw-{width}+10)*t/{duration}", fontsize=20)
        out = ffmpeg.output(input_with_text, file_path).overwrite_output()
        ffmpeg.run(out, capture_stdout=True, capture_stderr=True)  
        return filename
    except Exception as e:
        print(f"An error occurred: {e.stderr}")
        return None