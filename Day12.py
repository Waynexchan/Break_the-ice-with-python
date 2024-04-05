'''
def sqt_li():
  li_obj= map(lambda x : x**2,range(int(input("start: ")),int(input("end: "))) )
  print(list(li_obj))

sqt_li()
'''

'''

class American():
  @staticmethod
  def nationality():
    print('Amercian')

american= American()
american.nationality()

American.nationality()

'''

class American():
  def print_nationality(self):
    print('American')

class Newyorker(American):
  def people(self):
    print('New Yorker')

Peter = Newyorker()
Peter.print_nationality()
Peter.people()
