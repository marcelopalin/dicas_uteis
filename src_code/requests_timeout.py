import requests
import json
""" 
Vamos entender sobre o requests TIMEOUT utilizando
o auxílio do site https://httpbin.org/


"""


def main():
    try:
        delay = 9 # 1 a 10 seg

        # Quantos segundos esperar a resposta
        
        # Radical - Força do ERRO de Timeout
        # timeout = 0.001 

        # Timeout de 5 segundos
        timeout = 5

        r = requests.get('https://httpbin.org/delay/' + str(delay),
        timeout=5)
        # print(json.dumps(r.json(), indent=2))
        print(json.dumps(r.json(), indent=4, sort_keys=True))

        print('='*40)
        print("Request Successful! Timeout: {} Delay: {}".format(timeout,delay))
        print('='*40)

    except requests.exceptions.ConnectTimeout as err:
        print('ERRO de TIME OUT!!')
    except requests.exceptions.ReadTimeout as err:
        print('ERRO READTIMEOUT de TIME OUT!!')        
    except requests.exceptions.HTTPError as err:
        print ("Http Error:",err)
    except requests.exceptions.ConnectionError as err:
        print ("Error Connecting:",err)
    except requests.exceptions.Timeout as err:
        print ("Timeout Error:",err)
    except requests.exceptions.RequestException as err:
        print ("OOps: Something Else",err)        
        


if __name__ == "__main__":
    main()