from picamera2 import Picamera2
from time import sleep
from picamera2.encoders import H264Encoder
from picamera2.outputs import FfmpegOutput

picam2 = Picamera2()

def record_video(output_file, duration):
    # Initialize the Picamera2 instance
    picam2 = Picamera2()

    video_config = picam2.create_video_configuration()
    picam2.configure(video_config)
    encoder = H264Encoder(10000000)
    output = FfmpegOutput(output_file)
    
    # Start recording
    # # picam2.start_recording(encoder, output)
    picam2.start_recording('./images/video.mjpeg', output)
    print("Recording started...")

    sleep(10)  # Record for 10 seconds

# Stop recording
picam2.stop_recording()
print("Recording stopped!")