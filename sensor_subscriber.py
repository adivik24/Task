import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

class SensorSubscriber(Node):
    def __init__(self):
        super().__init__('sensor_subscriber')
        self.subscription = self.create_subscription(Float32,'sensor_x_readings',self.listener_callback,10)

    def listener_callback(self, msg):
        reading = msg.data
        if reading > 0.5:
            self.get_logger().info(f'Reading {reading:.2f} is greater than 0.5')
        if reading < 0.5:
            self.get_logger().info(f'Reading {reading:.2f} is less than 0.5')

def main(args=None):
    rclpy.init(args=args)
    node = SensorSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
