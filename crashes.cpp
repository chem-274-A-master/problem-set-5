#include <iostream>
#include <vector>
#include <random>
#include <chrono>


/*! Copies elements from one vector to another
 */
void copy_vector(const std::vector<int> & src,
                 std::vector<int> & dest)
{
    for(size_t i = 0; i < src.size(); i++)
        dest[i] = src[i];
}


int main(void)
{
    unsigned int seed = std::chrono::system_clock::now().time_since_epoch().count();
    std::default_random_engine engine(seed);
    std::uniform_int_distribution<int> dist(1, 1000);

    int size_1 = dist(engine);
    int size_2 = dist(engine);

    std::vector<int> vec1(size_1);
    std::vector<int> vec2(size_2);

    std::cout << vec1.size() << std::endl;
    std::cout << vec2.size() << std::endl;

    // Fill in vector 1
    for(int i = 0; i < size_1; i++)
        vec1[i] = dist(engine);

    // Copy into vector 2
    copy_vector(vec1, vec2);
        

    // Print out the vectors
    for(const auto & it : vec1)
        std::cout << it << std::endl;
    std::cout << std::endl;

    for(const auto & it : vec2)
        std::cout << it << std::endl;
    std::cout << std::endl;

    return 0;
}
