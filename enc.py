from PIL import Image
import numpy as np


def embed():
    msg = "sneaky script goes here :)"
    size = len(msg)

    w, h = 4000, 4000
    t = (h, w, 3)
    A = np.zeros(t, dtype=np.uint8)

    for i in range(int(h / 8)):
        for j in range(int(w / 8)):
            for c in range(3):
                A[i, j, c] = size

    ch = 0
    while ch < size:
        for bi in range(8):
            for bj in range(8):
                if bi == 0 and bj == 0:
                    continue
                for i in range(int(h / 8) * bi, int(h / 8) * (bi + 1)):
                    for j in range(int(w / 8) * bj, int(w / 8) * (bj + 1)):
                        ch = (bi * 8 + bj - 1) * 3
                        if ch >= size:
                            return A
                        for c in range(3):
                            if ch < size:
                                A[i, j, c] = int.from_bytes(msg[ch].encode(), "big")
                                ch += 1


res = embed()
img = Image.fromarray(res, "RGB")
img.save("img.png")