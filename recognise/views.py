from django.shortcuts import render
from recognise.models import Test
import cv2


def process_image(request):
    if request.method == 'GET':
        return render(request,'recognise/index.html')
    else:
        image = request.FILES['img']
        test = Test()
        test.image = image
        test.save()
        path = '/home/mayank/Desktop/FaceRecognition/' + str(test.image.url)
        img = cv2.imread(path)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        detector = cv2.CascadeClassifier('recognise/haarcascade_frontalface_default.xml')

        img = cv2.imread(path)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        faces = detector.detectMultiScale(gray, 1.3, 5)
        print(faces)
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 23, 100), 5)
        cv2.imwrite(path, img)

        print("Success")
        return render(request,'recognise/result.html',{'image':test.image.url,'faces':len(faces)})