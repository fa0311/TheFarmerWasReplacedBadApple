yt-dlp https://www.youtube.com/watch?v=FtutLA63Cp8 -o output.webm

if (Test-Path "frames") {
    Remove-Item -Recurse -Force "frames"
}
New-Item -ItemType Directory -Force -Path "frames"

ffmpeg -i output.webm -vf "fps=5,scale=32:32:flags=lanczos" frames/frame_%04d.png
