# Gradient computation for grayscale/color Canny edge detection
# Author: Muhammet Bastan, mubastan@gmail.com
# Updated: April 2025

import numpy as np
from scipy.ndimage import sobel, prewitt, gaussian_filter

def gradient(image: np.ndarray, type: int = 0):
    """
    Compute the gradient using Sobel or Prewitt operators.

    Args:
        image (np.ndarray): Input image (grayscale or single channel).
        type (int): Gradient type, 0 for Sobel, 1 for Prewitt.

    Returns:
        Tuple[np.ndarray, np.ndarray]: Gradients along x and y directions.
    """
    if type == 0:
        Ix = sobel(image, axis=1)
        Iy = sobel(image, axis=0)
    else:
        Ix = prewitt(image, axis=1)
        Iy = prewitt(image, axis=0)
    return Ix, Iy

def gray_gradient(image: np.ndarray):
    """
    Compute gradient magnitudes and directions for a grayscale image.

    Args:
        image (np.ndarray): Input grayscale image.

    Returns:
        Tuple[np.ndarray, np.ndarray]: Gradient magnitudes and directions.
    """
    Gx, Gy = gradient(image)
    Gm = np.sqrt(Gx**2 + Gy**2)
    Gd = np.arctan2(Gy, Gx)
    Gd[Gd > 0.5 * np.pi] -= np.pi
    Gd[Gd < -0.5 * np.pi] += np.pi
    return Gm, Gd

def gray_gradient_tensor(image: np.ndarray, sigma: float = 0.5):
    """
    Compute gradient tensor for a grayscale image.

    Args:
        image (np.ndarray): Input grayscale image.
        sigma (float): Smoothing parameter for Gaussian filter.

    Returns:
        Tuple[np.ndarray, np.ndarray]: Gradient magnitudes and directions.
    """
    g = image.astype('float32')
    gx, gy = gradient(g)
    cxx = gaussian_filter(gx * gx, sigma)
    cyy = gaussian_filter(gy * gy, sigma)
    cxy = gaussian_filter(2 * (gx * gy), sigma)

    cxx_cyy = cxx - cyy
    eps = 1e-7
    d = np.sqrt(cxx_cyy**2 + cxy**2 + eps)

    lambda1 = cxx + cyy + d
    Gm = np.sqrt(lambda1 + eps)
    Gd = 0.5 * np.arctan2(cxy, cxx_cyy)
    return Gm, Gd

def multi_gradient(imgs: list, gtype: int = 0, sigma: float = 0.5):
    """
    Compute color gradient using multiple single-channel images.

    Args:
        imgs (list): List of single-channel images.
        gtype (int): Gradient type, 0 for color tensor, 1 for max gradient.
        sigma (float): Smoothing parameter for Gaussian filter.

    Returns:
        Tuple[np.ndarray, np.ndarray]: Gradient magnitudes and directions.
    """
    if gtype == 1:
        return multi_gradient_max(imgs)

    N = len(imgs)
    gx, gy = gradient(imgs[0])
    cxx, cyy, cxy = gx * gx, gy * gy, gx * gy

    for i in range(1, N):
        gx, gy = gradient(imgs[i])
        cxx += gx * gx
        cyy += gy * gy
        cxy += gx * gy
    cxy = 2 * cxy

    cxx = gaussian_filter(cxx, sigma)
    cyy = gaussian_filter(cyy, sigma)
    cxy = gaussian_filter(cxy, sigma)

    cxx_cyy = cxx - cyy
    eps = 1e-9
    d = np.sqrt(cxx_cyy**2 + cxy**2 + eps)

    lambda1 = cxx + cyy + d
    Gm = np.sqrt(lambda1 + eps)
    Gd = 0.5 * np.arctan2(cxy, cxx_cyy)
    return Gm, Gd

def multi_gradient_max(imgs: list):
    """
    Compute maximum gradient for each pixel across channels.

    Args:
        imgs (list): List of single-channel images.

    Returns:
        Tuple[np.ndarray, np.ndarray]: Gradient magnitudes and directions.
    """
    Gm, Gd = gray_gradient(imgs[0])
    for img in imgs[1:]:
        Gm2, Gd2 = gray_gradient(img)
        mask = Gm2 > Gm
        Gm[mask] = Gm2[mask]
        Gd[mask] = Gd2[mask]
    return Gm, Gd

def rgb_gradient(image: np.ndarray, gtype: int = 0, sigma: float = 0.5):
    """
    Compute gradient from an RGB image.

    Args:
        image (np.ndarray): Input RGB image.
        gtype (int): Gradient type, 0 for color tensor, 1 for max gradient.
        sigma (float): Smoothing parameter for Gaussian filter.

    Returns:
        Tuple[np.ndarray, np.ndarray]: Gradient magnitudes and directions.
    """
    r, g, b = image[:, :, 0].astype('float32'), image[:, :, 1].astype('float32'), image[:, :, 2].astype('float32')
    imgs = [r, g, b]
    return multi_gradient(imgs, gtype, sigma) if gtype == 0 else multi_gradient_max(imgs)
