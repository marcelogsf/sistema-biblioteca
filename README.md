# 📚 Sistema Biblioteca

<p align="center">

<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>

<img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white"/>

<img src="https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white"/>

<img src="https://img.shields.io/badge/Django_Admin-Jazzmin-2C2C2C?style=for-the-badge"/>

</p>

---

## 📌 Sobre o Projeto

O Sistema Biblioteca foi desenvolvido utilizando **Django** e **PostgreSQL** com o objetivo de realizar o gerenciamento de livros, usuários e empréstimos de uma biblioteca.

A aplicação possui funcionalidades completas de cadastro, edição, remoção e controle de empréstimos, além de relatórios administrativos com filtros e exportação de dados em CSV.

O projeto também utiliza recursos avançados de banco de dados, como:

* Views
* Triggers
* Relacionamentos
* Validações automáticas
* Controle de disponibilidade de livros

---

## 🧠 Estrutura do Projeto

```bash
biblioteca/
├── migrations/
├── templates/
│   └── admin/
│       └── relatorio.html
├── admin.py
├── models.py
├── urls.py
├── views.py
└── seed.py
```

### 📌 Organização

* **models.py** → Estrutura das entidades e relacionamentos
* **views.py** → Regras de negócio e relatórios
* **admin.py** → Personalização do Django Admin
* **urls.py** → Rotas da aplicação
* **relatorio.html** → Tela administrativa de relatórios
* **migrations/** → Controle de versões do banco

---

## ⚙️ Tecnologias Utilizadas

* Python
* Django
* PostgreSQL
* Django Jazzmin
* HTML
* DBeaver
* GitHub

---

## ✨ Funcionalidades

### 📚 Livros

* Cadastro de livros
* Edição de livros
* Remoção de livros
* Controle de disponibilidade
* Exibição de status

---

### 👤 Usuários

* Cadastro de usuários
* Edição de usuários
* Remoção de usuários
* Controle por e-mail

---

### 🔄 Empréstimos

* Registro de empréstimos
* Associação entre livros e usuários
* Controle de devolução
* Atualização automática de disponibilidade
* Data automática do empréstimo
* Controle de status:

  * ✅ Devolvido
  * ❌ Pendente

---

### 📊 Relatórios

* Dashboard administrativo
* Quantidade total de empréstimos
* Quantidade de livros devolvidos
* Quantidade de empréstimos pendentes
* Filtros por:

  * Livro
  * Usuário
  * Status
* Exportação CSV

---

## 🖼️ Demonstração do Sistema

### 🔹 Dashboard Inicial

> (INSERIR PRINT DO DASHBOARD)

---

### 🔹 Tela de Livros

> (INSERIR PRINT DA TELA DE LIVROS)

---

### 🔹 Tela de Usuários

> (INSERIR PRINT DA TELA DE USUÁRIOS)

---

### 🔹 Tela de Empréstimos

> (INSERIR PRINT DA TELA DE EMPRÉSTIMOS)

---

### 🔹 Tela de Relatórios

> (INSERIR PRINT DA TELA DE RELATÓRIOS)

---

## 🗄️ Banco de Dados

O sistema utiliza o **PostgreSQL** como banco de dados relacional.

### 🔹 Tabela biblioteca_livro

| Campo      | Tipo         |
| ---------- | ------------ |
| id         | BigAutoField |
| titulo     | CharField    |
| autor      | CharField    |
| disponivel | BooleanField |

---

### 🔹 Tabela biblioteca_usuario

| Campo | Tipo         |
| ----- | ------------ |
| id    | BigAutoField |
| nome  | CharField    |
| email | EmailField   |

---

### 🔹 Tabela biblioteca_emprestimo

| Campo           | Tipo          |
| --------------- | ------------- |
| id              | BigAutoField  |
| livro_id        | ForeignKey    |
| usuario_id      | ForeignKey    |
| data_emprestimo | DateTimeField |
| data_devolucao  | DateTimeField |
| devolvido       | BooleanField  |

---

## 🔗 Relacionamentos

| Relacionamento       | Tipo |
| -------------------- | ---- |
| Livro → Empréstimo   | 1:N  |
| Usuário → Empréstimo | 1:N  |

### 📌 Explicação

* Um livro pode aparecer em vários empréstimos ao longo do tempo
* Um usuário pode realizar vários empréstimos
* Cada empréstimo pertence a apenas um livro e um usuário

---

## ⚡ Recursos Avançados do Banco

### 🔹 Trigger

A Trigger é responsável por atualizar automaticamente a disponibilidade dos livros.

```sql
CREATE TRIGGER trigger_emprestimo_livro
AFTER INSERT OR UPDATE
ON public.biblioteca_emprestimo
FOR EACH ROW
EXECUTE FUNCTION atualizar_disponibilidade();
```

---

### 🔹 Função da Trigger

```sql
CREATE OR REPLACE FUNCTION public.atualizar_disponibilidade()
 RETURNS trigger
 LANGUAGE plpgsql
AS $function$
BEGIN

    IF NEW.devolvido = FALSE THEN

        UPDATE biblioteca_livro
        SET disponivel = FALSE
        WHERE id = NEW.livro_id;

    ELSE

        UPDATE biblioteca_livro
        SET disponivel = TRUE
        WHERE id = NEW.livro_id;

    END IF;

    RETURN NEW;

END;
$function$;
```

---

### 🔹 View

A View `vw_emprestimos` foi criada para consolidar informações de empréstimos.

```sql
CREATE OR REPLACE VIEW public.vw_emprestimos
AS SELECT e.id,
    l.titulo AS livro,
    u.nome AS usuario,
    e.data_emprestimo,
    e.data_devolucao,
    e.devolvido
   FROM biblioteca_emprestimo e
     JOIN biblioteca_livro l ON e.livro_id = l.id
     JOIN biblioteca_usuario u ON e.usuario_id = u.id;
```

---

## 🧩 Tabelas Padrão do Django

```text
auth_group
auth_group_permissions
auth_permission
auth_user
auth_user_groups
auth_user_user_permissions
django_admin_log
django_content_type
django_migrations
django_session
```

---

## ⚙️ Como Executar o Projeto

### 1️⃣ Clonar o repositório

```bash
git clone https://github.com/marcelogsf/sistema-biblioteca.git
```

### 2️⃣ Acessar a pasta do projeto

```bash
cd sistema-biblioteca
```

### 3️⃣ Criar ambiente virtual

```bash
python -m venv venv
```

### 4️⃣ Ativar ambiente virtual

```bash
venv\Scripts\activate
```

### 5️⃣ Instalar dependências

```bash
pip install -r requirements.txt
```

### 6️⃣ Configurar PostgreSQL

Configurar as credenciais do banco no arquivo `settings.py`.

### 7️⃣ Executar migrations

```bash
python manage.py migrate
```

### 8️⃣ Criar superusuário

```bash
python manage.py createsuperuser
```

### 9️⃣ Executar servidor

```bash
python manage.py runserver
```

---

## 📦 Dependências

```txt
asgiref==3.11.1
Django==6.0.5
django-jazzmin==3.0.4
psycopg2-binary==2.9.12
sqlparse==0.5.5
tzdata==2026.2
```

---

## 🔐 Validações Implementadas

* Impedimento de empréstimo de livros indisponíveis
* Atualização automática da disponibilidade
* Controle automático de devolução
* Exportação CSV com suporte a acentuação
* Registro automático de datas

---

## 👨‍💻 Desenvolvedores

Maria Gabriele Araújo Gonçalves

Marcelo Gomes da Silva Filho

---

## 🔗 Repositório

🔗 [https://github.com/marcelogsf/sistema-biblioteca](https://github.com/marcelogsf/sistema-biblioteca)

---

## 📌 Status

✅ Projeto finalizado e funcional
