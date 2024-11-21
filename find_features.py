import os
from DBConnection import Db
import csv
import cv2
import numpy as np
db=Db()
listOfFiles = os.listdir('C:\\Users\\HP\\PycharmProjects\\leukemia project\\static\\ALL_IDB1\\im\\')
listOfFiles1 = os.listdir('C:\\Users\\HP\\PycharmProjects\\leukemia project\\static\\ALL_IDB1\\Others\\')
a=[]
#
properties = ['ASM', 'contrast', 'correlation', 'energy']
# headerlist=properties
# headerlist.append('Label')
# with open('C:\\Users\\HP\\PycharmProjects\\leukemia project\\static\\features.csv', 'w', newline='') as file:
#     writer=csv.writer(file)
#     writer.writerow(headerlist)
#
# for entry in listOfFiles:
#     filename=entry.split(".")[0]
#     label=filename.split("_")[1]
#     image_path = "C:\\Users\\HP\\PycharmProjects\\leukemia project\\static\\ALL_IDB1\\im\\"+entry
#     from PIL import Image
#
#     img = Image.open(image_path).convert('LA')
#     img.save('D:\\greyscale.png')
#
#
#
#     import cv2
#
#     im_gray = cv2.imread('D:\\greyscale.png', cv2.IMREAD_GRAYSCALE)
#     (thresh, im_bw) = cv2.threshold(im_gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
#     cv2.imwrite('C:\\Users\\HP\\PycharmProjects\\leukemia project\\static\\binary.png', im_bw)
#
#
#
#     img = cv2.imread('C:\\Users\\HP\\PycharmProjects\\leukemia project\\static\\binary.png', 0)
#     kernel = np.ones((5, 5), np.uint8)
#
#     opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
#     cv2.imwrite('D:\\opening.png', opening)
#     close = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
#
#     cv2.imwrite('D:\\close.png', close)
#
#     # finding erosion
#     import cv2
#     import numpy as np
#
#     des = cv2.bitwise_not(close)
#     contour, hier = cv2.findContours(des, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
#
#     for cnt in contour:
#         cv2.drawContours(des, [cnt], 0, 255, -1)
#
#     gray = cv2.bitwise_not(des)
#     cv2.imwrite('D:\\fill.png', gray)
#
#     # import mahotas as mt
#     #
#     # textures = mt.features.haralick(gray)
#     # ht_mean = textures.mean(axis=0)
#     #
#     # angular_second_moment=ht_mean[0]
#     # constrast=ht_mean[1]
#     # correlation=ht_mean[2]
#     # entropy=ht_mean[8]
#
#
#     import numpy as np
#     from skimage import io, color, img_as_ubyte
#     from skimage.feature import greycomatrix, greycoprops
#
#     rgbImg = io.imread('D:\\fill.png')
#     grayImg = img_as_ubyte(rgbImg)
#
#     distances = [1, 2, 3]
#     angles = [0, np.pi / 4, np.pi / 2, 3 * np.pi / 4]
#
#
#
#     glcm = greycomatrix(grayImg,
#                         distances=distances,
#                         angles=angles,
#                         symmetric=True,
#                         normed=True)
#
#     feats = np.hstack([greycoprops(glcm, 'ASM').ravel() for prop in properties])
#     feats1 = np.hstack([greycoprops(glcm, 'contrast').ravel() for prop in properties])
#     feats2 = np.hstack([greycoprops(glcm, 'correlation').ravel() for prop in properties])
#     feats3 = np.hstack([greycoprops(glcm, 'energy').ravel() for prop in properties])
#
#     k = np.mean(feats)
#     l = np.mean(feats1)
#     m = np.mean(feats2)
#     n = np.mean(feats3)
#
#     ar=[]
#     ar.append(k)
#     ar.append(l)
#     ar.append(m)
#     ar.append(n)
#     ar.append(label)
#
#     with open('C:\\Users\\HP\\PycharmProjects\\leukemia project\\static\\features.csv', 'a', newline='') as file:
#         writer = csv.writer(file)
#         writer.writerow(ar)
#
#         for entry in listOfFiles:
#             filename = entry.split(".")[0]
#             label = filename.split("_")[1]
#             image_path = "C:\\Users\\HP\\PycharmProjects\\leukemia project\\static\\ALL_IDB1\\im\\" + entry
#             from PIL import Image
#
#             img = Image.open(image_path).convert('LA')
#             img.save('D:\\greyscale.png')
#
#             import cv2
#
#             im_gray = cv2.imread('D:\\greyscale.png', cv2.IMREAD_GRAYSCALE)
#             (thresh, im_bw) = cv2.threshold(im_gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
#             cv2.imwrite('C:\\Users\\HP\\PycharmProjects\\leukemia project\\static\\binary.png', im_bw)
#
#             img = cv2.imread('C:\\Users\\HP\\PycharmProjects\\leukemia project\\static\\binary.png', 0)
#             kernel = np.ones((5, 5), np.uint8)
#
#             opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
#             cv2.imwrite('D:\\opening.png', opening)
#             close = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
#
#             cv2.imwrite('D:\\close.png', close)
#
#             # finding erosion
#             import cv2
#             import numpy as np
#
#             des = cv2.bitwise_not(close)
#             contour, hier = cv2.findContours(des, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
#
#             for cnt in contour:
#                 cv2.drawContours(des, [cnt], 0, 255, -1)
#
#             gray = cv2.bitwise_not(des)
#             cv2.imwrite('D:\\fill.png', gray)
#
#             # import mahotas as mt
#             #
#             # textures = mt.features.haralick(gray)
#             # ht_mean = textures.mean(axis=0)
#             #
#             # angular_second_moment=ht_mean[0]
#             # constrast=ht_mean[1]
#             # correlation=ht_mean[2]
#             # entropy=ht_mean[8]
#
#
#             import numpy as np
#             from skimage import io, color, img_as_ubyte
#             from skimage.feature import greycomatrix, greycoprops
#
#             rgbImg = io.imread('D:\\fill.png')
#             grayImg = img_as_ubyte(rgbImg)
#
#             distances = [1, 2, 3]
#             angles = [0, np.pi / 4, np.pi / 2, 3 * np.pi / 4]
#
#             glcm = greycomatrix(grayImg,
#                                 distances=distances,
#                                 angles=angles,
#                                 symmetric=True,
#                                 normed=True)
#
#             feats = np.hstack([greycoprops(glcm, 'ASM').ravel() for prop in properties])
#             feats1 = np.hstack([greycoprops(glcm, 'contrast').ravel() for prop in properties])
#             feats2 = np.hstack([greycoprops(glcm, 'correlation').ravel() for prop in properties])
#             feats3 = np.hstack([greycoprops(glcm, 'energy').ravel() for prop in properties])
#
#             k = np.mean(feats)
#             l = np.mean(feats1)
#             m = np.mean(feats2)
#             n = np.mean(feats3)
#
#             ar = []
#             ar.append(k)
#             ar.append(l)
#             ar.append(m)
#             ar.append(n)
#             ar.append(label)
#
#             with open('C:\\Users\\HP\\PycharmProjects\\leukemia project\\static\\features.csv', 'a',
#                       newline='') as file:
#                 writer = csv.writer(file)
#                 writer.writerow(ar)
#
#                 # db.insert("INSERT INTO `dataset_features` VALUES(NULL,'"+entry+"','"+str(k)+"','"+str(l)+"','"+str(m)+"','"+str(n)+"','"+label+"')")
#
# print("Trainming completed")
for entry in listOfFiles1:
    image_path = "C:\\Users\\HP\\PycharmProjects\\leukemia project\\static\\ALL_IDB1\\Others\\"+entry
    from PIL import Image

    img = Image.open(image_path).convert('LA')
    img.save('D:\\greyscale.png')



    import cv2

    im_gray = cv2.imread('D:\\greyscale.png', cv2.IMREAD_GRAYSCALE)
    (thresh, im_bw) = cv2.threshold(im_gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    cv2.imwrite('C:\\Users\\HP\\PycharmProjects\\leukemia project\\static\\binary.png', im_bw)



    img = cv2.imread('C:\\Users\\HP\\PycharmProjects\\leukemia project\\static\\binary.png', 0)
    kernel = np.ones((5, 5), np.uint8)

    opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
    cv2.imwrite('D:\\opening.png', opening)
    close = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

    cv2.imwrite('D:\\close.png', close)

    # finding erosion
    import cv2
    import numpy as np

    des = cv2.bitwise_not(close)
    contour, hier = cv2.findContours(des, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contour:
        cv2.drawContours(des, [cnt], 0, 255, -1)

    gray = cv2.bitwise_not(des)
    cv2.imwrite('D:\\fill.png', gray)

    # import mahotas as mt
    #
    # textures = mt.features.haralick(gray)
    # ht_mean = textures.mean(axis=0)
    #
    # angular_second_moment=ht_mean[0]
    # constrast=ht_mean[1]
    # correlation=ht_mean[2]
    # entropy=ht_mean[8]


    import numpy as np
    from skimage import io, color, img_as_ubyte
    from skimage.feature import greycomatrix, greycoprops

    rgbImg = io.imread('D:\\fill.png')
    grayImg = img_as_ubyte(rgbImg)

    distances = [1, 2, 3]
    angles = [0, np.pi / 4, np.pi / 2, 3 * np.pi / 4]



    glcm = greycomatrix(grayImg,
                        distances=distances,
                        angles=angles,
                        symmetric=True,
                        normed=True)

    feats = np.hstack([greycoprops(glcm, 'ASM').ravel() for prop in properties])
    feats1 = np.hstack([greycoprops(glcm, 'contrast').ravel() for prop in properties])
    feats2 = np.hstack([greycoprops(glcm, 'correlation').ravel() for prop in properties])
    feats3 = np.hstack([greycoprops(glcm, 'energy').ravel() for prop in properties])

    k = np.mean(feats)
    l = np.mean(feats1)
    m = np.mean(feats2)
    n = np.mean(feats3)

    ar=[]
    ar.append(k)
    ar.append(l)
    ar.append(m)
    ar.append(n)
    ar.append("2")

    with open('C:\\Users\\HP\\PycharmProjects\\leukemia project\\static\\features.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(ar)
