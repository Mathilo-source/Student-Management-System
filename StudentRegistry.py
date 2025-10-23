class StudentRegistry:  #a class for the module on student registry
    def __init__(self):       #a constructor
        self._students = {}      # a dict used to place the students details
        self._order = []         # Linked list to preserve insertion order

    def add_student(self, student):  #method to add students into dict
        sid = student['id']  #to extract id
        if sid in self._students:  #to check if id already exists
            raise ValueError("Student already exists")
        self._students[sid] = student  #if not the new id is inserted
        self._order.append(sid)  #following the order of the dict

    def get_student(self, sid):  #to retrieve an id
        return self._students.get(sid)

    def remove_student(self, sid):  #to delete a student
        if sid in self._students:
            del self._students[sid]
            self._order.remove(sid)
            return True
        return False

    def iterate_students(self):#loop through the dict
        for sid in self._order:
            yield self._students[sid]  #yield is used instead of return so as to produce one student at a time
