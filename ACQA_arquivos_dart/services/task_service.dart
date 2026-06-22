import 'package:flutter/foundation.dart';
import '../models/task.dart';

/// Serviço responsável por armazenar e organizar as tarefas em memória.
/// Cada tarefa pertence a um dia específico (chave no formato yyyy-MM-dd).
class TaskService {
  static final TaskService _instance = TaskService._internal();
  factory TaskService() => _instance;
  TaskService._internal();

  // dataKey -> lista de tarefas daquele dia
  final Map<String, List<Task>> _tasksByDate = {};

  String _keyFor(DateTime date) {
    return '${date.year}-${date.month.toString().padLeft(2, '0')}-${date.day.toString().padLeft(2, '0')}';
  }

  /// Retorna as tarefas de um dia, já ordenadas:
  /// 1) Pendentes em ordem alfabética
  /// 2) Concluídas em ordem alfabética
  List<Task> getTasksForDate(DateTime date) {
    final key = _keyFor(date);
    final tasks = _tasksByDate[key] ?? [];

    final pending = tasks.where((t) => !t.isDone).toList()
      ..sort((a, b) => a.title.toLowerCase().compareTo(b.title.toLowerCase()));
    final done = tasks.where((t) => t.isDone).toList()
      ..sort((a, b) => a.title.toLowerCase().compareTo(b.title.toLowerCase()));

    return [...pending, ...done];
  }

  /// Retorna true se houver pelo menos uma tarefa no dia (usado para marcar no calendário).
  bool hasTasks(DateTime date) {
    final key = _keyFor(date);
    return (_tasksByDate[key] ?? []).isNotEmpty;
  }

  void addTask(DateTime date, String title) {
    final key = _keyFor(date);
    _tasksByDate.putIfAbsent(key, () => []);
    _tasksByDate[key]!.add(
      Task(
        id: UniqueKey().toString(),
        title: title,
        date: date,
        isDone: false,
      ),
    );
  }

  void removeTask(DateTime date, Task task) {
    final key = _keyFor(date);
    _tasksByDate[key]?.removeWhere((t) => t.id == task.id);
  }

  void toggleDone(DateTime date, Task task) {
    final key = _keyFor(date);
    final list = _tasksByDate[key];
    if (list == null) return;
    final index = list.indexWhere((t) => t.id == task.id);
    if (index != -1) {
      list[index].isDone = !list[index].isDone;
    }
  }
}
