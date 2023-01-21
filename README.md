
# Olacy's Vet

O projeto consiste em um trabalho acadêmico de um e-commerce para uma veterinária fictícia, realizado com o framework 
Django o site tem como objetivo realizar vendas de produtos e uma assinatura mensal onde
o cliente receberia uma caixa com diversas surpresas para seu pet. Além de toda a estrutura 
que é necessária na relação empresa e cliente.



## Status

>  Status: Finalizado ✅


## Screenshots

![ezgif-4-19ea250511](https://user-images.githubusercontent.com/71050110/178052749-be1d1a22-fff6-4fe2-895f-adae7be3fd7a.gif)
![ezgif-4-0189017c75](https://user-images.githubusercontent.com/71050110/178052268-8ee42c84-4043-424f-9816-f20217646792.gif)


## Tecnlogias

As seguintes ferramentas foram usadas na construção do projeto:

[Django](https://www.djangoproject.com)

[Docker](https://www.docker.com)

[Mercado Pago API](https://www.mercadopago.com.br/developers/pt/guides/online-payments)
## Pré-requisitos

Antes de começar, você vai precisar ter instalado em sua máquina as seguintes ferramentas:
[Git](https://git-scm.com), [Docker](https://www.docker.com/get-started/). 
Além disto é bom ter um editor para trabalhar com o código como [VSCode](https://code.visualstudio.com/).
## 🎲 Rodando o projeto localmente

Para executar o projeto na pasta em que foi clonado abra o terminal e coloque o comando

```python
# Clone este repositório
$ git clone <https://github.com/olacyrodrigues/OlacyVet>

# No terminal, execute o comando
$ docker-compose up --build

#(opcional) caso queria acessar o container tirando a necessidade de ficar digitando docker-compose exec web em todos comandos basta executar:
$ docker-compose exec web bash

# Não esqueça de rodar as migrations:
 $ docker-compose exec web python manage.py migrate

# Se você quiser criar fotos para os seus produtos, utilize a fixture products.json. As imagens também estão nesse repositório, na pasta media. Para inserir os produtos no banco de dados execute:
$ docker-compose exec web python manage.py loaddata products

# Para criar um super usuario e poder usar a interface de admin use:
$ docker-compose exec web python manage.py createsuperuser

para acessar o site basta seguir este link: http://localhost:8000/
```


## Rodando os testes

Para rodar os testes, rode o seguinte comando

```bash
  docker-compose exec web pytest
```


## Referência

 - [Django 3 By Example](https://www.amazon.com.br/Aprenda-Django-com-Exemplos-Profissionais/dp/658605723X/ref=asc_df_658605723X/?tag=googleshopp00-20&linkCode=df0&hvadid=379748659420&hvpos=&hvnetw=g&hvrand=2034265693739587747&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1001646&hvtargid=pla-944617609858&psc=1)

## 🚀 Sobre mim
<p>Sou um desenvolvedor iniciante em busca constante de conhecimento, sinta-se à vontade para
me procurar em alguma rede social.</p>
<p> ps: não possuo direitos sobrea as imagens, seus usos foram única e exclusivamente para fins de estudo. caso alguém queira a retirada basta entrar em contato.</p>

[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/olacy-rodrigues-449a03170/)

[![Instagram](https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/olacyrodrigues/)

