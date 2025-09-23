
<img width="554" height="370" alt="image" src="https://github.com/user-attachments/assets/efa57d3f-7c9d-4b33-afeb-56fe3e1132bf" />
Neste diagrama temos as entidades: Usuario, Cliente, Servicos, Agenda e Administrador. Elas trabalham juntas
para formar a estrutura do site do salao de cabelos, permitindo que os usuarios agendem servicos, enquanto os
administradores supervisionam e controlam as atividades do sistema. A seguir uma breve explicacao de cada uma
delas:
• Usuario: Representa qualquer pessoa que use o sistema. E a classe base que contem informacoes comuns
a todos os usuarios, como ID, nome, e-mail.
• Cliente: Extensao da classe Usuario, que inclui funcoes especıficas para clientes.
• Servicos: Representa um tipo de servic¸o que e oferecido pelo salao de beleza e pode ser agendado pelo
cliente.
• Agenda: Horarios disponıveis para agendamento de algum servic¸o.
• Administrador: Representa o usuario que ir a gerenciar o sistema, podendo tambem cadastrar, alterar e
remover outros usuarios.
5.3 Diagramas de casos de uso
A Figura 2 mostra o Diagrama de Casos de Uso para o site do Salao de Beleza. O principal ator envolvido ´e o
Usuario Cadastrado. O ator esta relacionado a diferentes funcoes dentro da plataforma, como a realizacao de
cadastro, selecao de agendamento, visualizacao de perfil, edicao de perfil e gerencia de agendamento.

<img width="476" height="418" alt="image" src="https://github.com/user-attachments/assets/cf987e47-9d32-43ea-9c57-eb94dc8faaef" />

5.4 Diagramas de sequ ˆencia
A Figura 3 apresenta o diagrama de sequencia que representa os principais fluxos de interacão entre os compo-
nentes da aplicacao, abrangendo os processos de cadastro e login, criacao agendamentos, visulizacao de servicos
e edição de perfil. Esse diagrama descreve, de forma detalhada, a troca de mensagens entre os elementos do
sistema ao longo do tempo, evidenciando a ordem das operac¸ ˜oes, a dinamica dos processos e a dependencia
entre os requisitos funcionais.
Por meio dessa representacao, é possıvel compreender como os diferentes modulos da aplicacao interagem
para atender às funcionalidades esperadas.

<img width="579" height="652" alt="image" src="https://github.com/user-attachments/assets/d82efb98-d27e-4f9c-84f8-354e541cc391" />

5.5 Diagrama Entidade-Relacionamento
O diagrama Entidade-Relacionamento (ER) da aplicacao Envite, apresentado na Figura 4, ilustra as principais
entidades do sistema e as relacões existentes entre elas. Este diagrama e fundamental para garantir a consistencia
e integridade do banco de dados, alem de possibilitar um modelo eficiente para o armazenamento e gerenciamento
das informacoes.

<img width="554" height="310" alt="image" src="https://github.com/user-attachments/assets/7272f133-1a6f-4807-a0c5-43e2be402cfd" />

As principais entidades contempladas no modelo sao:
• Usuario: representa os participantes da plataforma, que podem atuar como organizadores de eventos ou
usuarios comuns.
• Evento: cont ´em as informac¸ ˜oes relativas aos eventos cadastrados no sistema.
• Participac¸ ˜ao: registra a relac¸ ˜ao entre usu ´arios e eventos, indicando quais usu ´arios confirmaram presenc¸a
em cada evento.
Quanto aos relacionamentos estabelecidos entre as entidades, observa-se que um usu ´ario pode criar m ´ultiplos
eventos, sendo que cada evento possui apenas um criador. Al ´em disso, um usu ´ario pode participar de diversos
eventos, e um mesmo evento pode contar com a participac¸ ˜ao de v ´arios usu ´arios, caracterizando assim uma
relac¸ ˜ao muitos-para-muitos entre as entidades Usu ´ario e Evento, mediada pela entidade Participac¸ ˜ao. Por fim,
um evento pode receber m ´ultiplas avaliac¸ ˜oes, entretanto, cada avaliac¸ ˜ao est ´a associada exclusivamente a um
´unico usu ´ario. O diagrama apresenta esses elementos e suas interconex ˜oes de forma detalhada, facilitando a
compreens ˜ao do modelo de dados adotado pela aplicac¸ ˜ao.
6 Custos do Projeto
7 Sprints
Nesta sec¸ ˜ao, ser ˜ao apresentadas e discutidas todas as sprints apresentadas na Sec¸ ˜ao 4 de acordo com o cro-
nograma apresentado. Foram totalizadas 17 Sprints, sendo as duas primeiras e as duas ´ultimas j ´a fixadas pela
disciplina.
7.1 Sprint 1 - Apresentac¸ ˜ao da disciplina - 14/08/2025
Explicac¸ ˜ao de como seria o funcionamento da disciplina, definindo as datas de entregas das Sprints, que foram
definidas como semanais, no hor ´ario da disciplina na Quinta-feira, salvo excec¸ ˜oes por feriados ou aviso pr ´evio de
impossibilidades.
11
7.2 Sprint 2 - Proposta e cronograma - 21/08/2025
Nesta sprint foi realizada a idealizac¸ ˜ao inicial do projeto T ˆania Cabelos. A proposta surgiu a partir da necessidade
de familiares de um dos membros do grupo em facilitar o agendamento de atendimentos em seu sal ˜ao de beleza.
Durante essa etapa, foi elaborada uma apresentac¸ ˜ao da proposta com os principais objetivos, funcionalidades
iniciais e p ´ublicos-alvo da aplicac¸ ˜ao. Tamb ´em foram definidos os requisitos essenciais para a primeira vers ˜ao do
site.
7.3 Sprint 3 - Definic¸ ˜ao de Escopo e Requisitos - 28/08/2025
Nessa sprint foram definidos o escopo do projeto, com os seus objetivos, requisitos funcionais e n ˜ao funcionais.
7.4 Sprint 4 - Diagramas - 04/09/2025
Nessa sprint foram desenvolvidos e apresentados os diagramas que comp ˜oe a modelagem inicial do sistema:
Diagrama de Casos de uso, Classe, Sequ ˆencia, Entidade e Relacionamento, Diagramas de Atividade
7.5 Sprint 5 - Desenvolvimento dos prot ´otipos de Telas - 11/09/2025
Nessa sprint foram feitos os prot ´otipos das principais interfaces do sistema, possibilitando um vislumbre da apar ˆencia
futura do mesmo. Os prot ´otipos desenvolvidos nessa iterac¸ ˜ao est ˜ao dispostos a seguir.
• Cadastro e Login: As telas de login e cadastro s ˜ao fundamentais para o controle de acesso. Elas permitem
que o usu ´ario entre no sistema com suas credenciais ou crie uma nova conta de maneira simples e segura.
Ambas as interfaces foram desenvolvidas com foco na usabilidade, apresentando campos bem definidos.
((a)) Tela de Login ((b)) Tela de Cadastro
<img width="562" height="161" alt="image" src="https://github.com/user-attachments/assets/44968b48-b1ce-4fcc-a898-6f1af8513504" />

• P ´agina Inicial: A p ´agina principal do site, com a apresentac¸ ˜ao da imagem visual do sal ˜ao.
• Funcionalidades: tela de direcionamento para as demais funcionalidades.
• Tabela de Servic¸ os: Mostra os servic¸os oferecidos pelo sal ˜ao, com o prec¸o m ´edio de cada.
• M´ıdias Sociais: Apresenta as m´ıdias sociais para que o cliente possa entrar em contato diretamente com a
atendente do sal ˜ao, possibilitando mais interac¸ ˜ao.
• Vitrine: Visualizac¸ ˜ao de procedimentos realizados em clientes.
• Agenda: Foram desenvolvidas duas vis ˜oes da agenda, para o cliente e para a atendente. Na vis ˜ao do
cliente ´e poss´ıvel ver os hor ´arios livres e realizar um agendamento, al ´em disso ele poder ´a editar ou cancelar
seus agendamentos. Na vis ˜ao da atendente ser ´a poss´ıvel visualizar a os hor ´arios que est ˜ao agendaos e ver
detalhes sobre o agendamento.
12
<img width="485" height="722" alt="image" src="https://github.com/user-attachments/assets/3ed7e9b7-1107-4619-a4f9-b324ee88e674" />

• Perguntas Frequentes: Nessa tela s ˜ao exibidas d ´uvidas frequentes que clientes costumam ter em certos
procedimentos.
• Avaliac¸ ˜oes : Avaliac¸ ˜oes dos clientes.
<img width="565" height="691" alt="image" src="https://github.com/user-attachments/assets/80819598-7ca3-4aad-9589-ce92715b2f53" />

• Perfis: Foram desenvolvidas duas telas de perfis de usu ´ario, uma para o cliente e outra para a atendente.
No perfil do cliente ele poder ´a ver e editar os agendamentos que ele possui em aberto, al ´em de poder editar
suas informac¸ ˜oes de perfil. No perfil da atendente ser ´a vis´ıvel os agendamentos em aberto, e ele poder ´a
14
editar informac¸ ˜oes de outros usu ´arios, como redefinir a senha, e editar informac¸ ˜oes administrativas.
((a)) Perfil do Cliente ((b)) Perfil da Atendente
Figura 14: Perfis do Cliente e da Atendente
8 Refer ˆencias Bibliogr ´aficas
[1] Lavanya Chandrasekaran, Bonnie A. Nardi, and Carolyn J. Linde. Non-Functional Requirements in Software
Engineering. Springer, 2012.
[2] Roger S. Pressman and Bruce R. Maxim. Engenharia de Software. McGraw-Hill, 8 edition, 2016.
[3] Ian Sommerville. Software Engineering. Pearson Education, 9 edition, 2011.
[4] Karl Wiegers and Joy Beatty. Software Requirements. Microsoft Press, 3 edition, 2014.
15
Anexos
Requisitos Funcionais
Numerac¸ ˜ao Descric¸ ˜ao Depende de
RF 01
Cadastro de Usu ´arios
- O sistema deve permitir o cadastro de novos usu ´arios.
RF 02 Autenticac¸ ˜ao de Usu ´arios RF 01
- O sistema deve permitir que usu ´arios fac¸am login e logout com
email e senha. Login Cliente e Login Administrador
.
RF 03
Gerenciamento de Perfis
RF 01- O perfil deve conter, nome e contato. Adicionar cpf e e-mail.
- Usu ´arios devem poder visualizar e editar suas informac¸ ˜oes pes-
soais no perfil.
- O perfil deve exibir os agendamentos criados pelo usu ´ario.
RF 04
Criac¸ ˜ao de Agendamentos
RF 01- O sistema deve permitir que qualquer usu ´ario crie (Selecione)
novos agendamentos, preenchendo informac¸ ˜oes como servic¸o,
data, hor ´ario.
RF 05
Listagem de Agendamentos
RF 01, RF 04- O administrador poder ´a ver os agendamentos na ordem em
que foram feitos.
- O administrador poder ´a filtrar os agendamentos por dia.
RF 06
Gerenciamento de Agendamentos
RF 01, RF 04- O sistema deve permitir que usu ´arios visualizem, editem e can-
cele um agendamento pendente.
RF 07
Quadro de Informac¸ ˜oes
- O sistema ter ´a um espac¸o dedicado a informac¸ ˜oes sobre contra
indicac¸ ˜oes de procedimentos.
RF 08
Tabela de servic¸ os
-O sistema contar ´a com uma tabela onde ficar ˜ao vis´ıveis os
servic¸os com seus respectivos prec¸os, de acordo com o tama-
nho do cabelo do cliente (pequeno, m ´edio, grande) e m ´edia de
durac¸ ˜ao do procedimento.
Tabela 2: Tabela dos Requisitos funcionais do site T ˆania Cabelos.
16
Requisitos N ˜ao Funcionais
Numerac¸ ˜ao Descric¸ ˜ao Depende de
RNF 01
Performance
- O sistema deve ser capaz de lidar com um volume razoável de
dados sem perda de desempenho.
RNF 02
Usabilidade
- A interface deve ser intuitiva, com fácil navegacão entre as fun-
cionalidades principais.
RNF 03
Compatibilidade
- O sistema deve ser compat´ıvel com os principais navegadores
e responsivo para dispositivos móveis.
Tabela 3: Tabela dos Requisitos não funcionais do site Tânia Cabelos.
17
