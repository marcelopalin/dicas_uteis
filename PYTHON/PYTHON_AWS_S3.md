# 1. AWS S3 BUCKET - PYTHON 3.6+ BOTO3

https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html

Para gerenciar seu Bucket (s3) na Amazon você necessita de um usuário com permissões.

https://realpython.com/python-boto3-aws-s3/

http://www.oznetnerd.com/python-demystifying-aws-boto3/

Múltiplas credenciais:
https://aws.amazon.com/pt/blogs/security/a-new-and-standardized-way-to-manage-credentials-in-the-aws-sdks/

## 1.1. Instalação

Em geral instalamos no ambiente virtual de um projeto de python3, porém, é possível instalar no SO Geral.

```bash
pip3 install boto3
```

Você tem o SDK. Mas você não poderá usá-lo agora, porque não sabe a qual conta da AWS ele deve se conectar.

Para que seja executado em sua conta da AWS, você precisará fornecer algumas credenciais válidas. Se você já tiver um usuário do IAM que tenha permissões totais para o S3, poderá usar as credenciais desse usuário (sua chave de acesso e sua chave de acesso secreta) sem precisar criar um novo usuário. Caso contrário, a maneira mais fácil de fazer isso é criar um novo usuário da AWS e, em seguida, armazenar as novas credenciais.


## 1.2. Como criar um usuário com permissões para Gerenciar meu Bucket?

### 1.2.1. Criando um usuário (programático) ADMIN para S3

Para criar um novo usuário, acesse sua conta da AWS:

- vá para Serviços e selecione IAM. 
- Em seguida, escolha Usuários e clique em Adicionar usuário.

Dê ao usuário um nome (por exemplo, boto3user ). Ativar acesso programático. Isso garantirá que esse usuário possa trabalhar com qualquer SDK compatível com o AWS ou fazer chamadas de API separadas.

Verifique se Access Type (x) Programmatic access

### 1.2.2. Escolha a Política de Acesso - Full Access

Para simplificar utilize o Full Acesss e no final guarde o ID e a Access Key.



### 1.2.3. Usuário com restrições para Gerenciar apenas 1 Bucket

Ao adicionar um usuário escolha "adicionar política em linha":

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": [
                "s3:ListBucket",
                "s3:GetBucketLocation"
            ],
            "Resource": "arn:aws:s3:::meubucket"
        },
        {
            "Sid": "VisualEditor1",
            "Effect": "Allow",
            "Action": [
                "s3:PutObject",
                "s3:GetObject",
                "s3:DeleteObject",
            ],
            "Resource": "arn:aws:s3:::meubucket/*"
        }
    ]
}
```

## 1.3. Programa para Listar os Buckets

```

```


## 1.4. Programa de como enviar uma pasta para o S3


```python
import boto3
import os
 
def upload_files(path):
    session = boto3.Session(
        aws_access_key_id='YOUR_AWS_ACCESS_KEY_ID',
        aws_secret_access_key='YOUR_AWS_SECRET_ACCESS_KEY_ID',
        region_name='YOUR_AWS_ACCOUNT_REGION'
    )
    s3 = session.resource('s3')
    bucket = s3.Bucket('YOUR_BUCKET_NAME')
 
    for subdir, dirs, files in os.walk(path):
        for file in files:
            full_path = os.path.join(subdir, file)
            with open(full_path, 'rb') as data:
                bucket.put_object(Key=full_path[len(path)+1:], Body=data)
 
if __name__ == "__main__":
    upload_files('/path/to/my/folder')
```




# 2. AWS CLI

A AWS Command Line Interface (CLI, interface da linha de comando) é uma ferramenta unificada para o gerenciamento de seus serviços da AWS. Com apenas uma ferramenta para fazer o download e configurar, você poderá controlar vários serviços da AWS pela linha de comando e automatizá-los usando scripts.

A CLI da AWS apresenta um novo conjunto de comandos de arquivos simples para transferências eficientes de arquivos para e do Amazon S3.

## 2.1. Instalação

Crie o ambiente virtual do projeto:

```
virtualenv -p python3 venv
```

Ative o ambiente virtual:

```bash
source venv\bin\activate
```

## 2.2. Verificando a Versão

```bash
aws --version

aws-cli/1.16.124 Python/3.6.7 Linux/4.15.0-46-generic botocore/1.12.114
```

## Configurando as Credenciais de Acesso

Quando você criou seu usuário IAM, você baixou (ou anotou) seu ID e sua Access Key:

Você precisará deles para concluir sua configuração.

Agora que você tem seu novo usuário, crie um novo arquivo ~/.aws/credentials:

$ touch ~ / .aws / credentials
Abra o arquivo e cole a estrutura abaixo. Preencha os espaços reservados com as novas credenciais de usuário que você baixou:

[padrão] 
aws_access_key_id  =  YOUR_ACCESS_KEY_ID 
aws_secret_access_key  =  YOUR_SECRET_ACCESS_KEY
Salve o arquivo.

Agora que você configurou essas credenciais, você tem um defaultperfil, que será usado pela Boto3 para interagir com sua conta da AWS.

Há mais uma configuração para configurar: a região padrão com a qual o Boto3 deve interagir. Você pode conferir a tabela completa das regiões da AWS compatíveis . Escolha a região mais próxima de você. Copie sua região preferida da coluna Região . No meu caso, estou usando eu-west-1 (Irlanda).

Crie um novo arquivo ~/.aws/config:

$ toque ~ / .aws / config
Adicione o seguinte e substitua o espaço reservado pelo que regionvocê copiou:

[padrão] 
region  =  YOUR_PREFERRED_REGION
Salve seu arquivo.
