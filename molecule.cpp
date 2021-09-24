#include <iostream>
#include <vector>
#include <sstream>
#include <map>

struct Atom
{
    int element; //!< Atomic Z-number
    double x;    //!< X-coordinate
    double y;    //!< Y-coordinate
    double z;    //!< Z-coordinate
};


class Molecule
{
    private:
        std::vector<Atom> atoms_;

    public:
        Molecule(const std::vector<Atom> & atoms)
            : atoms_(atoms)
        { }


        std::string molecular_formula() const
        {
            /* Write code to find the molecular formula here */
        }
};



int main(void)
{
    /* Some testing code below */
    // Create atoms to add to a molecule
    std::vector<Atom> atoms;
    atoms.push_back(Atom{6, 0.0, 0.0, 0.0});
    atoms.push_back(Atom{1, 0.0, 0.0, 1.0});
    atoms.push_back(Atom{1, 0.0, 1.0, 0.0});
    atoms.push_back(Atom{9, 1.0, 0.0, 0.0});
    atoms.push_back(Atom{9, 1.0, 1.0, 0.0});

    Molecule m(atoms);
    std::cout << m.molecular_formula() << std::endl;

    atoms.clear();
    atoms.push_back(Atom{7, 0.0, 0.0, 0.0});
    atoms.push_back(Atom{8, 0.0, 0.0, 1.0});
    atoms.push_back(Atom{8, 0.0, 1.0, 0.0});

    Molecule m2(atoms);
    std::cout << m2.molecular_formula() << std::endl;

    return 0;
}
