import cv2,os,datetime, time
import numpy as np

frames_to_merge = 10000

# initialize the HOG descriptor/person detector
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

RTSP_URL = 'http://192.168.178.59:50228/videostream.cgi?user=admin&pwd=lusche0815'
os.environ['OPENCV_FFMPEG_CAPTURE_OPTIONS'] = 'rtsp_transport;udp'

counter_total = 0
start_time = time.time()
while True:
    counter_total = counter_total + 1
    print("[SYS] starting run: " + str(counter_total))

    cap = cv2.VideoCapture(RTSP_URL, cv2.CAP_FFMPEG)
    
    if not cap.isOpened():
        print('Cannot open RTSP stream')
        exit(-1)

    _, frame = cap.read()
    height, width, layers = frame.shape
    size = (width,height)

    filename = str(str(datetime.datetime.now().strftime("%m-%d-%Y---%H-%M-%S")) + ".avi")
    out = cv2.VideoWriter(filename,cv2.VideoWriter_fourcc(*'DIVX'), 15, size)
    frame_counter = 0
    while True:
        frame_counter = frame_counter + 1
        # print(str(round((time.time() - start_time) / 60,1)) + 'min ' + ' -=> ' + str(frame_counter / frames_to_merge))

        ret, frame = cap.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
        boxes, weights = hog.detectMultiScale(frame, winStride=(8,8) )
        boxes = np.array([[x, y, x + w, y + h] for (x, y, w, h) in boxes])
        for (xA, yA, xB, yB) in boxes:
            # display the detected boxes in the colour picture
            print("HUMAN DETECTED!")
            cv2.rectangle(frame, (xA, yA), (xB, yB),(0, 255, 0), 2)

        out.write(frame)

        if frame_counter > frames_to_merge:
            break

        # img_array.append(frame)

        # if len(img_array) > frames_to_merge:
        #     break

    print("")
    print("[SYS] recording done!")
    # print("[SYS] saving...")
    cap.release()
    # for i in range(len(img_array)):
    #     out.write(img_array[i])
    out.release()
    cv2.destroyAllWindows()
    print("[SYS] saving done!")
    print(str(time.time() - start_time) + 's total!')