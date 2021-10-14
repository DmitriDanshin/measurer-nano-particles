from scipy.spatial.distance import euclidean
from imutils import perspective
from imutils import contours
import numpy as np
import imutils
import cv2


def handle_image(
        img_path="images/rm.png",
        gaussian_accuracy: int = 25,
        blur_accuracy: int = 60,
        size_accuracy: int = 19,
        particles_size_nm: int = 200,
        show_border: bool = False,
        show_size: bool = True,
        show_contours: bool = False,
):
    # Чтение фотографии
    image = cv2.imread(img_path)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (gaussian_accuracy, 9), 0)

    edged = cv2.Canny(blur, blur_accuracy, 6)
    edged = cv2.dilate(edged, None, iterations=1)
    edged = cv2.erode(edged, None, iterations=1)

    # Поиск контуров
    cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)

    (cnts, _) = contours.sort_contours(cnts)

    # Удаление слишком больших контуров (точность)
    cnts = [x for x in cnts if cv2.contourArea(x) > size_accuracy]

    # рисование границ
    if show_border:
        cv2.drawContours(image, cnts, -1, (0, 255, 0), 3)

    amount = (len(cnts))

    # Разрешение фото
    ref_object = cnts[0]
    box = cv2.minAreaRect(ref_object)
    box = cv2.boxPoints(box)
    box = np.array(box, dtype="int")
    box = perspective.order_points(box)
    (tl, tr, br, bl) = box
    dist_in_pixel = euclidean(tl, tr)
    dist_in_nm = particles_size_nm
    pixel_per_cm = dist_in_pixel / dist_in_nm

    # Рисование квадратов и надписей
    for cnt in cnts:
        box = cv2.minAreaRect(cnt)
        box = cv2.boxPoints(box)
        box = np.array(box, dtype="int")
        box = perspective.order_points(box)
        (tl, tr, br, bl) = box
        if show_contours:
            cv2.drawContours(image, [box.astype("int")], -1, (0, 0, 255), 0)

        mid_pt_horizontal = (tl[0] + int(abs(tr[0] - tl[0]) / 2), tl[1] + int(abs(tr[1] - tl[1]) / 2))
        mid_pt_vertical = (tr[0] + int(abs(tr[0] - br[0]) / 2), tr[1] + int(abs(tr[1] - br[1]) / 2))
        wid = euclidean(tl, tr) / pixel_per_cm
        ht = euclidean(tr, br) / pixel_per_cm
        if show_size:
            cv2.putText(image, "{:.1f}nm".format(wid), (int(mid_pt_horizontal[0] - 15), int(mid_pt_horizontal[1] - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 0), 2)
            cv2.putText(image, "{:.1f}nm".format(ht), (int(mid_pt_vertical[0] + 10), int(mid_pt_vertical[1])),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 0), 2)

    return image, amount
