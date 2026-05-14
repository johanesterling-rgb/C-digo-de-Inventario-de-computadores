 Sistema de Inventario — TechLogix
<img width="175" height="104" alt="image" src="https://github.com/user-attachments/assets/a7f151b1-64be-4621-9d0b-04f64e376127" />


**TechLogix** es un sistema de gestión de activos tecnológicos diseñado para departamentos de IT y oficinas modernas. Desarrollado en Python, permite el registro técnico, el seguimiento de hardware y la administración de estados operativos de equipos de cómputo de manera eficiente a través de la consola.

---

## Requisitos

* **Python 3.10** o superior (optimizado para el uso de `match` / `case`)
* Ejecución en terminal o consola de comandos
* Sin dependencias de librerías externas (Standard Library)

---



Al iniciar el script, se despliega un panel de control interactivo para gestionar el ciclo de vida de cada computador.

---

## Módulos del sistema

### 1. Registro de Activos (Alta)

Permite ingresar nuevos equipos al sistema capturando especificaciones técnicas críticas como procesador, memoria RAM y almacenamiento.

### 2. Visor de Inventario Global

Genera un reporte listado de todos los equipos registrados, mostrando de forma resumida el ID (Serial), la marca, el modelo y su estado actual de disponibilidad.

### 3. Control de Estados Operativos

Módulo dedicado a la gestión logística. Permite buscar un equipo por su serial único y actualizar su situación entre tres estados clave: **Disponible**, **Asignado** o en **Mantenimiento**.

### 4. Diagnóstico Técnico

Permite consultar la configuración detallada de hardware de un equipo específico para toma de decisiones sobre actualizaciones o reparaciones.

---

## Estructura de un Equipo

Cada activo dentro del inventario se organiza bajo la siguiente estructura de datos:

| Campo | Tipo | Descripción |
| --- | --- | --- |
| `serial` | `str` | Identificador único del hardware (ID) |
| `marca` | `str` | Fabricante del equipo |
| `modelo` | `str` | Referencia específica del fabricante |
| `procesador` | `str` | CPU instalada (ej. Intel i7, Ryzen 5) |
| `ram` | `int` | Capacidad de memoria en Gigabytes (GB) |
| `disco` | `int` | Capacidad de almacenamiento (GB) |
| `estado` | `str` | Situación actual (Disponible / Asignado / etc.) |

---

## Funciones del sistema

| Función | Tipo | Descripción |
| --- | --- | --- |
| `agregar_equipo()` | CRUD | Captura datos y añade un nuevo diccionario al inventario |
| `listar_equipos()` | Reporte | Itera la lista y formatea la salida visual de los equipos |
| `cambiar_estado()` | Logística | Localiza equipos por serial y modifica su llave de estado |
| `main()` | Entrada | Orquestador principal con bucle de control y menú de flujo |

---

## Información de la Gestión

| Campo | Valor |
| --- | --- |
| Sistema | TechLogix v1.0 |
| Departamento | Soporte Técnico / IT |
| Jurisdicción | Inventario de Activos Fijos |
| Entorno | Python 3.x |

---

## Autores

Proyecto desarrollado como solución práctica para la gestión de infraestructura tecnológica.
