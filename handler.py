import math

from scipy.spatial.distance import euclidean
from imutils import perspective
from imutils import contours as cnts
import numpy as np
import imutils
import cv2
import statistics


def find_contours(edged, size_accuracy):
    contours = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = imutils.grab_contours(contours)

    (contours, _) = cnts.sort_contours(contours)

    contours = [x for x in contours if cv2.contourArea(x) > size_accuracy]

    return contours


def get_scale(ref_object, particles_size_nm):
    box = cv2.minAreaRect(ref_object)
    box = cv2.boxPoints(box)
    box = np.array(box, dtype="int")
    box = perspective.order_points(box)
    (tl, tr, br, bl) = box
    dist_in_pixel = euclidean(tl, tr)
    dist_in_nm = particles_size_nm
    pixel_per_nm = dist_in_pixel / dist_in_nm

    return dist_in_pixel, dist_in_nm, pixel_per_nm


def get_statistics(sizes):
    max_particle_size = max(sizes)
    min_particle_size = min(sizes)

    mean = statistics.mean(sizes)
    mean = math.ceil(mean * 100) / 100

    median = statistics.median(sizes)
    sizes.sort()

    return max_particle_size, min_particle_size, mean, median, sizes


def handle_image(
        img_path="images/rm.png",
        gaussian_accuracy: int = 9,
        lower_threshold: int = 50,
        upper_threshold: int = 100,
        size_accuracy: int = 19,
        particles_size_nm: int = 200,
        show_border: bool = False,
        show_size: bool = True,
        show_contours: bool = False,
        canny: bool = False,
        handle: bool = True
):
    # Чтение фотографии
    image = cv2.imread(img_path)

    if not handle:
        return image, 0, 0, 0, [], 0, 0

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (gaussian_accuracy, 9), 0)

    edged = cv2.Canny(blur, lower_threshold, upper_threshold)
    edged = cv2.dilate(edged, None, iterations=1)
    edged = cv2.erode(edged, None, iterations=1)

    # Поиск контуров
    contours = find_contours(edged, size_accuracy)

    # рисование границ
    if show_border:
        cv2.drawContours(image, contours, -1, (0, 255, 0), 3)

    amount = len(contours)

    (dist_in_pixel,
     dist_in_nm, pixel_per_nm) = get_scale(contours[0], particles_size_nm)

    sizes = []

    # Рисование квадратов и надписей
    for cnt in contours:
        box = cv2.minAreaRect(cnt)
        box = cv2.boxPoints(box)
        box = np.array(box, dtype="int")
        box = perspective.order_points(box)
        (tl, tr, br, bl) = box
        if show_contours:
            cv2.drawContours(image, [box.astype("int")], -1, (0, 0, 255), 0)

        mid_pt_horizontal = (tl[0] + int(abs(tr[0] - tl[0]) / 2), tl[1] + int(abs(tr[1] - tl[1]) / 2))
        mid_pt_vertical = (tr[0] + int(abs(tr[0] - br[0]) / 2), tr[1] + int(abs(tr[1] - br[1]) / 2))
        wid = euclidean(tl, tr) / pixel_per_nm
        ht = euclidean(tr, br) / pixel_per_nm

        size = math.floor(math.sqrt(wid ** 2 + ht ** 2))
        sizes.append(size)

        if show_size:
            cv2.putText(image, "{:.1f}nm".format(wid), (int(mid_pt_horizontal[0] - 15), int(mid_pt_horizontal[1] - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (155, 255, 0), 2)
            cv2.putText(image, "{:.1f}nm".format(ht), (int(mid_pt_vertical[0] + 10), int(mid_pt_vertical[1])),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (155, 255, 0), 2)

    max_particle_size, min_particle_size, mean, median, sizes = get_statistics(sizes)

    if canny:
        image = edged
    return (image, amount,
            max_particle_size, min_particle_size,
            sizes, mean, median)
