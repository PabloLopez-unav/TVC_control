from pymodbus.client import ModbusTcpClient
import time

# Configuración de conexión
DRIVE_IP = "169.254.78.209"  # IP de tu driver Kollmorgen
PORT = 502
SLAVE_ID = 1

# Comandos MODBUS.MAP para Axis 1 y Axis 2
# Usando las direcciones reales de tu lista
COMMANDS = [
    # Axis 1
    "MODBUS.MAP 40095 AXIS1.EN",      # 40095 = AXIS1.EN
    "MODBUS.MAP 40121 AXIS1.DIS",     # 40121 = AXIS1.DIS
    "MODBUS.MAP 40005 AXIS1.ACTIVE",  # 40005 = AXIS1.ACTIVE
    "MODBUS.MAP 40007 AXIS1.MOTIONSTAT",  # 40007 = AXIS1.MOTIONSTAT
    "MODBUS.MAP 40009 AXIS1.DISSOURCES",  # 40009 = AXIS1.DISSOURCES
    "MODBUS.MAP 40011 AXIS1.FAULTED",  # 40011 = AXIS1.FAULTED
    "MODBUS.MAP 40035 AXIS1.VL.CMD",   # 40035 = AXIS1.VL.CMD

    # Axis 2
    "MODBUS.MAP 40145 AXIS2.EN",      # 40145 = AXIS2.EN
    "MODBUS.MAP 40140 AXIS2.DIS",     # 40140 = AXIS2.DIS
    "MODBUS.MAP 40055 AXIS2.ACTIVE",  # 40055 = AXIS2.ACTIVE
    "MODBUS.MAP 40057 AXIS2.MOTIONSTAT",  # 40057 = AXIS2.MOTIONSTAT
    "MODBUS.MAP 40059 AXIS2.DISSOURCES",  # 40059 = AXIS2.DISSOURCES
    "MODBUS.MAP 40061 AXIS2.FAULTED",  # 40061 = AXIS2.FAULTED
    "MODBUS.MAP 40085 AXIS2.VL.CMD",   # 40085 = AXIS2.VL.CMD
]

# Conectar al cliente Modbus TCP
client = ModbusTcpClient(DRIVE_IP, port=PORT)
if not client.connect():
    print("Error: No se pudo conectar al driver.")
    exit()

# Función para enviar un comando de texto al driver
def send_command(client, command):
    try:
        # Intentar escribir el comando como una cadena en un registro de comandos
        command_bytes = [ord(c) for c in command]
        response = client.write_registers(
            address=0x2000,  # Dirección para comandos de texto (ajusta según documentación)
            values=command_bytes,
            device_id=SLAVE_ID
        )
        if response.isError():
            print(f"Error al enviar el comando: {command}")
        else:
            print(f"Comando enviado: {command}")
    except Exception as e:
        print(f"Error: {e}")

# Enviar todos los comandos
for cmd in COMMANDS:
    send_command(client, cmd)
    time.sleep(0.5)  # Esperar entre comandos

# Cerrar la conexión
client.close()
print("Mapeo de registros completado.")