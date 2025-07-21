from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import Command, FindExecutable, PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():
    pkg_share = FindPackageShare('triciclo_robot').find('triciclo_robot')
    xacro_file = PathJoinSubstitution([pkg_share, 'urdf', 'triciclo.xacro'])

    robot_description = Command([FindExecutable(name='xacro'), ' ', xacro_file])

    return LaunchDescription([
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            parameters=[{'robot_description': robot_description}]
        ),
        Node(
            package='joint_state_publisher_gui',
            executable='joint_state_publisher_gui'
        ),
        Node(
            package='rviz2',
            executable='rviz2',
            arguments=['-d', PathJoinSubstitution([pkg_share, 'config', 'rviz_config.rviz'])]
        )
    ])
