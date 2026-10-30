# Conexiones externas y responsabilidad del consumo

## 1. Modelo inicial confirmado

- Cada usuario vinculará su propia cuenta de Garmin desde un botón de autorización en el frontal, sin generar ni copiar claves. Es un requisito de experiencia confirmado; la vía oficial aplicable aún debe validarse.
- La vinculación quedará guardada y asociada al usuario para que el backend pueda obtener sus datos sin repetir la autorización en cada consulta, inicio de sesión o reinicio de la aplicación, mientras siga siendo válida.
- Quien active los análisis con IA deberá aportar inicialmente su propio acceso a la API de OpenAI y asumir el consumo correspondiente. No será un requisito para consultar sus actividades.
- El usuario gestionará sus cuentas externas, su acceso, los créditos o facturación necesarios y las renovaciones que le correspondan.
- La aplicación gestionará las conexiones, protegerá las credenciales que custodie y mantendrá las integraciones. El modelo de cuentas propias no elimina estas responsabilidades.

La identidad de GolGoLab y las vinculaciones externas son conceptos separados. Tener una cuenta de GolGoLab no implica disponer de acceso a Garmin ni a OpenAI.

El primer uso será en el equipo del usuario; el alojamiento posterior no está elegido. Las vinculaciones deberán validarse para este entorno, incluidos los posibles retornos de autorización a la aplicación local. El destino de grupo reducido sigue vigente; ejecutar localmente no acredita que la modalidad elegida admita después un servicio compartido.

## 2. Experiencia de vinculación propuesta

Desde su cuenta, el usuario podrá ver el estado de cada conexión, iniciar la vinculación, volver a autorizar o sustituir credenciales cuando sea necesario y desconectarla. La conexión a OpenAI será opcional e independiente de Garmin.

El frontal iniciará el proceso. El backend verificará el resultado y mantendrá las credenciales necesarias, vinculadas al propietario y protegidas en el servidor. La interfaz mostrará el estado de conexión sin devolver secretos guardados ni conservarlos en almacenamiento persistente del navegador. El almacenamiento concreto de secretos está pendiente de diseño.

No se solicitará ni guardará la contraseña de Garmin o de OpenAI como mecanismo de vinculación. Tampoco se guardará una sesión de navegador como sustituto de una autorización oficial.

Desconectar una plataforma impedirá nuevas peticiones con esa conexión. La eliminación de los datos ya importados o de los análisis guardados se definirá por separado. La caducidad, la revocación y los problemas de acceso o de saldo se mostrarán de forma diferenciada.

### Vinculación de Garmin: comportamiento requerido

1. El usuario inicia sesión en GolGoLab y pulsa «Vincular Garmin».
2. Se abre la autorización oficial de Garmin, donde el usuario se identifica y concede los permisos necesarios. GolGoLab no recibe su contraseña.
3. El backend procesa el resultado y el servicio Garmin/datos deportivos conserva la vinculación de forma protegida, asociada al usuario correcto.
4. Las consultas posteriores usan la autorización guardada. Se renovarán las credenciales automáticamente si el mecanismo oficial lo permite.
5. Si el acceso se revoca o no puede renovarse, se mostrará «Volver a vincular». El usuario también podrá desconectar la cuenta.

El requisito de autorizar inicialmente no significa que la conexión sea perpetua. La caducidad de un token de acceso debería resolverse sin intervención cuando exista un mecanismo válido de renovación; sus condiciones se comprobarán antes de implementar.

Como modelo de persistencia propuesto, guardar el propietario local, la referencia a la identidad de Garmin, los permisos disponibles, fechas de caducidad, estado y referencias a los tokens protegidos. Un token de renovación solo se conservará si lo proporciona la vía validada. Los secretos se custodiarán cifrados o en un almacén de secretos del backend, con la clave de protección separada; el motor y el esquema concretos siguen abiertos.

Este requisito se refiere a Garmin. El mecanismo de conexión con OpenAI continúa pendiente de evaluación independiente.

## 3. Garmin: vías oficiales por evaluar

Consulta documental: 30 de octubre de 2026. No se ha probado ni aprobado una integración para GolGoLab.

Garmin distingue acceso Personal y Business. Personal permite obtener una clave en Garmin Connect y generar tokens para consultar los datos propios; Business está orientado a integraciones para varios usuarios. Por tanto, no se puede dar por disponible un botón de autorización para este proyecto solo porque cada usuario tenga una cuenta de Garmin. [Descripción oficial](https://developer.garmin.com/gc-developer-program/overview/).

La FAQ de Personal describe generación manual de claves personales y su uso para obtener tokens. Por sí sola esa vía no satisface el requisito acordado de autorización sin copiar claves. No se adopta como sustituto automático del botón de vinculación. [FAQ oficial de Personal](https://developer.garmin.com/gc-developer-program/personal/personal-faq).

La FAQ de Business confirma OAuth 2.0 y sitúa la documentación técnica detallada en el portal de desarrolladores, tras la aprobación del acceso. Es la vía que se debe investigar para comprobar el consentimiento, registro de aplicación, retorno local y renovación; mencionar OAuth 2.0 no acredita que GolGoLab tenga acceso ni que todos los detalles del flujo estén validados. El operador podría necesitar credenciales de aplicación, aunque el usuario final no copie claves. [FAQ oficial de Business](https://developer.garmin.com/gc-developer-program/enterprise/program-faq/).

Hay que comprobar además acceso al histórico y cobertura de entrenamientos, VFC y sueño. El botón oficial es un requisito confirmado, no una capacidad ya validada.

El usuario quiere consultar todo su histórico disponible. La descripción oficial de Business Starter indica entrega mediante push y no incluye datos históricos; no cubre por sí sola ese objetivo retroactivo. La documentación revisada de Personal tampoco acredita una recuperación histórica completa. Hace falta comprobar la cobertura real por tipo de dato antes de prometer la importación completa. [Modalidades y cobertura histórica oficiales](https://developer.garmin.com/gc-developer-program/overview/).

## 4. OpenAI: acceso propio y mecanismo de conexión

Consulta documental: 30 de octubre de 2026. Modelo económico confirmado; mecanismo de conexión pendiente.

La API estándar documenta autenticación mediante claves de API, entre otras credenciales, y exige protegerlas en el servidor. Usar una clave del proyecto del usuario es una opción a evaluar; no se considera un flujo de login ya aprobado ni se implementará la recogida de claves sin validar su encaje. [Autenticación oficial](https://developers.openai.com/api/reference/overview).

OpenAI también documenta Sign in with ChatGPT. La capacidad de utilizar el plan del usuario se describe para aplicaciones abiertas y alojadas localmente; para aplicaciones de pago o alojadas remotamente remite a un formulario de interés. No se presupone que GolGoLab pueda utilizarla por el mero hecho de ofrecer un login. [Uso del plan mediante Sign in with ChatGPT](https://developers.openai.com/siwc/token-sharing-open-source).

El requisito es disponer de acceso API habilitado y capacidad de consumo. No se exige por definición una suscripción a ChatGPT: existen beneficios de créditos API para determinados planes elegibles, con activación y condiciones propias. Habrá que verificar los derechos concretos de cada cuenta al configurar la conexión. [Créditos API para suscriptores](https://developers.openai.com/api/docs/guides/chatgpt-api-credits).

En el modelo inicial no se utilizará automáticamente una credencial pagada por el proveedor si falla la del usuario. El backend deberá utilizar únicamente la conexión correspondiente al solicitante y comunicar los problemas de acceso o consumo.

## 5. Posible evolución: consumo de IA a cargo del proveedor

Si el proyecto crece o se abre al público, se valorará que el proveedor de GolGoLab contrate y pague el acceso API y ofrezca los análisis como parte del servicio. Es una posibilidad, no una decisión de lanzamiento.

Antes de ese cambio habría que definir costes por usuario, límites de consumo, política comercial, mecanismos para evitar gasto no previsto y condiciones de transición. Conviene distinguir desde el diseño al propietario de los datos de quien asume el consumo, sin implementar ahora ambos modelos.

## 6. Validaciones pendientes

- Modalidad oficial de Garmin compatible con el grupo y el despliegue previsto.
- Mecanismo permitido de acceso propio a OpenAI para la ejecución local inicial y nueva evaluación si se pasa a un backend compartido.
- Custodia, renovación, sustitución y revocación de credenciales por plataforma.
- Comportamiento al desconectar: datos conservados, peticiones en curso y permisos revocados.
- Información sobre consumo que puede ofrecerse al usuario y límites que puede aplicar la aplicación.

Estas validaciones completan las de [VALIDACION_TECNICA.md](VALIDACION_TECNICA.md).
