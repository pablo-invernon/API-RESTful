
# Serverless REST API

Este ejemplo demuestra cómo configurar un [Servicios Web RESTful](https://en.wikipedia.org/wiki/Representational_state_transfer#Applied_to_web_services) que le permite crear, listar, obtener, actualizar y borrar listas de Tareas pendientes(ToDo). DynamoDB se utiliza para persistir los datos. 

Este ejemplo está obtenido del [repositorio de ejemplos](https://github.com/serverless/examples/tree/master/aws-python-rest-api-with-dynamodb) de Serverless Framework. Debido a que el objetivo de la práctica es implementar una serie de Pipelines de CI/CD de diferente manera, el objetivo principal del alumno no será codificar desde cero un servicio. Por eso se ha elegido este caso que aunque no es excesivamente complejo, si representa un reto en determinados puntos, al ser un ecosistema al que probablemente el alumno no estará acostumbrado.
## Estructura

Este repositorio consta de directorio separado para todas las operaciones de la lista de ToDos en Python. Para cada operación existe exactamente un fichero, por ejemplo "todos/delete.py". En cada uno de estos archivos hay exactamente una función definida.

La idea del directorio `todos` es que en caso de que se quiera crear un servicio que contenga múltiples recursos, por ejemplo, usuarios, notas, comentarios, se podría hacer en el mismo servicio. Aunque esto es ciertamente posible, se podría considerar la creación de un servicio separado para cada recurso. Depende del caso de uso y de la preferencia del desarrollador.

La estructura actual del repositorio sería la siguiente:


```
├── package.json
├── pipeline
│   ├── ENABLE-UNIR-CREDENTIALS
│   │   └── Jenkinsfile
│   ├── PIPELINE-FULL-CD
│   │   └── Jenkinsfile
│   ├── PIPELINE-FULL-PRODUCTION
│   │   └── Jenkinsfile
│   └── PIPELINE-FULL-STAGING
│       └── Jenkinsfile
├── README.md
├── serverless.yml
├── terraform
│   ├── configure_environment.sh
│   ├── main.tf
│   ├── outputs.tf
│   ├── resources
│   │   └── get-ssh-key.sh
│   ├── variables.tf
│   └── var.tfvars
├── test
│   ├── TestToDo.py
│   ├── ToDoCreateTable.py
│   ├── ToDoDeleteItem.py
│   ├── ToDoGetItem.py
│   ├── ToDoPutItem.py
│   └── ToDoUpdateItem.py
└── todos
    ├── create.py
    ├── decimalencoder.py
    ├── delete.py
    ├── get.py
    ├── __init__.py
    ├── list.py
    └── update.py
```

Directorios a tener en cuenta:
 - pipeline: en este directorio el alumno deberá de persistir los ficheros Jenkinsfile que desarrolle durante la práctica. Si bien es cierto que es posible que no se puedan usar directamente usando los plugins de Pipeline por las limitaciones de la cuenta de AWS, si es recomendable copiar los scripts en groovy en esta carpeta para su posterior corrección. Se ha dejado el esqueleto de uno de los pipelines a modo de ayuda, concretamente el del pipeline de PIPELINE-FULL-STAGING. 
 - test: en este directorio se almacenarán las pruebas desarrolladas para el caso práctico. A COMPLETAR POR EL ALUMNO
 - terraform: en este directorio se almacenan los scripts necesarios para levantar la infraestructura necesaria para el apartado B de la práctica. Para desplegar el contexto de Jenkins se ha de ejecutar el script de bash desde un terminal de linux (preferiblemente en la instancia de Cloud9). Durante el despliegue de la infraestructura, se solicitará la IP del equipo desde donde se va a conectar al servidor de Jenkins. Puedes consultarla previamente aquí: [cualesmiip.com](https://cualesmiip.com)
 - todos: en este directorio se almacena el código fuente de las funciones lambda con las que se va a trabajar

## Casos de uso

- API for a Web Application
- API for a Mobile Application

## Configuración

```bash
npm install -g serverless
```
## Despliegue con Serverless Framework

De cara a simplificar el despliegue, simplemente habría que ejecutar

```bash
serverless deploy
```

Los resultados esperados deberían de ser así:

```bash
Serverless: Packaging service…
Serverless: Uploading CloudFormation file to S3…
Serverless: Uploading service .zip file to S3…
Serverless: Updating Stack…
Serverless: Checking Stack update progress…
Serverless: Stack update finished…

Service Information
service: serverless-rest-api-with-dynamodb
stage: dev
region: us-east-1
api keys:
  None
endpoints:
  POST - https://45wf34z5yf.execute-api.us-east-1.amazonaws.com/dev/todos
  GET - https://45wf34z5yf.execute-api.us-east-1.amazonaws.com/dev/todos
  GET - https://45wf34z5yf.execute-api.us-east-1.amazonaws.com/dev/todos/{id}
  PUT - https://45wf34z5yf.execute-api.us-east-1.amazonaws.com/dev/todos/{id}
  DELETE - https://45wf34z5yf.execute-api.us-east-1.amazonaws.com/dev/todos/{id}
functions:
  serverless-rest-api-with-dynamodb-dev-update: arn:aws:lambda:us-east-1:488110005556:function:serverless-rest-api-with-dynamodb-dev-update
  serverless-rest-api-with-dynamodb-dev-get: arn:aws:lambda:us-east-1:488110005556:function:serverless-rest-api-with-dynamodb-dev-get
  serverless-rest-api-with-dynamodb-dev-list: arn:aws:lambda:us-east-1:488110005556:function:serverless-rest-api-with-dynamodb-dev-list
  serverless-rest-api-with-dynamodb-dev-create: arn:aws:lambda:us-east-1:488110005556:function:serverless-rest-api-with-dynamodb-dev-create
  serverless-rest-api-with-dynamodb-dev-delete: arn:aws:lambda:us-east-1:488110005556:function:serverless-rest-api-with-dynamodb-dev-delete
```

## Despliegue infraestructura de Terraform para el Apartado BTerraform

En la instancia de Cloud9, simplemente se ha de ejecutar el script de `configure_enviroment.sh`, dentro del directorio de [terraform](https://registry.terraform.io/).
Cuando se pregunte por la IP, indicar la del equipo desde se desea conectar. 
```bash
cd terraform
./configure_environment.sh
```

Si se desea desplegar desde un terminal local, recordar que este script está pensado para ejecutar en un entorno de Linux y que desde local, habrá que configurar las credenciales temporales de la cuenta de Aws Credentials dentro del fichero `~/.aws./credentials` del home del usuario.
## Uso

Se puede crear, lista, coger, actualizar y borrar una tarea, ejecutando los siguientes comandos `curl` desde la línea de comandos del terminal:
### Crear una tarea

```bash
curl -X POST https://XXXXXXX.execute-api.us-east-1.amazonaws.com/dev/todos --data '{ "text": "Learn Serverless" }'
```

No hay salida

### Listar todas las tareas

```bash
curl https://XXXXXXX.execute-api.us-east-1.amazonaws.com/dev/todos
```

Ejemplo de salida:
```bash
[{"text":"Deploy my first service","id":"ac90feaa11e6-9ede-afdfa051af86","checked":true,"updatedAt":1479139961304},{"text":"Learn Serverless","id":"206793aa11e6-9ede-afdfa051af86","createdAt":1479139943241,"checked":false,"updatedAt":1479139943241}]%
```

### Coger una tarea

```bash
# Replace the <id> part with a real id from your todos table
curl https://XXXXXXX.execute-api.us-east-1.amazonaws.com/dev/todos/<id>
```

Ejemplo de salida:
```bash
{"text":"Learn Serverless","id":"ee6490d0-aa11e6-9ede-afdfa051af86","createdAt":1479138570824,"checked":false,"updatedAt":1479138570824}%
```

### Actualizar una tarea

```bash
# Replace the <id> part with a real id from your todos table
curl -X PUT https://XXXXXXX.execute-api.us-east-1.amazonaws.com/dev/todos/<id> --data '{ "text": "Learn Serverless", "checked": true }'
```

Ejemplo de salida:
```bash
{"text":"Learn Serverless","id":"ee6490d0-aa11e6-9ede-afdfa051af86","createdAt":1479138570824,"checked":true,"updatedAt":1479138570824}%
```

### Borrar una tarea

```bash
# Replace the <id> part with a real id from your todos table
curl -X DELETE https://XXXXXXX.execute-api.us-east-1.amazonaws.com/dev/todos/<id>
```

No output

## Escalado

### AWS Lambda

Por defecto, AWS Lambda limita el total de ejecuciones simultáneas en todas las funciones dentro de una región dada a 100. El límite por defecto es un límite de seguridad que le protege de los costes debidos a posibles funciones desbocadas o recursivas durante el desarrollo y las pruebas iniciales. Para aumentar este límite por encima del predeterminado, siga los pasos en [Solicitar un aumento del límite para las ejecuciones simultáneas] (http://docs.aws.amazon.com/lambda/latest/dg/concurrent-executions.html#increase-concurrent-executions-limit).

### DynamoDB

Cuando se crea una tabla, se especifica cuánta capacidad de rendimiento provisto se quiere reservar para lecturas y escritos. DynamoDB reservará los recursos necesarios para satisfacer sus necesidades de rendimiento mientras asegura un rendimiento consistente y de baja latencia. Usted puede cambiar el rendimiento provisto y aumentar o disminuir la capacidad según sea necesario.

Esto se puede hacer a través de los ajustes en el `serverless.yml`.
```yaml
  ProvisionedThroughput:
    ReadCapacityUnits: 1
    WriteCapacityUnits: 1
```

En caso de que esperes mucha fluctuación de tráfico, te recomendamos que consultes esta guía sobre cómo escalar automáticamente el DynamoDB [https://aws.amazon.com/blogs/aws/auto-scale-dynamodb-with-dynamic-dynamodb/](https://aws.amazon.com/blogs/aws/auto-scale-dynamodb-with-dynamic-dynamodb/)