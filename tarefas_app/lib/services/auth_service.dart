/// Serviço de autenticação simulado (mock), sem depender do Firebase.
/// Armazena usuários em memória, apenas para fins de demonstração/avaliação.
class AuthService {
  // Singleton simples
  static final AuthService _instance = AuthService._internal();
  factory AuthService() => _instance;
  AuthService._internal();

  // "Banco de dados" em memória: email -> senha
  final Map<String, String> _users = {};

  String? loggedUserEmail;

  /// Tenta registrar um novo usuário.
  /// Retorna null se ok, ou uma mensagem de erro.
  String? register(String email, String password) {
    if (email.trim().isEmpty || password.trim().isEmpty) {
      return 'Preencha todos os campos.';
    }
    if (_users.containsKey(email)) {
      return 'Este e-mail já está cadastrado.';
    }
    if (password.length < 4) {
      return 'A senha deve ter pelo menos 4 caracteres.';
    }
    _users[email] = password;
    return null;
  }

  /// Tenta logar o usuário.
  /// Retorna null se ok, ou uma mensagem de erro.
  String? login(String email, String password) {
    if (!_users.containsKey(email)) {
      return 'Usuário não encontrado.';
    }
    if (_users[email] != password) {
      return 'Senha incorreta.';
    }
    loggedUserEmail = email;
    return null;
  }

  void logout() {
    loggedUserEmail = null;
  }
}
