### 📋 Briefing do cliente fictício

> "Tenho uma pequena loja/dropshipping e quero saber quando os concorrentes mudam o preço de 10-15 produtos específicos, ou quando um produto esgota. Hoje eu checo manualmente todo dia e às vezes esqueço. Quero um relatório diário automático."

### 🏗️ Etapa 1 — Setup

* Escolha 2-3 sites reais de e-commerce (comece com sites simples, sem captcha agressivo — evite Amazon/Mercado Livre no início)
* Defina a lista de produtos-alvo (URL + nome + categoria) — isso deve ficar em um arquivo de configuração separado do código, não hardcoded
* Estruture o projeto pensando em: um módulo para navegação/captura (Playwright), um módulo para persistência (onde salvar o histórico), um módulo para geração de relatório
* Decida desde já: onde esse histórico de preços vai morar? (Comece com SQLite/CSV — é suficiente e você já tem exposição a SQL)

### ⚙️ Etapa 2 — Funcionalidades principais

* Captura de preço e disponibilidade de cada produto configurado
* Comparação com a última leitura salva (detectar mudança de preço, produto esgotado, produto voltou ao estoque)
* Tratamento de falha por produto: se um produto falhar (site fora do ar, seletor não encontrado), os outros devem continuar — nenhuma falha isolada pode derrubar o job inteiro
* Logging estruturado: todo evento relevante (sucesso, falha, mudança detectada) deve ficar registrado, não só printado
* Geração de relatório diário (pode ser um `.txt`, `.csv` ou até um e-mail simples) resumindo o que mudou

### 🚀 Etapa 3 — Metas de expansão (para quando o básico estiver rodando)

* Agendamento automático (cron ou `schedule` do Python) rodando diariamente sem intervenção manual
* Rate limiting e delays humanizados entre requisições, pra não sobrecarregar o site alvo nem ser bloqueado
* Alertas automáticos (e-mail/Slack/Telegram) só quando houver mudança relevante, em vez de relatório sempre
* Retry com backoff exponencial para falhas temporárias de rede

### 👤 Quem usaria isso / o que isso demonstra pra recrutador

* **Quem usaria:** pequenos e-commerces, times de precificação, dropshippers, agências que monitoram concorrência
* **O que demonstra:** você não construiu "**um scraper**" — construiu um sistema tolerante a falhas, com persistência de estado, observabilidade (logs) e entrega de valor de negócio (relatório acionável). Isso é literalmente o vocabulário que aparece nas vagas que puxamos do Upwork, e é a mesma lógica que você já aplicou na Alumar (monitoramento com alertas por severidade) — só que agora em formato de portfólio público.
