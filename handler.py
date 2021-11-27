import math
import numpy as np
import imutils
import cv2
from scipy.spatial.distance import euclidean
from imutils import perspective
from imutils import contours as cnts
from assets.colors import LIME, CYAN, YELLOW, RED, BLUE, MAGENTA
from schemas.image import ImageCreate, ImageData
from utils.get_statistics import get_statistics
from utils.to_base64 import to_base64
from json import loads


def draw_text(box, scale, image):
    (tl, tr, br, bl) = box
    mid_pt_horizontal = (tl[0] + int(abs(tr[0] - tl[0]) / 2), tl[1] + int(abs(tr[1] - tl[1]) / 2))
    wid, ht = get_scaled_sizes(box, scale)

    size = math.floor(math.hypot(wid, ht))

    cv2.putText(image, "{:.1f}nm".format(size), (int(mid_pt_horizontal[0] - 15), int(mid_pt_horizontal[1] - 10)),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, CYAN, 2)


def get_scaled_sizes(box, scale):
    (tl, tr, br, bl) = box
    wid = euclidean(tl, tr) / scale
    ht = euclidean(tr, br) / scale
    return wid, ht


def apply_user_contours(image, scale, params):
    user_sizes = np.array([])
    user_box_contours = []
    user_contours = loads(params.user_contours[0])
    excluded_contours = loads(params.excluded_contours[0])

    for cnt in user_contours:
        box = np.array(cnt)
        # Удалить ненужный контур
        if box.tolist() in excluded_contours:
            continue

        user_box_contours.append(box.tolist())
        if params.show_contours:
            cv2.drawContours(image, [box.astype("int")], -1, YELLOW, 0)
        if params.show_size:
            draw_text(box, scale, image)
        if params.show_midpoints:
            draw_midpoints(box, image)
        wid, ht = get_scaled_sizes(box, scale)
        size = math.floor(math.hypot(wid, ht))
        user_sizes = np.append(user_sizes, size)
    return user_sizes, user_box_contours


def apply_canny(image, params):
    """Применить оператор Кэнни"""
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (params.gaussian_accuracy_width,
                                   params.gaussian_accuracy_height), 0)
    edged = cv2.Canny(blur, params.lower_threshold, params.upper_threshold)
    edged = cv2.dilate(edged, None, iterations=1)
    edged = cv2.erode(edged, None, iterations=1)
    return edged


def find_contours(edged, size_accuracy):
    """Поиск контуров"""
    contours = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = imutils.grab_contours(contours)
    (contours, _) = cnts.sort_contours(contours)
    return [cnt for cnt in contours if cv2.contourArea(cnt) > size_accuracy]


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


def midpoint(a, b):
    return (a[0] + b[0]) * 0.5, (a[1] + b[1]) * 0.5


def draw_midpoints(box, image):
    """Рисование линий через центр выделенного объекта"""
    (tl, tr, br, bl) = box

    (tltrX, tltrY) = midpoint(tl, tr)
    (blbrX, blbrY) = midpoint(bl, br)

    (tlblX, tlblY) = midpoint(tl, bl)
    (trbrX, trbrY) = midpoint(tr, br)

    cv2.circle(image, (int(tltrX), int(tltrY)), 5, BLUE, -1)
    cv2.circle(image, (int(blbrX), int(blbrY)), 5, BLUE, -1)
    cv2.circle(image, (int(tlblX), int(tlblY)), 5, BLUE, -1)
    cv2.circle(image, (int(trbrX), int(trbrY)), 5, BLUE, -1)

    cv2.line(image, (int(tltrX), int(tltrY)), (int(blbrX), int(blbrY)),
             MAGENTA, 2)
    cv2.line(image, (int(tlblX), int(tlblY)), (int(trbrX), int(trbrY)),
             MAGENTA, 2)


def draw_data(params, contours, image, scale):
    """ Рисование прямоугольников и надписей"""
    sizes = np.array([])
    box_contours = []
    excluded_contours = loads(params.excluded_contours[0])
    for cnt in contours:
        box = cv2.minAreaRect(cnt)
        box = cv2.boxPoints(box)
        box = np.array(box, dtype="int")
        box = perspective.order_points(box)
        box_contours.append(box.tolist())

        if box.tolist() in excluded_contours:
            continue

        # Отображение контуров
        if params.show_contours:
            cv2.drawContours(image, [box.astype("int")], -1, RED, 0)

        # Отображение линий
        if params.show_midpoints:
            draw_midpoints(box, image)

        wid, ht = get_scaled_sizes(box, scale)

        size = math.floor(math.hypot(wid, ht))
        sizes = np.append(sizes, size)

        if params.show_size:
            draw_text(box, scale, image)

    return sizes, box_contours, image


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

    scale = get_scale(contours[0], params.particles_size_nm)
    user_sizes, user_box_contours = apply_user_contours(image, scale, params)
    sizes, box_contours, image = draw_data(params, contours, image, scale)

    box_contours = box_contours + user_box_contours

    # Отображение границ на фото
    if params.show_border:
        cv2.drawContours(image, contours, -1, LIME, 3)

    sizes = np.concatenate((sizes, user_sizes))
    sizes = sizes.tolist()
    cv2.imwrite('image.png', image)
    image = to_base64()

    return ImageData(image=image, **get_statistics(sizes, box_contours).dict())
