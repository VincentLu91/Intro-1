#include <iostream>

using namespace std;

/* From Schaum's outlines: Programming in C++
 * Implement a Point class for two-dimensional points (x, y). Include a default constructor, a copy constructor,
 * a negate() function to transform the point into its negative, a norm() function to return the point's distance
 *from the origin (0,0), and a print() function */
 
class Point 
{
  private:
    double x;
    double y;
    
  public:
    
    // default constructor:
    Point() 
    {
      x = 0;
      y = 0;
    }
    
  
    Point(double X, double Y)
    {
      x = X;
      y = Y;
    }
    
    // copy constructor:
    Point(const Point &pt)
    {
      x = pt.x;
      y = pt.y;
    }
    
    //distance function:
    double norm()
    {
      return sqrt(x*x + y*y);
    }
    
    // function for coordinates negation:
    void negate()
    {
      x *= -1.0;
      y *= -1.0;
    }
    
    // print:
    void print()
    {
      cout << "The point is: (" << x << ", " << y <<  ")" << endl;
    }
  }
  
  // end of class definition
  
  int main()
  {
    Point p(14.2, 3.5);
    p.print();
    p.negate();
    double distance = p.norm();
    cout << "The distance from origin to point is: " << distance << endl;
    p.print();
    
    return 0;
  }
