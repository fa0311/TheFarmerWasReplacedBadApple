import os
import time

import frames

pixels = frames.d()
size = 32
frame_count = len(pixels) // (size * size)
fps = 5

print(f"Bad Apple 再生開始 ({frame_count}フレーム, {fps}fps, {size}x{size})")
time.sleep(1)

for f in range(frame_count):
    os.system('cls' if os.name == 'nt' else 'clear')
    
    frame_data = pixels[f*size*size:(f+1)*size*size]
    
    for y in range(size):
        line = ""
        for x in range(size):
            line += "██" if frame_data[y*size+x] else "  "
        print(line)
    
    print(f"\nフレーム: {f+1}/{frame_count}")
    time.sleep(1.0 / fps)

print("\n再生終了")
