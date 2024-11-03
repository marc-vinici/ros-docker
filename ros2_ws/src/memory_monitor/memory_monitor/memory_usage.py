# memory_monitor/memory_monitor/memory_usage.py
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import psutil

class MemoryUsage(Node):
    def __init__(self):
        super().__init__('memory_usage')
        self.publisher_ = self.create_publisher(String, 'memory_stats', 10)
        self.timer = self.create_timer(1.0, self.publish_memory_stats)
        self.total_memory = 0
        self.used_memory = 0
        self.used_memory_percentage = 0
        
    def get_memory_stats(self):
        mem = psutil.virtual_memory()
        self.total_memory = mem.total / (1024 ** 3)
        self.used_memory = mem.used / (1024 ** 3)
        self.used_memory_percentage = mem.percent
        

    def publish_memory_stats(self):
        self.get_memory_stats()

        message = String()
        message.data = (f'Total Memory: {self.total_memory:.2f} GB, '
                        f'Used Memory: {self.used_memory:.2f} GB, '
                        f'Usage: {self.used_memory_percentage}%')

        self.get_logger().info(f'Publishing: "{message.data}"')
        self.publisher_.publish(message)

def main(args=None):
    rclpy.init(args=args)
    memory_usage = MemoryUsage()
    rclpy.spin(memory_usage)
    memory_usage.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
