import 'package:flutter/material.dart';
import '../models/task.dart';
import '../services/task_service.dart';

class TaskListScreen extends StatefulWidget {
  final DateTime date;

  const TaskListScreen({super.key, required this.date});

  @override
  State<TaskListScreen> createState() => _TaskListScreenState();
}

class _TaskListScreenState extends State<TaskListScreen> {
  final _taskService = TaskService();
  late List<Task> _tasks;

  @override
  void initState() {
    super.initState();
    _refreshTasks();
  }

  void _refreshTasks() {
    setState(() {
      _tasks = _taskService.getTasksForDate(widget.date);
    });
  }

  void _showAddTaskDialog() {
    final controller = TextEditingController();

    showDialog(
      context: context,
      builder: (context) {
        return AlertDialog(
          title: const Text('Nova Tarefa'),
          content: TextField(
            controller: controller,
            autofocus: true,
            decoration: const InputDecoration(
              hintText: 'Descreva a tarefa',
              border: OutlineInputBorder(),
            ),
            onSubmitted: (_) => _confirmAddTask(controller.text),
          ),
          actions: [
            TextButton(
              onPressed: () => Navigator.of(context).pop(),
              child: const Text('Cancelar'),
            ),
            ElevatedButton(
              onPressed: () => _confirmAddTask(controller.text),
              child: const Text('Adicionar'),
            ),
          ],
        );
      },
    );
  }

  void _confirmAddTask(String title) {
    if (title.trim().isEmpty) return;
    _taskService.addTask(widget.date, title.trim());
    Navigator.of(context).pop();
    _refreshTasks();
  }

  void _toggleDone(Task task) {
    _taskService.toggleDone(widget.date, task);
    _refreshTasks();
  }

  void _removeTask(Task task) {
    _taskService.removeTask(widget.date, task);
    _refreshTasks();
  }

  @override
  Widget build(BuildContext context) {
    final dateLabel =
        '${widget.date.day.toString().padLeft(2, '0')}/${widget.date.month.toString().padLeft(2, '0')}/${widget.date.year}';

    return Scaffold(
      appBar: AppBar(
        title: Text('Tarefas - $dateLabel'),
      ),
      body: _tasks.isEmpty
          ? const Center(
              child: Text(
                'Nenhuma tarefa para este dia.\nToque em "+" para adicionar.',
                textAlign: TextAlign.center,
                style: TextStyle(color: Colors.grey),
              ),
            )
          : ListView.builder(
              padding: const EdgeInsets.symmetric(vertical: 8),
              itemCount: _tasks.length,
              itemBuilder: (context, index) {
                final task = _tasks[index];
                return Dismissible(
                  key: ValueKey(task.id),
                  direction: DismissDirection.endToStart,
                  background: Container(
                    color: Colors.red,
                    alignment: Alignment.centerRight,
                    padding: const EdgeInsets.only(right: 20),
                    child: const Icon(Icons.delete, color: Colors.white),
                  ),
                  onDismissed: (_) => _removeTask(task),
                  child: Card(
                    margin: const EdgeInsets.symmetric(horizontal: 12, vertical: 4),
                    child: ListTile(
                      leading: Checkbox(
                        value: task.isDone,
                        onChanged: (_) => _toggleDone(task),
                      ),
                      title: Text(
                        task.title,
                        style: TextStyle(
                          decoration:
                              task.isDone ? TextDecoration.lineThrough : null,
                          color: task.isDone ? Colors.grey : Colors.black,
                        ),
                      ),
                      trailing: IconButton(
                        icon: const Icon(Icons.delete_outline, color: Colors.redAccent),
                        onPressed: () => _removeTask(task),
                      ),
                      onTap: () => _toggleDone(task),
                    ),
                  ),
                );
              },
            ),
      floatingActionButton: FloatingActionButton(
        onPressed: _showAddTaskDialog,
        child: const Icon(Icons.add),
      ),
    );
  }
}
