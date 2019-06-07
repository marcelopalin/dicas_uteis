# 1. VSCODE

## 1.1. ALTERAR O TERMINAL DO VSCODE

    Para alterar o Terminal Integrado do Visual Studio Code use:

    CTRL + SHIFT + P

    E digite:

    ```bash
    Terminal: Select Default Shell
    ```

    obs: no Windows se o Terminal demorar para aparecer TECLE enter.


## 1.2. SALVAR OS PACOTES DO VSCODE PARA INSTALAR EM OUTRA MÁQUINA

```bash
    code --list-extensions > extensions.list
```
### 1.2.1. RESTAURANDO NO POWERSHELL WIN

```bash
cat extensions.list |% { code --install-extension $_}
```

### 1.2.2. RESTAURANDO NO LINUX

```bash
cat vscode-extensions.list | xargs -L 1 code --install-extension
```


# 2. PACOTES NPM 

## 2.1. Verificando as Atualizações

```bash
npm outdated
```
Package                            Current       Wanted       Latest  Location
@fortawesome/fontawesome-free        5.8.1        5.8.2        5.8.2
axios                               0.18.0       0.18.0       0.19.0
bootstrap-vue                  2.0.0-rc.19  2.0.0-rc.21  2.0.0-rc.21
core-js                              3.0.1        3.1.3        3.1.3
file-saver                           2.0.1        2.0.2        2.0.2
resolve-url-loader                   2.3.2        2.3.2        3.1.0
vue-notifications                    0.9.0        0.9.0        1.0.0
vue-password                         1.2.0        1.2.0        2.0.2
vue-sweetalert2                      1.6.4        1.6.4        2.0.5
vue-toasted                         1.1.26       1.1.27       1.1.27
vuex                                 3.1.0        3.1.1        3.1.1

## 2.2. ATUALIZANDO DETERMINADO PACOTE PARA A ÚLTIMA VERSÃO

```bash
npm install axios@latest --save
npm install @coreui/coreui@latest --save
npm install laravel-mix@latest --save
npm install sass@latest --save
npm install resolve-url-loader@latest --save
```

## 2.3. ATUALIZE O NPM PARA ULTIMA VERSAO

```bash
npm install npm@latest -g
```

# 3. AUDITANDO OS PACOTES NPM

```bash
npm audit
```


# 4. AUDITANDO AS VULNERABILIDADES

https://docs.npmjs.com/auditing-package-dependencies-for-security-vulnerabilities
https://www.voitanos.io/blog/don-t-be-alarmed-by-vulnerabilities-after-running-npm-install


