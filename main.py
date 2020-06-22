# my version 
class QuadraticEquationSolver:
  def __init__(self, eqn1, eqn2):
    self.eqn1 = eqn1
    self.eqn2 = eqn2
#hi
  def solve(self):
    co_efficients = self.__co_efficients()

    if not co_efficients:
      return None

    x1,y1,const1 = co_efficients[:3]
    x2,y2,const2 = co_efficients[3:]

    if x1 == x2 and y1 == y2:
      return None

    if x1 == x2:
      return self.__solve_equal_x(x1,y1,const1,x2,y2,const2)

    else:

      if y1 == y2:
        return self.__solve_equal_y(x1,y1,const1,x2,y2,const2)

      else:
        return self.__solve_unequal_coeffs(co_efficients)
  def print_solution(self):
    sol = self.solve()
    if sol:
      x,y = sol
      print("x =",x,"y =",y)
    else:
      print("error")
  def __solve_equal_x(self,x1,y1,const1,x2,y2,const2):
    ans = [0]*2
    if const1 == const2:
      ans[0] = const1
      return ans
    ans[1] = (const1 - const2)/(y1-y2)
    ans[0] = const1 - y1 * ans[1]
    return ans

  def __solve_equal_y(self,x1,y1,const1,x2,y2,const2):
    ans = [0]*2
    if const1 == const2:
      ans[1] = const1
      return ans

    ans[0] = (const1 - const2)/(x1 - x2)
    ans[1] = const1 - x1 * ans[0]
    return ans

  def __solve_unequal_coeffs(self,co_efficients):
    ans = [0]*2
    eqn1 = [i * co_efficients[3] for i in co_efficients[:3]]
    eqn2= [i * co_efficients[0] for i in co_efficients[3:]]
    # x will be equal
    x1,y1,const1 = eqn1
    x2,y2,const2 = eqn2
    return self.__solve_equal_x(x1,y1,const1,x2,y2,const2)

  def __co_efficients(self):
    first_equation = self.eqn2.replace(' ', '') 
    second_equation = self.eqn1.replace(' ','')
    try:
        equation1_parts = first_equation.split('=')
        equation2_parts = second_equation.split("=")
        # eq1 coefficients
        xyy_coefficent1 = equation1_parts[0].split("x")
        y_coefficient1 = xyy_coefficent1[1].split('y') 
        y_coefficient1.remove('') 
        xyy_coefficent1.extend(y_coefficient1)
        # eqn2 coefficients
        xyy_coefficent2 = equation2_parts[0].split("x") 
        y_coefficient2 = xyy_coefficent2[1].split('y') 
        y_coefficient2.remove('')
        xyy_coefficent2.extend(y_coefficient2) 
        co_efficients_in_pair = [[xyy_coefficent1[0], xyy_coefficent1[2], equation1_parts[1]], 
            [xyy_coefficent2[0], xyy_coefficent2[2], equation2_parts[1]]]
        co_efficients = []
        for pair in co_efficients_in_pair:
            for idx,val in enumerate(pair):
                if val == '' or val == '+': 
                    pair[idx] = 1 
                elif val == '-':
                    pair[idx] = -1
                else:
                    pair[idx] = int(val)
            co_efficients.extend(pair)
        return co_efficients
    except:
        return []


eqn = QuadraticEquationSolver("x+y=4","x-y=0")
eqn.print_solution()