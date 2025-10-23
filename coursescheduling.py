from collections import deque

class Course:
    def __init__(self, course_id, name, capacity):  
        self.id = course_id
        self.name = name
        self.capacity = capacity
        self.enrolled = set()
        self.waitlist = deque()   # Queue

    def enroll(self, sid):
        if len(self.enrolled) < self.capacity:
            self.enrolled.add(sid)
            return "enrolled"
        else:
            if sid not in self.waitlist:
                self.waitlist.append(sid)
            return "waitlisted"

    def process_waitlist(self):
        while len(self.enrolled) < self.capacity and self.waitlist:
            sid = self.waitlist.popleft()
            self.enrolled.add(sid)

class CourseScheduler:
    def __init__(self):
        self.courses = {}

    def add_course(self, course_id, name, capacity):
        self.courses[course_id] = Course(course_id, name, capacity)

    def enroll(self, sid, course_id):
        course = self.courses[course_id]
        return course.enroll(sid)
