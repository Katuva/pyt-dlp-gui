import asyncio
import json
import os
import subprocess

from Video import VideoDetails


class YtDlpWrapper:
    debug: bool = False

    video: VideoDetails

    def __init__(self, executable_path: str = "yt-dlp.exe") -> None:
        self.executable_path = executable_path

    async def run(self, args):
        process = await asyncio.create_subprocess_exec(
            self.executable_path,
            *args,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
            creationflags=subprocess.CREATE_NO_WINDOW if os.name == "nt" else 0
        )

        stdout, stderr = await process.communicate()

        if process.returncode != 0:
            raise RuntimeError(
                f"yt-dlp process failed with return code {process.returncode} and error message: {stderr.decode()}"
            )

        return stdout.decode()

    async def get_info(self, url: str) -> None:
        result = await self.run(["--dump-json", url])
        j = json.loads(result)

        if self.debug:
            with open("debug.json", "w") as f:
                json.dump(j, f, indent=4)

        video_formats = []
        for f in j["formats"]:
            try:
                if f["vcodec"] != "none":
                    video_formats.append(f)
            except KeyError:
                pass

        audio_formats = []
        for f in j["formats"]:
            try:
                if f["acodec"] != "none":
                    audio_formats.append(f)
            except KeyError:
                pass

        self.video = VideoDetails(
            title=j["title"],
            duration=j["duration_string"],
            description=j["description"],
            thumbnail=j["thumbnail"],
            filename=j["filename"],
            file_extension=j["ext"],
            video_formats=video_formats,
            audio_formats=audio_formats
        )

    async def download(self, url: str, filename: str, video_format: str = "bestvideo+bestaudio") -> None:
        await self.run(["-o", filename, f"-f {video_format}", url])
