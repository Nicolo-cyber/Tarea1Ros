from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, TimerAction
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from launch.substitutions import Command, PathJoinSubstitution, FindExecutable
from launch_ros.substitutions import FindPackageShare
import os

def generate_launch_description():
    pkg_share = FindPackageShare('triciclo_robot').find('triciclo_robot')
    world_file = PathJoinSubstitution([pkg_share, 'worlds', 'empty.world'])
    xacro_file = PathJoinSubstitution([pkg_share, 'urdf', 'triciclo.xacro'])

    robot_description = Command([FindExecutable(name='xacro'), ' ', xacro_file])

    # Gazebo simulator
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                FindPackageShare('gazebo_ros').find('gazebo_ros'),
                'launch',
                'gazebo.launch.py'
            )
        ),
        launch_arguments={'world': world_file}.items()
    )

    # Spawn robot entity
    spawn_entity = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        arguments=[
            '-entity', 'triciclo',
            '-topic', 'robot_description'
        ],
        output='screen'
    )

    # Publish robot_state
    robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        parameters=[{'robot_description': robot_description}],
        output='screen'
    )


    # Delays
    delayed_spawn = TimerAction(period=5.0, actions=[spawn_entity])

    return LaunchDescription([
        gazebo,
        robot_state_publisher,
        delayed_spawn,
    ])
