# Registro de decisiones

Este documento recoge acuerdos y su consecuencia práctica. Las opciones sin validar no se consideran decisiones.

## Decisiones confirmadas

| ID | Decisión | Consecuencia |
| --- | --- | --- |
| D-001 | La consulta deportiva debe funcionar sin IA. | La visualización y las importaciones no dependerán de un proveedor de IA. |
| D-002 | La aplicación contará inicialmente con una API convencional propia. | La integración MCP no forma parte del acceso inicial. La tecnología de la API sigue abierta. |
| D-003 | La aplicación gestionará su memoria contextual. | El contexto relevante deberá conservarse y recuperarse desde la aplicación. |
| D-004 | El contexto previo de ChatGPT se incorporará explícitamente. | No se presupone una transferencia automática del historial del proyecto. |
| D-005 | MCP queda fuera del alcance inicial. | Su diseño y validación podrán abordarse en una etapa posterior. |
| D-006 | La primera versión servirá a un grupo reducido con cuentas separadas. | La autenticación, la propiedad de los datos y el acceso independiente a Garmin deben contemplarse desde el inicio. |
| D-007 | El primer resultado útil es consultar actividades y ver la evolución. | La propuesta de primera entrega prioriza historial, detalle y evolución. |
| D-008 | El frontal se desarrollará con Angular. | Quedan pendientes la versión, las bibliotecas y la organización interna. |
| D-009 | La primera versión del frontal incluirá dashboard por usuario, gráficos, histórico, hitos y gestión de usuarios. | Hay que concretar el contenido del dashboard, los hitos y las operaciones y permisos de gestión de usuarios. |
| D-010 | El backend estará preparado desde la primera versión para comunicarse con Garmin y obtener entrenamientos por día y por rango, además de métricas como VFC y sueño. | Validar la cobertura de cada tipo de dato y definir sus campos y criterios temporales. La tecnología y el catálogo de otras métricas siguen abiertos. |
| D-011 | El backend se conectará a la API de OpenAI para enviar prompts con contexto y realizar los análisis solicitados por el usuario. | OpenAI queda elegido para esta integración. Definir análisis, contexto, modelo y límites; la consulta deportiva seguirá funcionando sin IA. D-017 concreta su entrega posterior al dashboard. |
| D-012 | El backend será responsable de la gestión de usuarios. | Definir operaciones, autenticación y permisos, con persistencia asociada a cada cuenta. |
| D-013 | La aplicación contará con una base de datos con capacidad de crecimiento. | Elegir el motor a partir del modelo de datos, las consultas y los volúmenes previstos; la escalabilidad deberá expresarse en objetivos verificables. |
| D-014 | Cada usuario vinculará su Garmin desde el frontal por una vía oficial, conservando la conexión para uso del backend. | Concretado por D-022: botón de autorización sin copiar claves. Modalidad y acceso siguen pendientes de validar. |
| D-015 | Inicialmente cada usuario aportará su acceso API a OpenAI y asumirá el consumo de sus análisis. | La conexión será opcional y separada por usuario. El mecanismo está por validar; no equivale a exigir una suscripción a ChatGPT. |
| D-016 | El proyecto incluirá un objetivo formativo sobre microservicios y evaluará esta arquitectura para el backend. | Acuerdo inicial, concretado por D-018 y D-020: tres servicios independientes desde el inicio. |
| D-017 | La primera entrega será de dashboard y datos; los análisis con IA se incorporarán después. | El servicio de IA no es necesario para completar la primera entrega. La utilidad deportiva se validará antes. |
| D-018 | Se comenzará con pocos servicios que se ejecuten y desplieguen de forma independiente. | Se adopta la separación en servicios por su valor formativo. Concreta D-016; los límites y el número inicial siguen pendientes en P-02. |
| D-019 | El primer uso será solo en el equipo del usuario; el alojamiento se decidirá después. | Se preparará ejecución local de los servicios. El uso inicial local no elimina el destino multiusuario ni acredita la viabilidad de un futuro despliegue compartido. |
| D-020 | Se comenzará con tres servicios: API/orquestación, usuarios y Garmin/datos deportivos. IA se añadirá después. | Usuarios tendrá proceso propio desde el inicio. Se confirma la distribución inicial de P-02; contratos, acceso a datos y autenticación interna siguen pendientes. |
| D-021 | El objetivo inicial es consultar todo el histórico disponible del usuario. | Validar qué histórico se puede recuperar por cada tipo de dato. No se garantiza que la API permita recuperar todos los años existentes en Garmin. |
| D-022 | Garmin se vinculará mediante un botón de autorización oficial, sin que el usuario genere o copie claves; la vinculación se conservará para consultas posteriores. | Investigar la vía oficial que permita este flujo y su renovación. Evitar repetir autorizaciones mientras la conexión sea válida; permitir revincular ante revocación o fallo de renovación. No adoptar claves personales manuales como sustitución implícita. |

D-001 a D-005 proceden del documento inicial. D-006 a D-022 se confirmaron el 30 de octubre de 2026. La propuesta detallada de alcance aún requiere revisión. El usuario ha indicado experiencia en el ecosistema .NET; se tomará como base para la propuesta tecnológica, sin considerar todavía aprobados framework y versión.

## Pendientes clave, en orden de resolución

P-01, P-02 y P-03 están resueltos a nivel de dirección y distribución inicial. En P-06 se ha acordado todo el histórico disponible como objetivo; su viabilidad sigue abierta en P-04. Los demás puntos siguen abiertos. Una propuesta no se considera aceptada por aparecer en esta tabla. Las pruebas técnicas no se sustituyen por una elección de producto.

| ID | Punto y tipo de resolución | Propuesta para revisar | Cuándo se considera cerrado |
| --- | --- | --- | --- |
| P-01 | Resuelto: primera entrega. | Dashboard y datos primero; IA después, según D-017. | Decisión registrada y alcance alineado. |
| P-02 | Resuelto: dirección y distribución inicial. | Tres servicios independientes según D-020: API/orquestación, usuarios y Garmin/datos deportivos. IA después. Repositorios internos propuestos. | Distribución registrada. Contratos, permisos y detalle de persistencia se desarrollan en P-08. |
| P-03 | Resuelto: forma de uso inicial. | Primero en el equipo del usuario; alojamiento posterior, según D-019. | Validar las conexiones para el entorno local. Un futuro despliegue compartido requerirá revisar su encaje. |
| P-04 | Integración oficial con Garmin. Investigación técnica dependiente de P-03. | Botón sin copiar claves confirmado por D-022. Investigar la vía Business/OAuth 2.0, su admisión, retorno local, renovación e histórico. Personal mediante claves manuales no satisface la experiencia acordada. | Modalidad aplicable, condiciones documentadas y prueba autorizada de vinculación persistente, recuperación de datos y desconexión. Las limitaciones quedan explícitas. |
| P-05 | Acceso propio a OpenAI. Investigación técnica dependiente de P-03 y necesaria antes de entregar IA. | Mantener consumo por usuario; comparar los mecanismos oficiales que encajen con el alojamiento elegido. | Se valida un mecanismo y su custodia, renovación y desconexión, y se comprueba una petición asociada al usuario correcto. |
| P-06 | Datos y dashboard. Parcialmente definido, con apoyo de P-04. | Histórico completo disponible confirmado como objetivo. Se propone listado y detalle de running, distancia y duración por periodo, evolución del ritmo, resúmenes de VFC y sueño y pocos hitos. Consultar datos almacenados con fecha de actualización visible. | Se acuerdan indicadores, unidades, hitos, zona horaria, cobertura histórica y sincronización. Análisis y contexto se concretarán antes de entregar IA. |
| P-07 | Tamaño del grupo, acceso y operación. Decisión del usuario. | Primero local. Para abrir al grupo: alta por invitación, datos privados y administrador sin acceso deportivo implícito. Faltan cifras de usuarios, concurrencia, presupuesto y crecimiento. | Antes de datos reales: acceso, secretos y copias locales definidos. Antes de abrir al grupo: tamaño, operaciones, presupuesto y objetivos de recuperación acordados. |
| P-08 | Tecnologías y contratos. Evaluación técnica con P-02 y P-03 resueltos; restricciones de P-04, P-06 y P-07. | Dada la experiencia del usuario, proponer .NET con ASP.NET Core. Framework, versión y librerías pendientes. Comparar persistencia con el histórico y los tres servicios. Alojamiento público se decide después. | Se acuerdan backend, motor de datos, autenticación, contratos, arranque local y límites; se comprueba un recorrido entre servicios. P-05 deberá cerrarse antes de entregar IA. |

P-04 es la principal dependencia externa de la entrega deportiva. P-05 condiciona la entrega con IA. Mientras se verifican, se puede avanzar en documentación y pruebas con datos simulados, sin confundirlas con una integración validada.

## Puntos que pueden esperar

La distribución exacta 70/30, la navegación mediante asistente, Android, MCP y el modelo de consumo pagado por el proveedor se mantienen como evolución futura. La memoria avanzada se concretará después de acordar los primeros análisis; no exige elegir ahora una base vectorial.

## Aclaraciones de la revisión

- La separación de IA en una segunda entrega comenzó como propuesta y ahora está confirmada por D-017.
- La gestión de usuarios del frontal es su interfaz; el backend aplica las operaciones y permisos. No son dos sistemas independientes de usuarios.
- Microservicios, escalabilidad de la base de datos y apertura pública son decisiones distintas. El objetivo formativo justifica evaluar servicios independientes aunque el grupo sea pequeño.
- Las claves, autorizaciones y costes externos pueden pertenecer al usuario; el operador conserva las responsabilidades de integración, custodia y operación que le correspondan.

## Opciones aún abiertas

Se comenzará con tres servicios independientes y se añadirá IA después. La distribución acordada y la propuesta de repositorios internos se describen en [ARQUITECTURA_BACKEND.md](ARQUITECTURA_BACKEND.md). Falta diseñar contratos y persistencia, y confirmar la tecnología a partir de la experiencia en .NET.

Capacitor y Cloudflare siguen siendo propuestas. También están pendientes el lenguaje y entorno del backend, el motor de base de datos, la autenticación y la forma de ejecutar las importaciones. OpenAI está elegido para los análisis, pero el modelo y los detalles de integración siguen abiertos.

La vista simultánea de aplicación y asistente, con distribución orientativa 70/30 y posible navegación mediante el asistente, es una idea futura por madurar. Se describe en [ECOSISTEMA.md](ECOSISTEMA.md); no forma parte de la primera entrega ni es un diseño aprobado.

Si el proyecto crece o se abre al público, se valorará que el proveedor asuma el coste del acceso a OpenAI. Es una alternativa futura pendiente de evaluación. El reparto de responsabilidades y las comprobaciones oficiales están en [CONEXIONES_Y_CONSUMO.md](CONEXIONES_Y_CONSUMO.md).

## Cómo registrar una nueva decisión

Añadir un ID y recoger fecha, decisión, motivo, alternativas relevantes y consecuencias. Cuando sustituya una decisión anterior, conservar la referencia y explicar el cambio. Actualizar después los requisitos y la visión afectados.
