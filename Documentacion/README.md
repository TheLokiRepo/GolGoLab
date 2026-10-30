# Documentación de GolGoLab

Estado: definición previa a la implementación.

El objetivo es concretar qué debe resolver la aplicación y comprobar su viabilidad antes de elegir una arquitectura definitiva.

## Síntesis del proyecto

GolGoLab tendrá un frontal Angular y una API propia para un grupo reducido con cuentas separadas. Cada usuario consultará su dashboard, gráficos, histórico e hitos a partir de los entrenamientos y métricas disponibles en Garmin, incluidos VFC y sueño. El contenido concreto del panel sigue pendiente.

El backend gestionará usuarios, conexiones y datos, y ofrecerá análisis opcionales con OpenAI mediante prompts con contexto. Inicialmente cada usuario aportará su acceso a OpenAI y asumirá su consumo. La aplicación conservará su propia memoria contextual.

Se empezará con tres servicios independientes: API/orquestación, usuarios y Garmin/datos deportivos. Se ejecutarán primero en el equipo del usuario. El usuario tiene experiencia en .NET, que orienta la propuesta tecnológica. El motor de datos y el alojamiento posterior siguen abiertos. Se desea consultar todo el histórico disponible, sujeto a verificar el acceso. La primera entrega será de dashboard y datos; IA llegará después como servicio adicional. Como evolución se contempla un asistente persistente, Android y, fuera del alcance inicial, MCP.

## Qué necesitamos resolver ahora

El orden de decisión y los criterios para cerrar cada punto están centralizados en [DECISIONES.md](DECISIONES.md). Ya se han confirmado la entrega sin IA, el uso de servicios independientes y el comienzo local. Las integraciones requieren además comprobación técnica.

1. **Primera entrega, confirmado:** dashboard y datos; IA después.
2. **Arquitectura inicial, confirmado:** API/orquestación, usuarios y Garmin/datos deportivos independientes. Faltan contratos y tecnología; .NET es la propuesta basada en la experiencia del usuario.
3. **Forma de uso, confirmado:** primero en el equipo del usuario; alojamiento posterior.
4. **Viabilidad externa:** comprobar la modalidad oficial de Garmin y, cuando corresponda, el acceso propio a OpenAI para la forma de alojamiento elegida.
5. **Dimensionamiento y detalle:** métricas, hitos, histórico, sincronización, altas de usuarios y presupuesto. Con ello se podrán elegir backend, base de datos y alojamiento.

## Distinciones que guían el diseño

- Las funcionalidades deportivas deben funcionar sin IA, aunque se decida entregar ambas en la misma versión.
- El asistente persistente y su navegación son una evolución distinta de ofrecer análisis bajo demanda.
- Las conexiones externas pertenecen a cada usuario; la aplicación mantiene la integración y protege las credenciales que gestione.
- Garmin debe vincularse mediante botón oficial sin copiar claves. La conexión se conserva mientras sea válida; la modalidad y la renovación necesitan validación técnica.
- Un componente funcional no equivale necesariamente a un proceso o microservicio.
- El acceso a datos puede resolverse mediante repositorios internos; un motor escalable no exige un servicio genérico de persistencia.

## Guía de lectura

| Documento | Contenido |
| --- | --- |
| [PROYECTO.md](PROYECTO.md) | Visión general, acuerdos y posibles vías de evolución. |
| [ECOSISTEMA.md](ECOSISTEMA.md) | Componentes, responsabilidades y evolución prevista. Frontal Angular, backend con Garmin y OpenAI, y persistencia; catálogo en construcción. |
| [ARQUITECTURA_BACKEND.md](ARQUITECTURA_BACKEND.md) | Servicios independientes, objetivo formativo, límites candidatos y ejecución local. |
| [CONEXIONES_Y_CONSUMO.md](CONEXIONES_Y_CONSUMO.md) | Vinculaciones por usuario, responsabilidad de consumo y vías oficiales pendientes de validar. |
| [ALCANCE_Y_REQUISITOS.md](ALCANCE_Y_REQUISITOS.md) | Primera entrega, recorrido de usuario y criterios para comprobar que funciona. |
| [DECISIONES.md](DECISIONES.md) | Decisiones confirmadas y cuestiones que requieren una respuesta. |
| [VALIDACION_TECNICA.md](VALIDACION_TECNICA.md) | Comprobaciones necesarias sobre Garmin, datos, seguridad y alojamiento. |

El diagrama general está al principio de [ECOSISTEMA.md](ECOSISTEMA.md), con versiones [PNG](diagramas/ecosistema.png), [SVG](diagramas/ecosistema.svg) y [fuente editable en Mermaid](diagramas/ecosistema.mmd). Distingue el alcance inicial, los componentes posteriores y las funciones de operación.

## Cómo mantener estos documentos

- **Confirmado:** acordado explícitamente; sirve como base del proyecto.
- **Propuesto:** punto de partida para debatir; todavía no es un compromiso.
- **Pendiente:** falta una respuesta o una comprobación con evidencia.

PROYECTO.md resume la visión. Cada documento de detalle desarrolla su área; DECISIONES.md es la referencia para el estado de los acuerdos y la prioridad de los pendientes. Las preguntas locales de los demás documentos desarrollan esos puntos y no constituyen prioridades adicionales. Si una decisión cambia, se registra el motivo y se actualizan los documentos afectados.

## Próximo paso

Validar qué vía oficial de Garmin cubre la ejecución local y cuánto histórico permite recuperar de entrenamientos, VFC y sueño. Concretar métricas, hitos y sincronización y revisar la propuesta .NET antes de elegir persistencia y contratos. No es necesario cerrar ahora Android, la distribución 70/30, el alojamiento público, el modelo comercial futuro ni la memoria avanzada.
