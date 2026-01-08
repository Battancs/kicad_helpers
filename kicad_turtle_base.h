#ifndef KICAD_TURTLE_BASE_H
#define KICAD_TURTLE_BASE_H

#include <cmath>

/**
 * @brief Base class for turtle graphics implementation in KiCad
 * 
 * This abstract base class provides the fundamental interface for
 * turtle graphics drawing on PCB boards. Derived classes should
 * implement the actual drawing operations specific to their backend.
 */
class KicadTurtleBase {
protected:
    double xpos;        ///< Current X position
    double ypos;        ///< Current Y position
    double heading;     ///< Current heading angle in degrees
    bool pendown;       ///< Pen state (true = drawing, false = moving)
    double width;       ///< Line width
    
public:
    /**
     * @brief Constructor
     * @param x Initial X position
     * @param y Initial Y position
     * @param angle Initial heading angle in degrees
     */
    KicadTurtleBase(double x, double y, double angle)
        : xpos(x), ypos(y), heading(angle), pendown(true), width(0.3) {}
    
    /**
     * @brief Virtual destructor
     */
    virtual ~KicadTurtleBase() {}
    
    /**
     * @brief Move forward by the specified distance
     * @param pixels Distance to move
     */
    virtual void forward(double pixels) {
        double radians = heading * M_PI / 180.0;
        double dx = std::cos(radians) * pixels;
        double dy = std::sin(radians) * pixels;
        gotoReal(xpos + dx, ypos + dy);
    }
    
    /**
     * @brief Move backward by the specified distance
     * @param pixels Distance to move
     */
    virtual void backward(double pixels) {
        forward(-pixels);
    }
    
    /**
     * @brief Move to absolute position
     * @param x Target X coordinate
     * @param y Target Y coordinate
     * 
     * This method must be implemented by derived classes to perform
     * the actual drawing or movement operation.
     */
    virtual void gotoReal(double x, double y) = 0;
    
    /**
     * @brief Lift the pen (stop drawing)
     */
    virtual void penUp() {
        pendown = false;
    }
    
    /**
     * @brief Lower the pen (start drawing)
     */
    virtual void penDown() {
        pendown = true;
    }
    
    /**
     * @brief Turn left by the specified angle
     * @param angle Angle in degrees
     */
    virtual void turnLeft(double angle) {
        heading += angle;
        heading = std::fmod(heading, 360.0);
        if (heading < 0.0) {
            heading += 360.0;
        }
    }
    
    /**
     * @brief Turn right by the specified angle
     * @param angle Angle in degrees
     */
    virtual void turnRight(double angle) {
        turnLeft(-angle);
    }
    
    /**
     * @brief Set the line width
     * @param w Width value
     */
    virtual void setWidth(double w) {
        width = w;
    }
    
    /**
     * @brief Get current X position
     * @return Current X coordinate
     */
    double getX() const { return xpos; }
    
    /**
     * @brief Get current Y position
     * @return Current Y coordinate
     */
    double getY() const { return ypos; }
    
    /**
     * @brief Get current heading
     * @return Current heading angle in degrees
     */
    double getHeading() const { return heading; }
    
    /**
     * @brief Check if pen is down
     * @return True if pen is down, false otherwise
     */
    bool isPenDown() const { return pendown; }
    
    /**
     * @brief Get current line width
     * @return Current width value
     */
    double getWidth() const { return width; }
};

#endif // KICAD_TURTLE_BASE_H
