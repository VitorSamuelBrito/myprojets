class Task {
  String id;
  String title;
  bool isDone;
  DateTime date;

  Task({
    required this.id,
    required this.title,
    required this.date,
    this.isDone = false,
  });
}
