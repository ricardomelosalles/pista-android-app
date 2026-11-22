# Pista – app Android

Este projeto transforma o Pista em app Android que **grava o GPS com a tela bloqueada** (com a notificação "Pista · gravando corrida").

## Gerar o APK (sem instalar nada no computador)
1. No GitHub, crie um repositório novo (ex.: `pista-android`) e envie **todo o conteúdo desta pasta**, incluindo a pasta oculta `.github`. Se ela não subir, crie o arquivo `.github/workflows/build-apk.yml` pelo GitHub (Add file > Create new file) e cole o conteúdo do arquivo de mesmo nome.
2. Abra a aba **Actions**, escolha **Gerar APK** e toque em **Run workflow**. Leva de 5 a 10 minutos.
3. Quando terminar, abra a execução e baixe o arquivo **Pista-apk** (em Artifacts). Extraia o zip: dentro está o `app-debug.apk`.
4. Passe o APK para o celular e instale (permita "instalar apps desconhecidos" para o navegador ou gerenciador de arquivos).

## Primeiro uso
- Permissão de localização: **Durante o uso do app** basta. Permita também as notificações.
- Redmi/MIUI: em Configurações > Apps > Pista, ative **Inicialização automática** e, em Economia de bateria, escolha **Sem restrições**.

## Limitações
- Monitor cardíaco por Bluetooth não funciona no app (só no Chrome). O campo manual de bpm continua.
- Salvar foto, GPX e backup abre a folha de compartilhar do Android: escolha Arquivos, Drive ou Galeria.
- O arquivo `www/index.html` é o mesmo da versão web: quando alterar o app, copie o novo para `www/` e o GitHub gera outro APK.
