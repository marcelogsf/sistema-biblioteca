from biblioteca.models import Livro, Usuario


# 📚 50 LIVROS
livros = [
    ("Harry Potter e a Pedra Filosofal", "J.K. Rowling"),
    ("Harry Potter e a Câmara Secreta", "J.K. Rowling"),
    ("Harry Potter e o Prisioneiro de Azkaban", "J.K. Rowling"),
    ("O Hobbit", "J.R.R. Tolkien"),
    ("O Senhor dos Anéis", "J.R.R. Tolkien"),
    ("1984", "George Orwell"),
    ("A Revolução dos Bichos", "George Orwell"),
    ("Dom Casmurro", "Machado de Assis"),
    ("Memórias Póstumas de Brás Cubas", "Machado de Assis"),
    ("O Pequeno Príncipe", "Antoine de Saint-Exupéry"),
    ("Percy Jackson", "Rick Riordan"),
    ("Jogos Vorazes", "Suzanne Collins"),
    ("Em Chamas", "Suzanne Collins"),
    ("A Esperança", "Suzanne Collins"),
    ("It: A Coisa", "Stephen King"),
    ("O Iluminado", "Stephen King"),
    ("Duna", "Frank Herbert"),
    ("Código Da Vinci", "Dan Brown"),
    ("Anjos e Demônios", "Dan Brown"),
    ("Inferno", "Dan Brown"),
    ("A Culpa é das Estrelas", "John Green"),
    ("Quem é Você, Alasca?", "John Green"),
    ("Cidade de Papel", "John Green"),
    ("Crepúsculo", "Stephenie Meyer"),
    ("Lua Nova", "Stephenie Meyer"),
    ("Eclipse", "Stephenie Meyer"),
    ("Amanhecer", "Stephenie Meyer"),
    ("As Crônicas de Nárnia", "C.S. Lewis"),
    ("O Leão, a Feiticeira e o Guarda-Roupa", "C.S. Lewis"),
    ("Eragon", "Christopher Paolini"),
    ("Eldest", "Christopher Paolini"),
    ("Brisingr", "Christopher Paolini"),
    ("Maze Runner", "James Dashner"),
    ("Prova de Fogo", "James Dashner"),
    ("A Cura Mortal", "James Dashner"),
    ("Diário de um Banana", "Jeff Kinney"),
    ("O Diário de Anne Frank", "Anne Frank"),
    ("O Alquimista", "Paulo Coelho"),
    ("Veronika Decide Morrer", "Paulo Coelho"),
    ("Onze Minutos", "Paulo Coelho"),
    ("Capitães da Areia", "Jorge Amado"),
    ("Vidas Secas", "Graciliano Ramos"),
    ("Senhora", "José de Alencar"),
    ("Iracema", "José de Alencar"),
    ("Drácula", "Bram Stoker"),
    ("Frankenstein", "Mary Shelley"),
    ("Sherlock Holmes", "Arthur Conan Doyle"),
    ("O Morro dos Ventos Uivantes", "Emily Brontë"),
    ("Orgulho e Preconceito", "Jane Austen"),
    ("Romeu e Julieta", "William Shakespeare"),
]


# 👤 50 USUÁRIOS
usuarios = [
    ("João Silva", "joao1@gmail.com"),
    ("Maria Oliveira", "maria2@gmail.com"),
    ("Pedro Santos", "pedro3@gmail.com"),
    ("Ana Costa", "ana4@gmail.com"),
    ("Lucas Lima", "lucas5@gmail.com"),
    ("Juliana Souza", "juliana6@gmail.com"),
    ("Carlos Henrique", "carlos7@gmail.com"),
    ("Fernanda Alves", "fernanda8@gmail.com"),
    ("Rafael Gomes", "rafael9@gmail.com"),
    ("Patrícia Rocha", "patricia10@gmail.com"),
    ("Gabriel Martins", "gabriel11@gmail.com"),
    ("Larissa Fernandes", "larissa12@gmail.com"),
    ("Bruno Ribeiro", "bruno13@gmail.com"),
    ("Camila Carvalho", "camila14@gmail.com"),
    ("Eduardo Melo", "eduardo15@gmail.com"),
    ("Amanda Barros", "amanda16@gmail.com"),
    ("Felipe Araújo", "felipe17@gmail.com"),
    ("Bianca Teixeira", "bianca18@gmail.com"),
    ("Gustavo Nunes", "gustavo19@gmail.com"),
    ("Vanessa Cardoso", "vanessa20@gmail.com"),
    ("Ricardo Batista", "ricardo21@gmail.com"),
    ("Isabela Moura", "isabela22@gmail.com"),
    ("Thiago Monteiro", "thiago23@gmail.com"),
    ("Natália Freitas", "natalia24@gmail.com"),
    ("Leonardo Dias", "leonardo25@gmail.com"),
    ("Mariana Campos", "mariana26@gmail.com"),
    ("André Vieira", "andre27@gmail.com"),
    ("Tatiane Pinto", "tatiane28@gmail.com"),
    ("Daniel Moraes", "daniel29@gmail.com"),
    ("Beatriz Correia", "beatriz30@gmail.com"),
    ("Vinicius Lopes", "vinicius31@gmail.com"),
    ("Clara Rezende", "clara32@gmail.com"),
    ("Henrique Duarte", "henrique33@gmail.com"),
    ("Aline Farias", "aline34@gmail.com"),
    ("Matheus Cavalcante", "matheus35@gmail.com"),
    ("Sabrina Mendes", "sabrina36@gmail.com"),
    ("Igor Sales", "igor37@gmail.com"),
    ("Carolina Borges", "carolina38@gmail.com"),
    ("Murilo Castro", "murilo39@gmail.com"),
    ("Renata Medeiros", "renata40@gmail.com"),
    ("Paulo César", "paulo41@gmail.com"),
    ("Débora Lima", "debora42@gmail.com"),
    ("Samuel Rodrigues", "samuel43@gmail.com"),
    ("Michele Andrade", "michele44@gmail.com"),
    ("Caio Pereira", "caio45@gmail.com"),
    ("Elisa Gomes", "elisa46@gmail.com"),
    ("Otávio Fernandes", "otavio47@gmail.com"),
    ("Yasmin Rocha", "yasmin48@gmail.com"),
    ("Victor Hugo", "victor49@gmail.com"),
    ("Helena Martins", "helena50@gmail.com"),
]


# 📚 INSERIR LIVROS
for titulo, autor in livros:
    Livro.objects.get_or_create(
        titulo=titulo,
        autor=autor
    )

print("✅ 50 livros cadastrados!")


# 👤 INSERIR USUÁRIOS
for nome, email in usuarios:
    Usuario.objects.get_or_create(
        nome=nome,
        email=email
    )

print("✅ 50 usuários cadastrados!")