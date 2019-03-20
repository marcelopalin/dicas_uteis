# Editando JOBS do Crontab com Python

Simples e útil.

Vamos supor que você possua um script python que deve ser rodado em horários específicos.
Neste caso, vamos supor que seja às 8H10M a rodada do MEU_SCRIPT.py e o comentário dele
seja 'MEU_SCRIPT_PRINCIPAL'

Ex:
```
10 8 * * * /usr/bin/python3 /home/ubuntu/projeto/MEU_SCRIPT.py >> /home/ubuntu/logs/cron_meu_script.log # MEU_SCRIPT_PRINCIPAL
```

Se rodarmos o código abaixo acessaremos o CRON do usuário **ubuntu**:

```python

        # Crontab
        from crontab import CronTab
        my_cron = CronTab(user='ubuntu')

        # Imprime todas os JOBS do CRON
        for job in my_cron:
            print(job)

        # E
        iter1 = my_cron.find_command('MEU_SCRIPT.py')  
        iter2 = my_cron.find_comment('MEU_SCRIPT_PRINCIPAL')  
        iter3 = my_cron.find_time("10 8 * * *")

        for job1 in iter1:  
            print(job1)

        for job2 in iter2:  
            print(job2)

        for job3 in iter3:  
            print(job3)

        # Removendo um Job
        my_cron.remove(job2)

        # Criando uma Linha no Cron
        job = my_cron.new(command='/usr/bin/python3 /home/ubuntu/rodada/NOVO_SCRIPT.py >> /home/ubuntu/logs/cron_novo.log', comment='NOVO_SCRIPT')
        # Definindo o tempo de execucao
        job.minute.every(1) # */1 * (a cada 1 minuto)
        job.hour.every(10)  # * */10 (a cada 10 horas)

        # Resumo ficará

        # Verificando se é válido
        job.is_valid()

        # Escrevendo as alterações
        my_cron.write()

        # Outra maneira de encontrar o JOB por comentário
        for job in my_cron:
            if job.comment == 'NOVO_SCRIPT':
                print(job)
```


## Compensação de trabalhos de Crontab

python-crontabfornece métodos para limpar ou remover trabalhos de crontab. 
Você pode remover um cron job do crontabbaseado no agendamento, comentário ou comando.
Vamos dizer que você quer limpar o trabalho com o comentário dateinfodo crontab. O código seria:

```python
from crontab import CronTab
 
my_cron = CronTab(user='roy')
for job in my_cron
    if job.comment == 'dateinfo':
        my_cron.remove(job)
        my_cron.write()
```

Da mesma forma, para remover um trabalho com base em um comentário, você pode chamar diretamente o removemétodo my_cronsem nenhuma iteração. Aqui está o código:

```python
my_cron.remove(comment='dateinfo')
```

Para remover todos os trabalhos do crontab, você pode chamar o remove_allmétodo.

```python
my_cron.remove_all()
```

Uma vez feito com as alterações, escreva de volta para o cron usando o seguinte comando:

```python
my_cron.write()
```


## Calculando a Frequência do Trabalho

Para verificar quantas vezes seu trabalho é executado usando python-crontab, 
você pode usar o frequency método. Depois de ter o trabalho, você pode chamar 
o método chamado frequency, que retornará o número de vezes que o 
trabalho é executado em um ano.

```

from crontab import CronTab
 
my_cron = CronTab(user='roy')
for job in my_cron:
    print job.frequency()

```

Para verificar o número de vezes que o trabalho é executado em uma hora, você pode usar o método frequency_per_hour.

```python
my_cron = CronTab(user='roy')
for job in my_cron:
    print job.frequency_per_hour()
```    

Para verificar a frequência do trabalho em um dia, você pode usar o método **frequency_per_day**. 


## Verificando o cronograma de trabalho

python-crontab fornece a funcionalidade para verificar o agendamento de um trabalho específico. 
Para que isso funcione, você precisará que o **croniter** módulo seja instalado em seu sistema. 

```bash
pip install croniter
```

Depois de ter **croniter** instalado, ligue para o método de agendamento no trabalho para obter o agendamento de trabalho.

```python
sch = job.schedule(date_from=datetime.datetime.now())
```

Agora você pode obter o próximo agendamento de trabalho usando o get_nextmétodo.

```python
print(sch.get_next())
```

Aqui está o código completo:

```python
import datetime
from crontab import CronTab
 
my_crons = CronTab(user='jay')
for job in my_crons:
    sch = job.schedule(date_from=datetime.datetime.now())
    print sch.get_next()
```

Você pode até obter o agendamento anterior usando o  **get_prev** método.