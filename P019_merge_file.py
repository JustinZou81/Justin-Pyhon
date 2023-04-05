course_teacher_map = {}

with open("./course_teacher.txt", encoding="utf-8") as fin:
    for line in fin:
        line = line[:-1]
        course, teacher = line.split(",")
        course_teacher_map[course] = teacher
# print(course_teacher_map)
with open("./course_student_grade_maxminavg.txt", encoding="utf-8") as fin:
    for line in fin:
        line = line[:-1]
        course, sno, sname, sgrade = line.split(",")
        teacher = course_teacher_map.get(course)
        print(course, teacher, sno, sname, sgrade)
