# Tarea1Ros
Nicolas Saavedra Silva 
Winston Matamala Chomba
David Valdivia Torres

En este GitHub se encuentran los archivos y paquetes de ROS2 para la simulación de un robot tipo triciclo. Como su nombre lo indica este robot posee tres ruedas, donde la única delantera posee motricidad y dirección, mientras que las dos traseras son ruedas sin tracción.

Primero es necesario dirigirse mediante la terminal a la carpeta donde se encuentran los paquetes, una vez ahí se utiliza el siguiente comando para compilar los mismos:

colcon build

Una vez los paquetes son correctamente compilados, se utiliza el siguiente comando para cargar las variables y configuraciones requeridas

source install/setup.bash

Posteriormente, para visualizar el modelo del triciclo en RViz, se debe aplicar el siguiente comando en la misma terminal:

ros2 launch triciclo_robot display_rviz.launch.py

Este archivo launch está programado para que tome el modelo en XACRO, y luego se genera un URDF para la visualización en RViz. Esto es ya que en XACRO existen mas funciones como repetición de macros, mayor legibilidad y facilidad de mantenimiento, entre otros.

RViz también ofrece la capacidad de mover los ejes definidos en el modelo mediante una aplicación emergente que funciona como publicador.

Para la visualización del modelo en el simulador Gazebo se deben repetir los pasos anteriores en una nueva terminal, es decir luego de llegar al directorio con los paquetes nuevamente se usa secuencialmente:

colcon build
source install/setup.bash

Posteriormente se utiliza este comando para abrir Gazebo con el robot implementado:

ros2 launch triciclo_robot gazebo.launch.py

Lo que hace este launch es lanzar el mundo en vacío en el software de simulación, luego llama al modelo del triciclo en formato XACRO (que nuevamente es convertido a URDF por el mismo) para cargarlo en Gazebo. Este comando también publica el nodo node_state_publisher, el cual permite que se pueda monitorear las variables del robot en todo momento (sensores, coordenadas, etc). Finalmente se abre Gazebo donde se inicia automáticamente la simulación, para evitar errores intencionalmente se inicia el mundo en Gazebo y en 5 segundos se incorpora el modelo del robot.

Tambien se agrego un archivo launch controllers.launch.py para lanzar los ndos de los controladores, ya que en el xacro se agrego un plugin para poder controlar el robot en gazebo, este se debe lanzar una vez este corriendo el triciclo en gazebo.

finalemnte existe una carpeta Tarea1 con resultados de simulaciones. 
