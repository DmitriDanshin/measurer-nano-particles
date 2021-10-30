import math
import numpy as np
import imutils
import cv2
from scipy.spatial.distance import euclidean
from imutils import perspective
from imutils import contours as cnts
from schemas.image import ImageCreate, ImageData
from utils.get_statistics import get_statistics
from utils.to_base64 import to_base64


def apply_canny(image, params):
    """Применить оператор Кэнни"""
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (params.gaussian_accuracy, 9), 0)
    edged = cv2.Canny(blur, params.lower_threshold, params.upper_threshold)
    edged = cv2.dilate(edged, None, iterations=1)
    edged = cv2.erode(edged, None, iterations=1)
    return edged


def find_contours(edged, size_accuracy):
    """Поиск контуров"""
    contours = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = imutils.grab_contours(contours)
    (contours, _) = cnts.sort_contours(contours)
    contours = [x for x in contours if cv2.contourArea(x) > size_accuracy]

    return contours


def get_scale(ref_object, particles_size_nm):
    """Посчитать масштаб фото"""
    box = cv2.minAreaRect(ref_object)
    box = cv2.boxPoints(box)
    box = np.array(box, dtype="int")
    box = perspective.order_points(box)
    (tl, tr, br, bl) = box
    dist_in_pixel = euclidean(tl, tr)
    dist_in_nm = particles_size_nm
    pixel_per_nm = dist_in_pixel / dist_in_nm

    return pixel_per_nm


def draw_data(params, contours, image, scale):
    """ Рисование прямоугольников и надписей"""
    sizes = []
    for cnt in contours:
        box = cv2.minAreaRect(cnt)
        box = cv2.boxPoints(box)
        box = np.array(box, dtype="int")
        box = perspective.order_points(box)
        (tl, tr, br, bl) = box
        if params.show_contours:
            cv2.drawContours(image, [box.astype("int")], -1, (0, 0, 255), 0)

        mid_pt_horizontal = (tl[0] + int(abs(tr[0] - tl[0]) / 2), tl[1] + int(abs(tr[1] - tl[1]) / 2))
        mid_pt_vertical = (tr[0] + int(abs(tr[0] - br[0]) / 2), tr[1] + int(abs(tr[1] - br[1]) / 2))
        wid = euclidean(tl, tr) / scale
        ht = euclidean(tr, br) / scale

        size = math.floor(math.sqrt(wid ** 2 + ht ** 2))
        sizes.append(size)

        if params.show_size:
            cv2.putText(image, "{:.1f}nm".format(wid), (int(mid_pt_horizontal[0] - 15), int(mid_pt_horizontal[1] - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (155, 255, 0), 2)
            cv2.putText(image, "{:.1f}nm".format(ht), (int(mid_pt_vertical[0] + 10), int(mid_pt_vertical[1])),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (155, 255, 0), 2)

        return sizes, image


def handle_image(path="image.png", params: ImageCreate = ImageCreate()):
    # Чтение фотографии
    image = cv2.imread(path)

    # Обработка фото
    if not params.handle:
        image = to_base64()
        return ImageData(image=image)

    edged = apply_canny(image, params)

    # Отображение результата оператора Кэнни на фото
    if params.canny:
        image = edged

    contours = find_contours(edged, params.size_accuracy)

    # Отображение границ на фото
    if params.show_border:
        cv2.drawContours(image, contours, -1, (0, 255, 0), 3)

    scale = get_scale(contours[0], params.particles_size_nm)

    sizes, image = draw_data(params, contours, image, scale)

    cv2.imwrite('image.png', image)
    image = to_base64()

    return ImageData(image=image, **get_statistics(sizes).dict())
