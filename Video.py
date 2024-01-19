from dataclasses import dataclass


@dataclass
class VideoDetails:
    title: str
    duration: str
    description: str
    thumbnail: str
    filename: str
    file_extension: str
    video_formats: list
    audio_formats: list
