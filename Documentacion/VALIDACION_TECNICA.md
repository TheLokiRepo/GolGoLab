# Validación técnica previa

Este documento define qué investigar; no acredita que una integración o plataforma sea viable. Las conclusiones deben incorporar fuentes, fecha de consulta y, cuando proceda, una prueba reproducible sin secretos ni datos personales en el repositorio.

## 1. Acceso a Garmin: primera dependencia

La primera revisión de fuentes oficiales distingue modalidades Personal y Business y no acredita todavía un flujo aplicable a GolGoLab. Véanse las fuentes, la fecha y los límites de esta revisión en [CONEXIONES_Y_CONSUMO.md](CONEXIONES_Y_CONSUMO.md).

Comprobar antes de elegir la infraestructura:

- Vías de acceso disponibles, requisitos de admisión y condiciones aplicables a un grupo de usuarios.
- Mecanismo de autorización por usuario, renovación, revocación y posibles restricciones de autenticación.
- Botón oficial sin copiar claves: comprobar admisión de la aplicación, retorno al entorno local, permisos y persistencia. La ruta Personal de claves manuales no satisface este requisito por sí sola; investigar Business/OAuth 2.0 y sus condiciones.
- Verificar consulta tras reiniciar los servicios, renovación automática cuando se admita y revinculación ante revocación o fallo de renovación. No asumir que un token ni la autorización duran indefinidamente.
- Actividades y métricas accesibles, acceso al histórico, paginación y límites de consulta.
- Objetivo de todo el histórico disponible: verificar la fecha más antigua recuperable por tipo de dato y registrar límites. La ausencia de histórico en Business Starter y la cobertura no acreditada de Personal se describen en CONEXIONES_Y_CONSUMO.md.
- Cobertura diferenciada de entrenamientos por día y rango, VFC y sueño: campos, permisos y resolución temporal. No asumir que el acceso a actividades da acceso a las demás métricas.
- Semántica de fechas y zonas horarias, límites de los rangos y fecha de referencia de las sesiones de sueño.
- Posibilidades de actualización: consulta periódica, notificaciones u otros mecanismos que se documenten.
- Tratamiento de actividades modificadas y eliminadas, y disponibilidad de identificadores estables.
- Costes, restricciones de almacenamiento y dependencias operativas.

**Resultado esperado:** una nota con fuentes y fecha, una muestra anonimizada de los campos disponibles y una conclusión sobre si la vía evaluada cubre la primera entrega. No se presupone acceso aprobado ni equivalencia entre mecanismos oficiales y no oficiales.

**Prueba propuesta, si la vía lo permite:** autorizar dos cuentas de prueba, importar una ventana pequeña de actividades de cada una, comprobar las consultas por día y rango, repetir la importación sin duplicados y comprobar un fallo de acceso. Verificar por separado la obtención de VFC y sueño y documentar cualquier dato no accesible. Si no hay una vía viable, registrar el impedimento y revisar el alcance.

## 2. Modelo de datos y límites de responsabilidad

Propuesta conceptual, sin elegir todavía base de datos:

| Entidad | Responsabilidad |
| --- | --- |
| Usuario | Identidad dentro de la aplicación y preferencias de unidades y zona horaria. |
| Conexión con Garmin | Asociación con el usuario, estado de autorización y referencias protegidas a credenciales. |
| Actividad | Propietario, identificador de origen, métricas normalizadas y fecha de actualización. |
| Datos de VFC y sueño | Propietario, procedencia, periodo o sesión de referencia y valores disponibles, sin exigir una actividad asociada. Estructura pendiente de conocer los datos reales. |
| Ejecución de importación | Estado, ventana solicitada, progreso disponible y error sin secretos. |

Evaluar si hace falta conservar datos originales y durante cuánto tiempo. La memoria, las conversaciones y los resúmenes de IA se diseñarán cuando se aborde esa funcionalidad, manteniendo su relación con el usuario.

La API deberá comprobar la propiedad de los datos en cada operación. La interfaz presentará los datos; la validación de acceso y la comunicación protegida con Garmin corresponderán al backend. El contrato de API se definirá después de aprobar el alcance y conocer los datos reales.

## 3. Elección de tecnologías

Angular está elegido para el frontal. Evaluar sus detalles de implementación y comparar las opciones aún abiertas después de conocer los requisitos de integración:

| Área | Criterios de evaluación |
| --- | --- |
| Frontend | Con Angular elegido, evaluar bibliotecas de interfaz y gráficos, accesibilidad y adaptación a móvil. Tener en cuenta la posible vista futura con asistente. |
| Backend | Compatibilidad con Garmin y OpenAI, gestión de usuarios, autenticación, importaciones prolongadas, pruebas y mantenimiento. |
| Persistencia | Consultas por usuario y periodo, integridad, migraciones, copias, crecimiento de capacidad y coste bajo los volúmenes y la concurrencia previstos. |
| Alojamiento | Compatibilidad del entorno de ejecución, tareas programadas, secretos, límites, ubicación de datos y coste total. Cloudflare es una opción por evaluar. |
| Android posterior | Reutilización de interfaz, autenticación y distribución. Capacitor es una propuesta futura. |

No basta con comparar el coste del alojamiento web: incluir almacenamiento, copias, procesos de sincronización y servicios de autenticación. El coste de IA se evaluará de forma separada cuando se defina esa etapa.

## 4. Operación y protección de datos

Definir antes de desplegar con usuarios reales:

- Alta y baja de usuarios, caducidad de sesiones y recuperación del acceso.
- Gestión y revocación de secretos; información permitida en registros.
- Borrado de cuenta, datos importados, conexiones y tratamiento de las copias.
- Copias de seguridad, prueba de restauración y objetivos de recuperación.
- Registro de fallos de importación y forma de detectar problemas.
- Entorno de desarrollo y datos de prueba sin credenciales ni historial personal en el repositorio.

## 5. Orden de trabajo propuesto

1. Acordar las métricas, el histórico y el recorrido de la primera entrega.
2. Verificar las vías de acceso a Garmin para varias cuentas.
3. Elegir autenticación, backend, persistencia y alojamiento con las restricciones comprobadas.
4. Definir el modelo de datos y el contrato de API de esa entrega.
5. Implementar un recorrido completo: acceso, importación, listado, detalle y evolución.
6. Verificar separación entre usuarios, integridad, errores y recuperación antes de abrir el uso al grupo.

La definición funcional y la investigación de Garmin pueden avanzar en paralelo. Si alguna conclusión cambia el alcance, registrar la decisión antes de continuar con la implementación dependiente.

Se ha acordado comenzar con API/orquestación, usuarios y Garmin/datos deportivos como tres servicios independientes y ejecución local. El usuario tiene experiencia en .NET, que orienta la propuesta de ASP.NET Core pendiente de confirmar. Se concretarán contratos y propiedad de datos según [ARQUITECTURA_BACKEND.md](ARQUITECTURA_BACKEND.md). El alojamiento compartido se evaluará después.

## 6. Base de datos y crecimiento

Antes de elegir el motor, estimar usuarios iniciales y previstos, años de histórico, registros por usuario, detalle de VFC y sueño, volumen de contexto y análisis, y consultas simultáneas. Acordar objetivos de respuesta y coste. Estas cifras están pendientes; no hay un volumen de escalabilidad validado.

Comparar los motores candidatos con consultas representativas: entrenamientos por día y rango, evolución por periodo, métricas diarias y recuperación del contexto de un usuario. Evaluar integridad, índices, migraciones, copias, restauración, ampliación de capacidad y compatibilidad con el backend y el alojamiento. Registrar la decisión con evidencia y límites conocidos.

## 7. Integración con OpenAI

Para la etapa de IA, contrastar la documentación oficial vigente y definir el mecanismo de integración, modelo y formato de respuesta. Este documento registra la necesidad funcional; todavía no se han validado detalles de la API ni costes.

El modelo inicial será acceso y consumo propios de cada usuario, con ejecución local. La revisión documental de autenticación, Sign in with ChatGPT y créditos está en [CONEXIONES_Y_CONSUMO.md](CONEXIONES_Y_CONSUMO.md). Antes de implementar, validar qué mecanismo admite ese entorno y volver a evaluarlo si se decide alojamiento compartido, sin asumir que login, autorización API y facturación sean equivalentes.

Concretar tipos de análisis, datos enviados, plantillas de prompts, selección de contexto, conservación de resultados, tratamiento de errores y límites de uso por usuario. Probar con casos acordados que el análisis utiliza el contexto esperado, sin datos de otras cuentas, y que la aplicación mantiene su consulta deportiva cuando el proveedor no está disponible.
