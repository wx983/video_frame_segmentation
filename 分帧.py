# -*- coding:utf-8 -*-

"""
@author:老艾
@file: create_image.py
@time: 2018/09/25
"""

import numpy as np
import cv2
import os
import sys


def cut(video_file, target_dir):
    '''
    切分所有的文件
    :param all_file: 所有的文件列表
    :param target_dir: 图片存放文件夹
    :return: 无返回
    '''

    cap = cv2.VideoCapture(video_file)  # 获取到一个视频
    isOpened = cap.isOpened  # 判断是否打开
    # 为单张视频，以视频名称所谓文件名，创建文件夹
    temp = os.path.split(video_file)[-1]
    dir_name = temp.split('.')[0]

    single_pic_store_dir = os.path.join(target_dir, dir_name)
    if not os.path.exists(single_pic_store_dir):
        os.mkdir(single_pic_store_dir)


    i = 0
    while isOpened:

        i += 1

        (flag, frame) = cap.read()  # 读取一张图像

        fileName = 'image' + str(i) + ".jpg"
        if (flag == True):
            # 以下三行 进行 旋转
            #frame = np.rot90(frame, -1)


            #print(fileName)
            # 设置保存路径
            save_path = os.path.join(single_pic_store_dir, fileName)
            #print(save_path)
            res = cv2.imwrite(save_path, frame, [cv2.IMWRITE_JPEG_QUALITY, 70])
            #print(res)
        else:
            break

    return single_pic_store_dir

if __name__ == '__main__':
    video_file = 'I:/HVAV场景实时录制视频_剪辑后的视频/HV_syq_1128.mp4'
    target_dir = './'

    cut(video_file, target_dir)