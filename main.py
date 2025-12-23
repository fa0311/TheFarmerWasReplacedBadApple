import glob

import cv2

frame_files = sorted(glob.glob("frames/frame_*.png"))
frames = []
for frame_file in frame_files:
    img = cv2.imread(frame_file, cv2.IMREAD_GRAYSCALE)
    _, binary = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    frames.append((binary // 255).tolist())

flat = [x for frame in frames for row in frame for x in row]

rle = []
v, c = flat[0], 1
for x in flat[1:]:
    if x == v:
        c += 1
    else:
        rle.append([v, c])
        v, c = x, 1
rle.append([v, c])

counts = []
for v, c in rle:
    counts.append(c)

with open("frames.py", 'w') as f:
    f.write('D=[\n')
    for i in range(0, len(counts), 100):
        chunk = counts[i:i+100]
        f.write(str(chunk)[1:-1] + ',\n')
    f.write(']\n')
    f.write('def d():\n')
    f.write(' r=[]\n')
    f.write(' for i in range(len(D)):\n')
    f.write('  v=i%2==1\n')
    f.write('  for _ in range(D[i]):\n')
    f.write('   r.append(v)\n')
    f.write(' return r\n')

total_size = sum(len(str(c)) + 1 for c in counts)
