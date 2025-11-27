from pydub import AudioSegment
import os
import subprocess

class Converter:
    def __init__(self):
        pass

    def to_wav(self, input_file, output_folder):
        try:
            # Construct output path
            input_filename = os.path.basename(input_file)
            output_file = os.path.join(output_folder, f"{os.path.splitext(input_filename)[0]}.wav")
            
            # Construct ffmpeg command
            command = [
                'ffmpeg',
                '-i', input_file,
                '-ar', '8000',   # Sample rate
                '-ac', '1',      # Number of audio channels
                '-c:a', 'pcm_mulaw',
                output_file
            ]
            
            # Run ffmpeg command
            subprocess.run(command, check=True)

        except subprocess.CalledProcessError as e:
            print(f"[WARNING] Error converting file: {e}")

    def is_formated(self, file_path):
        try:
            audio_info = self.audio_info(file_path)
            
            # Define required specifications
            required_specs = {
                'duration_seconds': None,  # You can set a duration check if needed
                'channels': 1,
                'frame_rate': 8000
            }
            
            # Check if audio matches the specifications
            if (audio_info['channels'] == required_specs['channels'] and
                    audio_info['frame_rate'] == required_specs['frame_rate']):
                return True
            return False
        
        except Exception as e:
            print(f"[WARNING] {e}")

    def print_audio_format(self, file_path):
        try:
            audio = AudioSegment.from_file(file_path)
            audio_info = {
                'file_name': os.path.basename(file_path),
                'duration_seconds': len(audio) / 1000.0,
                'channels': audio.channels,
                'frame_rate': audio.frame_rate,
                'sample_width': audio.sample_width * 8  # Convert bytes to bits
            }
            print(f"File: {audio_info['file_name']}")
            print(f"  Duration: {audio_info['duration_seconds']} seconds")
            print(f"  Channels: {audio_info['channels']}")
            print(f"  Frame Rate: {audio_info['frame_rate']} Hz")
            print(f"  Sample Width: {audio_info['sample_width']}-bit")
        except Exception as e:
            print(f"[ERROR] Could not read file {file_path}: {e}")

    def execute(self, file_list, output_folder):
        for file_path in file_list:
            try:
                # Check if the audio needs conversion
                if not self.is_formated(file_path):
                    self.to_wav(file_path, output_folder)
                    print(f"Converted: {file_path}")
                else:
                    print(f"Already formatted: {os.path.basename(file_path)}")
            except Exception as e:
                print(f"[WARNING] {e}")