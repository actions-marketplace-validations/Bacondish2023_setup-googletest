#ifndef ABSTRACT_WRITER_HPP_
#define ABSTRACT_WRITER_HPP_


#include <cstdint>
#include <cstddef>


class AbstractWriter
{
public:
    AbstractWriter();
    virtual ~AbstractWriter();
    void write(const uint8_t *buffer, std::size_t count);

    virtual void writeByte(std::uint8_t data) = 0;
};


#endif /* ABSTRACT_WRITER_HPP_ */
