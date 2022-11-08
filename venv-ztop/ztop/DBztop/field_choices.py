# TEC DEPARTMENTS CHOICES

# Academic departments
CENTRO_GRADUADOS = 'centro_graduados'
CIENCIAS_BASICAS = 'ciencias_basicas'
DESARROLLO_ACADEMICO = 'desarrollo_academico'
DIVISION_ESTUDIOS_PROF = 'division_estudios_prof'
DIVISION_ESTUDIOS_POSGRADO = 'division_estudios_posgrado'
ECONOMICO_ADMINISTRATIVAS = 'economico_administrativas'
ELECTRICA_ELECTRONICA = 'electrica_electronica'
ING_INDUSTRIAL = 'ing_industrial'
METAL_MECANICA = 'metal_mecanica'
SISTEMAS = 'sistemas'
DEPT_INGENIERIA = 'dept_ingenieria'
QUIMICA_BIOQUIMICA = 'quimica_bioquimica'

# Planeacion y Vinculacion departments
CENTRO_INFO = 'centro_info'
COMUNICACION_DIFUSION = 'comunicacion_difusion'
ACT_EXTRAESCOLARES = 'act_extraescolares'
VINCULACION = 'vinculacion'
PLANEACION = 'planeacion'
SERVICIOS_ESCOLARES = 'servicios_escolares'

# Administrative services departments
CENTRO_COMPUTO = 'centro_computo'
RECURSOS_FINANCIEROS = 'recursos_financieros'
MANTENIMIENTO = 'mantenimiento'
RECURSOS_HUMANOS = 'recursos_humanos'
MATERIALES_SERVICIOS = 'materiales_servicios'
SISTEMA_GESTION_CALIDAD = 'sistema_gestion_calidad'
TRANSPORTES = 'transportes'

# Other departments
CIIA = 'ciia'

# Departments choices list
DEPARTMENTS_CHOICES = [
    (CENTRO_GRADUADOS, 'Centro de Graduados e Investigación en Química'),
    (CIENCIAS_BASICAS, 'Ciencias Básicas'),
    (DESARROLLO_ACADEMICO, 'Desarrollo Académico'),
    (DIVISION_ESTUDIOS_PROF, 'División de Estudios Profesionales'),
    (DIVISION_ESTUDIOS_POSGRADO, 'División de Estudios de Posgrado e Investigación'),
    (ECONOMICO_ADMINISTRATIVAS, 'Económico Administrativas'),
    (ELECTRICA_ELECTRONICA, 'Eléctrica y Electrónica'),
    (ING_INDUSTRIAL, 'Ingeniería Industrial'),
    (METAL_MECANICA, 'Metal Mecánica'),
    (SISTEMAS, 'Sistemas y Computación'),
    (DEPT_INGENIERIA, 'Departamento de Ingeniería'),
    (QUIMICA_BIOQUIMICA, 'Química y Bioquímica'),
    (CENTRO_INFO, 'Centro de Información'),
    (COMUNICACION_DIFUSION, 'Comunicación y Difusión'),
    (ACT_EXTRAESCOLARES, 'Actividades Extraescolares'),
    (VINCULACION, 'Gestión Tecnológica y Vinculación'),
    (PLANEACION, 'Planeación, Programación y Presupuestación'),
    (SERVICIOS_ESCOLARES, 'Servicios Escolares'),
    (CENTRO_COMPUTO, 'Centro de Cómputo'),
    (RECURSOS_FINANCIEROS, 'Recursos Financieros'),
    (MANTENIMIENTO, 'Mantenimiento y Equipo'),
    (RECURSOS_HUMANOS, 'Recursos Humanos'),
    (MATERIALES_SERVICIOS, 'Materiales y Servicios'),
    (SISTEMA_GESTION_CALIDAD, 'Sistema de Gestión de Calidad'),
    (TRANSPORTES, 'Transportes IT Tijuana'),
    (CIIA, 'CIIA')
]

###############################################################################


# Monitor ports constants
AVAILABLE = 'available'
UNAVAILABE = 'unavailable'
INVALID = 'invalid'

MONITOR_PORT_CHOICES = [
    (AVAILABLE, 'Available'),
    (UNAVAILABE, 'Unavailable'),
    (INVALID, 'Does not apply')
]

###############################################################################

# OS choice constants
LINUX = 'linux'
MACOS = 'macos'
WINDOWS_XP = 'w_xp'
WINDOWS_VISTA = 'w_vista'
WINDOWS_7 = 'w_7'
WINDOWS_8 = 'w_8'
WINDOWS_10 = 'W_10'
WINDOWS_11 = 'w_11'
WINDOWS_SERVER = 'w_server'
NONE = 'none'

OS_CHOICES = [
    (LINUX, 'Linux'),
    (MACOS, 'MacOS'),
    (WINDOWS_XP, 'Windows XP'),
    (WINDOWS_VISTA, 'Windows Vista'),
    (WINDOWS_7, 'Windows 7'),
    (WINDOWS_8, 'Windows 8'),
    (WINDOWS_10, 'Windows 10'),
    (WINDOWS_11, 'Windows 11'),
    (NONE, 'None')
]

###############################################################################

# Drive type constants
HDD = 'hdd'
SSD = 'ssd'

DRIVE_TYPE_CHOICES = [
    (HDD, 'Mechanical Disk (HDD)'),
    (SSD, 'Solid State Disk (SSD)'),
    (NONE, 'None')
]

###############################################################################

# Item type constants
PC = 'pc'
MONITOR = 'monitor'

ITEM_TYPE_CHOICES = [
    (PC, 'PC'),
    (MONITOR, 'Monitor')
]