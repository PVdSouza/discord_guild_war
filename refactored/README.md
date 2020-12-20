# Documentação (yes)

## GuildSystem

### [Building.py](building.py)

Nesse arquivo estão as configurações das buildings, é aqui que os novos tipos de building devem ser adicionados.
Ele utiliza alguns padrões de organização para que seja fácil adicionar, modificar e remover tipos diferentes de buildings.

**Esse não é um arquivo de classe**: As funções contidas nesse arquivo são funções de direta modificação em buildings (inclusive, nenhuma função sequer tem acesso à informações do objeto guilda), portanto eles não possuem lógica de controle, por exemplo:

- A função level_up modifica a building diretamente. Ela não verifica se essa building pode ser atualizada, se o dono possui recursos suficientes ou algo do gênero.
- A função create_building não verifica se a guilda já possui outra building daquele tipo.

Os tipos de building atuais são: Hall, Mine, Quarry e Cabin.
A função de crescimento de custos de recursos para upar para o próximo nível é: custo_inicial * nivel.
A função de production_rate das buildings é: 2 * nivel.

### [Guild.py](guild.py)

Nesse arquivo estão as configurações de guilds, possui funções para serialização das mesmas, e elas são responsáveis pelo controle de suas buildings.
Ele utiliza alguns padrões de organização para que seja fácil adicionar, modificar e remover configurações de guild.

**Esse não é um arquivo de classe**: As funções contidas nesse arquivo são funções de direta modificação em guilds, portanto eles não possuem lógica de controle sobre as mesmas, por exemplo:

- A função level_up_building modifica uma building fazendo todo o controle necessário. Ela verifica se essa building pode ser atualizada, se o dono possui recursos suficientes, etc.
- Uma futura função de ataque de uma guild A vs guild B não estará nesse arquivo, nele só estará uma função receive_damage, ou update_power por exemplo. Uma função para controlar um ataque será implementada em um arquivo específico.

### [Main.py](main.py)

Arquivo em que o Pedro testa coisas, é só isso mesmo.

## [Sample.py](../sample.py)

Bicho, complicado isso aqui hein
