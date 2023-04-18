######################################################
##          Read image data from .bag file          ##
##                                                  ##
##                                                  ##
##
##
##
##
######################################################

# Import Libraries
import rosbag
from sensor_msgs.msg import Image
from PIL import Image
import numpy as np
from matplotlib import pyplot as plt


def GetImageData(location_bag_file, img_topic = '/d455/depth/image_rect_raw'):
    '''
    First part inspired by: http://wiki.ros.org/rosbag/Code%20API 

    location_bag_file   - Path to the .bag file. 
                          If it is in the same directory just the name of the bag file.
    img_topic           - ROS topic of the camera.
                          Can be found by using TODO: functionxyz

    '''
    bag = rosbag.Bag(location_bag_file)
    image_data = []
    for topic, msg, t in bag.read_messages(topics=[img_topic]):
        image_data.append(msg)
    bag.close()
    return image_data

def DispImg(msg):
    #(480, 848, 2)
    im = np.frombuffer(msg.data, dtype=np.uint8).reshape(msg.height, msg.width, -1)
    new_im1 = im[:,:,0]
    new_im2 = im[:,:,1]

    img = Image.fromarray(new_im1, 'L')
    plt.imshow(img,cmap='gray',)
    plt.show()

    img = Image.fromarray(new_im2, 'L')
    plt.imshow(img,cmap='gray')
    plt.show()

'''
>>> import bag2image as i
>>> k = []
>>> k = i.GetImageData('test3.bag')
>>> i.DispImg(k[0])
'''





