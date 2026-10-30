# Alcance y requisitos

## 1. Base confirmada

- Primera versión para un grupo reducido con cuentas separadas.
- Prioridad: consultar las actividades y ver la evolución deportiva.
- Enfoque inicial en running.
- Consulta y visualización disponibles sin IA.
- API propia y memoria contextual gestionada por la aplicación.
- Frontal Angular con dashboard por usuario, gráficos, histórico, hitos y gestión de usuarios. El detalle de estas capacidades está por definir.
- Backend preparado desde la primera versión para consultar entrenamientos por día y por rango de fechas, además de VFC y sueño. La cobertura de Garmin y el detalle de los datos requieren validación.
- Gestión de usuarios a cargo del backend y base de datos con capacidad de crecimiento; motor, autenticación y operaciones pendientes.
- Primera entrega de dashboard y datos; integración opcional con OpenAI para análisis mediante prompts con contexto en una entrega posterior.
- Tres servicios independientes desde el inicio: API/orquestación, usuarios y Garmin/datos deportivos. Primera ejecución en el equipo del usuario y alojamiento posterior por decidir.
- Objetivo de consultar todo el histórico disponible, sujeto a validar cuánto puede recuperarse para cada tipo de dato.
- Vinculación oficial de Garmin mediante botón, sin generar ni copiar claves, guardada por usuario para consultas posteriores. Modalidad y renovación pendientes de validación.
- Acceso API propio a OpenAI y consumo a cargo del usuario que active IA. El modelo y las responsabilidades se detallan en [CONEXIONES_Y_CONSUMO.md](CONEXIONES_Y_CONSUMO.md).

El resto de este documento es una propuesta para revisar. Los criterios de aceptación describen cómo verificarla si se aprueba.

La primera entrega empieza por datos y dashboard sin IA, según D-017 de [DECISIONES.md](DECISIONES.md). Los detalles funcionales siguientes aún requieren revisión.

## 2. Primera entrega propuesta

Un usuario accede a su cuenta, vincula su fuente de datos de Garmin, incorpora sus entrenamientos y puede consultar su historial, el detalle de una actividad y su evolución durante un periodo.

| Área | Propuesta para la primera entrega | Criterio de aceptación |
| --- | --- | --- |
| Cuenta | Acceder a una cuenta individual. Mecanismo de alta y autenticación pendiente. | El usuario puede iniciar y cerrar sesión; una sesión no válida no permite consultar datos privados. |
| Gestión de usuarios | Backend responsable de gestionar las cuentas del grupo. Concretar operaciones y permisos. | Pendiente de definir las operaciones y quién puede realizarlas. |
| Dashboard | Presentar información relevante y gráficos propios del usuario. Indicadores pendientes. | El panel solo muestra datos del usuario autorizado; los valores coinciden con las actividades del periodo seleccionado. |
| Hitos | Mostrar hitos del usuario. Definición y origen pendientes. | Pendiente de acordar qué constituye un hito y cómo verificarlo. |
| Acceso a Garmin | Botón de autorización oficial sin copiar claves; conservar la conexión para el backend. | La asociación pertenece al usuario correcto y permite consultar tras reiniciar la aplicación sin nueva autorización mientras sea válida. Verificar renovación si se admite, revinculación cuando sea necesaria y desconexión. |
| Importación | Objetivo confirmado: todo el histórico disponible. Actualización manual propuesta. Cobertura y mecanismo de recuperación pendientes de validar. | Repetir la importación no duplica datos; mostrar última actualización correcta, cobertura importada y limitaciones, sin presentar datos parciales como histórico completo. |
| Listado | Consultar actividades de running por periodo, con fecha, distancia y duración. | Solo aparecen actividades del usuario y del periodo seleccionado; existe un estado claro cuando no hay datos. |
| Consulta por fecha | Consultar los entrenamientos del usuario de un día concreto o de un rango de días. | Con zona horaria y límites previamente acordados, se devuelven todos los entrenamientos correspondientes y ninguno de fuera del intervalo, incluida la paginación si procede. |
| VFC y sueño | Obtener desde el backend las métricas disponibles de cada usuario. Campos y periodos pendientes. | Tras validar el acceso, comprobar los campos acordados frente a la fuente y distinguir datos ausentes de valores cero. Su presentación en el frontal queda por concretar. |
| Detalle | Consultar los datos básicos de un entrenamiento. | Fecha, distancia, duración y ritmo se presentan con unidades y significado definidos; un dato ausente no aparece como cero. |
| Evolución | Ver agregados por semana o mes. Métricas concretas pendientes. | Los totales coinciden con las actividades del periodo; las semanas sin actividad se distinguen de los periodos sin datos importados. |
| Errores | Mostrar fallos de acceso o importación y permitir reintentar. | Un fallo no borra el historial ya importado ni se presenta como una actualización correcta. |

La importación directa depende de verificar las condiciones y posibilidades de Garmin. Si no es viable, cualquier alternativa, como una importación de archivos, requerirá revisar el alcance antes de implementarla.

## 3. Datos por concretar

Propuesta mínima: identificador de origen, usuario propietario, tipo de actividad, fecha y zona horaria disponible, distancia y duración. El ritmo se incorporará o calculará cuando los datos lo permitan.

Antes de cerrar los requisitos hay que definir:

- Si la duración y el ritmo usan tiempo en movimiento o tiempo total.
- Qué métricas adicionales son necesarias: frecuencia cardiaca, desnivel, cadencia, vueltas u otras.
- Qué deportes entran en los agregados y cómo tratar actividades mixtas.
- Cómo se calculan los periodos, qué día empieza la semana y qué zona horaria se utiliza.
- Qué ocurre con actividades editadas o eliminadas en Garmin.
- Cómo recuperar todo el histórico disponible y distinguir lo importado, lo pendiente y lo no recuperable de un periodo sin entrenamientos.

VFC y sueño están incluidos en el alcance funcional del backend, aunque no estén asociados a actividades. Quedan por concretar sus campos, resolución temporal, fecha de referencia y disponibilidad. No se incluyen por defecto rutas GPS ni otras métricas de salud; cualquier incorporación adicional debe acordarse.

## 4. Requisitos transversales propuestos

- **Separación entre cuentas:** validar en el servidor la propiedad de cada recurso. No basta con ocultarlo en la interfaz. Verificar con dos usuarios que no pueden leer o modificar datos ajenos.
- **Credenciales:** mantener secretos y tokens fuera del código, de los registros y de las respuestas al navegador. Evitar almacenar contraseñas de Garmin; el mecanismo final depende de la integración validada.
- **Privacidad:** permitir desconectar Garmin y definir cómo borrar la cuenta y sus datos. Acordar también el tratamiento de copias de seguridad y registros.
- **Integridad:** conservar la procedencia de los datos y evitar duplicados al reintentar una importación.
- **Uso:** interfaz adaptable a escritorio y móvil, con estados de carga, error y ausencia de datos comprensibles.
- **Operación:** poder detectar importaciones fallidas y restaurar los datos a partir de una copia comprobada. Frecuencia y objetivos de recuperación pendientes.
- **IA opcional:** activación explícita, envío limitado al contexto necesario y separación del historial por usuario. La consulta deportiva no depende de una clave ni de un servicio de IA, aunque se decida entregar los análisis en la misma versión.
- **Persistencia y crecimiento:** definir volumen de datos, usuarios concurrentes y tiempos de respuesta objetivo para elegir y verificar el motor de base de datos.

### Validación propuesta para la etapa de análisis con IA

Una petición de análisis del usuario autenticado deberá llegar al backend, que preparará el prompt con los datos acordados y devolverá el resultado de OpenAI. Comprobar que solo se incorpora contexto del usuario autorizado, que las credenciales guardadas no se devuelven al frontal y que los errores no impiden consultar las actividades. Los casos concretos para valorar la utilidad de los análisis se definirán junto con los tipos de análisis y sus prompts.

Verificar también que se utiliza el acceso propio del solicitante, que la conexión puede sustituirse o desconectarse y que los fallos de acceso o consumo no se resuelven cargando peticiones a una cuenta del proveedor. Las credenciales guardadas no se devolverán al frontal.

## 5. Fuera de la primera entrega propuesta

La exclusión de análisis con IA en la primera entrega está confirmada. Las demás exclusiones siguen formando parte de la propuesta detallada de alcance.

- Análisis y conversaciones con IA, y recuperación de memoria histórica.
- Vista simultánea con asistente persistente y navegación mediante el asistente; idea futura descrita en [ECOSISTEMA.md](ECOSISTEMA.md).
- Aplicación Android empaquetada y publicación en tiendas.
- Servidor MCP e integración con ChatGPT.
- Funciones sociales, clasificaciones, entrenadores o acceso compartido a datos de otra cuenta.
- Planificación automática de entrenamientos y recomendaciones médicas.

Consultar evolución requiere comparar periodos de forma básica; la comparación avanzada entre entrenamientos puede definirse después.

## 6. Cuándo estaría lista

La primera entrega se consideraría utilizable cuando se complete el recorrido de la sección 2 con datos reales de al menos dos cuentas de prueba autorizadas, se compruebe su separación y se validen los totales frente a las actividades de origen. También deben comprobarse el reintento de una importación y la recuperación tras un fallo de acceso.

Los objetivos cuantitativos de rendimiento y volumen quedan pendientes de conocer el tamaño del grupo y del histórico. No hay una fecha de entrega comprometida.
