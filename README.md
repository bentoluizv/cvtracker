# CVTracker: Job Application Manager

## Descrição do Projeto

O **CVTracker** é uma aplicação projetada para ajudar usuários a gerenciar e acompanhar seus processos seletivos de emprego de forma eficiente e organizada. Com funcionalidades que incluem registro de candidaturas, lembretes de prazos importantes e integração com o Google Calendar, o CVTracker visa simplificar o acompanhamento de oportunidades de trabalho.

### Objetivo

O objetivo principal do CVTracker é fornecer uma ferramenta intuitiva e prática para que os usuários possam monitorar suas candidaturas, manter-se organizados e aumentar suas chances de sucesso em processos seletivos.

### Resumo

O CVTracker permite que os usuários:

- Registrem e atualizem informações sobre suas candidaturas.
- Recebam lembretes automáticos de prazos importantes.
- Visualizem uma lista consolidada de todas as candidaturas com detalhes relevantes.
- Sincronizem eventos importantes com o Google Calendar.

## Histórias do Usuário

| **Como**                     | **Quero**                                      | **Para**                                                                 |
|-------------------------------|-----------------------------------------------|--------------------------------------------------------------------------|
| Como usuário                 | Registrar processos seletivos de emprego      | Acompanhar as empresas para as quais me candidatei e monitorar o progresso das minhas candidaturas. |
| Como usuário                 | Adicionar detalhes importantes sobre cada candidatura | Me manter organizado e informado com prazos, feedbacks e outras informações relevantes. |
| Como usuário                 | Visualizar uma lista de todas as minhas candidaturas | Rapidamente ver o status e os detalhes de cada candidatura.             |
| Como usuário                 | Atualizar o status das minhas candidaturas    | Refletir mudanças como receber feedback, agendar entrevistas ou ser contratado. |
| Como usuário                 | Excluir candidaturas                         | Remover entradas desatualizadas ou irrelevantes do meu rastreador.       |
| Como usuário                 | Receber lembretes de prazos importantes       | Não perder datas críticas relacionadas às minhas candidaturas.           |
| Como usuário                 | Adicionar eventos ao meu calendário do Google | Garantir que prazos importantes e entrevistas sejam lembrados com notificações automáticas. |

---

### Requisitos Funcionais

| **RF#** | **Descrição**                                                                                                                                                                                                 |
|---------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| RF1     | Implementar operações de CRUD (criar, ler, atualizar e excluir) para entradas de processos seletivos, garantindo que cada ação seja confirmada antes de ser concluída. |
| RF2     | Definir campos obrigatórios para cada entrada de processo seletivo, incluindo: Nome da empresa, Título do cargo, Data da candidatura, Prazos, Status, Notas ou informações adicionais. |
| RF3     | Exibir uma lista consolidada de todas as candidaturas, apresentando de forma clara os seguintes detalhes principais: Nome da empresa, Título do cargo, Status atual, Próximo prazo relevante. |
| RF4     | Implementar funcionalidade de filtro e busca para candidaturas com base nos seguintes critérios: Status, Nome da empresa, Título do cargo. |
| RF5     | Configurar notificações ou lembretes automáticos para prazos futuros, como entrevistas ou datas de envio, permitindo que os usuários ajustem a antecedência do alerta. |
| RF6     | Integrar o aplicativo com o Google Calendar para adicionar eventos automaticamente, como entrevistas ou prazos importantes, com notificações configuráveis. |
| RF7     | Desenvolver uma interface intuitiva, com navegação clara e design responsivo para uso em dispositivos móveis e desktops. |
| RF8     | Garantir a persistência e segurança dos dados inseridos pelos usuários, utilizando criptografia quando necessário, e assegurando que os dados permaneçam disponíveis entre sessões. |
| RF9     | Implementar uma funcionalidade de confirmação antes de excluir qualquer entrada, para evitar remoções acidentais. |

### Schema Entidade-Relacionamento

#### Entidade: Usuário

| **Propriedade** | **Tipo**       | **Descrição**                                   |
|------------------|---------------|-------------------------------------------------|
| id              | Inteiro       | Identificador único do usuário.                |
| nome            | Texto         | Nome completo do usuário.                      |
| email           | Texto         | Endereço de e-mail único do usuário.           |
| senha           | Texto         | Senha criptografada do usuário.                |
| data_criacao    | Data/Hora     | Data e hora de criação do registro.            |

#### Entidade: Candidatura

| **Propriedade** | **Tipo**       | **Descrição**                                   |
|------------------|---------------|-------------------------------------------------|
| id              | Inteiro       | Identificador único da candidatura.            |
| usuario_id      | Inteiro       | Referência ao usuário que criou a candidatura. |
| empresa         | Texto         | Nome da empresa associada à candidatura.       |
| titulo_cargo    | Texto         | Título do cargo para o qual o usuário aplicou. |
| data_candidatura| Data          | Data em que a candidatura foi realizada.       |
| status          | Texto         | Status atual da candidatura.                   |
| notas           | Texto         | Informações adicionais sobre a candidatura.    |
| data_criacao    | Data/Hora     | Data e hora de criação do registro.            |

#### Entidade: Prazo

| **Propriedade** | **Tipo**       | **Descrição**                                   |
|------------------|---------------|-------------------------------------------------|
| id              | Inteiro       | Identificador único do prazo.                  |
| candidatura_id  | Inteiro       | Referência à candidatura associada.            |
| descricao       | Texto         | Descrição do prazo (ex.: "Entrevista técnica").|
| data_prazo      | Data/Hora     | Data e hora do prazo.                          |
| lembrete        | Booleano      | Indica se o lembrete está ativado.             |
| data_criacao    | Data/Hora     | Data e hora de criação do registro.            |

#### Entidade: Evento

| **Propriedade** | **Tipo**       | **Descrição**                                   |
|------------------|---------------|-------------------------------------------------|
| id              | Inteiro       | Identificador único do evento.                 |
| candidatura_id  | Inteiro       | Referência à candidatura associada.            |
| google_event_id | Texto         | Identificador do evento no Google Calendar.    |
| titulo          | Texto         | Título do evento.                              |
| data_evento     | Data/Hora     | Data e hora do evento.                         |
| notificacao     | Booleano      | Indica se notificações estão ativadas.         |
| data_criacao    | Data/Hora     | Data e hora de criação do registro.            |

### Observações

- A entidade **Usuário** é necessária para suportar múltiplos usuários no sistema.
- A entidade **Candidatura** armazena as informações principais de cada processo seletivo.
- A entidade **Prazo** permite gerenciar múltiplos prazos associados a uma candidatura.
- A entidade **Evento** suporta a integração com o Google Calendar, armazenando informações sobre eventos importantes.

Este modelo pode ser expandido conforme novas funcionalidades sejam adicionadas ao sistema.

### Roadmap de Desenvolvimento

- [ ] Permitir registro de processos seletivos de emprego.
- [ ] Adicionar detalhes importantes sobre cada candidatura.
- [ ] Exibir uma lista consolidada de todas as candidaturas.
- [ ] Atualizar o status das candidaturas.
- [ ] Implementar exclusão de candidaturas.
- [ ] Adicionar lembretes de prazos importantes.
- [ ] Sincronizar eventos importantes com o Google Calendar.
- [ ] Criar notificações automáticas para prazos críticos.
- [ ] Criar relatórios e estatísticas sobre candidaturas.
