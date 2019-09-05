class object_counter:
    num_of_object=0
    def __init__(self):
        object_counter.num_of_object+=1
    @staticmethod
    def display_count():
        print(object_counter.num_of_object)
o1=object_counter()
object_counter.display_count()