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
    // Constructing with vector & moment of inertia
    std::cout << "WATER" << std::endl;
    std::vector<Atom> atoms;
    atoms.push_back(Atom{8, 15.99491462, 1.0000,  1.0000,  0.2404});
    atoms.push_back(Atom{1, 1.007825032, 1.0000,  2.4326, -0.9611});
    atoms.push_back(Atom{1, 1.007825032, 1.0000, -2.4326, -0.9611});

    Molecule h2o(atoms);
    // Calculate and print inertia tensor
    // Calculate and print principal moments
    // Determine molecular rotor type

    std::cout << "METHANE" << std::endl;
    atoms.clear();
    atoms.push_back(Atom{6, 12.011,       0.0000,  0.0000,  0.0000});
    atoms.push_back(Atom{1, 1.007825032,  0.6291,  0.6291,  0.6291});
    atoms.push_back(Atom{1, 1.007825032, -0.6291, -0.6291,  0.6291});
    atoms.push_back(Atom{1, 1.007825032, -0.6291,  0.6291, -0.6291});
    atoms.push_back(Atom{1, 1.007825032,  0.6291, -0.6291, -0.6291});

    Molecule ch4(atoms);
    // Calculate and print inertia tensor
    // Calculate and print principal moments
    // Determine molecular rotor type

    return 0;
}
