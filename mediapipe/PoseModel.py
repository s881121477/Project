# -*- coding: utf-8 -*-
"""
Created on Fri Nov 26 10:51:22 2021

@author: Yongsheng
"""

import cv2
import time
import mediapipe as mp


class poseDetector:
    def __init__(self, mode=False, smooth=True,
                 detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.smooth = smooth
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpdraw = mp.solutions.drawing_utils
        self.mppose = mp.solutions.pose
        self.pose = self.mppose.Pose(self.mode, self.smooth,
                                     self.detectionCon, self.trackCon)

    def findPose(self, img, draw=True):

        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.res = self.pose.process(imgRGB)
        # print(res.pose_landmarks)
        if self.res.pose_landmarks:
            if draw:
                self.mpdraw.draw_landmarks(img, self.res.pose_landmarks, self.mppose.POSE_CONNECTIONS)

        return img

    def getPosition(self, img, draw=True):
        lmlist = []
        if self.res.pose_landmarks:

            for id, lm in enumerate(self.res.pose_landmarks.landmark):
                h, w, c = img.shape
                # print(id, lm)
                cx, cy = int(lm.x * w), int(lm.y * h)
                # print(cx,cy)
                lmlist.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 1, (255, 0, 0), cv2.FILLED)

        return lmlist


def main():
    file_name = "nosensor.mp4"
    window_name = "window"
    cap = cv2.VideoCapture(file_name)
    # cv2.namedWindow(window_name, cv2.WND_PROP_FULLSCREEN)
    # cv2.setWindowProperty(window_name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    # cap = cv2.resize(cap, (640, 640))
    # fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    # out = cv2.VideoWriter('output.mp4', fourcc, 15.0, (640, 480), True)
    ptime = 0
    detector = poseDetector()
    while True:
        success, img = cap.read()
        img = detector.findPose(img)
        # chk = img.shape y==540 x==960
        # print(chk)
        lmlist = detector.getPosition(img, draw=False)
        if len(lmlist) != 0:
            # print(lmlist[32][1], lmlist[32][2])
            cv2.circle(img, (lmlist[31][1], lmlist[31][2]), 4, (255, 0, 0), cv2.FILLED)
            cv2.circle(img, (lmlist[32][1], lmlist[32][2]), 4, (255, 0, 0), cv2.FILLED)
            if lmlist[32][1] in range(400, 500) and lmlist[32][2] in range(180, 360):
                cv2.putText(img, '5', (480, 350), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 2)
            elif lmlist[32][1] in range(616, 925) and lmlist[32][2] in range(360, 540):
                cv2.putText(img, '3', (770, 450), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 2)
            elif lmlist[32][1] in range(1, 308) and lmlist[32][2] in range(360, 540):
                cv2.putText(img, '1', (154, 450), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 2)
            elif lmlist[32][1] in range(1, 308) and lmlist[32][2] in range(180, 360):
                cv2.putText(img, '4', (200, 350), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 2)
            elif lmlist[32][1] in range(1, 350) and lmlist[32][2] in range(50, 270):
                cv2.putText(img, '7', (250, 270), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 2)
            elif lmlist[32][1] in range(616, 925) and lmlist[32][2] in range(50, 270):
                cv2.putText(img, '9', (700, 250), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 2)
            elif lmlist[32][1] in range(700, 925) and lmlist[32][2] in range(180, 360):
                cv2.putText(img, '6', (770, 320), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 2)

        cv2.circle(img, (495, 326), 4, (255, 0, 0), cv2.FILLED)
        ctime = time.time()
        fps = 1 / (ctime - ptime)
        ptime = ctime
        cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 2)
        # out.write(img)
        cv2.imshow(window_name, img)

        key = cv2.waitKey(1)
        # ESC
        if key == 27:
            break

    cap.release()
    # out.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
