# Visión de GolGoLab

## 1. Propósito

Crear una aplicación propia para consultar y analizar entrenamientos y evolución deportiva a partir de Garmin, inicialmente centrada en running. Permitirá trabajar con datos estructurados sin compartir capturas manualmente.

La aplicación debe ser útil por sí misma. Los análisis con IA serán opcionales y conservarán su contexto en la aplicación. El proyecto también servirá para aprender arquitectura de microservicios.

Estado: definición funcional y técnica, previa a la implementación. La guía de lectura está en [README.md](README.md) y los acuerdos completos en [DECISIONES.md](DECISIONES.md).

## 2. Base acordada

| Área | Acuerdo | Lo que aún falta concretar |
| --- | --- | --- |
| Usuarios | Destino inicial de grupo reducido con cuentas separadas; el primer uso será solo en el equipo del usuario. | Tamaño del grupo, operaciones de gestión y alojamiento posterior. |
| Frontal | Angular con dashboard por usuario, gráficos, histórico, hitos y gestión de usuarios. | Indicadores, gráficos, definición de hitos y navegación. |
| Backend | API propia y tres servicios iniciales: API/orquestación, usuarios y Garmin/datos deportivos. IA después. | Tecnología, contratos y autenticación. El usuario tiene experiencia en .NET, base de la propuesta tecnológica. |
| Garmin | Botón de autorización oficial sin copiar claves, con conexión persistente por usuario. Entrenamientos por día y rango, VFC y sueño. | Modalidad, retorno local y renovación aplicables, cobertura efectiva e histórico disponible. |
| IA | API de OpenAI desde el backend para análisis solicitados mediante prompts con contexto. Después de la primera entrega y opcional. | Mecanismo de conexión, modelos, primeros análisis y selección del contexto. |
| Consumo de IA | Inicialmente cada usuario aporta acceso API propio y asume el consumo. | Validación del mecanismo para ejecución local. Modelo pagado por el proveedor solo como posibilidad futura. |
| Persistencia | Base de datos con capacidad de crecimiento y objetivo de consultar todo el histórico disponible; contexto y memoria propios de la aplicación. | Motor, propiedad de datos, cobertura histórica efectiva, volumen y recuperación. |

El requisito de vinculación oficial sin copiar claves no acredita acceso a las APIs. La persistencia evita repetir autorizaciones mientras el acceso sea válido; no garantiza una conexión perpetua. Las limitaciones y fuentes están en [CONEXIONES_Y_CONSUMO.md](CONEXIONES_Y_CONSUMO.md).

## 3. Componentes y límites

El ecosistema se organiza en frontal, backend y persistencia. Garmin y OpenAI son plataformas externas con conexión por usuario. El catálogo funcional está en [ECOSISTEMA.md](ECOSISTEMA.md).

La distribución inicial acordada del backend es API/orquestación, usuarios y Garmin/datos deportivos como servicios independientes, con un servicio de IA posterior. Los repositorios internos por servicio son una propuesta; los contratos y el detalle de persistencia siguen abiertos. El diseño se desarrolla en [ARQUITECTURA_BACKEND.md](ARQUITECTURA_BACKEND.md).

## 4. Entregas y evolución

| Etapa | Resultado esperado | Estado |
| --- | --- | --- |
| Validación previa | Concretar datos y límites de servicios y comprobar acceso oficial a Garmin para ejecución local. | Trabajo necesario antes de implementar la integración dependiente. |
| Primera entrega | Dashboard, consulta y evolución deportiva, gestión de usuarios e integración de datos. Sin IA. | Prioridad confirmada; detalle y aceptación en ALCANCE_Y_REQUISITOS.md. |
| Análisis con IA | Peticiones de análisis con contexto mediante OpenAI. | Posterior a la primera entrega; detalle pendiente. |
| Asistente integrado | Aplicación y asistente persistente, con posible navegación desde este. Reparto orientativo 70/30 en escritorio. | Idea por madurar, sin fecha ni diseño aprobado. |
| Distribución y otras integraciones | Evaluar alojamiento para el grupo, Android mediante Capacitor y acceso desde ChatGPT mediante MCP. | Posibilidades independientes, sin orden cerrado. MCP fuera del alcance inicial. |

No hay fechas, motor de datos ni plataforma de alojamiento aprobados. Cloudflare y Capacitor siguen siendo opciones por evaluar. La forma de alojamiento se revisará cuando se supere la etapa local.

## 5. Contexto y memoria

La aplicación seleccionará el contexto necesario para cada análisis. Como fuentes propuestas se contemplan entrenamientos, métricas, objetivos, preferencias, conversación reciente y resúmenes históricos. El contenido, la conservación y el mecanismo de recuperación se definirán al acordar los primeros análisis.

La información previa de ChatGPT que se quiera conservar deberá incorporarse explícitamente; no se transferirá automáticamente. Mantener la posibilidad de cambiar de modelo o proveedor es un criterio propuesto para el diseño futuro.

## 6. Cómo seguir

Resolver los pendientes por orden en [DECISIONES.md](DECISIONES.md). Los requisitos se mantienen en [ALCANCE_Y_REQUISITOS.md](ALCANCE_Y_REQUISITOS.md) y las pruebas técnicas en [VALIDACION_TECNICA.md](VALIDACION_TECNICA.md).

Al cerrar una cuestión, registrar la decisión y actualizar solo el detalle afectado y esta síntesis cuando cambie la visión. Evitar convertir propuestas en acuerdos o duplicar listas de pendientes en varios documentos.
