#include <iostream>
#include <cassert>

#include <vector>
#include <array>

struct Atom
{
    int atomic_number; //!< Atomic Z-number
    double mass; //!< Atomic mass
    double x;    //!< X-coordinate
    double y;    //!< Y-coordinate
    double z;    //!< Z-coordinate
};


class Molecule
{
    private:
        std::vector<Atom> atoms_;

    public:
        Molecule() {}

        Molecule(const std::vector<Atom> & atoms) : atoms_(atoms) {}

        Atom & get_atom(int i) { return atoms_.at(i); }

        const Atom & get_atom(int i) const { return atoms_.at(i); }

        void add_atom(const Atom & atom) { atoms_.push_back(atom); }

        size_t size() const { return atoms_.size(); }

        void clear() { atoms_.clear(); }


        std::array<std::array<double, 3>, 3>
        inertia_tensor() const
        {
            std::array<std::array<double, 3>, 3> I;
            I[0][0] = I[0][1] = I[0][2] = I[1][0] = I[1][1] = I[1][2] = I[2][0] = I[2][1] = I[2][2] = 0.0;
            
            for(size_t i = 0; i < atoms_.size(); i++)
            {
                // Ixx
                I[0][0] += atoms_[i].mass * (atoms_[i].y*atoms_[i].y + atoms_[i].z*atoms_[i].z);
                // Iyy
                I[1][1] += atoms_[i].mass * (atoms_[i].x*atoms_[i].x + atoms_[i].z*atoms_[i].z);
                // Izz
                I[2][2] += atoms_[i].mass * (atoms_[i].x*atoms_[i].x + atoms_[i].y*atoms_[i].y);

                // Ixy
                I[0][1] += -atoms_[i].mass * atoms_[i].x * atoms_[i].y;
                // Ixz
                I[0][2] += -atoms_[i].mass * atoms_[i].x * atoms_[i].z;
                // Iyz
                I[1][2] += -atoms_[i].mass * atoms_[i].y * atoms_[i].z;
                }

            // Tensor is symmetric
            I[1][0] = I[0][1];
            I[2][0] = I[0][2];
            I[2][1] = I[1][2];
              
            return I;
        }
        
};


int main(void)
{
    //////////////////////////////////////////////////
    // Constructing with vector & moment of inertia
    //////////////////////////////////////////////////

    /* Construct a water molecule with the following information

        Element  Atomic mass      X       Y       Z
        O        15.99491462   1.0000   1.0000  0.2404
        H        1.007825032   1.0000   2.4326 -0.9611
        H        1.007825032   1.0000  -2.4326 -0.9611
    */

    // Calculate and print inertia tensor
    // Calculate and print principal moments
    // Determine molecular rotor type


    //---------------------------------------------------------------//

    /* Construct a methane molecule with the following information

            Element  Atomic mass          X       Y       Z
              C        12.011        0.0000   0.0000   0.0000
              H        1.007825032   0.6291   0.6291   0.6291
              H        1.007825032  -0.6291  -0.6291   0.6291
              H        1.007825032  -0.6291   0.6291  -0.6291
              H        1.007825032   0.6291  -0.6291  -0.6291
    */

    // Calculate and print inertia tensor
    // Calculate and print principal moments
    // Determine molecular rotor type

    return 0;
}
