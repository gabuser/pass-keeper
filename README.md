# pass keeper<br>
### sumário 📚
- [🔍 INTRODUÇÃO](#introdução-do-projeto)
- [⚙️ INSTALAÇÃO](#como-baixar)
- [🚀 INSTRUÇÕES](#como-usar)
- [🏁 FINALIZAÇÃO](#considerações-finais)

### introdução do projeto

Pass Keeper é um gerenciador de senhas simples, desenvolvido com o objetivo de estudar lógica de programação e banco de dados. O projeto visa armazenar senhas localmente no computador do usuário, garantindo maior privacidade e segurança.

Ao contrário de soluções baseadas na nuvem, o Pass Keeper permite que o usuário gerencie suas senhas sem limitações de espaço, estando restrito apenas ao armazenamento disponível no seu próprio dispositivo.

Este projeto é uma base para aprendizado e pode — e deve — ser aprimorado continuamente para oferecer mais funcionalidades e segurança e também para ser otimizado com o tempo.

# como baixar? 
### sem precisar usar o git para baixar
> Code > Download zip
### baixando as dependências
>pip install -r requirements.txt

> ⚠️ **ATENÇÃO**<br>
> Python precisa ser instalado antes do requirements.txt para que possa funcionar corretamente <br>

site oficial:```https://www.python.org/downloads/```

> ❕	**AVISO**<br>
>Caso o python não for instalado, erros inesperados podem ocorrer.

# como usar?
### chave usada para criptografar os dados🔒
>Ao logar na sua conta criada, o script irá fornecer uma chave que será usada para criptografar e descriptografar os seus dados. Aparece logo quando você loga na conta se ainda não possuir uma.

>⚠️CUIDADO: <br>
>Após perder não será possível recuperar as senhas armazenadas.

>Não compartilhe essa senha com ninguém, caso contrário, essa pessoa poderá acessar seus dados sensíveis.

> 💡DICA: Você pode guardar nesse gerenciador ou em outro local que você considere seguro.

### como usar os recursos de recuperação de conta?📪
>Para usar é necessário que você faça as configurações necessárias na sua conta gmail para permitir que essa aplicação possa se comunicar com os serviços do google.

> Em seguida, você precisa entrar nesse link abaixo e criar uma senha chamada de "app passwords"

>🔗 Links para auxiliar abaixo:
```
https://myaccount.google.com/apppasswords
```
```
https://www.youtube.com/watch?v=ZfEK3WP73eY
```
>💡DICA: <br>
>após você gerar uma senha em "app passwords", então você vai copiar ela e guardar nessa aplicação.

>Vá na terceira opção nesta aplicação, aperte a opção 3 e cola essa senha lá.

# considerações finais💭
### Projeto 🧾
> Esse projeto foi feito com o intuito de aprendizagem, isso significa que pode conter vulnerabilidades que não foram exploradas por mim.

### testes🚧
> Ainda precisa ser feito testes em outros computadores por outros usuários, sinta-se a vontade para testa-lo e relatar possível problemas de funcionamento.

> É recomendável que você coloque uma permissão específica no arquivo.db, porque ainda não foi implementado Uma forma de segurança contra deleções acidentais ou propositais desse arquivo. Isso porquê ainda está na fase inicial.

## Dependências

Este projeto utiliza as seguintes bibliotecas externas:

- [bcrypt](https://pypi.org/project/bcrypt/) — Licença Apache 2.0  
- [cryptography](https://pypi.org/project/cryptography/) — Licença Apache 2.0  

As licenças dessas bibliotecas são independentes da licença deste projeto. Por favor, consulte os repositórios oficiais para mais detalhes.