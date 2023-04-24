######################################################
##          Read image data from .bag file          ##
##                                                  ##
##                                                  ##
######################################################

# Import Libraries
import rosbag
from sensor_msgs.msg import Image
from PIL import Image
import numpy as np
from matplotlib import pyplot as plt
from bagpy import bagreader
import pandas as pd
import seaborn as sea


def getTopics(location_bag_file):
    '''
    TODO: Description
    '''
    bag = rosbag.Bag(location_bag_file)
    topics = list(bag.get_type_and_topic_info()[1].keys())
    return(topics)


def getImageData(location_bag_file, img_topic = '/d455/infra1/image_rect_raw'):
    '''
    First part inspired by: http://wiki.ros.org/rosbag/Code%20API 

    location_bag_file   - Path to the .bag file. 
                          If it is in the same directory just the name of the bag file.
    img_topic           - ROS topic of the camera.
                          Can be found out using: getTopics(location_bag_file)
    '''
    bag = rosbag.Bag(location_bag_file)
    image_data = []
    for topic, msg, t in bag.read_messages(topics=[img_topic]):
        image_data.append(msg)
    bag.close()
    return image_data

def dispImg(msg):
    '''
    TODO: Description
    
    '''
    #(480, 848, 1)
    im = np.frombuffer(msg.data, dtype=np.uint8).reshape(msg.height, msg.width)
    img = Image.fromarray(im, 'L')
    plt.imshow(img,cmap='gray')
    plt.title
    plt.show()

def dispImgDisparity(msg1, msg2):
    '''
    TODO: Description
    
    '''
    im = np.frombuffer(msg1.data, dtype=np.uint8).reshape(msg1.height, msg1.width) \
        -np.frombuffer(msg2.data, dtype=np.uint8).reshape(msg2.height, msg2.width)
    img = Image.fromarray(im, 'L')
    plt.imshow(img,cmap='gray')
    plt.show()

def getDepthData(location_bag_file, img_topic = '/d455/depth/image_rect_raw'):
    '''
                              TODO:

    First part inspired by: http://wiki.ros.org/rosbag/Code%20API 

    location_bag_file   - Path to the .bag file. 
                          If it is in the same directory just the name of the bag file.
    img_topic           - ROS topic of the camera.
                          Can be found out using: getTopics(location_bag_file)
    '''
    bag = rosbag.Bag(location_bag_file)
    image_data = []
    for topic, msg, t in bag.read_messages(topics=[img_topic]):
        image_data.append(msg)
    bag.close()
    return image_data

def dispDepthImg(msg):
    '''
    TODO: Description
    '''
    #(480, 848, 2)

    #print(msg.data.shape)

    im = np.frombuffer(msg.data, dtype=np.uint16).reshape(msg.height, msg.width)
    img1 = Image.fromarray(im)
    np_img = np.array(img1)
    center_depth = np_img[int(msg.height*0.5),int(msg.width*0.5)] *0.001 # *0.001 to get from mm -> m
    print("Depth in the middle of the image: ", print(center_depth))
    plt.imshow(img1,cmap='gray')
    plt.show()

    # img2 = Image.fromarray(new_im2)
    # #print(img2[100,430]/1000)
    # aaaa = np.array(img2)
    # print(type(aaaa))
    # print(aaaa[400,600])
    # print(aaaa[400,600]/1000)
    # plt.imshow(aaaa,cmap='gray')
    # plt.show()

    # f, axarr = plt.subplots(1,2)
    # axarr[0].imshow(img1)
    # axarr[1].imshow(img2)

    # img = im[:,:,0] + im[:,:,1]
    # plt.imshow(img,cmap='gray')
    # plt.show()