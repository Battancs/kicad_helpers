#include "kicad_turtle_base.h"
#include <iostream>

/**
 * @brief Example implementation of KicadTurtleBase for console output
 * 
 * This class demonstrates how to derive from KicadTurtleBase.
 * It simply prints drawing operations to the console.
 */
class ConsoleTurtle : public KicadTurtleBase {
public:
    ConsoleTurtle(double x, double y, double angle)
        : KicadTurtleBase(x, y, angle) {}
    
    /**
     * @brief Implementation of goto that prints to console
     * @param x Target X coordinate
     * @param y Target Y coordinate
     */
    void gotoReal(double x, double y) override {
        if (pendown) {
            std::cout << "Drawing line from (" << xpos << ", " << ypos 
                      << ") to (" << x << ", " << y << ")" 
                      << " with width " << width << std::endl;
        } else {
            std::cout << "Moving from (" << xpos << ", " << ypos 
                      << ") to (" << x << ", " << y << ")" << std::endl;
        }
        xpos = x;
        ypos = y;
    }
};

/**
 * @brief Example usage of the turtle graphics base class
 */
int main() {
    std::cout << "KiCad Turtle Graphics Example" << std::endl;
    std::cout << "==============================" << std::endl << std::endl;
    
    // Create a turtle at position (100, 100) facing 0 degrees (right)
    ConsoleTurtle turtle(100.0, 100.0, 0.0);
    
    // Draw a square
    std::cout << "Drawing a square:" << std::endl;
    for (int i = 0; i < 4; i++) {
        turtle.forward(50.0);
        turtle.turnLeft(90.0);
    }
    
    std::cout << std::endl << "Moving without drawing:" << std::endl;
    turtle.penUp();
    turtle.forward(100.0);
    
    std::cout << std::endl << "Drawing a triangle:" << std::endl;
    turtle.penDown();
    turtle.setWidth(0.5);
    for (int i = 0; i < 3; i++) {
        turtle.forward(60.0);
        turtle.turnLeft(120.0);
    }
    
    return 0;
}
