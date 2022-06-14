from PIL import Image
import numpy as np


def extract():
    src = "img.png"
    msg = ""
    img = Image.open(src)
    w = img.size[0]
    h = img.size[1]
    A = np.asarray(img)

    size = A[int(h/16),int(w/16),0]

    ch = 0
    for bi in range(8):
        for bj in range(8):
            if bi == 0 and bj == 0:
                continue
            for c in range(3):
                if ch < size:
                    n = int(A[int(h/16)+int(h/8)*bi, int(w/16)+int(w/8)*bj, c])
                    msg += n.to_bytes(1, 'big').decode('utf-8')
                    ch += 1
                else:
                    return msg


print(extract())