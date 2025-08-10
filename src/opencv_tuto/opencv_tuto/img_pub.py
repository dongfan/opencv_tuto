import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

class ImagePublisher(Node):
    def __init__(self):
        super().__init__('img_publisher')
        self.publisher_ = self.create_publisher(Image, 'image_raw', 10)
        time_period = 0.01
        self.timer = self.create_timer(time_period, self.timer_callback)  # 10 Hz
        self.cap = cv2.VideoCapture(0)
        self.cv_bridge = CvBridge()

    def timer_callback(self):
        ret, frame = self.cap.read()
        img = self.cv_bridge.cv2_to_imgmsg(frame, encoding='bgr8')
        self.publisher_.publish(img)
        cv2.waitKey(1)

def main():
    rclpy.init()
    node = ImagePublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()