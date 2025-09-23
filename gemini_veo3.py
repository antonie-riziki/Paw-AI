import time
from google import genai
from google.genai import types
import os

# client = genai.Client()
client = genai.Client(api_key="AIzaSyC96GyY2XMAKKoJqX318CgcwS3e4EQTh_w")

prompt = f"""

Yeti is holding a selfie stick (that’s where the camera is) walking through a lush Nairobi forest path, early morning light 
filtering through trees, natural movement, slight camera bob as Yeti walks. Speaking directly to camera saying: 
“Eish, hello Nairobi! Ni Yeti wako hapa, kule ndani ya miti — conservation iko calling! Africa’s Talking Women in Tech Hackathon iko 
Wednesday 24th. Huwezi sit back — we Kenyan women, we coders, designers, hustlers — tukuje tuna-build solutions: track wildlife, 
stop poachers, educate the mama na mtoto kwa SMS/USSD. Ni Nairobi matter — fresh air, real change! Let’s hack this thing, tukiungana 
kwa PAW AI.” Forest ambience: birds chirping, leaves rustling. No subtitles, no text overlay.

"""

operation = client.models.generate_videos(
    model="veo-3.0-generate-001",
    prompt=prompt,
)

# Poll the operation status until the video is ready.
while not operation.done:
    print("Waiting for video generation to complete...")
    time.sleep(10)
    operation = client.operations.get(operation)

# Download the generated video.
generated_video = operation.response.generated_videos[0]
client.files.download(file=generated_video.video)
generated_video.video.save("yeti_example.mp4")
print("Generated video saved to yeti_example.mp4")