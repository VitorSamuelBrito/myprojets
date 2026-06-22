# Minhas Tarefas (Flutter)

App de exemplo em Flutter com:
- Tela de Cadastro/Login (mock, sem Firebase, dados em memória)
- Tela de Calendário (usando o pacote `table_calendar`)
- Tela de Lista de Tarefas por dia, com adição via `showDialog`
- Tarefas pendentes são listadas primeiro (ordem alfabética), seguidas das concluídas (ordem alfabética)
- Funcionalidades: adicionar, remover (deslizar ou ícone de lixeira) e marcar tarefas como concluídas

## Como executar

1. Tenha o Flutter SDK instalado (https://docs.flutter.dev/get-started/install).
2. Extraia este projeto e, no terminal, dentro da pasta `todo_app`, execute:
   ```
   flutter pub get
   flutter run
   ```
3. Para rodar no Android Studio: abra a pasta `todo_app` como projeto Flutter e clique em "Run".
4. Para rodar em um simulador Windows/Linux/Web, use, por exemplo:
   ```
   flutter run -d windows
   ```
   ou
   ```
   flutter run -d chrome
   ```

## Como usar o app

1. Na tela inicial, toque em "Não tem conta? Cadastre-se" para criar um usuário (e-mail + senha, mín. 4 caracteres).
2. Volte para a tela de Login e entre com as credenciais cadastradas.
3. Na tela de Calendário, selecione um dia e toque em "Ver tarefas do dia".
4. Na tela de Lista de Tarefas:
   - Toque no botão "+" para adicionar uma nova tarefa (via dialog).
   - Toque no checkbox ou na tarefa para marcá-la como concluída/pendente.
   - Deslize a tarefa para a esquerda ou toque no ícone de lixeira para removê-la.
5. As tarefas pendentes aparecem sempre no topo da lista (em ordem alfabética), seguidas das concluídas (também em ordem alfabética).

## Observação sobre persistência

Por solicitação do enunciado, o Firebase não foi implementado. Os dados (usuários e tarefas)
são armazenados em memória através dos serviços `AuthService` e `TaskService`
(em `lib/services/`), o que é suficiente para demonstração e avaliação em simulador.
Caso o app seja reiniciado, os dados são perdidos.

## Estrutura de pastas

```
lib/
 ├── main.dart
 ├── models/
 │   └── task.dart
 ├── services/
 │   ├── auth_service.dart
 │   └── task_service.dart
 └── screens/
     ├── login_screen.dart
     ├── register_screen.dart
     ├── calendar_screen.dart
     └── task_list_screen.dart
```
