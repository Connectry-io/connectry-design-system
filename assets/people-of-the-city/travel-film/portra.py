#!/usr/bin/env python3
"""Portra pass: gives clean generated plates the nostalgic film look of the original People of the City stills.

Targets were measured from the originals (a05, e_l06, l01, e_a13, NY01 cab): blacks lifted to about 12,
highlights rolled under 245, warm shadows (red minus blue about +15), richer mid saturation, softer
micro detail, and coarse clumped grain. New plates measured near-black shadows, cool shadow cast,
low saturation at night and digital crispness, which is what read as "polished".
"""
import sys, numpy as np, cv2

def portra(img, seed=11, strength=1.0):
    im = img.astype(np.float32) / 255.0
    h, w = im.shape[:2]; k = w / 2048.0

    # Softer micro detail: film never resolves like a digital sensor.
    im = cv2.GaussianBlur(im, (0, 0), 0.7 * k)

    # Tone: lift and warm the blacks, roll the highlights, gentle mid contrast.
    b, g, r = im[..., 0], im[..., 1], im[..., 2]
    def curve(x, lift, top):
        x = lift + (top - lift) * x
        return x + 0.06 * np.sin(np.pi * (x - 0.5)) * (1 - np.abs(2 * x - 1))  # soft S in the mids only
    r = curve(r, 0.060, 0.970); g = curve(g, 0.054, 0.962); b = curve(b, 0.046, 0.940)
    im = np.stack([b, g, r], -1)

    # Warm shadows, creamy highlights: the Portra cast.
    lum = im.mean(2, keepdims=True)
    sh = np.clip(1 - lum / 0.45, 0, 1); hi = np.clip((lum - 0.6) / 0.4, 0, 1)
    im = (im + sh * np.array([-0.010, 0.002, 0.014]) + hi * np.array([-0.025, 0.000, 0.012])).astype(np.float32)

    # Richer mid colour, kept off the highlights so skin does not turn orange.
    hsv = cv2.cvtColor(np.clip(im, 0, 1).astype(np.float32), cv2.COLOR_BGR2HSV)
    mid = np.clip(1 - np.abs(hsv[..., 2] - 0.5) * 1.6, 0.35, 1)
    hsv[..., 1] = np.clip(hsv[..., 1] * (1 + 0.28 * mid * strength * (1 - hsv[..., 1]) ** 1.5), 0, 1)
    im = cv2.cvtColor(hsv.astype(np.float32), cv2.COLOR_HSV2BGR)

    # A touch of haze: old lenses and film bloom softly around light.
    im = (im * 0.88 + cv2.GaussianBlur(im, (0, 0), 6 * k) * 0.12).astype(np.float32)

    # Halation: bright sources bleed a warm red-orange glow.
    lumf = im.mean(2)
    hot = np.clip((lumf - 0.78) / 0.22, 0, 1)
    glow = cv2.GaussianBlur(hot, (0, 0), 14 * k)[..., None] * np.array([0.02, 0.10, 0.22])
    im = im + glow * strength

    # Gentle vignette.
    yy, xx = np.mgrid[0:h, 0:w].astype(np.float32)
    d = ((xx / w - 0.5) ** 2 + (yy / h - 0.5) ** 2) / 0.5
    im = (im * (1 - 0.09 * d[..., None] * strength)).astype(np.float32)

    # Clumped film grain, strongest in the mids, a little colour in it.
    rng = np.random.default_rng(seed)
    n = rng.normal(0, 1, (h, w)).astype(np.float32)
    n = cv2.GaussianBlur(n, (0, 0), 0.75 * k); n /= n.std() + 1e-6
    nc = cv2.GaussianBlur(rng.normal(0, 1, (h, w, 3)).astype(np.float32), (0, 0), 1.4 * k); nc /= nc.std() + 1e-6
    lumf = im.mean(2, keepdims=True)
    amp = (0.008 + 0.010 * (1 - np.abs(lumf - 0.45) * 1.8).clip(0, 1)) * strength
    im = im + n[..., None] * amp + nc * amp * 0.15

    return (np.clip(im, 0, 1) * 255).astype(np.uint8)

if __name__ == "__main__":
    src, out = sys.argv[1], sys.argv[2]
    cv2.imwrite(out, portra(cv2.imread(src)), [cv2.IMWRITE_JPEG_QUALITY, 95])
