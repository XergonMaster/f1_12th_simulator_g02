import matplotlib.pyplot as plt
import rospy
from sensor_msgs.msg import LaserScan

# Inicializa el nodo de ROS si aún no está inicializado
rospy.init_node('scan_plotter', anonymous=True)

# Función de callback para procesar los datos del tópico /scan
def scan_callback(data):
    # Obtén los ángulos (radianes) del escaneo
    angles = [data.angle_min + i * data.angle_increment for i in range(len(data.ranges))]
    
    # Obtén las distancias medidas
    distances = data.ranges

    # Crea un gráfico de dispersión (scatter plot)
    plt.figure(figsize=(8, 6))
    plt.scatter(angles, distances, s=1)  # s ajusta el tamaño de los puntos
    plt.xlabel('Ángulo (radianes)')
    plt.ylabel('Distancia (metros)')
    plt.title('Escaneo láser')

    # Muestra el gráfico
    plt.show()

# Suscribe al tópico /scan
rospy.Subscriber('/scan', LaserScan, scan_callback)

# Mantén el programa en ejecución para recibir y graficar datos
rospy.spin()